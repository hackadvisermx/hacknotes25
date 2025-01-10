
- Al abrir reto parece una imagen gif, pero en realidad es un png con algunos efectos
- El archivo de imagen, se carga desde la hoja de estilos

```
/* source: milkslap-milkslap.scss */
body {
  margin: 0;
  padding: 0;
  overflow: hidden; }

a {
  color: inherit; }

.center {
  width: 1080px;
  height: 720px;
  margin: 0 auto; }

#image {
  height: 720px;
  margin-top: 5%;
  margin-bottom: 20px;
  background-image: url(concat_v.png);
  background-position: 0 0; }

#foot {
  margin-bottom: 5px;
  color: #999999; }
  #foot h1 {
    font-family: serif;
    font-weight: normal;
    font-size: 1rem;
    text-align: center; }
```

- descargamos
```
wget http://mercury.picoctf.net:7585/concat_v.png
--2024-10-08 14:07:44--  http://mercury.picoctf.net:7585/concat_v.png
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:7585... connected.
HTTP request sent, awaiting response... 200 OK
Length: 18095920 (17M) [image/png]
Saving to: ‘concat_v.png’

concat_v.png            100%[============================>]  17.26M   215KB/s    in 62s     

2024-10-08 14:08:49 (287 KB/s) - ‘concat_v.png’ saved [18095920/18095920]

```

- examinamos un poco

```
┌──(kali㉿kali)-[~/picoctf/forensic/milkslap]
└─$ file concat_v.png 
concat_v.png: PNG image data, 1280 x 47520, 8-bit/color RGB, non-interlaced
                                                                                             
┌──(kali㉿kali)-[~/picoctf/forensic/milkslap]
└─$ exiftool concat_v.png 
ExifTool Version Number         : 12.76
File Name                       : concat_v.png
Directory                       : .
File Size                       : 18 MB
File Modification Date/Time     : 2021:03:15 13:24:47-05:00
File Access Date/Time           : 2024:10:08 14:09:53-05:00
File Inode Change Date/Time     : 2024:10:08 14:08:49-05:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1280
Image Height                    : 47520
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1280x47520
Megapixels                      : 60.8

```


- zsteg colapsa, agregamos esto al archivo .zshrc

```
export RUBY_THREAD_VM_STACK_SIZE=500000000
```


- dcodificamos
```
steg concat_v.png          
imagedata           .. text: "\n\n\n\n\n\n\t\t"
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"

```