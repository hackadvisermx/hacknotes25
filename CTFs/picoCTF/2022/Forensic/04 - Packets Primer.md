# Packets Primer

Download the packet capture file and use packet analysis software to find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/203/network-dump.flag.pcap)

# Solucion

- Seguir el tcp stream y ahi esta


```
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/packetsprimer]
└─$ cat flag  | tr -d ' '
picoCTF{p4ck37_5h4rk_7d32b1de}

```