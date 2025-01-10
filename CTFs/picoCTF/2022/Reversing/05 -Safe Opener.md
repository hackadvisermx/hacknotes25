# Safe Opener

Can you open this safe? I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/463/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: `picoCTF{password`


## Solucion
- esta harcodeada en el codigo java en base 64


```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/safeopener]
└─$ echo cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz | base64 -d              
pl3as3_l3t_m3_1nt0_th3_saf3                                                                                                                     

picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```
