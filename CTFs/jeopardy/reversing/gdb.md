# GNU Debugger


## Configuraciones

	set disassembly-flavor intel

## Informacion

| comando       | descripcion                                      
|:--------------|:--------------------------------------------------------|
|info functions | mostrar información de las funciones
|info registeres| información de los registros
| x/10x address | mostrar en hexadecimal
| x/10s address | mostrar como cadena
| x/10i address | mostrar como instrucciones
| p $eglags     | mostrar banderas
| p/t $eflags   | mosrtar banderas en binario


x/30xg

$eflags

## Comandos

- Ver los opcodes 
disassemble /r main





## Depuración

| comando       | descripcion                                      
|:--------------|:--------------------------------------------------------| 
| br main       | poner un punto de interrupción en la función main
| stepo         | avanazar por pasos
| <Enter>       | repetir la última instrucción
| si            | entrar a la función
| ni            | no entra a función
| c             | continua normal hasta alcanzar el siguiente break point
| info break    | lista breakpoints
| dele #        | borrar breakpoint


## Gdb Text User Interface
- Layouts
command
assembly
register

- Agregar un layout
```
layout assembly
```
c - x a             Entrar y salir del modo TUI
ctrl + x + n        Establecer numero de ventanas a visualizar
ctrl + x + o        Cambiar la ventana activa

- navegar por la linea de comandos cuando una ventana esta activa
c - p   arriba
c - n   abajo
c - b   izquierda
c - f   derecha

## Referencias

[GDB TUI](https://sourceware.org/gdb/onlinedocs/gdb/TUI.html)

- Ver los opcodes
- 