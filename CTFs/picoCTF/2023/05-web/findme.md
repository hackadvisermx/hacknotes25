# findme

Help us test the form by submiting the username as `test` and password as `test!` The website running [here](http://saturn.picoctf.net:58941/).

## Solución

- Primero ingresar con : test test
- Segundo: test test1
- Atrapar las redirecciones

```
GET /next-page/id=cGljb0NURntwcm94aWVzX2Fs HTTP/1.1
Host: saturn.picoctf.net:58941
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://saturn.picoctf.net:58941/
Connection: close
Cookie: PHPSESSID=lj3gcm06t7pt9nsbdvqd1uerm6
Upgrade-Insecure-Requests: 1

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 264
ETag: W/"108-/7O7VTeecocneZ8ZrGW1rxPrD4s"
Date: Tue, 21 Mar 2023 01:27:12 GMT
Connection: close

<!DOCTYPE html>
<head>
    <title>flag</title>
</head>
<body>
    <script>
        setTimeout(function () {
           // after 2 seconds
           window.location = "/next-page/id=bF90aGVfd2F5XzAxZTc0OGRifQ==";
        }, 0.5)
      </script>
    <p></p>
</body>
```

## Bandera

picoCTF{proxies_all_the_way_01e748db}