# Roboto Sans

The flag is somewhere on this web application not necessarily on the website. Find it. Check [this](http://saturn.picoctf.net:65442/) out.

# Solucion

```bash

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/freshjava]
└─$ curl http://saturn.picoctf.net:65442/robots.txt
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/   


┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/freshjava]
└─$ curl http://saturn.picoctf.net:65442/js/myfile.txt
picoCTF{Who_D03sN7_L1k5_90B0T5_a4f5cc70}

```