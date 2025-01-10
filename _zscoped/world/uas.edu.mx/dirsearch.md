```
ffuf -u https://www.uas.edu.mx/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -ic -t 350 -e .php,.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://www.uas.edu.mx/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .php .txt 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 350
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

img                     [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 314ms]
pdf                     [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 1646ms]
                        [Status: 200, Size: 88817, Words: 10366, Lines: 2140, Duration: 373ms]
index.php               [Status: 200, Size: 88817, Words: 10366, Lines: 2140, Duration: 406ms]
multimedia              [Status: 301, Size: 242, Words: 14, Lines: 8, Duration: 620ms]
css                     [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 1668ms]
manual                  [Status: 301, Size: 238, Words: 14, Lines: 8, Duration: 325ms]
src                     [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 386ms]
js                      [Status: 301, Size: 234, Words: 14, Lines: 8, Duration: 573ms]
er                      [Status: 301, Size: 234, Words: 14, Lines: 8, Duration: 194ms]
pre                     [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 286ms]
eventos                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 264ms]
phpmyadmin              [Status: 403, Size: 212, Words: 15, Lines: 9, Duration: 153ms]
index_.php              [Status: 200, Size: 86049, Words: 10242, Lines: 2087, Duration: 368ms]
                        [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 332ms]
informes                [Status: 301, Size: 240, Words: 14, Lines: 8, Duration: 104ms]
conn                    [Status: 301, Size: 236, Words: 14, Lines: 8, Duration: 171ms]

```

/er/
https://www.uas.edu.mx/er/files/index.php
```
index.php               [Status: 200, Size: 2085, Words: 328, Lines: 58, Duration: 113ms]
img                     [Status: 301, Size: 238, Words: 14, Lines: 8, Duration: 110ms]
files                   [Status: 301, Size: 240, Words: 14, Lines: 8, Duration: 121ms]
pdf                     [Status: 301, Size: 238, Words: 14, Lines: 8, Duration: 114ms]
css                     [Status: 301, Size: 238, Words: 14, Lines: 8, Duration: 167ms]
up                      [Status: 301, Size: 237, Words: 14, Lines: 8, Duration: 376ms]
js                      [Status: 301, Size: 237, Words: 14, Lines: 8, Duration: 163ms]
temp                    [Status: 301, Size: 239, Words: 14, Lines: 8, Duration: 117ms]
fonts                   [Status: 301, Size: 240, Words: 14, Lines: 8, Duration: 168ms]
documentos              [Status: 301, Size: 245, Words: 14, Lines: 8, Duration: 236ms]
                        [Status: 200, Size: 2085, Words: 328, Lines: 58, Duration: 228ms]
conn                    [Status: 301, Size: 239, Words: 14, Lines: 8, Duration: 128ms]

```