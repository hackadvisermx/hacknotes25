
# Matryoshka doll
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

# Solucion
- Extraemos lo contenido en las imagenes varias veces hasta sacar la flag

### Forma 1 - usar unzip hasta que salga

```
[unzip dolls.jpg](<┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ ls -la                         
total 648
drwxrwxr-x 2 kali kali   4096 Oct  8 11:50 .
drwxrwxr-x 9 kali kali   4096 Oct  8 11:47 ..
-rw-rw-r-- 1 kali kali 651634 Mar 15  2021 dolls.jpg
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ file dolls.jpg 
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ unzip dolls.jpg              
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg     
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ ls    
base_images  dolls.jpg
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ cd base_images 
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka/base_images]
└─$ ls
2_c.jpg
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka/base_images]
└─$ unzip 2_c.jpg  
Archive:  2_c.jpg
warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/3_c.jpg     
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka/base_images]
└─$ ls -l 
total 380
-rw-r--r-- 1 kali kali 383940 Mar 15  2021 2_c.jpg
drwxrwxr-x 2 kali kali   4096 Oct  8 11:53 base_images
                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka/base_images]
└─$ cd base_images 
                                                                                     
┌──(kali㉿kali)-[~/…/forensic/matryoshka/base_images/base_images]
└─$ ls   
3_c.jpg
                                                                                     
┌──(kali㉿kali)-[~/…/forensic/matryoshka/base_images/base_images]
└─$ unzip 3_c.jpg 
Archive:  3_c.jpg
warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/4_c.jpg     
                                                                                     
┌──(kali㉿kali)-[~/…/forensic/matryoshka/base_images/base_images]
└─$ ls
3_c.jpg  base_images
                                                                                     
┌──(kali㉿kali)-[~/…/forensic/matryoshka/base_images/base_images]
└─$ cd base_images 
                                                                                     
┌──(kali㉿kali)-[~/…/matryoshka/base_images/base_images/base_images]
└─$ ls
4_c.jpg
                                                                                     
┌──(kali㉿kali)-[~/…/matryoshka/base_images/base_images/base_images]
└─$ unzip 4_c.jpg 
Archive:  4_c.jpg
warning [4_c.jpg]:  79578 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: flag.txt                
                                                                                     
┌──(kali㉿kali)-[~/…/matryoshka/base_images/base_images/base_images]
└─$ ls
4_c.jpg  flag.txt
                                                                                     
┌──(kali㉿kali)-[~/…/matryoshka/base_images/base_images/base_images]
└─$ cat flag.txt  
picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}                                                                                     
┌──(kali㉿kali)-[~/…/matryoshka/base_images/base_images/base_images>)

```

## Forma 2 - usar binwalk hasta que salga


```bash
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ binwalk --extract dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378955, uncompressed size: 383936, name: base_images/2_c.jpg
651613        0x9F15D         End of Zip archive, footer length: 22

                                                                                 
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka]
└─$ cd _dolls.jpg.extracted 
                                                                                 
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka/_dolls.jpg.extracted]
└─$ ls    
4286C.zip  base_images
                                                                                 
┌──(kali㉿kali)-[~/picoctf/forensic/matryoshka/_dolls.jpg.extracted]
└─$ cd base_images         
                                                                                 
┌──(kali㉿kali)-[~/…/forensic/matryoshka/_dolls.jpg.extracted/base_images]
└─$ 

```


```bash
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ pwd
/home/kali/picoctf/forensic/matryoshka/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted
                                                                                 
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ cat flag.txt
picoCTF{ac0072c423ee13bfc0b166af72e25b61}                                                                                 
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ 

```