# c0rrupt

We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.

# Solucion
- Ver tipo de archivo
```bash
┌──(kali㉿kali)-[~/picoCTF/forensic/corrupt]
└─$ file mystery       
mystery: data
```
- Google> magic bytes > https://en.wikipedia.org/wiki/List_of_file_signatures

- ver la cabecera del archivo
```bash
xxd -g 1 mystery | head
```

- corregir la cabecera del archivo para que sea un PNG, con hexeditors:
```bash
hexeditor mystery
```
	- 8 bytes
	- 89 50 4E 47 0D 0A 1A 0A
	- ^X salir y guardar

- verificar que paso, aun sigue sendo data, pero el encabezado se actualizo

```bash
file mystery
xxd -g 1 mystery | head
```

- despues del encabezado vienen una serie de chunks 
	- 4 bytes para la longitud 
	- 4 bytes para el tipo
	- contenido con la longitud declarada anteriormente

- corregir IHDR : 43 22 44 52  por    49 48 44 52
```bash
file mystery
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
```

- intentar abrir pero aun error

- instalar pngcheck y verificar PNG
```bash
sudo apt i44nstall pngcheck
pngcheck -v fixed.png

mystery  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERROR: mystery
```

- corregir pHys

Pixels per unit, X axis: 4 bytes (unsigned integer)
Pixels per unit, Y axis: 4 bytes (unsigned integer)
Unit specifier:          1 byte

	aa 00 16 25 00 00 16 25 - 00 00 16 25 00 00 16 25

- verificar de nuevo
```bash
pngcheck mystery
mystery  invalid chunk length (too large)
ERROR: mystery

```
~ corregir el tamano del chunk antes del idat es el tama;o
	AA AA FF A5 - 00 00 FF A5

- corregir chunk anterior para que diga IDAT
	AB 44 45 54 - 49 44 41 54



picoCTF{c0rrupt10n_1847995}

## Referencias

- fle signatures : https://en.wikipedia.org/wiki/List_of_file_signatures
- png : https://en.wikipedia.org/wiki/Portable_Network_Graphics