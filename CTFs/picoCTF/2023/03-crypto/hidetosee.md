# HideToSee

How about some hide and seek heh? Look at this image [here](https://artifacts.picoctf.net/c/241/atbash.jpg).
Hint: Download the image and try to extract it.

## Solución

```
➜  hidetosee steghide --extract -sf atbash.jpg
Enter passphrase:
wrote extracted data to "encrypted.txt".
➜  hidetosee cat encrypted.txt
krxlXGU{zgyzhs_xizxp_7867098z}
```

- estaba encriptada con abatsh ciper.
## Bandera

`picoCTF{atbash_crack_7867098a}`



## Referencia
- https://www.dcode.fr/atbash-cipher
-