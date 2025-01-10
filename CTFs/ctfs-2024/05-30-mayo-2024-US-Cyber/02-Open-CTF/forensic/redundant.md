# Redundant

### 100

My meme got corrupted somehow and cut off the punchline. Can you help?

Author: [tsuto](https://github.com/jselliott)

## Solve

- Offesets 0x8 y 0x12 esta el alto y el ancho, primero se trato de modificar el alto


- Se corrigieron una serie de errores CRC en los chunks, usando un editor hexadecimal
- Expected es lo que aparecia, se cambio por computed

``` forensic pngcheck redundant.png
zlib warning:  different version (expected 1.2.13, using 1.3)

redundant.png  CRC error in chunk IHDR (computed bd73b950, expected 762f6af5)
ERROR: redundant.png
➜  forensic pngcheck redundant.png
zlib warning:  different version (expected 1.2.13, using 1.3)

redundant.png  CRC error in chunk IDAT (computed 1ca1c693, expected 4c4f4c21)
ERROR: redundant.png
➜  forensic pngcheck redundant.png
zlib warning:  different version (expected 1.2.13, using 1.3)

redundant.png  CRC error in chunk IDAT (computed 1afad93f, expected 4c4f4c21)
ERROR: redundant.png
➜  forensic pngcheck redundant.png
zlib warning:  different version (expected 1.2.13, using 1.3)

OK: redundant.png (1600x901, 24-bit RGB, non-interlaced, 73.2%).
```



```
SIVUSCG{1nv4l1d_chunk5_l0l}
```