# shark on wire 2
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Solucion

### Forma 1
- Abrir el archivo en wireshark

```bash
wireshark capture.pcap &  
```

- Establecer un filtro en wireshark

udp.stream eq 32 , dice `start` y va dirigido al puerto 22
udp.stream eq 60, dice `end` y va dirigido al 22 tambien

udp.dstport == 22
udp.port == 22

- El puerto origen, si le quitas - 5000, iba formando las caracteres ascii en decimal

```python
>>> chr(112)
'p'
>>> chr(105)
'i'
>>> chr(99)
'c'
>>> chr(111)
'o'
>>> 

```

### Forma 2

- Instalar la libreria:  `scapy`

```bash
sudo apt install python3-pip
sudo python3 -m pip install scapy

sudo apt install python3-scapy 
```

- Un script de python para resolver el problema v1

```python 
from scapy.all import *

packets = rdpcap('capture.pcap')

flag=''

for p in packets:
    if UDP in p and p[UDP].dport == 22:
        if p[UDP].sport > 5000:
            flag+=chr(p[UDP].sport - 5000)

print(flag)

```

- Un script de python para resolver el problema v2

```python

from scapy.all import *

packets = rdpcap('capture.pcap')

flag=''

for p in packets:
    if UDP in p and p[UDP].dport == 22:
        if p[UDP].sport > 5000:
            print( chr( p[UDP].sport - 5000 ), end="" )
```

## Forma 3

En whireshark, Mark All Displayerd
File - Export packet disection - As plain text

```
cat hola3.txt | grep Source | cut -d ' ' -f7 | awk '$0' | cut -c2- | grep -v 000 |  xclip -selection clipboard
```


```
cat data.txt | grep UDP | awk '{print $7}' | cut -c2- | grep -v 000
```

- cut -c2- , toma del segundo caracter en adelante
- grep -v 000 , ignora lineas que tengan 000
## Ligas
- scapy : https://scapy.net/
