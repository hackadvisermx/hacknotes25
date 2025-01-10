# Search source

The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is [here](http://saturn.picoctf.net:56488/)

Hint> How could you mirror the website on your local machine so you could use more powerful tools for searching?


# Solucion
- Hacer mirror


- Buscar en los directorios


```bash
┌──(kali㉿kali)-[~/…/picoctf2022/web/saturn.picoctf.net:56488/css]
└─$ pwd           
/home/kali/hacking/ctfs2022/picoctf2022/web/saturn.picoctf.net:56488/css
                                                                                                      
┌──(kali㉿kali)-[~/…/picoctf2022/web/saturn.picoctf.net:56488/css]
└─$ grep -r pico
style.css:     background-image: url('http://saturn.picoctf.net:56488/images/fevicon.png');
style.css:/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_227d64bd} **/

```





