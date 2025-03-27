Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip)

Hitnts: 
1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Solucion
- Creamos una carpeta y descargamos el archivo

```
castr-picoctf@webshell:~/tabtab$ 
castr-picoctf@webshell:~/tabtab$ 
castr-picoctf@webshell:~/tabtab$ 
castr-picoctf@webshell:~/tabtab$ wget https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip
--2025-02-12 23:03:52--  https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4521 (4.4K) [application/octet-stream]
Saving to: 'Addadshashanammu.zip'

Addadshashanammu.z 100%[===============>]   4.42K  --.-KB/s    in 0s      

2025-02-12 23:03:53 (1.58 GB/s) - 'Addadshashanammu.zip' saved [4521/4521]

castr-picoctf@webshell:~/tabtab$ ls
Addadshashanammu.zip
```

- lo descomprimimos
```
castr-picoctf@webshell:~/tabtab$ ls
Addadshashanammu.zip
castr-picoctf@webshell:~/tabtab$ unzip Addadshashanammu.zip 
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
castr-picoctf@webshell:~/tabtab$ 
```

- Para ir al ultimo rincon, presionalos Tab 11 veces segun lo dice la pista, y ejecutamos el binario para obtener la bandera
```
castr-picoctf@webshell:~/tabtab$ ls
Addadshashanammu  Addadshashanammu.zip
castr-picoctf@webshell:~/tabtab$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
castr-picoctf@webshell:~/tabtab/Addadshashanammu/Almurbalarammi/Ashalmimilk
ala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ls
fang-of-haynekhtnamet
castr-picoctf@webshell:~/tabtab/Addadshashanammu/Almurbalarammi/Ashalmimilk
ala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ file fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=55548d0314fdf7999b966728d19712cdf8a52e58, not stripped
castr-picoctf@webshell:~/tabtab/Addadshashanammu/Almurbalarammi/Ashalmimilk
ala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ./fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
castr-picoctf@webshell:~/tabtab/Addadshashanammu/Almurbalarammi/Ashalmimilk
ala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ 
```