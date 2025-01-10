 # Quite Random
500

“Find out what message is hidden in this image.”


## Solucion
- La imagen es un QR pero al leerlo marca error

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ sudo apt install zbar-tools    
                                             
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ zbarimg ChristoperEdee.png 
scanned 0 barcode symbols from 1 images in 0.02 seconds


WARNING: barcode data was not detected in some image(s)
 
```
- La imagen, no se abre como imgagen, binwalk dice que es un rar

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ binwalk ChristoperEdee.png   

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
2884          0xB44           RAR archive data, version 5.x
```

- La imagen original .png trae un password adentro para el rar
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ strings -n 8 ChristoperEdee.png
mtx.png0
@!Q6:s8H
bCHydvh@*
Vi\DyW*I
mtx.png0
pass:k155
```

- al abrirlo trae una imagen mtx.png, con una secuencia de numeros

7 9 1
4 6 8
3 5 2

- Dividir la imagen en un radio de 3x3
- op1 n jao
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ convert ChristoperEdee.png -crop 3x3@ s%02d.png 
```
- op2
Image splitter
https://pinetools.com/es/partir-imagenes


- Rerdenar en la secuencia, para corregir el qr
1 2 3
4 5 6
7 8 9

- op1 juntar
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ montage  s02.png s08.png s06.png s03.png s07.png s04.png s00.png s05.png s01.png -geometry +3+3 -tile 3x3 okbar.png

```

- op2 juntar

Merge
https://products.aspose.app/imaging/image-merge/navigation/result
- Leemos y ya jala
- 
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/obfuscation/quiterandom]
└─$ zbarimg MergedImages.png 
QR-Code:flagMX{ug0t1t}
scanned 1 barcode symbols from 1 images in 0.03 seconds


```


# Referencias

https://stackoverflow.com/questions/56414667/how-to-crop-a-image-into-several-rectangular-grids-using-imagemagick

eog - vsualizador de imagenes gnomes


Image splitter
https://pinetools.com/es/partir-imagenes

Merge
https://products.aspose.app/imaging/image-merge/navigation/result


