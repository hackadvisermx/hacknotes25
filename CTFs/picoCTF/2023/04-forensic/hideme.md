
Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/493/flag.png).

## Solucion

```
➜  hideme unzip flag.png
Archive:  flag.png
warning [flag.png]:  39739 extra bytes at beginning or within zipfile
  (attempting to process anyway)
   creating: secret/
  inflating: secret/flag.png
➜  hideme cd secret
➜  secret ls
flag.png
```

- la bandera estaba en el archivo flag.png que estaba dentro de flag.png original


`picoCTF{Hiddinng_An_imag3_within_@n_ima9e_5cf64968}`