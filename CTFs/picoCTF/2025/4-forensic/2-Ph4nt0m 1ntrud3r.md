
# Ph4nt0m 1ntrud3r

A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/960abba2fdbc9be5013ef87f1df67213e9b63d4561d7a8c8c1ce7a4ce40a547e/myNetworkTraffic.pcap) and try to get the flag.

1. Filter your packets to narrow down your search.
2. Attacks were done in timely manner.
3. Time is essential

## Solucion

- Analizamos paquetes tshark
```
┌──(.venv2)─(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap 
 

```

- Solo aquellos tcp , se reduce en 2
```
┌──(.venv2)─(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y tcp
  

```

- los datos de los paquetes 
```
┌──(.venv2)─(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y tcp -T fields -e tcp.segment_data 
424e41556436553d
657a46305833633063773d3d
6e30746e346a593d
595a59417645733d
63476c6a62304e5552673d3d
685769557671513d
587a4d3063336c6664413d3d
66513d3d
675673526f50553d
77326952486e673d
596d68664e484a665a513d3d
6f5a59725047453d
2b5a7968387a553d
32466c6a5541773d
7a3349797a76673d
4e575534597a63345a413d3d
67436a7679396f3d
4736557a744a773d
356837663967773d
4c7050755136773d
626e52666447673064413d3d
514845534847593d

```

- los decodificamos
-p vaciado en ascii
-r reversea el hexadecimal
```
┌──(.venv2)─(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y tcp -T fields -e tcp.segment_data | xxd -p -r
BNAUd6U=ezF0X3c0cw==n0tn4jY=YZYAvEs=cGljb0NURg==hWiUvqQ=XzM0c3lfdA==fQ==gVsRoPU=w2iRHng=YmhfNHJfZQ==oZYrPGE=+Zyh8zU=2FljUAw=z3Iyzvg=NWU4Yzc4ZA==gCjvy9o=G6UztJw=5h7f9gw=LpPuQ6w=bnRfdGg0dA==QHESHGY=  
```

- Agregamos el campo de tiempo y ordenamos
```
┌──(.venv2)─(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp" -T fields -e frame.time -e tcp.segment_data -e tcp.len | sort -k4
 

```

- elegimos solo aquellos de longitud 12 y 4
```                                                                                                                                                                                                                            
┌──(.venv2)─(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data -e tcp.len | sort -k4
 

```

- tomamos la columna de los datos
```
┌──(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data -e tcp.len | sort -k4 | awk '{print $6}'  
 
```

- decodificamos y convertimos
```
┌──(kali㉿kali)-[~/tmp/picoctf2025/forensic/pahntom]
└─$ tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e frame.time -e tcp.segment_data -e tcp.len | sort -k4 | awk '{print $6}' | xxd -p -r | base64 -d
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_e5e8c78d}  
```