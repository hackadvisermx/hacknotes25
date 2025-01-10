# File types
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from [here](https://artifacts.picoctf.net/c/327/Flag.pdf).

Hint> Remember that some file types can contain and nest other files

# Solucion
- el archivo dice ser un pdf pero es un bash

- hay que cambiar la extension o copiarlo 

- al ejecutar pide uudecode, instalamos sharutils 


- instalar uudecode

``` bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ sudo apt-get install sharutils
```

- vemos tipo de archivo ( ar file )

```
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag
flag: current ar archive

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ ar t flag
flag

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ ar x flag
                
```


- vemos tipo de archivo ( cpo file)

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag
flag: cpio archive

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ cpio -t -F flag 
flag
2 blocks

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ cpio -i -F flag -r       
rename flag -> flag2
2 blocks

```



- vemos tipo de archivo ( bzip2 )

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2
flag2: bzip2 compressed data, block size = 900k

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2 flag2.bz2
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ bzip2 -d flag2.bz2        

```


- vemos tipo de archivo ( gzip )

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2
flag2: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:46 2022, from Unix, original size modulo 2^32 330

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2 flag2.gz 
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ gzip -d flag2.gz  
```




- vemos tipo de archivo ( lzip )

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2
flag2: lzip compressed data, version: 1

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ sudo apt install lzip     


┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lzip -l flag2 
  uncompressed     compressed   saved  name
           283            330 -16.61%  flag2

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lzip -d flag2



```


- vemos tipo de archivo ( lz4)

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2.out 
flag2.out: LZ4 compressed data (v1.4+)

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ sudo apt install lz4 

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lz4 --list flag2.out 
    Frames           Type Block  Compressed  Uncompressed     Ratio   Filename
         1       LZ4Frame   B4I      283.00             -         -   flag2.out

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2.out flag2.lz4 
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lz4 -d flag2.lz4      
Decoding file flag2 
flag2.lz4            : decoded 266 bytes   

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2.out flag2.lz4 
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lz4 -d flag2.lz4      
Decoding file flag2 
flag2.lz4            : decoded 266 bytes   
```


- vemos tipo de archivo ( LZMA )

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2
flag2: LZMA compressed data, non-streamed, size 255

                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2 flag2.lzma
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lzma -d flag2.lzma 



```

- vemos tipo de archivo ( lzop )

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2
flag2: lzop compressed data - version 1.040, LZO1X-1, os: Unix
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ sudo apt install lzop

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lzop -l flag2
method      compressed  uncompr. ratio uncompressed_name
LZO1X-1           197       197 100.0% flag2.raw
                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2 flag2.lzop
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lzop -d flag2.lzop 

```

- vemos tipo de archivo ( lzip)

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2
flag2: lzip compressed data, version: 1
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ lzip -d flag2     
                  fol

```


- vemos tipo de archivo ( XZ )

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2.out
flag2.out: XZ compressed data, checksum CRC64
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ sudo apt install xz-utils

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ mv flag2.out flag2.xz 

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ xz -d -v -k -f flag2.xz

                      
```
- vemos tipo de archivo ( ar file )

```bash
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ file flag2   
flag2: ASCII text



┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ cat flag2
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f35613833373565307d0a
                                                  
```


- hex to ascii

```bash

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/filetypes]
└─$ xxd -r -p flag2
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_5a8375e0}



picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_5a8375e0}

```




## Recursos

- [GNU sharutils](https://en.wikipedia.org/wiki/GNU_Sharutils)
- [ ar file ](https://en.wikipedia.org/wiki/Ar_(Unix))
- [cpio file ] (https://es.wikipedia.org/wiki/Cpio)


