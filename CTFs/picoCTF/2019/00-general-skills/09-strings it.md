Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings) without running it?

Hint:
1. [strings](https://linux.die.net/man/1/strings)

## Solucion

```castr-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
--2025-02-12 22:43:54--  https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: 'strings'

strings            100%[===============>] 757.84K  1.81MB/s    in 0.4s    

2025-02-12 22:43:54 (1.81 MB/s) - 'strings' saved [776032/776032]

castr-picoctf@webshell:~$ file strings 
strings: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0cdedfba33422d235dba8c90e00fb77b235f1ff8, not stripped
castr-picoctf@webshell:~$ strings strings | grep pico
picoCTF{5tRIng5_1T_7f766a23}
castr-picoctf@webshell:~$ 
```

