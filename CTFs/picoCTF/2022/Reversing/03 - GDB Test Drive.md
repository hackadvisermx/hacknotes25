# GDB Test Drive

Can you get the flag? Download this [binary](https://artifacts.picoctf.net/c/119/gdbme). Here's the test drive instructions:

-   `$ chmod +x gdbme`
-   `$ gdb gdbme`
-   `(gdb) layout asm`
-   `(gdb) break *(main+99)`
-   `(gdb) run`
-   `(gdb) jump *(main+104)`

## solucion

picoCTF{d3bugg3r_dr1v3_93b87433}


https://daddycocoaman.dev/posts/picoctf/2022/picoctf-2022-reverse-engineering/#gdb-test-drive



- cambiar entre ventanas con layout asm
```
ctrl+x
o
```

- salir del layout
```
ctrl +x
a
```