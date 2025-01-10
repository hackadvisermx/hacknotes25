HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.


## Ejemplos

```bash
cat targets.txt| httpx -silent -probe

echo 173.0.84.0/24 | httpx -silent

| httpx -favicon
| httpx -asn
httpx -l urls.txt -path /v1/api -sc
cat targets.txt| httpx -title
cat targets.txt |  httpx -title -content-length -status-code
| httpx -status-code -mc 200,302
| httpx -tech-detect
httpx -l targets.txt -tech-detect | grep Wordpress -i

echo 10.1.0.0/16 | httpx -title -web-server -status-code

echo 148.217.50.0/24 | httpx -title -web-server -status-code -follow-redirects -vhost -ip


```




- Referencias
- https://unsafe.sh/go-73021.html
