o # ka

I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png)


hint> https://en.wikipedia.org/wiki/Visual_cryptography


hint> Think of different ways you can "stack" images

## Solucion 
Criptgrafia visual

https://es.frwiki.wiki/wiki/Cryptographie_visuelle

### Stegsolve
- descargar > https://github.com/zardus/ctf-tools/blob/master/stegsolve/install
- abrir una imagen, luego la otra
- aparece la flag


## way 2
```
sudo apt install imagemagickP

convert scrambled1.png scrambled2.png -compose Add -composite c.png
```



- Instalar image magic
```bash
sudo apt-get install imagemagick
```

- combinar pero no sale flag

```bash
convert scrambled1.png scrambled2.png  +append salida.jpg
```




```python
from PIL import Image
import numpy as np
import os

file_names = ["scrambled1.png", "scrambled2.png"]
img_data = [np.asarray(Image.open(f'{name}')) for name in file_names]

data = img_data[0].copy() + img_data[1].copy()

new_image = Image.fromarray(data)
new_image.save("out.png", "PNG")
```

```python
from PIL import Image
import numpy as np

imagen1 = np.asarray( Image.open('scrambled1.png') )
imagen2 = np.asarray( Image.open('scrambled2.png') )

data = imagen1 + imagen2

nueva = Image.fromarray(data)
nueva.save("out.png", "PNG")

```

## Ligas
- visual cryptography : https://en.wikipedia.org/wiki/Visual_cryptography
- image magick: https://imagemagick.org/index.php
- stegsolve : https://github.com/zardus/ctf-tools/blob/master/stegsolve/install