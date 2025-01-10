#  tunn3l_v1s10n


Formato BMP

- Inicio de los datos de la imagen después del encabezado
0A 
40 (28 00 hex)

ba d0 - 2800

- Tamaño del encabezado del bit map
0E
40 (28 00 hex)

ba d0 - 2800

 
Windows and OS/2 bitmap headers

Size
40  BITMAPINFOHEADER Windows NT
(28 00 en hex)


- En el offset 16 la altura del bitmap

32 01  se cambia por 40 03

picoCTF{qu1t3_a_v13w_2020}