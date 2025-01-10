# Reversing commands 1

- vaciado hexadecimal con hexdump
```
hexdump -C binary
```

- ver el interior del binario con objdump

| Comando               | Acción
|:----------------------|:--------------------------|
| objdump -d binary     | desensambla el binario
| objdump -x binary     | muestra el encabezado

secciones interesantes son: .text y .rodata

## Ver la traza con :  strace y ltrace

> verificar llamadas a funciones del sistema
```
man syscalls
strace ./binary
```
Ejemplos de esas funciones: execv(), write()

> verificar llamadas a funciones en librerias (c library)
```
ltrace binary
```
 
 Referencias
 [Hopper diass for MAC](https://www.hopperapp.com)
