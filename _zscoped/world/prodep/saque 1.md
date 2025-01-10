
## Directorios

```
ffuf -u https://promep.sep.gob.mx/solicitudesv3/FUZZ -w /tools/seclists/Discovery/Web-Content/big.txt -t 50

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://promep.sep.gob.mx/solicitudesv3/FUZZ
 :: Wordlist         : FUZZ: /tools/seclists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 50
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

administracion          [Status: 301, Size: 189, Words: 9, Lines: 2, Duration: 108ms]
avisos                  [Status: 301, Size: 181, Words: 9, Lines: 2, Duration: 109ms]
comun                   [Status: 301, Size: 180, Words: 9, Lines: 2, Duration: 109ms]
contacto                [Status: 301, Size: 183, Words: 9, Lines: 2, Duration: 123ms]
docs                    [Status: 301, Size: 179, Words: 9, Lines: 2, Duration: 104ms]
email                   [Status: 301, Size: 180, Words: 9, Lines: 2, Duration: 189ms]
favicons                [Status: 301, Size: 183, Words: 9, Lines: 2, Duration: 112ms]
general                 [Status: 301, Size: 182, Words: 9, Lines: 2, Duration: 106ms]
imagenes                [Status: 301, Size: 183, Words: 9, Lines: 2, Duration: 125ms]
img                     [Status: 301, Size: 178, Words: 9, Lines: 2, Duration: 111ms]
js                      [Status: 301, Size: 177, Words: 9, Lines: 2, Duration: 105ms]
mantenimiento           [Status: 301, Size: 188, Words: 9, Lines: 2, Duration: 115ms]
pdfs                    [Status: 301, Size: 179, Words: 9, Lines: 2, Duration: 166ms]
public                  [Status: 301, Size: 181, Words: 9, Lines: 2, Duration: 105ms]
:: Progress: [20476/20476] :: Job [1/1] :: 428 req/sec :: Duration: [0:00:53] :: Errors: 0 ::
```

```
Index.php               [Status: 200, Size: 3618, Words: 449, Lines: 65, Duration: 159ms]
	administracion          [Status: 301, Size: 189, Words: 9, Lines: 2, Duration: 112ms]
avisos                  [Status: 301, Size: 181, Words: 9, Lines: 2, Duration: 102ms]
captcha.php             [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 116ms]
comun                   [Status: 301, Size: 180, Words: 9, Lines: 2, Duration: 104ms]
contacto                [Status: 301, Size: 183, Words: 9, Lines: 2, Duration: 111ms]
contador.txt            [Status: 200, Size: 4, Words: 1, Lines: 1, Duration: 118ms]
docs                    [Status: 301, Size: 179, Words: 9, Lines: 2, Duration: 117ms]
email                   [Status: 301, Size: 180, Words: 9, Lines: 2, Duration: 374ms]
error.php               [Status: 200, Size: 2181, Words: 336, Lines: 59, Duration: 113ms]
favicons                [Status: 301, Size: 183, Words: 9, Lines: 2, Duration: 111ms]
funciones.php           [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 114ms]
general                 [Status: 301, Size: 182, Words: 9, Lines: 2, Duration: 129ms]
imagenes                [Status: 301, Size: 183, Words: 9, Lines: 2, Duration: 110ms]
img                     [Status: 301, Size: 178, Words: 9, Lines: 2, Duration: 112ms]
index1.php              [Status: 302, Size: 7718, Words: 537, Lines: 159, Duration: 169ms]
index.php               [Status: 200, Size: 3618, Words: 449, Lines: 65, Duration: 198ms]
info.php                [Status: 200, Size: 53636, Words: 2370, Lines: 680, Duration: 134ms]
js                      [Status: 301, Size: 177, Words: 9, Lines: 2, Duration: 117ms]
mantenimiento           [Status: 301, Size: 188, Words: 9, Lines: 2, Duration: 122ms]
pdfs                    [Status: 301, Size: 179, Words: 9, Lines: 2, Duration: 110ms]
public                  [Status: 301, Size: 181, Words: 9, Lines: 2, Duration: 114ms]
resultados.php          [Status: 200, Size: 1948, Words: 249, Lines: 58, Duration: 161ms]X§
```

## Interesante

- https://promep.sep.gob.mx/solicitudesv3/info.php
- https://promep.sep.gob.mx/solicitudesv3/avisos/ , https://promep.sep.gob.mx/solicitudesv3/avisos/aviso_integral.php
