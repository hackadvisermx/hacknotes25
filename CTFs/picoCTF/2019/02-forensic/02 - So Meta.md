# So Meta

Find the flag in this [picture](https://jupiter.challenges.picoctf.org/static/00efdf2961da1e21470ffc0d496c3cc2/pico_img.png).

## Solucion
- Explicar lo que son los metadaos

- Exiftool
```bash
sudo apt install exiftool

┌──(kali㉿kali)-[~/picoCTF/forensic/someta]
└─$ ls -la
total 116
drwxr-xr-x 2 kali kali   4096 Mar  9 20:30 .
drwxr-xr-x 4 kali kali   4096 Mar  9 20:30 ..
-rw-r--r-- 1 kali kali 108795 Oct 26  2020 pico_img.png
                                                                                                      
┌──(kali㉿kali)-[~/picoCTF/forensic/someta]
└─$ exiftool pico_img.png 
ExifTool Version Number         : 12.40
File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 KiB
File Modification Date/Time     : 2020:10:26 14:38:23-04:00
File Access Date/Time           : 2022:03:09 20:30:50-05:00
File Inode Change Date/Time     : 2022:03:09 20:30:50-05:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_fec06741}
Image Size                      : 600x600
Megapixels                      : 0.360
                                         
```
 
  . exiftool img,  exiftool img -Artist
 
 ```bash
(kali㉿kali)-[~/picoCTF/forensic/someta]
└─$ exiftool pico_img.png -Artist
Artist                          : picoCTF{s0_m3ta_fec06741} 
 ``` 
  

  . strings -n 
```
strings -n 10 pico_img.png | grep pico
picoCTF{s0_m3ta_fec06741}

```

## Referencias
- [Metadatos](https://es.wikipedia.org/wiki/Metadatos)
- metadata: https://en.wikipedia.org/wiki/Metadata