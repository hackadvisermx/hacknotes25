
# Timing is Everything

[](https://github.com/jselliott/SIV-US-Cyber-Open/blob/main/challenges/Forensics/timing-is-everything/README.md#timing-is-everything)

## Description

[](https://github.com/jselliott/SIV-US-Cyber-Open/blob/main/challenges/Forensics/timing-is-everything/README.md#description)

Timing is everything....

Author: r0m

## Files

[](https://github.com/jselliott/SIV-US-Cyber-Open/blob/main/challenges/Forensics/timing-is-everything/README.md#files)

- [timingiseverything.pcap](https://github.com/jselliott/SIV-US-Cyber-Open/blob/main/challenges/Forensics/timing-is-everything/files/timingiseverything.pcap)

## Source

```python
from scapy.all import *
import os
from Crypto.Util.number import bytes_to_long
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import base64
import random

KEY = os.urandom(16)
FLAG = b"SIVUSCG{g0ing_b4ck_1n_t1me_f0r_fl4gs}"

cipher = AES.new(KEY, AES.MODE_ECB)

CT = base64.b64encode(cipher.encrypt(pad(FLAG,16)))

def write(pkt):
    wrpcap('timing.pcap', pkt, append=True)

T = 1714579200

client = IP(src="10.0.0.1",dst="10.0.0.2")/UDP(sport=123,dport=123)/NTP(mode="client",
                                                                        orig=int(T + scapy.layers.ntp._NTP_BASETIME),
                                                                        recv=int(T + scapy.layers.ntp._NTP_BASETIME),
                                                                        sent=int(T + scapy.layers.ntp._NTP_BASETIME),)/NTPAuthenticator(key_id=bytes_to_long(b"AES"),dgst=KEY)

write(client)


packets = []

for i,x in enumerate(CT):

    server = IP(src="10.0.0.2",dst="10.0.0.1")/UDP(sport=123,dport=123)/NTP(mode="server",
                                                                            orig=int((T+i) + scapy.layers.ntp._NTP_BASETIME),
                                                                            recv=int((T+i) + scapy.layers.ntp._NTP_BASETIME),
                                                                            sent=int((T+i) + scapy.layers.ntp._NTP_BASETIME),
                                                                            ref=x)

    client = IP(src="10.0.0.1",dst="10.0.0.2")/UDP(sport=123,dport=123)/NTP(mode="client",
                                                                            orig=int((T+i) + scapy.layers.ntp._NTP_BASETIME),
                                                                            recv=int((T+i) + scapy.layers.ntp._NTP_BASETIME),
                                                                            sent=int((T+i) + scapy.layers.ntp._NTP_BASETIME))
    packets.append((server,client))

while len(packets) > 0:

    idx = random.randint(0,len(packets)-1)
    s,c = packets.pop(idx)
    write(s)
    write(c)
```

## Solve

