Unzip this archive and find the flag.

- [Download zip file](https://artifacts.picoctf.net/c/503/big-zip-files.zip)

## Solucion

- Descargamos el archivo y lo desempacamos

```bash
castr-picoctf@webshell:~/bigzip$ unzip big-zip-files.zip

castr-picoctf@webshell:~/bigzip/big-zip-files$ ls -R
uff ...

```

- Tenemos que hacer una busqueda recursiva
```
grep -R picoCTF
folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
castr-picoctf@webshell:~/bigzip/big-zip-files$ 
```