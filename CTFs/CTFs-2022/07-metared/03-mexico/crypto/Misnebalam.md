# Misnebalam

Old henequen hacienda that hides secrets, located in the Santa María Yaxché police station, in Yucatan.


## Solucion

- Descomprimimos el archivo
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/crypto/misnebalam]
└─$ ls
misnebalan.7z
                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/crypto/misnebalam]
└─$ 7z x misnebalan.7z 

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,2 CPUs Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz (40661),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2307895 bytes (2254 KiB)

Extracting archive: misnebalan.7z
--
Path = misnebalan.7z
Type = 7z
Physical Size = 2307895
Headers Size = 138
Method = LZMA2:3m
Solid = -
Blocks = 1

Everything is Ok

Size:       2308037
Compressed: 2307895

```

- Sale un .docx, lo decomprimimos
```bash
──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/crypto/misnebalam]
└─$ ls -la
total 4544
drwxrwx--- 1 root vboxsf   16384 Oct  5 13:44 .
drwxrwx--- 1 root vboxsf   16384 Oct  5 13:44 ..
-rwxrwx--- 1 root vboxsf 2308037 Sep 27 22:35 misnebalam.docx
-rwxrwx--- 1 root vboxsf 2307895 Oct  5 13:44 misnebalan.7z
                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/crypto/misnebalam]
└─$ unzip misnebalam.docx
Archive:  misnebalam.docx
  inflating: _rels/.rels             
  inflating: word/_rels/document.xml.rels  
  inflating: word/document.xml       
  inflating: word/styles.xml         
  inflating: word/theme/theme1.xml   
  inflating: word/fontTable.xml      
  inflating: word/settings.xml       
  inflating: [Content_Types].xml     
  inflating: word/media/image1.png   
  inflating: docProps/app.xml        
  inflating: docProps/core.xml       
  inflating: word/media/misnebalam-fantasma.png
```

- hay dos imagenes en la carleta /word/media
- una trae una pista
```bash
┌──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ exiftool misnebalam-fantasma.png 
ExifTool Version Number         : 12.44
File Name                       : misnebalam-fantasma.png
Directory                       : .
File Size                       : 1502 kB
File Modification Date/Time     : 2022:04:29 10:33:28-04:00
File Access Date/Time           : 2022:10:05 13:46:09-04:00
File Inode Change Date/Time     : 2022:04:29 10:33:28-04:00
File Permissions                : -rwxrwx---
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1200
Image Height                    : 630
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1200x630
Megapixels                      : 0.756
                                                                                                     
┌──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ exiftool image1.png             
ExifTool Version Number         : 12.44
File Name                       : image1.png
Directory                       : .
File Size                       : 798 kB
File Modification Date/Time     : 2022:04:05 23:03:10-04:00
File Access Date/Time           : 2022:10:05 13:46:08-04:00
File Inode Change Date/Time     : 2022:04:05 23:03:10-04:00
File Permissions                : -rwxrwx---
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 800
Image Height                    : 464
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Artist                          : Metared CTF 2022
Copyright                       : OpnStg
Image Size                      : 800x464
Megapixels                      : 0.371
                                                                                                     
┌──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ 

```

- En los metadatos del .docx hay un pass presumiblemente para la image1>
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/crypto/misnebalam]
└─$ exiftool misnebalam.docx 
ExifTool Version Number         : 12.44
File Name                       : misnebalam.docx
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2022:09:27 22:35:32-04:00
File Access Date/Time           : 2022:10:05 13:44:43-04:00
File Inode Change Date/Time     : 2022:09:27 22:35:32-04:00
File Permissions                : -rwxrwx---
File Type                       : DOCX
File Type Extension             : docx
MIME Type                       : application/vnd.openxmlformats-officedocument.wordprocessingml.document
Zip Required Version            : 20
Zip Bit Flag                    : 0
Zip Compression                 : Deflated
Zip Modify Date                 : 2022:04:06 03:24:38
Zip CRC                         : 0x2301d0e8
Zip Compressed Size             : 217
Zip Uncompressed Size           : 573
Zip File Name                   : _rels/.rels
Template                        : Normal.dotm
Total Edit Time                 : 0
Application                     : LibreOffice
App Version                     : 15.0000
Pages                           : 1
Words                           : 113
Characters                      : 605
Characters With Spaces          : 718
Paragraphs                      : 7
Create Date                     : 2022:04:03 04:22:08Z
Creator                         : M1Sn3B@l@m
Description                     : 
Language                        : es-MX
Last Modified By                : 
Modify Date                     : 2022:04:05 22:11:12Z
Revision Number                 : 1
Subject                         : 
Title                           : 

```

```
Creator                         : M1Sn3B@l@m
```

- Instalar > https://www.openstego.com/
- https://github.com/syvaidya/openstego/releases
https://github.com/syvaidya/openstego/releases/download/openstego-0.8.5/openstego_0.8.5-1_all.deb

```bash
──(kali㉿kali)-[~/Downloads]
└─$ sudo dpkg -i openstego_0.8.5-1_all.deb 
[sudo] password for kali: 
Selecting previously unselected package openstego.
(Reading database ... 372340 files and directories currently installed.)
Preparing to unpack openstego_0.8.5-1_all.deb ...
Unpacking openstego (0.8.5-1) ...
Setting up openstego (0.8.5-1) ...
Processing triggers for desktop-file-utils (0.26-1) ...
Processing triggers for mailcap (3.70+nmu1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for kali-menu (2022.4.1) ...

```

- Abrimos el programa y sacamos la bandera del archivo: misnebalam-fantasma.png, usando el pass encontrado : M1Sn3B@l@ms

```
──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ ls    
FileFlag  image1.png  misnebalam-fantasma.png
                                                                                                     
┌──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ cat FileFlag 
ZmxhZ01Ye01pU05lQjRMNG19
                                                                                                     
┌──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ cat FileFlag | base64 -d
flagMX{MiSNeB4L4m}                                                                                                     
┌──(kali㉿kali)-[~/…/crypto/misnebalam/word/media]
└─$ 


```