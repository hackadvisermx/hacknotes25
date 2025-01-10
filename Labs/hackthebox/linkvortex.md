

```
linkvortex nmap -n -Pn -p- --min-rate 4000 10.10.11.47 -vv -sV --max-retries 0
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-20 00:03 UTC
NSE: Loaded 46 scripts for scanning.
Initiating SYN Stealth Scan at 00:03
Scanning 10.10.11.47 [65535 ports]
Discovered open port 80/tcp on 10.10.11.47
Discovered open port 22/tcp on 10.10.11.47
Warning: 10.10.11.47 giving up on port because retransmission cap hit (0).
Completed SYN Stealth Scan at 00:03, 16.50s elapsed (65535 total ports)
Initiating Service scan at 00:03
Scanning 2 services on 10.10.11.47
Completed Service scan at 00:03, 6.26s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.47.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 00:03
Completed NSE at 00:03, 0.61s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 00:03
Completed NSE at 00:03, 0.52s elapsed
Nmap scan report for 10.10.11.47
Host is up, received user-set (0.12s latency).
Scanned at 2024-12-20 00:03:35 UTC for 24s
Not shown: 43219 closed tcp ports (reset), 22314 filtered tcp ports (no-response)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 63 Apache httpd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.29 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 54491 (2.180MB)
➜  linkvortex
```

```
curl linkvortex.htb/robots.txt
User-agent: *
Sitemap: http://linkvortex.htb/sitemap.xml
Disallow: /ghost/
Disallow: /p/
Disallow: /email/
Disallow: /r/
```

