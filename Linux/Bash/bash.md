# Bash

## Variables
```bash
name="Carlos"
echo $name
```

## Depurar

- Depurar un programa en la terminal
```
bash -x ./file.sh
```

- Poner en el código las líneas a depurar (otra forma)
```bash
echo "hola"
..
..
set -x
 # esto es lo que se depura
set +x
..
```

- Variables múltiples
```bash
nombre="Juan"
edad=21
echo "$nombre tiene $edad años de edad"
```

## Parametros

Los parámetros inician con $0 (es el nombre del programa)

- Tomar el primer parámetro de la línea de comando
```bash
nombre=$1
echo $nombre
```

- Conocer el número de parámetros
```bash
echo $#
```

## Arreglos

- Declarar arreglo, imprimir todos sus elementos

```bash
transporte=('carro' 'tren' 'bicicleta' 'camion')
echo "${transporte[@]}"
```

- Imprimir un elemento en particular
```bash
echo "${transporte[1]}"
```

- Remover un elemento o cambiar un elemento
```bash
unset transporte[1]
transporte[1]="patienta"
```


## Condicionales

| Operador          | Descripcion
|:------------------|:-------------------
| -eq   | Igual
| -ne   | Diferente
| -gt   | Mayor que
| -lt   | Menor que
| -ge   | Mayor o iguel

- Ejemplo 1

```bash
count=10
if [ $count -eq 10]
then
    echo "verdadero"
else
    echo "falso"
fi
```
- Ejemplo 2 - verificar si un archivo existe y si se tienen permisos de escritura
```bash
msg="hello"
if [ -f "$filename" && -w "$filename" ]
then
    echo "hello" > "$filename"
else
    tocuh "$filename"
    echo "hello" > "$filename"
```
Notas:

| op    | Verifica 
|:----  |:--------
| -f    | Si el archivo existe
| -w    | Si tiene permios de escritura
| -r    | Si se tienen permisos de lectura
| -d    | Si el archivo es un directoroo


Refetencias
- [Codewars](https://www.codewars.com/)






