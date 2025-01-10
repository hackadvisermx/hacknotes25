- hay que armar un codebar para el primer room escondido en ligas de redes sociales 

linkedin
https://hubs.la/Q02bklp30

twitter
https://hubs.la/Q02btlld0

discord - # aoc-2023-side-quest
https://assets.tryhackme.com/additional/aoc2023/b3620/e94fa.png

tryhackme quest room
https://assets.tryhackme.com/additional/aoc2023/6d156/50af2.png


## Link

https://tryhackme.com/room/adv3nt0fdbopsjcap


## Solucion

- Abrir el archivo y filtrar paquetes del handskae
(wlan.fc.type_subtype == 0x08 || wlan.fc.type_subtype == 0x05 || eapol) && wlan.addr==22:c7:12:c7:e2:35

. Crackerlos
aircrack-ng masdatos.pcap -w /usr/share/wordlists/rockyou.txt -e FreeWifiBFC
KEY FOUND! [ Christmas ]


```
 a83f1d1d1d1f2d068ed447cee9fd3aaab2864289faf84993d7c1a029973d449f
```


## research
https://book.hacktricks.xyz/v/es/generic-methodologies-and-resources/exfiltration


## Referencias

- https://kalitut.com/how-to-extract-handshake-from-capture/
- https://kalitut.com/decrypt-wi-fi-traffic-wireshark/
- https://jorisvr.nl/wpapsk.html
- 



