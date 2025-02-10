# Bases

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Solucion 1
Resolver con Python
```
>>> import base64
>>> base64.b64decode("bDNhcm5fdGgzX3IwcDM1")
b'l3arn_th3_r0p35'
>>> base64.b64decode("bDNhcm5fdGgzX3IwcDM1").decode()
'l3arn_th3_r0p35'


picoCTF{l3arn_th3_r0p35}
```

## Solucion 2
Resolver en bash
```
castr-picoctf@webshell:~$ echo bDNhcm5fdGgzX3IwcDM1 | base64 -d 
l3arn_th3_r0p35

castr-picoctf@webshell:~$ 

picoCTF{l3arn_th3_r0p35}
```

## Solucion 3
Resolver con cyberchef
```
Input: bDNhcm5fdGgzX3IwcDM1
Recipe: From Base64
Output: l3arn_th3_r0p35

picoCTF{l3arn_th3_r0p35}
```

## Referencia
- https://gchq.github.io/CyberChef/
