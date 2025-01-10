```
root@kali:~# arp-scan -l
Interface: eth0, type: EN10MB, MAC: 0e:56:6e:85:24:c5, IPv4: 10.0.0.101
Starting arp-scan 1.9.7 with 256 hosts (https://github.com/royhills/arp-scan)
10.0.0.1        0e:4b:85:4d:6a:d3       (Unknown: locally administered)
10.0.0.2        0e:4b:85:4d:6a:d3       (Unknown: locally administered)
10.0.0.102      0e:b7:64:9e:59:49       (Unknown: locally administered)
10.0.0.103      0e:cf:87:ad:da:f1       (Unknown: locally administered)

8 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9.7: 256 hosts scanned in 2.054 seconds (124.63 hosts/sec). 4 responded
root@kali:~# 

```


```
root@kali:~# curl -I 10.0.0.102
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 3831
Accept-Ranges: bytes
Server: HFS 2.3
Set-Cookie: HFS_SID=0.578116914723068; path=/; 
Cache-Control: no-cache, no-store, must-revalidate, max-age=-1

```

```
root@kali:~# searchsploit HFS 2.3
----------------------------------------------------- ---------------------------------
 Exploit Title                                       |  Path
----------------------------------------------------- ---------------------------------
HFS (HTTP File Server) 2.3.x - Remote Command Execut | windows/remote/49584.py
HFS Http File Server 2.3m Build 300 - Buffer Overflo | multiple/remote/48569.py
Rejetto HTTP File Server (HFS) 2.2/2.3 - Arbitrary F | multiple/remote/30850.txt
Rejetto HTTP File Server (HFS) 2.3.x - Remote Comman | windows/remote/34668.txt
Rejetto HTTP File Server (HFS) 2.3.x - Remote Comman | windows/remote/39161.py
Rejetto HTTP File Server (HFS) 2.3a/2.3b/2.3c - Remo | windows/webapps/34852.txt
----------------------------------------------------- ---------------------------------
Shellcodes: No Results

```

## 10.0.0.103

### Escaneo

```bash
root@kali:~/Downloads# nmap -n -Pn -vv 10.0.0.103
Starting Nmap 7.92 ( https://nmap.org ) at 2025-01-06 22:19 IST
Initiating ARP Ping Scan at 22:19
Scanning 10.0.0.103 [1 port]
Completed ARP Ping Scan at 22:19, 0.07s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 22:19
Scanning 10.0.0.103 [1000 ports]
Discovered open port 22/tcp on 10.0.0.103
Discovered open port 80/tcp on 10.0.0.103
Discovered open port 9000/tcp on 10.0.0.103
Completed SYN Stealth Scan at 22:19, 0.05s elapsed (1000 total ports)
Nmap scan report for 10.0.0.103
Host is up, received arp-response (0.00029s latency).
Scanned at 2025-01-06 22:19:57 IST for 0s
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE    REASON
22/tcp   open  ssh        syn-ack ttl 64
80/tcp   open  http       syn-ack ttl 64
9000/tcp open  cslistener syn-ack ttl 63
MAC Address: 0E:CF:87:AD:DA:F1 (Unknown)

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.28 seconds
           Raw packets sent: 1001 (44.028KB) | Rcvd: 1001 (40.040KB)
root@kali:~/Downloads# 

```

##### Puerto 80
```
root@kali:~/Downloads# curl -I 10.0.0.103
HTTP/1.1 302 Found
Server: nginx
Date: Mon, 06 Jan 2025 16:51:29 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: keep-alive
Cache-Control: no-cache
Content-Security-Policy: 
Location: http://10.0.0.103/users/sign_in
Permissions-Policy: interest-cohort=()
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-Frame-Options: SAMEORIGIN
X-Gitlab-Meta: {"correlation_id":"01JGY8ENC83DZ6NRRBKDJ123DY","version":"1"}
X-Permitted-Cross-Domain-Policies: none
X-Request-Id: 01JGY8ENC83DZ6NRRBKDJ123DY
X-Runtime: 0.057516
X-Ua-Compatible: IE=edge
X-Xss-Protection: 1; mode=block
Strict-Transport-Security: max-age=63072000
Referrer-Policy: strict-origin-when-cross-origin

```