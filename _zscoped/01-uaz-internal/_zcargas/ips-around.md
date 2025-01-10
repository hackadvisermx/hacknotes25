
```
──(kali㉿kali)-[~/rh]
└─$ nmap -n -Pn -p3306,80,443,8080 -T3 10.1.205.1/24 -vv --open
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-11-29 13:14 CST
Initiating Connect Scan at 13:14
Scanning 256 hosts [4 ports/host]
Discovered open port 80/tcp on 10.1.205.2
Discovered open port 80/tcp on 10.1.205.3
Discovered open port 80/tcp on 10.1.205.4
Discovered open port 80/tcp on 10.1.205.5
Discovered open port 80/tcp on 10.1.205.8
Discovered open port 80/tcp on 10.1.205.9
Discovered open port 80/tcp on 10.1.205.20
Discovered open port 80/tcp on 10.1.205.50
Discovered open port 443/tcp on 10.1.205.1
Discovered open port 443/tcp on 10.1.205.2
Discovered open port 443/tcp on 10.1.205.3
Discovered open port 443/tcp on 10.1.205.4
Discovered open port 443/tcp on 10.1.205.5
Discovered open port 443/tcp on 10.1.205.8
Discovered open port 443/tcp on 10.1.205.20
Discovered open port 443/tcp on 10.1.205.50
Discovered open port 80/tcp on 10.1.205.60
Discovered open port 8080/tcp on 10.1.205.1
Discovered open port 8080/tcp on 10.1.205.9
Completed Connect Scan at 13:14, 3.47s elapsed (1024 total ports)
Nmap scan report for 10.1.205.1
Host is up, received user-set (0.0017s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 closed tcp port (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE    REASON
443/tcp  open  https      syn-ack
8080/tcp open  http-proxy syn-ack

Nmap scan report for 10.1.205.2
Host is up, received user-set (0.0018s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 closed tcp port (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.3
Host is up, received user-set (0.0017s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 closed tcp port (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.4
Host is up, received user-set (0.0017s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 closed tcp port (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.5
Host is up, received user-set (0.0017s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 2 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.8
Host is up, received user-set (0.0051s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 filtered tcp ports (host-unreach), 1 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.9
Host is up, received user-set (0.0051s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 closed tcp port (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE    REASON
80/tcp   open  http       syn-ack
8080/tcp open  http-proxy syn-ack

Nmap scan report for 10.1.205.20
Host is up, received user-set (0.0056s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 1 closed tcp port (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.50
Host is up, received user-set (0.0047s latency).
Scanned at 2023-11-29 13:14:17 CST for 2s
Not shown: 2 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE REASON
80/tcp  open  http    syn-ack
443/tcp open  https   syn-ack

Nmap scan report for 10.1.205.60
Host is up, received user-set (0.022s latency).
Scanned at 2023-11-29 13:14:18 CST for 1s
Not shown: 2 closed tcp ports (conn-refused), 1 filtered tcp port (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 256 IP addresses (256 hosts up) scanned in 3.50 seconds

```


```
──(kali㉿kali)-[~/rh]
└─$ echo 10.1.205.1/24 | httpx-toolkit -title -web-server -status-code -follow-redirects -vhost -ip -p 80,8080,443

    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\__/\__/ .___/_/|_|
             /_/              v1.1.5

		projectdiscovery.io

Use with caution. You are responsible for your actions.
Developers assume no liability and are not responsible for any misuse or damage.
https://10.1.205.3 [200] [" + ID_EESX_Welcome + "] [] [10.1.205.3]
https://10.1.205.3 [200] [" + ID_EESX_Welcome + "] [] [10.1.205.3]
https://10.1.205.5 [200] [] [] [10.1.205.5]
https://10.1.205.8 [200] [Welcome to Citrix Hypervisor 8.2.0] [] [10.1.205.8]
http://10.1.205.9 [200] [Index of /] [Apache/2.4.29 (Ubuntu)] [vhost] [10.1.205.9]
https://10.1.205.1:8080 [303,200] [] [none] [10.1.205.1] [https://10.1.205.1:8080/auth/login?from_page=/]
https://10.1.205.1 [200] [Fireware XTM User Authentication] [] [10.1.205.1]
https://10.1.205.1 [200] [Fireware XTM User Authentication] [] [10.1.205.1]
http://10.1.205.9 [200] [Index of /] [Apache/2.4.29 (Ubuntu)] [vhost] [10.1.205.9]
https://10.1.205.1:8080 [303,200] [] [none] [10.1.205.1] [https://10.1.205.1:8080/auth/login?from_page=/]
http://10.1.205.20 [301,] [Dimension] [WatchGuard] [vhost] [10.1.205.20] [https://10.1.205.20/]
https://10.1.205.20 [] [Dimension] [WatchGuard] [vhost] [10.1.205.20]
http://10.1.205.5 [301,200] [] [] [10.1.205.5] [https://10.1.205.5/]
http://10.1.205.5 [301,200] [] [] [10.1.205.5] [https://10.1.205.5/]
http://10.1.205.5 [301,200] [] [] [10.1.205.5] [https://10.1.205.5/]
http://10.1.205.3 [301,200] [" + ID_EESX_Welcome + "] [] [10.1.205.3] [https://10.1.205.3/]
https://10.1.205.50 [200] [] [] [10.1.205.50]
https://10.1.205.50 [200] [] [] [10.1.205.50]
http://10.1.205.60 [200] [Redirigir al navegador a otra URL] [Apache/2.4.54 (Debian)] [vhost] [10.1.205.60]
http://10.1.205.50 [301,200] [] [] [10.1.205.50] [https://10.1.205.50/]

```