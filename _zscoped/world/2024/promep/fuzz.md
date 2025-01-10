```
ffuf -u https://promep.sep.gob.mx/solicitudesv3/FUZZ -w /tools/seclists/Discovery/Web-Content/big.txt -t 100

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
 :: Threads          : 100
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

administracion          [Status: 301, Size: 189, Words: 9, Lines: 2, Duration: 317ms]
comun                   [Status: 301, Size: 180, Words: 9, Lines: 2, Duration: 486ms]
docs                    [Status: 301, Size: 179, Words: 9, Lines: 2, Duration: 854ms]
general                 [Status: 301, Size: 182, Words: 9, Lines: 2, Duration: 36ms]
img                     [Status: 301, Size: 178, Words: 9, Lines: 2, Duration: 659ms]
js                      [Status: 301, Size: 177, Words: 9, Lines: 2, Duration: 21ms]
mantenimiento           [Status: 301, Size: 188, Words: 9, Lines: 2, Duration: 357ms]
packs                   [Status: 301, Size: 180, Words: 9, Lines: 2, Duration: 201ms]
:: Progress: [20476/20476] :: Job [1/1] :: 69 req/sec :: Duration: [0:02:18] :: Errors: 0 ::
```