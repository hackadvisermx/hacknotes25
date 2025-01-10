```
 nmap -n -Pn 10.1.205.9 -vvv   
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-01 18:38 CST
Initiating Connect Scan at 18:38
Scanning 10.1.205.9 [1000 ports]
Discovered open port 80/tcp on 10.1.205.9
Discovered open port 22/tcp on 10.1.205.9
Discovered open port 8080/tcp on 10.1.205.9
Discovered open port 8081/tcp on 10.1.205.9
Discovered open port 8084/tcp on 10.1.205.9
Discovered open port 8083/tcp on 10.1.205.9
Discovered open port 8082/tcp on 10.1.205.9
Discovered open port 8085/tcp on 10.1.205.9
Completed Connect Scan at 18:38, 4.69s elapsed (1000 total ports)
Nmap scan report for 10.1.205.9
Host is up, received user-set (0.065s latency).
Scanned at 2024-01-01 18:38:26 CST for 5s
Not shown: 992 closed tcp ports (conn-refused)
PORT     STATE SERVICE         REASON
22/tcp   open  ssh             syn-ack
80/tcp   open  http            syn-ack
8080/tcp open  http-proxy      syn-ack
8081/tcp open  blackice-icecap syn-ack
8082/tcp open  blackice-alerts syn-ack
8083/tcp open  us-srv          syn-ack
8084/tcp open  websnp          syn-ack
8085/tcp open  unknown         syn-ack

Read data files from: /usr/bin/../share/nmap
9,Nmap done: 1 IP address (1 host up) scanned in 4.71 seconds

```

```
PORT     STATE SERVICE          REASON  VERSION
80/tcp   open  http             syn-ack Apache httpd 2.4.29

```