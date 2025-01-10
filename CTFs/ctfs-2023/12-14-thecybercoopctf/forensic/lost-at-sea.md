## Lost at Sea

### 100

I dropped my flag in the sea. Help me find it among the sharks!

 [lost-at-sea.pcapng](https://thecybercoopctf.ctfd.io/files/d9caaec04f791cc527c1d4e72531c5b9/lost-at-sea.pcapng?token=eyJ1c2VyX2lkIjo3OTksInRlYW1faWQiOjQ4MywiZmlsZV9pZCI6MzB9.ZX0i9w.k_OSV87ZXg6tnxfWgxxPsycG-KY "lost-at-sea.pcapng")

## solucion

### way1

```
astr@mymac lostatsea % strings lost-at-sea.pcapng | grep flag
GET /flag%7Bb4by_5h4rk_do0_d0o_d00_d0o_d0o_1n_th3_s34%7D HTTP/1.1
<p>The requested URL /flag{b4by_5h4rk_do0_d0o_d00_d0o_d0o_1n_th3_s34} was not found on this server.</p>
castr@mymac lostatsea %
```

### way2
- Abrir con wireshark y seguir el stream
```
GET /flag%7Bb4by_5h4rk_do0_d0o_d00_d0o_d0o_1n_th3_s34%7D HTTP/1.1
Host: 192.168.0.20
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.11.1

HTTP/1.1 404 Not Found
Date: Wed, 31 Jan 2018 18:52:31 GMT
Server: Apache/2.4.18 (Ubuntu)
Content-Length: 323
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /flag{b4by_5h4rk_do0_d0o_d00_d0o_d0o_1n_th3_s34} was not found on this server.</p>
<hr>
<address>Apache/2.4.18 (Ubuntu) Server at 192.168.0.20 Port 80</address>
</body></html>

```