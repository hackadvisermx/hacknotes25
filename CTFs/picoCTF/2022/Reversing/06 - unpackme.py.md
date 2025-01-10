# unpackme.py

Can you get the flag? Reverse engineer this [Python program](https://artifacts.picoctf.net/c/468/unpackme.flag.py).


## solucion

- modificar un poco el codigo

```pyhton
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABiMD1Dt87s50caSunQlHoZqPOwtGNaQXexN-gjKwZeuLEN_-v6UcFJHVXOT4B6DcD1SB7cnd6yTcHg9e9LZCAeJY2cJ0r0sfyG>

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
print(plain)

#exec(plain.decode())

```

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/unpackme]
└─$ python3 unpackme.flag.py 
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_8aef58d2}')\nelse:\n  print('That password is incorrect.')\n\n"

```



picoCTF{175_chr157m45_8aef58d2}