	 # Need For Speed
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/cd51b2c95be9f3626db6fe6665afb5a3/need-for-speed).
Hint: What is the final key?



## Solucion

- ver en wikipedia > ELf Format
	- Encabezado
	- Encabezados de secciones
	- Tabla de symbolos
- ver los bytes del enabezado 52bytes para 32 bits, 64 bytes para 64 bits
```
xxd -l 64 need-for-speed
```

- ver código con readelf
```
readelf -h need-for-speed
readelf -S need-for-speed
readelf -x .rodata need-for-speed
readelf -x .text need-for-speed

readelf -s need-for-speed
```


- ver el codigo con obdump

```bash
objdump -t need-for-speed

objdump -t need-for-speed  | grep 'F .text'
0000000000000690 l     F .text	0000000000000000              deregister_tm_clones
00000000000006d0 l     F .text	0000000000000000              register_tm_clones
0000000000000720 l     F .text	0000000000000000              __do_global_dtors_aux
0000000000000760 l     F .text	0000000000000000              frame_dummy
00000000000009d0 g     F .text	0000000000000002              __libc_csu_fini
000000000000076a g     F .text	0000000000000087              decrypt_flag
000000000000080e g     F .text	0000000000000021              alarm_handler
00000000000008d8 g     F .text	0000000000000042              header
000000000000087d g     F .text	000000000000002f              get_key
0000000000000960 g     F .text	0000000000000065              __libc_csu_init
0000000000000660 g     F .text	000000000000002b              _start
000000000000091a g     F .text	000000000000003e              main
00000000000007f1 g     F .text	000000000000001d              calculate_key
00000000000008ac g     F .text	000000000000002c              print_flag
000000000000082f g     F .text	000000000000004e              set_timer


objdump -D need-for-speed -M intel | grep '<main>:' -A 20
objdump -D need-for-speed -M intel | grep '<calculate_key>:' -A 20
```

~ que es gdb

https://www.gnu.org/software/gdb/
https://sourceware.org/gdb/current/onlinedocs/gdb/

~ ayuda dentro de gb

	help


~ cargar el binario con gdb

gdb need-for-speed
 
~ obtener informacion de las funciones

```bash
info functions
``` 

~ desensamblar main (att)

	disassemble main

~ cambiar el sabor a intel y desembalar de nuevo

	set disassembly-flavor intel
	disassemble main

~ modificar en settins de gdb

	nano ~/.gdbinit
	set disassembly-flavor intel


~ poner punto de interrupción
	break main
	info break

~ ejecutar programa

	run o  r


### way 1 : saltarse la función (poner break en ella y regresarse sin ejecutarla)

	b set_timer
	return 
	continue
 

### way 2 : mandar llamar solo las funciones necesarias

	b main
	call (int) get_key()
	call (int) print_flag()
	PICOCTF{Good job keeping bus #3b89d39c speeding along!}

## way 3 - sigalrm

handle SIGALRM ignore

PICOCTF{Good job keeping bus #24c43740 speeding along!}

### way 4 : parchar el binario

	- mostrar la función main en gdb
		0x0000000000000992 <+30>:	call   0x87f <set_timer>

	- ir hex editor offset 992 y poner nops
		hexeditor need-for-speed
		ctrl + t  992
		90 90 90 90 90  ( 992 a 997


## way5: parchar el binario con dd

```bash
echo '\x90\x90\x90\x90\x90' | dd of=flag bs=1 seek=$((0x938)) count=5 conv=notrunc

o
printf '\x90\x90\x90\x90\x90' | dd of=need-for-speed bs=1 seek=2360 count=5 conv=notrunc 

5+0 records in
5+0 records out
5 bytes copied, 6.9804e-05 s, 71.6 kB/s

```
	2360 es 0x938 pero en decimal



ref>
sol1: https://blog.ramgi.dev/needforspeed.html
sols: https://github.com/HHousen/PicoCTF-2019/blob/master/Reverse%20Engineering/Need%20For%20Speed/README.md

Gdb:
https://web.eecs.umich.edu/~sugih/pointers/gdbQS.html


