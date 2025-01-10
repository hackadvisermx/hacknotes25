# backups

RANCID resplados de los dipositivos de red


```
HOST	TIPO	DOMINIO	IP	NETMASK	GATEWAY	NS1	NS2	SERVICIOS	RAM	PROCESADORES	HD	UBICACIÓN	SO	ADMINISTRADOR	PASSWORD
backups	Virtual	reduaz.mx	10.1.201.5	255.255.255.0	10.1.201.1	148.217.18.6	10.2.205.3	RANCID, MariaDB	2 GB	1	50 GB	CIT	LINUX	

root	f&7epHUChE@U
```

## Proceder

- se identifico RANCID como software para respaldar la configuración de dispositivos CISCO
- copia de backups en /opt/backups

```bash
/var/log/audit

tail /var/log/audit/auth.log -n 100 | grep 'sshd'

tar -czvf backs.tar.gz backups/
scp -r root@10.1.201.5:/opt/back.tar.gz .

tar xvzf back.tar.gz

```

ViewVC es una interfaz de navegador para repositorios de control de versiones CVS y Subversion. Genera plantillas HTML para presentar directorios navegables, revisión, y para cambiar listados de registros. Puede mostrar versiones específicas de archivos así como diferencias entre esas versiones



remover accessos ssh
https://unix.stackexchange.com/questions/127432/logging-ssh-access-attempts

## Borrar historial
 
```bash
cat /dev/null > ~/.bash_history && history -c
```

- Acesso web:

```
https://10.1.201.5/viewvc
admin	3r2theSWe+Ak

```