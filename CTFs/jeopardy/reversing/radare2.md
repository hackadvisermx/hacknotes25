# Radare 2

- Basicos

| comando      | descripcion                                      
|:-------------|:-------------------------------------------------| 
| aaa          | analiza todas las funciones del ejecutable         
| afl          | lista todas las funciones que se encontraron     
| iz	       | lista las cadenas                                
| pdf @sym.main| desensabla la función main                       
| VV @main	   | va al modo visual de flujo                       
| p	           | cambia de modo dentro                            
| q	           | sale de un modo de visualización    
| tab , s+tab  | moverse entre bloques
| s+ h j k l   | mover un bloque
| ?            | ayuda                      
 
 - Informacion

| comando      | descripcion                                       
|:-------------|:-------------------------------------------------| 
| ia           | informacion del archivo cargado 
| ie           | punto de entrada 
| il           | librerias
| im           | direccion de la funcion main 
| izz          | todas las cadenas en el binario 

- navegacion por la memoria

| comando      | descripcion                                       
|:-------------|:-------------------------------------------------| 
| s            | direccion acutal de memoria donde estamos
| s sys.main   | ir a la direccion de la funcion main
| sr rax       | va a la direccion del registro rax
| s +1         | mueve un byte adelante
| s -1         | mueve un byte hacia atras


- Imprimir

| comando      | descripcion                                       
|:-------------|:-------------------------------------------------------| 
| px           | imprime hex de la direccion actual
| pd           | desensambar lo que hay en memoria
| px @rbp      | ver el contenido de la direccion a la que apunta un registro
| px @0x...    | ver el contenido de la memoria en la direción 0x...
| pxc          | ver el contenido con comentarios


- Modo deburacion

| comando       | descripcion                                       
|:--------------|:-------------------------------------------------| 
| r2 -d file    | abrir un archivo en modo depuracion
| db addr       | poner un punto de interrupcion
| db            | listar puntos de interrupcion
| dc            | ejecutar el programa
| ds            | ejecutar un paso de instruccion
| afvd          | muestra el valor de las variables con nombre cuando se esta 
| dr eax=0x0    | cambiar el valor de un registro
| ood           | volver a cargar el archivo en modo depuracion
| dr            | ver el valor de los registros
| VV            | parar al modo gráfico para depurar
| :             | estando en VV pasar a modo comando :dc ejecitar
| s             | estando en VV avanza por instrucciones (veremos rip: moverse en el diagrama)
| V!            ? 


