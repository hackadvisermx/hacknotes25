# logon
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/13594/` ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594
- hints:
	- Hmm it doesn't seem to check anyone's password, except for Joe's?


## Solución
https://jupiter.challenges.picoctf.org/problem/13594/
- Solo valida el password para el usuario Joe
- No valida el password para los demas
	- Se crean 3 cookies, admin false, los otros, ponen el user y el password el mismo que le damos
		- admin : false
		- password: password
		- username: admin

### Dar primero la explicación

#### Se cargan al inicio de la página algunos componentes
- que es jquery: https://es.wikipedia.org/wiki/JQuery
- bootstrap: https://es.wikipedia.org/wiki/Bootstrap_(framework)
- jumbotron: https://getbootstrap.com/docs/4.0/components/jumbotron/

#### Es preciso saber sobre los fundamentos de http
- que es http: https://developer.mozilla.org/en-US/docs/Web/HTTP
- que soon los http headers: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
	- request headers: https://developer.mozilla.org/en-US/docs/Glossary/Request_header
		- request methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
	- response headers: https://developer.mozilla.org/en-US/docs/Glossary/Response_header
		- response codes:  https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- que son las cookies: https://es.wikipedia.org/wiki/Cookie_(inform%C3%A1tica)
. podemos obtener ayuda de cada encabezado en el signo de interrogacion en el inspector

### Desde la web
-  ver headers en firefox
- Instalar plugin cookie editor (mordida a la izquierda)
- modificar el encabezado y la cookie admin = true

#### Desde la consola
- ver headers con curl ( -v , -I --head )
```bash
curl -s https://jupiter.challenges.picoctf.org/problem/13594/flag -H 'Cookie: username=user; password=pass; admin=True'  | grep pico
```


## Notas adicionales

 

- 