# RED
Download the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)

1. The picture seems pure, but is it though?
2. Red?Ged?Bed?Aed?
3. Check whatever Facebook is called now.

## Solucion

```
┌──(kali㉿kali)-[~/tmp/picoctf2025/forensic/red]
└─$ exiftool red.png 
ExifTool Version Number         : 13.10
File Name                       : red.png
Directory                       : .
File Size                       : 796 bytes
File Modification Date/Time     : 2025:03:09 19:21:15-05:00
File Access Date/Time           : 2025:03:10 15:17:37-05:00
File Inode Change Date/Time     : 2025:03:09 19:21:26-05:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 128
Image Height                    : 128
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
Image Size                      : 128x128
Megapixels                      : 0.016

```

```
C rimson heart, vibrant and bold,.
H earts flutter at your sight..
E venings glow softly red,.
C herries burst with sweet life..
K isses linger with your warmth..
L ove deep as merlot..
S carlet leaves falling softly,.
B old in every stroke.
```

```
┌──(kali㉿kali)-[~/tmp/picoctf2025/forensic/red]
└─$ zsteg -a red.png               
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="

```

- base64 decode
```
Gljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==
```

picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

- mas fino
```
zsteg -s l red.png

zsteg --lsb red.png

zsteg --lsb --channel rgba red.png

```
## Solucion 2



 

## Referencias

- Tool: https://www.aperisolve.com/
