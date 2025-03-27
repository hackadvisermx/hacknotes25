# ffuf

## fuzz extensions

```
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://SERVER_IP:PORT/blog/indexFUZZ
```

## fuzz parameters

```shell
ffuf -u 'http://10.10.163.135/sqli-labs/Less-1/?FUZZ=1' -c -w /tools/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fw 39t
```

## fuzzing parameter values

```shell
for i in {0..255}; do echo $i; done | ffuf -u 'http://10.10.163.135/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
```

```bash
for i in $(seq 1 1000); do echo $i >> ids.txt; done
ffuf -w ids.txt  -u http://admin.academy.htb:32689/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs 768
```

```bash
ffuf -u http://faculty.academy.htb:31608/courses/linux-security.php7 -w /opt/useful/SecLists/Usernames/Names/names.txt -X POST -d 'username=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs 781
```


## fuzzing parameter names

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx
```

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt  -u http://admin.academy.htb:32689/admin/admin.php?FUZZ=key  -v -fs 798
```

- POST
  
```
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt  -u http://admin.academy.htb:32689/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded'  -fs 798
```

## fuzzing http form password

```shell
ffuf -u http://10.10.163.135/sqli-labs/Less-11/ -c -w  /tools/wordlists/seclists/Passwords/Leaked-Databases/hak5.txt -X POST -d 'uname=Dummy&passwd=FUZZ&submit=Submit' -fs 1435 -H 'Content-Type: application/x-www-form-urlencoded' 
```

## Find vhosts and subdomains

```shell
ffuf -u http://FUZZ.mydomain.com -c -w /tools/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fs 0
```

```shell
ffuf -u http://mydomain.com -c -w /tools/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.mydomain.com' -fs 0
```

## Proxifying ffuf traffic

- Pasar las solicitudes a un proxy http o socks

```shell
ffuf -u http://10.10.163.135/ -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -x http://127.0.0.1:8080
```

- Pasar solo las solicitudes que conincidan:

```shell
ffuf -u http://10.10.163.135/ -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -replay-proxy http://127.0.0.1:8080
```

## Ignore # en wordlists (-ic)

```shell
ffuf -u http://10.10.163.135/FUZZ -c -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -fs 0
```

## Otras opciones

| opcion              | Descripcion |
|:--------------------|:-----------------------------|
| -of md -o ffuf.md   | Grabar salida en formato md
| -request            | Reutilizar request raw http
| -ic                 | Ignorar # en el wordlist
| -w -                | Recibir wordlst desde stdin
| -v                  | Imprimir full URL
| -r                  | Seguir redirects
| -c                  | Colorizar la salida

## Recursivo

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v
```
