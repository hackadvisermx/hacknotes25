# extensions

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

Hints:
- How do operating systems know what kind of file it is? (It's not just the ending!
- Make sure to submit the flag as picoCTF{XXXXX}

# Solucion

- hexeditor para ver encabezado y saber que es png
- o con comando file
- solo cambiar la extension de .txt a .png


```bash
┌──(kali㉿kali)-[~/picoCTF/forensic/extensions]
└─$ ls -la
total 20
drwxr-xr-x 2 kali kali 4096 Mar  9 20:44 .
drwxr-xr-x 6 kali kali 4096 Mar  9 20:43 ..
-rw-r--r-- 1 kali kali 9984 Oct 26  2020 flag.txt
                                                                                                      
┌──(kali㉿kali)-[~/picoCTF/forensic/extensions]
└─$ file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
                                                                                                      
┌──(kali㉿kali)-[~/picoCTF/forensic/extensions]
└─$ mv flag.txt flag.png
```

## Referencias

- file format: https://en.wikipedia.org/wiki/File_format
- fle signatures : https://en.wikipedia.org/wiki/List_of_file_signatures
