# Generales del lenguaje


## Tipos de datos

| Tipo   | Ejemplo    |
| :----- | :--------- |
| int    | a = 28     |
| float  | b = 1.5    |
| str    | c = "Hola" |
| bool   | d = True   |
| NoType | e = None   |


## Estructuras de datos

| Tipo  | Descripción                     | Ejemplo                               |
| :---- | :------------------------------ | ------------------------------------- |
| list  | secuencia de valores mutables   | nombres=["Carlos","Esteban","Fatima"] |
| tuple | secuencia de valores inmutables |                                       |
| set   | colección de valores únicos     |                                       |
| dict  | colección de pares key-value    |                                       |

### Listas [] - Ordenadas, cambiables, permiten duplicados

| Meetodo | Funcion
|:--------|----------
| append    | agregar un elemento al final de la lista
| clear     | remuve todos los elementos de la lista
| copy      | copia una lista en otra variable
| count     | Regresa el numero de veces que un elemento ocurre en la lista
| extend    | extiende la lista agregando un iterable al final
| index     | recibe elemento y devuelve indice de su primera ocurrencia
| insert    | inserta elemento en un posición determinada   
| pop       | devuelve el último elemento
| remove    | recibe elemento y borra la primera aparición (ValueError si no esta)
| reverse   | Invierte el orden de la lista
| sort      | Ordena la lista


Pedir ayuda, teclear en el interprete de python:
```
help(list)
```

### Tuplas () - Ordenadas, no cambiables, permiten duplicados

| Meetodo   | Funcion
|:----------|----------
| count     | Regresa el numero de veces que un elemento ocurre en la tupla
| index     | Busca en la tupla por un elemento especificado y regresa la posición donde fue econtrado

### Conjuntos {} - no ordenada, no cambiable, no duplicados

| Meetodo                       | Funcion
|:------------------------------|--------------------------------------------------------------
| add()                         | agregar un elemento al conjunto
| clear()                       | remover todos los elementos del conjunto
| copy()                        | regresa una copia del c
| difference()                  | regresa un conjunto con la diferencia entre 2 o mas conjuntos
| difference_update()           | remueve los elementos en este conjunto que esta incluidos tambión en otro conjunto
| discard()                     | remueve un elemento especificado 
| intersection()                |
| interesection_update()        |
| isdisjoint()                  |
| issubset()                    |
| issuperset()                  |
| pop()                         |
| remove()                      |
| symmetric_difference()        |
| symmetric_difference_update() |

### Diccionaros {} - no odenado, cambiable, no permite duplicados




Referencias
- [Python Tutorial - w3schools](https://www.w3schools.com/python/default.asp)
- [Programación en Python Nivel básico](https://entrenamiento-python-basico.readthedocs.io/es/latest/)
