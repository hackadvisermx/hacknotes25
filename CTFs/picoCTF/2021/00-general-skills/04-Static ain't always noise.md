Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static)? This [BASH script](https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh) might help!

# Solucion

- Descargamos los archivos
```
castr-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static
--2025-02-12 22:50:31--  https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/static
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8376 (8.2K) [application/octet-stream]
Saving to: 'static'

static             100%[===============>]   8.18K  --.-KB/s    in 0s      

2025-02-12 22:50:31 (232 MB/s) - 'static' saved [8376/8376]

castr-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh
--2025-02-12 22:50:38--  https://mercury.picoctf.net/static/bc72945175d643626d6ea9a689672dbd/ltdis.sh
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 785 [application/octet-stream]
Saving to: 'ltdis.sh'

ltdis.sh           100%[===============>]     785  --.-KB/s    in 0s      

2025-02-12 22:50:38 (376 MB/s) - 'ltdis.sh' saved [785/785]

castr-picoctf@webshell:~$ 
```

Analizamos su tipo:
```
castr-picoctf@webshell:~$ ls
README.txt  ltdis.sh  static
castr-picoctf@webshell:~$ file ltdis.sh 
ltdis.sh: Bourne-Again shell script, ASCII text executable
castr-picoctf@webshell:~$ file static 
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=33934f7b8aea8e359749ed57dca4cd26d6059acf, not stripped
castr-picoctf@webshell:~$ 
```

- Analizamos el script de bash
Lo que hace es mandar llamar objdump sobre el binario y guarda el resultado en un archivo de texto

```
castr-picoctf@webshell:~$ bash ltdis.sh 
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
castr-picoctf@webshell:~$ ls
README.txt  ltdis.sh  static
castr-picoctf@webshell:~$ bash ltdis.sh static 
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
castr-picoctf@webshell:~$ 
```
- Buscamos la bandera en el archivo de texto
```
astr-picoctf@webshell:~$ cat static.ltdis.strings.txt | grep pico
   1020 picoCTF{d15a5m_t34s3r_1e6a7731}
```