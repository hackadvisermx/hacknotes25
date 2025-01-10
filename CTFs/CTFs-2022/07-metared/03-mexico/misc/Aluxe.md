# Aluxe

The naughty aluxes learned to send spam and hide a flag.

Archivo: Qatar

## Solucion
Nos dan un archivo 

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/misc/aluxe]
└─$ file Qatar
Qatar: RFC 822 mail, ASCII text, with very long lines (61662), with CRLF line terminators

```

Parece ser un mensaje de correo, en el cual identificamos un encabezad muy particular:

```
x-header-aluxe:  IGRhdGE6aW1hZ2UvcG5nO2Jhc2U2NCxpVkJPUncwS0dnb0FBQUFOU1VoRVVnQUFBUVFBQUFHQkNBWUFBQUNBZGM5aEFBQTBISHBVV0hSU1lYY2djSEp2Wm1sc1pTQjBlWEJsSUdWNGFXWUFBSGphclp4cmtpNG5rcWIveHlwcUNRSEJkVGxBZ0ZudllKWS96eE9aVWtuVjFUUGRabDJucEpQSy9ESXU0UDVlSElkci81Ly9PTmMvL3ZHUEVISy9yNVJySzcyVW0vK2xubm9jZk5IdW4vLzE3OS9oVHQrL2YvNl   
```

Lo pasamos al portapapeles

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/misc/aluxe]
└─$ grep x-header Qatar | xclip -selection clipboard

```

Se lo pasamos a cyberchef, lo decodica cmo una imagen en base 64: https://gchq.github.io/CyberChef 
```bash 
 data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQQAAAGBCAYAAACAdc9hAAA0HHpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjarZxrki4nkqb/xypqCQHBdTlAgFnvYJY

```

Lo pasamos de base64 a imagen: https://base64.guru/converter/decode/image


flagMX{A1ux3Tr4v13s0}

