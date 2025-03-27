Can you crack the password to get the flag?Download the password checker [here](https://artifacts.picoctf.net/c/17/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/17/level3.hash.bin) in the same directory too.There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

Hints:
1. To view the level3.hash.bin file in the webshell, do: `$ bvi level3.hash.bin`
2. To exit `bvi` type `:q` and press enter.
3. The `str_xor` function does not need to be reverse engineered for this challenge.
## Solucion

- Descargamos los archivos
```
castr-picoctf@webshell:~/reto$ ls -la
total 12
drwxrwxr-x 2 castr-picoctf castr-picoctf   73 Feb 14 23:01 .
drwxr-xr-x 6 castr-picoctf castr-picoctf  206 Feb 14 23:00 ..
-rw-rw-r-- 1 castr-picoctf castr-picoctf   31 Mar 16  2023 level3.flag.txt.enc
-rw-rw-r-- 1 castr-picoctf castr-picoctf   16 Mar 16  2023 level3.hash.bin
-rw-rw-r-- 1 castr-picoctf castr-picoctf 1337 Mar 16  2023 level3.py
castr-picoctf@webshell:~/reto$ 
```

- vemos el binario del has
```
castr-picoctf@webshell:~/reto$ xxd level3.hash.bin 
00000000: e16d 55a5 5d80 dddd 52a8 3eab ea57 2b7b  .mU.]...R.>..W+{

```

- revisamos el codigo, hay 7 posibles passwords, hay que obtener el hash y compararlo con el del archivo binario, so coincide nos muestra la bandera
```
import hashlib

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_3_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_3_pw_check()


# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
```


- modificamos el programa





- obtenemos la flag
```
castr-picoctf@webshell:~/reto$ python level3.py 
That password is incorrect
That password is incorrect
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
castr-picoctf@webshell:~/reto$ 
```