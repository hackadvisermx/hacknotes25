```
 ssh -oHostKeyAlgorithms=+ssh-dss -oPubkeyAcceptedAlgorithms=+ssh-rsa root@148.217.94.98
 pr0y3ctrelo4d

root@monitor-uaz:~# hostname
monitor-uaz


root@monitor-uaz:~# cat /usr/local/nagios/etc/htpasswd.users
nagiosadmin:7UiBTHImigZ1A
jdeli:ErNX62NjMMgXw
auditoria:m5a0mv4.G9FO6
root@monitor-uaz:~#


root@monitor-uaz:/usr/local/nagios/etc# cat htpasswd.users
nagiosadmin:7UiBTHImigZ1A
jdeli:XdIiGj9qN4wXs
auditoria:m5a0mv4.G9FO6
root@monitor-uaz:/usr/local/nagios/etc#

```

- cambiar password
```
htpasswd /usr/local/nagios/etc/htpasswd.users 
```

- permisos y grupos
```
root@monitor-uaz:/usr/local/nagios/etc/objects# pwd
/usr/local/nagios/etc/objects
root@monitor-uaz:/usr/local/nagios/etc/objects# ls
commands.cfg  hosts.cfg      hosts.cfg.save  printer.cfg   services.cfg.old  templates.cfg    windows.cfg
contacts.cfg  hosts.cfg.old  localhost.cfg   services.cfg  switch.cfg        timeperiods.cfg
root@monitor-uaz:/usr/local/nagios/etc/objects#

contacts.cfg
```

## Acceso web
```
http://148.217.94.98/nagios/ 
nagiosadmin
pr0y3ctrelo4d
```



## referencias

https://ngelinux.com/how-to-add-your-id-as-admin-in-nagios/

