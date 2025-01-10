```
(gdb) br *(main+59)
Breakpoint 2 at 0x401141
(gdb) r
Starting program: /root/hackdata/picoctf/gymexclusive/debugger0_b
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 2, 0x0000000000401141 in main ()
(gdb) i r
rax            0x4af4b             307019
```