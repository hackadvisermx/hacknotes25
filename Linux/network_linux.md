

## Saber si alguien me esta haciendo ping
```
tcpdump -i tun0 -v icmp and 'icmp[icmptype]=icmp-echo'
```