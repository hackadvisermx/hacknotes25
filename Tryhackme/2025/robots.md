
## Escaneo de puertos

```
┌──(root㉿kali)-[/home/kali/tmp/tryhackme/robots]
└─# nmap -sV -sC -T5 -p- -n -Pn -v 10.10.239.215
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-16 09:51 CDT
NSE: Loaded 157 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 09:51
Completed NSE at 09:51, 0.00s elapsed
Initiating NSE at 09:51
Completed NSE at 09:51, 0.00s elapsed
Initiating NSE at 09:51
Completed NSE at 09:51, 0.00s elapsed
Initiating SYN Stealth Scan at 09:51
Scanning 10.10.239.215 [65535 ports]
Discovered open port 22/tcp on 10.10.239.215
Discovered open port 80/tcp on 10.10.239.215
SYN Stealth Scan Timing: About 17.61% done; ETC: 09:54 (0:02:25 remaining)
SYN Stealth Scan Timing: About 23.37% done; ETC: 09:55 (0:03:20 remaining)
SYN Stealth Scan Timing: About 31.05% done; ETC: 09:56 (0:03:35 remaining)
SYN Stealth Scan Timing: About 51.80% done; ETC: 09:58 (0:03:19 remaining)
SYN Stealth Scan Timing: About 58.20% done; ETC: 09:58 (0:02:57 remaining)
Stats: 0:04:09 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 58.52% done; ETC: 09:58 (0:02:56 remaining)
SYN Stealth Scan Timing: About 66.01% done; ETC: 09:58 (0:02:34 remaining)
Warning: 10.10.239.215 giving up on port because retransmission cap hit (2).
SYN Stealth Scan Timing: About 72.12% done; ETC: 09:58 (0:02:08 remaining)
Discovered open port 9000/tcp on 10.10.239.215
SYN Stealth Scan Timing: About 78.35% done; ETC: 09:58 (0:01:39 remaining)
SYN Stealth Scan Timing: About 83.78% done; ETC: 09:58 (0:01:16 remaining)
SYN Stealth Scan Timing: About 89.73% done; ETC: 09:58 (0:00:48 remaining)
Completed SYN Stealth Scan at 09:59, 488.86s elapsed (65535 total ports)
Initiating Service scan at 09:59
Scanning 3 services on 10.10.239.215
Completed Service scan at 09:59, 11.56s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.239.215.
Initiating NSE at 09:59
Completed NSE at 09:59, 5.06s elapsed
Initiating NSE at 09:59
Completed NSE at 09:59, 0.73s elapsed
Initiating NSE at 09:59
Completed NSE at 09:59, 0.00s elapsed
Nmap scan report for 10.10.239.215
Host is up (0.18s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 (protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.61
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.61 (Debian)
| http-robots.txt: 3 disallowed entries 
|_/harming/humans /ignoring/human/orders /harm/to/self
|_http-title: 403 Forbidden
9000/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-server-header: Apache/2.4.52 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: Host: robots.thm

NSE: Script Post-scanning.
Initiating NSE at 09:59
Completed NSE at 09:59, 0.00s elapsed
Initiating NSE at 09:59
Completed NSE at 09:59, 0.00s elapsed
Initiating NSE at 09:59
Completed NSE at 09:59, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 506.72 seconds
           Raw packets sent: 70780 (3.114MB) | Rcvd: 139233 (19.601MB)

```
# Robots

- Robots
```
http://10.10.239.215/robots.txt

Disallow: /harming/humans
Disallow: /ignoring/human/orders
Disallow: /harm/to/self
```

## Web 80

```
http://10.10.239.215/harming/humans/
http://10.10.239.215/ignoring/human/orders/

http://robots.thm/harm/to/self/
```

# http://robots.thm/harm/to/self/ 

- Registramos al usuario hacker con fecha 02/12/1971
- Sacamos el m5sum para el password
```
┌──(root㉿kali)-[/home/kali/tmp/tryhackme/robots]
└─# echo -n "hacker0212" | md5sum
38a47ca06fc361922683f992b4a86841  -

```

- Creamos un user pas el xss con fecha 02/12/1971 y le sacamos el md5sum para el password
```
<script>alert(2)</script>

┌──(root㉿kali)-[/home/kali/tmp/tryhackme/robots]
└─# echo -n "<script>alert(2)</script>0212" | md5sum     
a655ecffbc84ace8b02df06daf400055  -

a655ecffbc84ace8b02df06daf400055
```


### Directorios 
```
┌──(root㉿kali)-[/home/kali/tmp/tryhackme/robots]
└─# ffuf -u http://robots.thm/harm/to/self/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 300 -ic -e .php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://robots.thm/harm/to/self/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 300
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

login.php               [Status: 200, Size: 795, Words: 125, Lines: 36, Duration: 185ms]
index.php               [Status: 200, Size: 662, Words: 99, Lines: 35, Duration: 228ms]
                        [Status: 200, Size: 662, Words: 99, Lines: 35, Duration: 228ms]
admin.php               [Status: 200, Size: 370, Words: 29, Lines: 28, Duration: 190ms]
css                     [Status: 301, Size: 319, Words: 20, Lines: 10, Duration: 180ms]
register.php            [Status: 200, Size: 976, Words: 155, Lines: 39, Duration: 3287ms]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 180ms]
config.php              [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 193ms]
[WARN] Caught keyboard interrupt (Ctrl-C)
```


## Web 9000

http://robots.thm:9000/

```
http://robots.thm:9000/server-status

Forbidden

You don't have permission to access this resource.
Apache/2.4.52 (Ubuntu) Server at robots.thm Port 9000
```



## Referencias

### Writeups
- https://0xb0b.gitbook.io/writeups/tryhackme/2025/robots
- https://jaxafed.github.io/posts/tryhackme-robots/

