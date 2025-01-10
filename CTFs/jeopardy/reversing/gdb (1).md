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
bit | sym | name
------------------
  0 |  CF | carry
  1 |  -- | (always 1)
  2 |  PF | parity
  3 |  -- | (always 0)
  4 |  AF | adjust
  5 |  -- | (always 0)
  6 |  ZF | zero
  7 |  SF | sign
  8 |  TF | trap
  9 |  IF | interrupt
 10 |  DF | direction
 11 |  OF | overflow

 rightmost most digit is CF

 




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
source
assembly
register

- Agregar un layout
```
set layout assembly
```
c - x a             Entrar y salir del modo TUI
ctrl + x + n        Establecer numero de ventanas a visualizar
ctrl + x + o        Cambiar la ventana activa

- navegar por la linea de comandos cuando una ventana esta activa
c - p   arriba
c - n   abajo
c - b   izquierda
c - f   derecha


## Referencias>

[GDB TUI](https://sourceware.org/gdb/onlinedocs/gdb/TUI.html)
