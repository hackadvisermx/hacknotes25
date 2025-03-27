# Linux Enumeration

- Enumerar hosts

```bash
/etc/hosts
/etc/resolv.conf 
```

- Enumerar pings

```bash
for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); do
```


## System

- Linux distribution and release version

```bash
ls /etc/*-release
/etc/lsb-release  /etc/os-release

cat /etc/*-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.4 LTS"
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.4 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal

```
- Hostname
```
hostname
red-linux-enumeration
```
- /etc/passwd
```bash
user@red-linux-enumeration:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
```

- TimeZone
```bash
ubuntu@Linux4n6:~$ cat /etc/timezone 
Asia/Karachi
```

```bash
ubuntu@Linux4n6:~$ cat /etc/passwd | column -t -s :
root                  x  0      0      root                                /root                    /bin/bash
daemon                x  1      1      daemon                              /usr/sbin                /usr/sbin/nologin
```


- /etc/shadow
```bash
user@red-linux-enumeration:~$ cat /etc/shadow
cat: /etc/shadow: Permission denied
```

- groups 
```bash
user@red-linux-enumeration:~$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,strategos
tty:x:5:syslog
disk:x:6:
lp:x:7:

```
- maill
```
user@red-linux-enumeration:~$ ls -lh /var/mail
total 0
```
- Installed aplications
```
ls -lh /usr/bin
ls -lh /usr/sbin
dpkg -l 
```

## Users

- who, whoami, w, id

```
user@red-linux-enumeration:~$ who
user     pts/0        2022-12-21 02:28 (10.10.123.224)
user@red-linux-enumeration:~$ whoami
user
user@red-linux-enumeration:~$ w
 02:38:50 up 18 min,  1 user,  load average: 0.00, 0.14, 0.46
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
user     pts/0    10.10.123.224    02:28    2.00s  0.06s  0.00s w
user@red-linux-enumeration:~$ id
uid=1005(user) gid=1005(user) groups=1005(user),27(sudo)
user@red-linux-enumeration:~$ 
```

- last, sudo -l

```bash
user@red-linux-enumeration:~$ last
user     pts/0        10.10.123.224    Wed Dec 21 02:28   still logged in
reboot   system boot  5.4.0-120-generi Wed Dec 21 02:20   still running
reboot   system boot  5.4.0-120-generi Mon Jun 20 13:10 - 13:13  (00:02)
randa    pts/0        10.20.30.1       Mon Jun 20 11:00 - 11:01  (00:00)
reboot   system boot  5.4.0-120-generi Mon Jun 20 09:58 - 11:01  (01:03)

wtmp begins Mon Jun 20 09:58:27 2022
user@red-linux-enumeration:~$ sudo -l
[sudo] password for user: 
Matching Defaults entries for user on red-linux-enumeration:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user may run the following commands on red-linux-enumeration:
    (ALL : ALL) ALL
user@red-linux-enumeration:~$ 

```

- sudoers list
```bash
ubuntu@Linux4n6:~$ sudo cat /etc/sudoers
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults	env_reset
Defaults	mail_badpass
Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root	ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo	ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```



## Networking
- ip
```bash
user@red-linux-enumeration:~$ ip address show
user@red-linux-enumeration:~$ ip a s
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:28:2a:2b:e5:77 brd ff:ff:ff:ff:ff:ff
    inet 10.10.13.38/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2199sec preferred_lft 2199sec
    inet6 fe80::28:2aff:fe2b:e577/64 scope link 
       valid_lft forever preferred_lft forever
```

- interfaces
```bash
ubuntu@Linux4n6:~$ cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
ubuntu@Linux4n6:~$ ls /etc/network/interfaces.d/*
ls: cannot access '/etc/network/interfaces.d/*': No such file or directory
ubuntu@Linux4n6:~$ 
```


- dns servers
```bash
user@red-linux-enumeration:~$ cat /etc/resolv.conf 

nameserver 127.0.0.53
options edns0 trust-ad
search eu-west-1.compute.internal
```

- hosts
```bash
ubuntu@Linux4n6:~$ cat /etc/network/interfaces
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
ubuntu@Linux4n6:~$ ls /etc/network/interfaces.d/*
ls: cannot access '/etc/network/interfaces.d/*': No such file or directory
ubuntu@Linux4n6:~$ 
```


- ports 
`netstat`
-a show listening, no-listening
-p show PID
-t  TCP
-u UDP
-l show only listening 
-n show numeric instad resolving
```bash
user@red-linux-enumeration:~$ sudo netstat -ptl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:ldap            0.0.0.0:*               LISTEN      748/slapd           
tcp        0      0 localhost:ircd          0.0.0.0:*               LISTEN      741/inspircd        
tcp        0      0 ip-10-10-13-38.e:domain 0.0.0.0:*               LISTEN      610/named           
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN      610/named           
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN      580/systemd-resolve 
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      693/sshd: /usr/sbin 
tcp        0      0 localhost:953           0.0.0.0:*               LISTEN      610/named           
tcp6       0      0 [::]:ldap               [::]:*                  LISTEN      748/slapd           
tcp6       0      0 red-linux-enumer:domain [::]:*                  LISTEN      610/named           
tcp6       0      0 ip6-localhost:domain    [::]:*                  LISTEN      610/named           
tcp6       0      0 [::]:ftp                [::]:*                  LISTEN      637/vsftpd          
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      693/sshd: /usr/sbin 
tcp6       0      0 ip6-localhost:953       [::]:*                  LISTEN      610/named           
user@red-linux-enumeration:~$ 
```

- List open files (losf)
-i  internt a network conection
-:667 limita a un cireto puerto

```
user@red-linux-enumeration:~$ sudo lsof -i :6667
```


```
sudo lsof -i -P -n

```


- Login information
```bash
ubuntu@Linux4n6:~$ sudo last -f /var/log/wtmp
reboot   system boot  5.4.0-1029-aws   Fri Mar 31 06:06   still running
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 21:00   still running
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 20:50 - 21:00  (00:10)
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 09:40 - 09:43  (00:03)
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 05:01 - 09:23  (04:22)
reboot   system boot  5.4.0-1029-aws   Sat Apr 16 22:51 - 23:10  (00:18)
reboot   system boot  5.4.0-1029-aws   Sat Apr 16 20:10 - 21:43  (01:32)
wtmp begins Sat Apr 16 20:10:29 2022
```

- Logs de autenticación
```bash
ubuntu@Linux4n6:~$ cat /var/log/auth.log | tail
Mar 31 06:07:32 Linux4n6 gnome-keyring-daemon[1244]: The SSH agent was already initialized
Mar 31 06:07:32 Linux4n6 polkitd(authority=local): Registered Authentication Agent for unix-session:2 (system bus name :1.70 [/usr/lib/x86_64-linux-gnu/polkit-mate/polkit-mate-authentication-agent-1], object path /org/mate/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Mar 31 06:07:39 Linux4n6 dbus-daemon[591]: [system] Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
Mar 31 06:08:00 Linux4n6 pkexec[1805]: ubuntu: Error executing command as another user: Not authorized [USER=root] [TTY=unknown] [CWD=/home/ubuntu] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Mar 31 06:12:39 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /etc/sudoers
Mar 31 06:12:39 Linux4n6 sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Mar 31 06:12:39 Linux4n6 sudo: pam_unix(sudo:session): session closed for user root
Mar 31 06:14:29 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f /var/log/wtmp
Mar 31 06:14:29 Linux4n6 sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Mar 31 06:14:29 Linux4n6 sudo: pam_unix(sudo:session): session closed for user root
```


## Running Services

`ps aux`

```
user@red-linux-enumeration:~$ ps aux | grep THM
randa        638  0.0  0.0   2608   592 ?        Ss   02:21   0:00 /bin/sh -c /home/randa/THM-24765.sh
randa        646  0.0  0.2   6892  2316 ?        S    02:21   0:00 /bin/bash /home/randa/THM-24765.sh
user        2702  0.0  0.0   6432   720 pts/0    S+   03:14   0:00 grep --color=auto THM

```


## Cron jobs

```bash
ubuntu@Linux4n6:~$ cat /etc/crontab 
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
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
ubuntu@Linux4n6:~$
```

### Service startup

```bash
ubuntu@Linux4n6:~$ ls /etc/init.d/
acpid             cups-browsed       lvm2                         rsync
alsa-utils        dbus               lvm2-lvmpolld                rsyslog
anacron           gdm3               multipath-tools              saned
apparmor          grub-common        network-manager              screen-cleanup
apport            hddtemp            networking                   speech-dispatcher
atd               hibagent           open-iscsi                   spice-vdagent
avahi-daemon      hwclock.sh         open-vm-tools                ssh
bluetooth         irqbalance         openvpn                      udev
console-setup.sh  iscsid             plymouth                     ufw
cron              kerneloops         plymouth-log                 unattended-upgrades
cryptdisks        keyboard-setup.sh  pppd-dns                     uuidd
cryptdisks-early  kmod               procps                       whoopsie
cups              lightdm            pulseaudio-enable-autospawn  x11-common
ubuntu@Linux4n6:~$ 
```

### .Bashrc

```bash
ubuntu@Linux4n6:~$ cat .bashrc 
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```

### Sudo execution history
```bash
ubuntu@Linux4n6:~$ cat /var/log/auth.log* | grep -i COMMAND | tail
Apr 17 21:02:52 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last -f
Apr 17 21:02:58 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/last
Apr 17 21:04:29 Linux4n6 sudo: tryhackme : user NOT in sudoers ; TTY=pts/0 ; PWD=/home/tryhackme ; USER=root ; COMMAND=/usr/bin/apt-get install apache2
Apr 17 21:07:45 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/syslog
Apr 17 21:08:18 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/syslog
Apr 17 21:08:40 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/syslog
Apr 17 21:08:55 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/syslog
Apr 17 21:10:53 Linux4n6 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /var/log/syslog
Mar 31 06:07:11 Linux4n6 sudo:   ubuntu : TTY=unknown ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/python3 -m websockify 80 localhost:5901 -D
Mar 31 06:07:11 Linux4n6 sudo:   ubuntu : TTY=unknown ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/sbin/runuser -l ubuntu -c vncserver :1 -depth 24 -geometry 1900x1200
ubuntu@Linux4n6:~$ 
```

### Bash history

```bash
ubuntu@Linux4n6:~$ cat ~/.bash_history 
ls -a
ls -al
unlink .bash_history
ls -a
rm -rf bash_logout
history -w
ls -a
ls -al
```

### Files accessed using vim
```bash
ubuntu@Linux4n6:~$ cat ~/.viminfo 
# This viminfo file was generated by Vim 8.1.
# You may edit it if you're careful!

# Viminfo version
|1,4

# Value of 'encoding' when this file was written
*encoding=latin1


# hlsearch on (H) or off (h):
```

## Syslog
- The Syslog contains messages that are recorded by the host about system activity
```bash
ubuntu@Linux4n6:~$ cat /var/log/syslog* | head
Mar 31 06:07:11 Linux4n6 rsyslogd: [origin software="rsyslogd" swVersion="8.2001.0" x-pid="608" x-info="https://www.rsyslog.com"] rsyslogd was HUPed
Mar 31 06:07:12 Linux4n6 udisksd[615]: Acquired the name org.freedesktop.UDisks2 on the system message bus
Mar 31 06:07:12 Linux4n6 systemd[1]: Started Disk Manager.
Mar 31 06:07:12 Linux4n6 systemd[862]: Started Pending report trigger for Ubuntu Report.
Mar 31 06:07:12 Linux4n6 blueman-mechanism[589]: Unable to init server: Could not connect: Connection refused
Mar 31 06:07:12 Linux4n6 systemd[862]: Reached target Paths.
Mar 31 06:07:12 Linux4n6 systemd[862]: Reached target Timers.
Mar 31 06:07:12 Linux4n6 systemd[862]: Starting D-Bus User Message Bus Socket.
Mar 31 06:07:12 Linux4n6 systemd[862]: Listening on GnuPG network certificate management daemon.
Mar 31 06:07:12 Linux4n6 systemd[862]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
```

### Auth logs
- The auth logs contain information about users and authentication-related logs
```bash
ubuntu@Linux4n6:~$ cat /var/log/auth.log* | head
Mar 31 06:07:16 Linux4n6 sshd[1088]: Server listening on 0.0.0.0 port 22.
Mar 31 06:07:16 Linux4n6 sshd[1088]: Server listening on :: port 22.
Mar 31 06:07:16 Linux4n6 sudo: pam_unix(sudo:session): session closed for user root
Mar 31 06:07:16 Linux4n6 CRON[807]: pam_unix(cron:session): session closed for user ubuntu
Mar 31 06:07:16 Linux4n6 runuser: pam_unix(runuser-l:session): session closed for user ubuntu
Mar 31 06:07:16 Linux4n6 sudo: pam_unix(sudo:session): session closed for user root
Mar 31 06:07:16 Linux4n6 CRON[808]: pam_unix(cron:session): session closed for user ubuntu
Mar 31 06:07:23 Linux4n6 lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Mar 31 06:07:23 Linux4n6 systemd-logind[614]: New session c1 of user lightdm.
Mar 31 06:07:23 Linux4n6 systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
ubuntu@Linux4n6:~$
```

### Third-party logs
- Similar to the syslog and authentication logs, the `/var/log/` directory contains logs for third-party applications such as webserver, database, or file share server logs.
```bash
ubuntu@Linux4n6:~$ ls /var/log
Xorg.0.log             cloud-init.log  gdm3                    prime-offload.log
Xorg.0.log.old         cups            gpu-manager-switch.log  prime-supported.log
alternatives.log       dist-upgrade    gpu-manager.log         private
alternatives.log.1     dmesg           hp                      samba
amazon                 dmesg.0         journal                 speech-dispatcher
apt                    dmesg.1.gz      kern.log                syslog
auth.log               dmesg.2.gz      kern.log.1              syslog.1
auth.log.1             dmesg.3.gz      kern.log.2.gz           syslog.2.gz
auth.log.2.gz          dmesg.4.gz      landscape               unattended-upgrades
btmp                   dpkg.log        lastlog                 wtmp
btmp.1                 dpkg.log.1      lightdm
cloud-init-output.log  fontconfig.log  openvpn
ubuntu@Linux4n6:~$ 
```