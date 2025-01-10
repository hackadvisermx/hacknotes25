
## Solucion

- Se trata de un archivo con .7z sin password
- Usaremos `johntheripper` , hay que instalar unas librerias antes:
```
sudo apt install libcompress-raw-lzma-perl
```
- Sacamos el hash del .7z: 
```
7z2john flag.7z > hash
```

## Una forma
```
sudo hashcat -m 11600 hash1 /usr/share/wordlists/rockyou.txt

```