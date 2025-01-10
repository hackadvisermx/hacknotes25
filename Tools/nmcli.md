# nmcli

Es una utilidad de línea de comando utilizada para administrar y controlar `NetworManager`, permitiendo a los usuarios configurar las conexiones de red, desplegar el estado de la red y solucionar problemas de red

## Ver configuración de la red

```
nmcli general status

STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN     METERED      
connected  full          missing  enabled  missing  enabled  no (guessed) 
```

```
nmcli device  

DEVICE  TYPE      STATE                   CONNECTION         
eth0    ethernet  connected               Wired connection 1 
lo      loopback  connected (externally)  lo  
```

```
nmcli connection 

NAME                UUID                                  TYPE      DEVICE 
Wired connection 1  7fda4a2b-1138-4444-9492-df5f2868681e  ethernet  eth0   
lo                  ebf970ca-84a2-4c51-a791-ba2a89732705  loopback  lo  

nmcli device show
GENERAL.DEVICE:                         eth0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         00:0C:29:B1:6A:FF
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     Wired connection 1
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/2
WIRED-PROPERTIES.CARRIER:               on
IP4.ADDRESS[1]:                         192.168.100.95/24
IP4.GATEWAY:                            192.168.100.1
IP4.ROUTE[1]:                           dst = 192.168.100.0/24, nh = 0.0.0.0, mt = 100
IP4.ROUTE[2]:                           dst = 0.0.0.0/0, nh = 192.168.100.1, mt = 100
IP4.DNS[1]:                             192.168.100.1
IP6.ADDRESS[1]:                         fe80::20c:29ff:feb1:6aff/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = fe80::/64, nh = ::, mt = 1024

GENERAL.DEVICE:                         lo
GENERAL.TYPE:                           loopback
GENERAL.HWADDR:                         00:00:00:00:00:00
GENERAL.MTU:                            65536
GENERAL.STATE:                          100 (connected (externally))
GENERAL.CONNECTION:                     lo
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/1
IP4.ADDRESS[1]:                         127.0.0.1/8
IP4.GATEWAY:                            --
IP6.ADDRESS[1]:                         ::1/128
IP6.GATEWAY:                            --
```

```
nmcli device show eth0

GENERAL.DEVICE:                         eth0
GENERAL.TYPE:                           ethernet
GENERAL.HWADDR:                         00:0C:29:B1:6A:FF
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     Wired connection 1
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/2
WIRED-PROPERTIES.CARRIER:               on
IP4.ADDRESS[1]:                         192.168.100.95/24
IP4.GATEWAY:                            192.168.100.1
IP4.ROUTE[1]:                           dst = 192.168.100.0/24, nh = 0.0.0.0, mt = 100
IP4.ROUTE[2]:                           dst = 0.0.0.0/0, nh = 192.168.100.1, mt = 100
IP4.DNS[1]:                             192.168.100.1
IP6.ADDRESS[1]:                         fe80::20c:29ff:feb1:6aff/64
IP6.GATEWAY:                            --
IP6.ROUTE[1]:                           dst = fe80::/64, nh = ::, mt = 1024                
```

## Administrar dispositivos de red

```
nmcli device connect eth0   
Device 'eth0' successfully activated with '7fda4a2b-1138-4444-9492-df5f2868681e'.
```

```
nmcli device disconnect eth0
Device 'eth0' successfully disconnected.
```

```
nmcli device monitor  
```

## Referencias
- https://x.com/xmodulo/status/1824058559216120113/photo/1