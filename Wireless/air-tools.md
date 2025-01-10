- Mostrar interfaz inalambrica
```
sudo iw dev           
phy#1
        Interface wlan0
                ifindex 4
                wdev 0x100000001
                addr 12:d8:f6:ff:4a:95
                type managed
                txpower 20.00 dBm
                                       
```

- Poner tarjeta de red en modo monitor
```
sudo airmon-ng check
sudo airmon-ng check kill

sudo airmon-ng start wlan0
```

## Configuración de red inalámbrica

```
iwconfig

lo        no wireless extensions.

eth0      no wireless extensions.

tun0      no wireless extensions.

wlan0     IEEE 802.11  Mode:Monitor  Frequency:2.457 GHz  Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off

```