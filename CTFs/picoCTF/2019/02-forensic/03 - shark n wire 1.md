# shark on wire 1
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.

## Solucion 
- abrir el archivo con whireshark
- explicar los paquetes y el encapsulamiento
 - que son los streams, conjunto de paquetes
 - ordenar por protocolo
 - seguir streass, la flag esta udp.streams eq 6


picoCTF{StaT31355_636f6e6e}


Ligas


- packet analyzer - https://en.wikipedia.org/wiki/Packet_analyzer
- pcap  - https://www.comparitech.com/net-admin/pcap-guide/