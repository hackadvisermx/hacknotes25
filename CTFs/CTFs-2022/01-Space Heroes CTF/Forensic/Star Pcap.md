# Star Pcap







### Intento 1

```python
from scapy.all import *
import base64

capture = rdpcap('star.pcap')
ping_data = ""

for packet in capture:
   if packet[ICMP].type == 8: # Echo request
       ping_data += packet.load

print(base64.b64decode(ping_data))

```

### Intento 2

```python
from scapy.all import *
import base64

capture = rdpcap('star.pcap')
ping_data = ""

for packet in capture:
        code = packet[ICMP].code
        ping_data += chr(code)      

print(base64.b64decode(ping_data).decode())

```

```bash
python exp2.py
shctf{L0g1c-i$-th3-begiNNing-0f-wi$doM}
```