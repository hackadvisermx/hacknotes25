# WebNet1

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag.

## Solucion

~ WebNet1 - Points: 450

### Forma 1
- cambar la llave TLS
- extraer imagen
- hacerle strings
```bash
strings -n 10 vulture.jpg 
picoCTF{honey.roasted.peanuts}
```

### Forma 2
- way 1 con wire shark
	- cambiar la llave TLS para que sea la del reto actual
	- buscar nuevamente
	- ir al flow del http, donde se descarga la imagen vultre.jpg
	- buscar ahi en las opciones de abajo asta encontrar
```cmd
......JFIF..............Exif..MM.*.................J...........R.(...........;.........Z................................picoCTF{honey.roasted.peanuts}......ICC_PROFILE.......lcms....mntrRGB XYZ .........).9acspAPPL...................................-lcms...............................................

```
	
### Forma 3
```bash
ssldump -r capture.pcap -k picopico.key -d | grep pi -A 10
```

```
   00 00 00 01 00 00 00 01 70 69 63 6f 43 54 46 7b    ........picoCTF{
    68 6f 6e 65 79 2e 72 6f 61 73 74 65 64 2e 70 65    honey.roasted.pe
    61 6e 75 74 73 7d 00 00 ff e2 02 1c 49 43 43 5f    anuts}......ICC_

```

`picoCTF{honey.roasted.peanuts}`

