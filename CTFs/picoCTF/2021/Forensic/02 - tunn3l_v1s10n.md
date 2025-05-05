#  tunn3l_v1s10n


## Formato BMP

### Inicio de los datos de la imagen después del encabezado

Descripción:
- El encabezado es de 40 bytes, hex(40) = 28 
- Eso se especifica en el offset 0A, así que debemos poner ahí un 28

Procedimiento:
- El offset :  `0A`
- Se le pone 40 :  40 (28 00 hex)
- Queda así:  ba d0 - 2800

### Tamaño del encabezado del bit map

Descripción:
- El tamaño del encabezado es de 40 bytes , hex(40) = 28
- Eso se especifica en el offest `0x0E` , así que hay que poner  ahí un 28

Procedimiento:
- El offset: `0E`
- Se le pone: 40 (28 00 hex)
- Queda así: ba d0 - 2800


Windows and OS/2 bitmap headers
Size
40  BITMAPINFOHEADER Windows NT
(28 00 en hex)


### Corrregir la altura del bitmap para poder ver la bandera

Descripción:
- En el offset `0x16` es la altura del bitmap

Procedimiento:
- 32 01  se cambia por 40 03

picoCTF{qu1t3_a_v13w_2020}


## Referencias
- https://en.wikipedia.org/wiki/BMP_file_format
- 