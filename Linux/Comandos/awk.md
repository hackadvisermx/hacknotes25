# awk
Awk is a scripting language used for manipulating data and generating reports.The awk command programming language requires no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators.

## Sintaxis
```bash
awk [flags] [select pattern/find(sort)/commands] [input file]
```

## opciones

| Bandera | Descripción |
|---------|---------------|
| FS | Separador de campo |
| OFS | Separador en la salida |
| ORS | Separador de registro |
| -F | También usada para separador de campo |
| -v | Puede ser usada para especificar variables como BEGIN{OFS=":"} |
 

## Ejemplos

- Imprimir un archivo
```bash
awk '{print}' file.txt
```
- Buscar un patron en un archivo
```bash
awk '/ctf/' file.txt
```
- Delimitadores de campo: columna 1 y 3 del archivo, separador espacio, con y sin espacio separando el resultado
```bash
awk '{print $1 $3}' file.txt
awk '{print $1,$3}' file.tx
```
- Numerar líneas en la salida
```bash
awk '{print NR,$0}' file.txt
```
- Separador de campo FS puesto a 'o', imprime columnas 1 y 3 y al final un resumen del no de líneas
```bash
awk 'BEGIN {FS="o"} {print $1,$3} END{print "Total Rows=",NR}'
```
- FS a espacio, OFS (output field separator) a ":" y las columnas 1 y 4
```bash
 awk 'BEGIN{FS=" "; OFS=":"} {print $1,$4}' awk.txt
 awk -F " " 'BEGIN{OFS=":"} {print $1,$4}' awk.txt
```
- Separador de registro ORS a "," la columna 1
```bash
awk 'BEGIN{ORS=","} {print $1}' awk.txt
awk -v ORS="," '{print $1}' awk.txt
```