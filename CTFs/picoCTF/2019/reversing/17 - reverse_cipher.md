ka# reverse_cipher

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this). Can you reverse the flag

objdump and Gihdra are some tools that could assist with this

## Solucion
- Google: x64 Assembly
- https://www.intel.com/content/dam/develop/external/us/en/documents/introduction-to-x64-assembly-181178.pdf




- vemos con objdump
```bash
objdump -D rev -M intel | grep '<main>:' -B 10 -A 20

```

- ver las cadenas del binario
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/reversecipher]
└─$ objdump -dj .rodata rev

rev:     file format elf64-x86-64


Disassembly of section .rodata:

0000000000002000 <_IO_stdin_used>:
    2000:       01 00 02 00 00 00 00 00 72 00 66 6c 61 67 2e 74     ........r.flag.t
    2010:       78 74 00 61 00 72 65 76 5f 74 68 69 73 00 00 00     xt.a.rev_this...
    2020:       4e 6f 20 66 6c 61 67 20 66 6f 75 6e 64 2c 20 70     No flag found, p
    2030:       6c 65 61 73 65 20 6d 61 6b 65 20 73 75 72 65 20     lease make sure 
    2040:       74 68 69 73 20 69 73 20 72 75 6e 20 6f 6e 20 74     this is run on t
    2050:       68 65 20 73 65 72 76 65 72 00 70 6c 65 61 73 65     he server.please
    2060:       20 72 75 6e 20 74 68 69 73 20 6f 6e 20 74 68 65      run this on the
    2070:       20 73 65 72 76 65 72 00                              server.

```




- Que tenemos
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/reversecipher]
└─$ cat rev_this     
picoCTF{w1{1wq85jc=2i0<}                                                                                                      
┌──(kali㉿kali)-[~/picoctf/reversing/reversecipher]
└─$ cat rev_this | wc
      0       1      24

```

- Tiene 24 carateres, pero solo 18 {} en medio de las llaves son la bandera en realidad



- instalar ghidra
```bash
sudo apt install ghidra
```
~ abrir ghidra y crear nuevo proyecto, abrir el archivo

	File - New Project / Non-Shared Project
	Project Name = test / Finish
	File - Import file  / Ok .. OK
	Doble click / Analyze / Ok

~ ir al symbol tree y buscar main
	functions / main
	ventana derecha : Decompile main

~ renombre variables para entender
	Derecho / Rename Variable
		
### Análisis

- El cifrado no afecta mas que a la bandera por eso se brnca los primeros 8 caracteres picoCTF{ here }
```c
  for (i = 0; i < 8; i = i + 1) {
    r = rev[i];
    fputc((int)r,frev);
  }
```

- Si es par le suma 5, Su es impar le resta 2, Asi que solo hay que revertirlo:
```c
  for (j = 8; (int)j < 0x17; j = j + 1) {
    if ((j & 1) == 0) {
      r = rev[(int)j] + '\x05';
    }
    else {
      r = rev[(int)j] + -2;
    }
    fputc((int)r,frev);
  }
```

```python
>>> 1 & 0
0
>>> 1 & 1
1
>>> 2 & 1
0
>>> 3 & 1
1
>>> 4 & 1
0
>>> 
```

~ exploit

```python
cifrado = open('rev_this','r').read() 

flag=''

for i in range(8,len(cifrado)-1):
    if i & 1 == 0 :
        flag +=  chr( ord(cifrado[i]) - 5 )
    else:
        flag +=  chr( ord(cifrado[i]) + 2)

print(flag)
```

