


```
cat /etc/resolv.conf

domain uaz.edu.mx
search uaz.edu.mx
nameserver 10.2.205.3
nameserver 10.2.205.4
nameserver 8.8.8.8

```

```
nano /etc/resolv.conf

#domain uaz.edu.mx
#search uaz.edu.mx
#nameserver 10.2.205.3
#nameserver 10.2.205.4
nameserver 8.8.8.8




systemctl reload NetworkManager
NetworkManager --print-config
```

- antes
```
sudo nano /etc/NetworkManager/NetworkManager.conf
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=false

```

```
[main]
plugins=ifupdown,keyfile
dns=none
rc-manager=unmanaged

[ifupdown]
managed=false


```