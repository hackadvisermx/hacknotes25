
```
148.217.94.76

ssh -oHostKeyAlgorithms=+ssh-dss -oPubkeyAcceptedAlgorithms=+ssh-rsa root@148.217.94.76
pr0y3ctrelo4d

vigilante:/usr/local/nagios/etc# hostname
vigilante

```

```
vigilante:/usr/local/nagios/etc# cat htpasswd.users
nagiosadmin:q8QZqBxwjgGwM
rpasillas:qN7dbHcXlKs16
deli:IJe1R0zs3Ch96
rgomez:YYkjpRVF8R2Lc
alex:UaKvbukwxAuks
river:Lu5YibaDR86Yw
gareth:Bjl83tz7d.E46
```

```
 /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
 htpasswd /usr/local/nagios/etc/htpasswd.users river
New password:
Re-type new password:
Updating password for user river

/etc/init.d/nagios restart
```

## acceso web

```
http://148.217.94.76/nagios/
river
uaz@2009@
```