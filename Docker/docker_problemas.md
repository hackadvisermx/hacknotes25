


## Con el DNS

- aqui se guarda la configuracion del docker en mac

/System/Volumes/Update/mnt1/Users/castr/.docker/daemon.json

## Desinstalar docker mac

https://stackoverflow.com/questions/44346109/how-to-easily-install-and-uninstall-docker-on-macos

## Con los mirrors de update

https://askubuntu.com/questions/872933/how-to-fix-hash-sum-mismatch-error-on-fresh-docker-image-update

20.10 Groovy
```
rm -rf /etc/apt/sources.list
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy-updates main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt groovy-updates main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy-backports main restricted universe multiverse" >> /etc/apt/sources.list
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy-security main restricted universe multiverse" >> /etc/apt/sources.list
```
- Agregar al contenedor para corregir temporalmente el problema de repos oficiales

RUN \
rm -rf /etc/apt/sources.list && \
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy main restricted universe multiverse" >> /etc/apt/sources.list && \
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt groovy-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt groovy-security main restricted universe multiverse" >> /etc/apt/sources.list 
