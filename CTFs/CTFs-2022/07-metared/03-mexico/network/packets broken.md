#  ¡packets broken!



# Solucion
- Te dan un archivo de captura de paquetes dañado
- Lo examinamos con un editor hexadecimal
- ```
```cmd
___________________________________________PASS:XOR just 4 fun_________________________________________________

```

- Tomamos en hex la parte de XOR just 4 fun

```
584F52206A75737420342066756E
```


```


- Lo reparamos con pcapfix
```bash
──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/network/packets broken]
└─$ sudo apt install pcapfix      
```

```bash
──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/network/packets broken]
└─$ pcapfix broken.pcap 
pcapfix 1.1.7 (c) 2012-2021 Robert Krause

[*] Reading from file: broken.pcap
[*] Writing to file: fixed_broken.pcap
[*] File size: 8509956 bytes.
[+] This is a PCAP file.
[*] Analyzing Global Header...
[+] The global pcap header seems to be fine!
[*] Analyzing packets...
[*] Progress:  20.01 %
[*] Progress:  40.01 %
[+] CORRECTED Packet #5882 at position 3982514 (1665357324 | 104106 | 2866 | 2866).
[*] Progress:  60.00 %
[*] Progress:  80.03 %
[*] Progress: 100.00 %
[*] Wrote 11742 packets to file.
[+] SUCCESS: 1 Corruption(s) fixed!

```

- Lo abrimos ya reparado y en el stream 10589 encontramos, stream 357
```bash
GET /seemore.html HTTP/1.1
Host: www.flag.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: es-419,es;q=0.9,es-ES;q=0.8
If-None-Match: "0-5ea3f14d10ca9"
If-Modified-Since: Wed, 05 Oct 2022 00:58:56 GMT

HTTP/1.1 304 Not Modified
Date: Sun, 09 Oct 2022 23:16:46 GMT
Server: Apache/2.4.54 (Debian)
Last-Modified: Wed, 05 Oct 2022 00:58:56 GMT
ETag: "0-5ea3f14d10ca9"
Accept-Ranges: bytes
X-flag: 00111110001000110011001101000111001001110010110100001000000100100001000001011000010010110000101000011010000111000110100100101100000011010100010001011110000110110001000001000111011111110100000001001000010101010010101000011100011011000011101100100110010011000101100100001000
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive


```

- decodificar usand el xor pass encontrado arriba

https://www.dcode.fr/xor-cipher

