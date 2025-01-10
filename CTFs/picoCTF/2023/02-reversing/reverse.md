Try reversing this file? Can ya? I forgot the password to this [file](https://artifacts.picoctf.net/c/369/ret). Please find it for me?

## Solucion

```
r2 ret
aaa
afl
pdf@main


 ┌─< 0x00001280      751a           jne 0x129c
│       │   0x00001282      488d3dbf0d00.  lea rdi, str.Password_correct__please_see_flag:_picoCTF3lf_r3v3r5ing_succe55ful_fe733618 ; 0x2048 ; "Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_fe733618}" ; const char *s                                                                                                                                                                              
│       │   0x00001289      e802feffff     call sym.imp.puts           ; int puts(const char *s)



```

## Bandera

picoCTF{3lf_r3v3r5ing_succe55ful_fe733618}


