

```
 nmap -n -Pn -vv -sV 10.1.205.9
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-01 01:23 UTC
Happy 26th Birthday to Nmap, may it live to be 126!
NSE: Loaded 46 scripts for scanning.
Initiating SYN Stealth Scan at 01:23
Scanning 10.1.205.9 [1000 ports]
Discovered open port 8080/tcp on 10.1.205.9
Discovered open port 22/tcp on 10.1.205.9
Discovered open port 80/tcp on 10.1.205.9
Discovered open port 8082/tcp on 10.1.205.9
Discovered open port 8081/tcp on 10.1.205.9
Discovered open port 8084/tcp on 10.1.205.9
Discovered open port 8083/tcp on 10.1.205.9
Completed SYN Stealth Scan at 01:24, 1.71s elapsed (1000 total ports)
Initiating Service scan at 01:24
Scanning 7 services on 10.1.205.9
Completed Service scan at 01:24, 15.73s elapsed (7 services on 1 host)
NSE: Script scanning 10.1.205.9.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 01:24
Completed NSE at 01:24, 0.48s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 01:24
Completed NSE at 01:24, 0.35s elapsed
Nmap scan report for 10.1.205.9
Host is up, received user-set (0.15s latency).
Scanned at 2023-09-01 01:23:59 UTC for 18s
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE          REASON         VERSION
22/tcp   open  ssh              syn-ack ttl 63 OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http             syn-ack ttl 63 Apache httpd 2.4.29
8080/tcp open  http-proxy       syn-ack ttl 63
8081/tcp open  blackice-icecap? syn-ack ttl 63
8082/tcp open  blackice-alerts? syn-ack ttl 63
8083/tcp open  us-srv?          syn-ack ttl 63
8084/tcp open  websnp?          syn-ack ttl 63
```