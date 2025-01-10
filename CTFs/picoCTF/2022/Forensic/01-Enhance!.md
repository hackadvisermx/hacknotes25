# Enhance!

Download this image file and find the flag.

-   [Download image file](https://artifacts.picoctf.net/c/140/drawing.flag.svg)

# Solucion
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/enhance]
└─$ cat drawing.flag.svg | grep tspan | cut -d '>' -f 2 | cut -d '<' -f 1 | tr -d '\n' | tr -d ' '
picoCTF{3nh4nc3d_58bd3420}                                                                                                      
```