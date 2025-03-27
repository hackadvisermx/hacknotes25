
Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/13/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) in the same directory too.

Hitnts:
1. Does that encoding look familiar?
2. The `str_xor` function does not need to be reverse engineered for this challenge.


## Solucion

- Descargamos
```
castr-picoctf@webshell:~/reto$ ls -la
total 8
drwxrwxr-x 2 castr-picoctf castr-picoctf  50 Feb 14 22:55 .
drwxr-xr-x 6 castr-picoctf castr-picoctf 206 Feb 13 00:44 ..
-rw-rw-r-- 1 castr-picoctf castr-picoctf  31 Mar 16  2023 level2.flag.txt.enc
-rw-rw-r-- 1 castr-picoctf castr-picoctf 914 Mar 16  2023 level2.py
castr-picoctf@webshell:~/reto$ 
```
- Analizamos el código
	- La comparacion del password se hace con catacteres, solo hay que decodificarlos y sabremos el password
```Python
castr-picoctf@webshell:~/reto$ cat level2.py 
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()
```

- decodificamos
```bash
astr-picoctf@webshell:~/reto$ python
Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)
'de76'
```

- Obtenemos la bandera
```
castr-picoctf@webshell:~/reto$ python level2.py 
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a
```