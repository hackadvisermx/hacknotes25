# Proxy Tools

Es posible interceptar las peticiones que se hacen en la línea de comandos, se puede user `ProxyChains` o usar el parámetro de `proxy` de la herramienta en cuestión.


## Proxychains

- Modificar la configuración en `/etc/proxychains.conf` algo similar a:

```bash
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4         127.0.0.1 9050
#socks5 127.0.0.1 1080
http 127.0.0.1 8089
https 127.0.0.1 8080
```

Y se cambia también el a modo `Quiet` en la misma configuración:

```bash
# Quiet mode (no output from library)
quiet_mode
```

- Luego ya para usarlo, anteponemos `proxychains` al comando 

```bash
proxychains curl http://wwww.uaz.edu.mx
```

Y observamos en burp o zap que se pasa la solicitud por el proxy.

## El proxy de cada app

Por ejemplo para mandar las peticiones web de Nmap via proxy

- Forma 1 proxy nmap
  
```bash
nmap --proxies http://127.0.0.1:8080 www.cfe.mx -Pn -sC -v
```

- Forma 2 via Proxychains

```bash
proxychains nmap www.cfe.mx -Pn -sC -v
```


## El proxy en modulos de Metasploit

```
use auxiliary/scanner/http/http_put
set rhosts www.uaz.edu.mx
set proxies http:127.0.0.1:8080
run
```
