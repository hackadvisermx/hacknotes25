
# FindAndOpen

Someone might have hidden the password in the trace file. Find the key to unlock [this file](https://artifacts.picoctf.net/c/411/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/411/dump.pcap) might be good to analyze.

hints
- Download the pcap and look for the password or flag.
- Don't try to use a password cracking tool, there are easier ways here.

## Solución

- Esto encontre en los paquetes ethernet en el tipo de protocolo
6865 3143 7361 314d

43 47 49 46
- Esto en las direcciones fuente y destino de la primera tanda de paquetes
Flying on Ethernet secret: Is this the flag
Could the flag have been splitted?

- 


 