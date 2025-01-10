Can you see the flag in this BINARY, this SCRIPT can help

## Solucion

- Nos dan dos archivos un binario y un script
- Se puede sacar con el script, o directamente con strings

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-4-stage-peru/generalskills/binaryinsigth]
└─$ strings -n 20 b1n
/lib64/ld-linux-x86-64.so.2
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTable
Oh hai! Wait what? A flag? Yes, it's around here somewhere!
Fl@g{Mr_Rob0t_3th1c4l_H@ck3R25}
GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
deregister_tm_clones
__do_global_dtors_aux
__do_global_dtors_aux_fini_array_entry
__frame_dummy_init_array_entry
_GLOBAL_OFFSET_TABLE_
_ITM_deregisterTMCloneTable
__libc_start_main@@GLIBC_2.2.5
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5

```