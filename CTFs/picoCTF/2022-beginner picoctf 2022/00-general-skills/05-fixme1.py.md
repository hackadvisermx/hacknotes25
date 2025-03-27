Fix the syntax error in this Python script to print the flag.[Download Python script](https://artifacts.picoctf.net/c/26/fixme1.py)

Hints
1. Indentation is very meaningful in Python
2. To view the file in the webshell, do: `$ nano fixme1.py`
3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
4. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion
- descargamos
```
castr-picoctf@webshell:~$ mkdir reto
castr-picoctf@webshell:~$ cd reto
castr-picoctf@webshell:~/reto$ wget https://artifacts.picoctf.net/c/26/fixme1.py
--2025-02-13 00:44:12--  https://artifacts.picoctf.net/c/26/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.43, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                 100%[===================================>]     837  --.-KB/s    in 0s      

2025-02-13 00:44:12 (4.58 MB/s) - 'fixme1.py' saved [837/837]
```

- Corremos y vemos error
```
castr-picoctf@webshell:~/reto$ python fixme1.py 
  File "/home/castr-picoctf/reto/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```

- Corregimos el error en la sangria de la linea 20 print ....
```python
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_ke>


flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x>

  
flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
```

- ejecutamos

```
astr-picoctf@webshell:~/reto$ python fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
```