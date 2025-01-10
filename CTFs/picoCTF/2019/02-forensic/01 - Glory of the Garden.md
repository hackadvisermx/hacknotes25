# Glory of the Garden

This [garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg) contains more than it seems.

## Solucion

 - con un hexeditor, buscar con ctrl + w, pag arriba, pag 
 abajo, salor

```
┌──(kali㉿kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ hexeditor garden.jpg 

```
 - con strings -n
 
 ```bash
 ──(kali㉿kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ ls -la
total 2252
drwxr-xr-x 2 kali kali    4096 Mar  9 16:40 .
drwxr-xr-x 3 kali kali    4096 Mar  9 16:40 ..
-rw-r--r-- 1 kali kali 2295192 Oct 26  2020 garden.jpg
                                                                                                      
┌──(kali㉿kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ strings garden.jpg -n 10 | grep pico
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
                                                                                                      
┌──(kali㉿kali)-[~/picoCTF/forensic/gloryofthegarden]
└─$ 

 ```

## Ligas:
- hexeditor: https://en.wikipedia.org/wiki/Hex_editor
