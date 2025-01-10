# sed

## Sintaxis
```bash
sed [flags] [pattern/script] [input file]
```



## Ejemplos
- Imprime las líneas de las 3 a las 5
```bash
sed -n '3,5p' file.txt
```
- Imprime todo excepto las líneas
```bash
sed '3,5d' file.txt
```
- Multiples rangos de lineas 
```bash
sed -n -e '1,2p' -e '4,5p' file.txt
```
- De las líneas 1 a 3, busca john y reemplaza por JOHN, globalmente
```bash
sed -e '1,3 s/john/JOHN/g' file.txt
```
- Iniciar a buscar desde el patrón n , en este caso 1
```bash
sed 's/youtube/YOUTUBE/1' file.txt
```

- en el parametro al fnal de la expresión, los posibles valores

| Flag | Descripción    |
|-----|-----------------|
| /g  | Globalmente, generalmente trabaja con s/ |
| /i | No distingue entre may y min |
| /d | Borra el patron
| /p | Imprime los patrones 
| /n | Empieza en la concidencia n del patron

- Elimina dobles espacios en el archivo
```bash
sed 's/  */ /g' sed1.txt
```

- Substituye cada 3a ocurrencia de la palabra hack por back en cada linea dentro del archivo
```bash
sed 's/hack/back/3g' file.txt
```
- Lo mismo pero solo en las lineas 3 y 4
```bash
sed '3,4 s/hack/back/3g' file.txt
```

