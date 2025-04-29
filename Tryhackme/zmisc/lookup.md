

```
nmap -n -Pn -p- --min-rate 4000 10.10.4.87 -vv -sV --max-retries 0
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-17 03:36 UTC
NSE: Loaded 46 scripts for scanning.
Initiating SYN Stealth Scan at 03:36
Scanning 10.10.4.87 [65535 ports]
Discovered open port 22/tcp on 10.10.4.87
Discovered open port 80/tcp on 10.10.4.87
Warning: 10.10.4.87 giving up on port because retransmission cap hit (0).
Completed SYN Stealth Scan at 03:36, 16.60s elapsed (65535 total ports)
Initiating Service scan at 03:36
Scanning 2 services on 10.10.4.87
Completed Service scan at 03:36, 6.38s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.4.87.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 03:36
Completed NSE at 03:36, 0.79s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 03:36
Completed NSE at 03:36, 0.74s elapsed
Nmap scan report for 10.10.4.87
Host is up, received user-set (0.21s latency).
Scanned at 2024-12-17 03:36:05 UTC for 24s
Not shown: 49310 closed tcp ports (reset), 16223 filtered tcp ports (no-response)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 61 OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.84 seconds
           Raw packets sent: 65535 (2.884MB) | Rcvd: 60835 (2.433MB)
```

- agregamos a /etc/hosts
```
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost

212.129.28.21 vtcsec
10.10.4.87 lookup.thm

```

