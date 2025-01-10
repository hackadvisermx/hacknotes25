
```
dig version.bind CHAOS TXT @10.10.158.68

; <<>> DiG 9.11.3-1ubuntu1.18-Ubuntu <<>> version.bind CHAOS TXT @10.10.158.68
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8637
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 72773c6cdddf6e290100000064f3de18031dd89496c1b0b0 (good)
;; QUESTION SECTION:
;version.bind.			CH	TXT

;; ANSWER SECTION:
version.bind.		0	CH	TXT	"9.16.1-Ubuntu"

;; Query time: 0 msec
;; SERVER: 10.10.158.68#53(10.10.158.68)
;; WHEN: Sun Sep 03 02:15:04 BST 2023
;; MSG SIZE  rcvd: 95

```

```
nmap -p21,22,53,1337,1883 -sC 10.10.158.68 -T4

Starting Nmap 7.60 ( https://nmap.org ) at 2023-09-03 02:43 BST
Nmap scan report for ip-10-10-158-68.eu-west-1.compute.internal (10.10.158.68)
Host is up (0.00024s latency).

PORT     STATE SERVICE
21/tcp   open  ftp
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.210.44
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 5
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh
53/tcp   open  domain
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
1337/tcp open  waste
1883/tcp open  mqtt
MAC Address: 02:95:FA:4A:B9:37 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 9.36 seconds

```

```
nmap --script mqtt-subscribe -p 1883 10.10.188.102

Starting Nmap 7.60 ( https://nmap.org ) at 2023-09-03 03:50 BST
Nmap scan report for ip-10-10-188-102.eu-west-1.compute.internal (10.10.188.102)
Host is up (0.00035s latency).

PORT     STATE SERVICE
1883/tcp open  mosquitto version 1.6.9
| mqtt-subscribe: 
|   Topics and their most recent payloads: 
|     $SYS/broker/clients/connected: 0
|     $SYS/broker/subscriptions/count: 0
|     $SYS/broker/load/bytes/sent/15min: 0.00
|     $SYS/broker/load/messages/received/15min: 0.00
|     $SYS/broker/load/publish/sent/1min: 0.00
|     $SYS/broker/clients/disconnected: 0
|     $SYS/broker/publish/bytes/received: 0
|     $SYS/broker/load/connections/5min: 0.00
|     $SYS/broker/clients/expired: 0
|     $SYS/broker/load/bytes/received/15min: 0.00
|     $SYS/broker/load/sockets/1min: 0.00
|     $SYS/broker/load/publish/received/5min: 0.00
|     $SYS/broker/publish/messages/dropped: 0
|     $SYS/broker/load/publish/dropped/1min: 0.00
|     $SYS/broker/load/publish/sent/15min: 0.00
|     $SYS/broker/clients/total: 0
|     $SYS/broker/load/sockets/15min: 0.00
|     $SYS/broker/messages/sent: 0
|     $SYS/broker/load/messages/sent/5min: 0.00
|     $SYS/broker/publish/bytes/sent: 0
|     $SYS/broker/retained messages/count: 52
|     $SYS/broker/shared_subscriptions/count: 0
|     $SYS/broker/heap/maximum: 47688
|     $SYS/broker/messages/stored: 52
|     $SYS/broker/uptime: 33 seconds
|     $SYS/broker/publish/messages/received: 0
|     $SYS/broker/load/messages/sent/15min: 0.00
|     $SYS/broker/store/messages/bytes: 177
|     $SYS/broker/messages/received: 0
|     $SYS/broker/load/sockets/5min: 0.00
|     $SYS/broker/load/publish/sent/5min: 0.00
|     $SYS/broker/load/bytes/sent/5min: 0.00
|     $SYS/broker/load/bytes/received/1min: 0.00
|     $SYS/broker/bytes/sent: 0
|     $SYS/broker/version: mosquitto version 1.6.9
|     $SYS/broker/load/publish/received/1min: 0.00
|     $SYS/broker/load/publish/received/15min: 0.00
|     $SYS/broker/load/publish/dropped/5min: 0.00
|     $SYS/broker/clients/inactive: 0
|     $SYS/broker/store/messages/count: 52
|     $SYS/broker/bytes/received: 0
|     $SYS/broker/load/connections/1min: 0.00
|     $SYS/broker/publish/messages/sent: 0
|     $SYS/broker/load/bytes/sent/1min: 0.00
|     $SYS/broker/load/messages/received/5min: 0.00
|     $SYS/broker/load/publish/dropped/15min: 0.00
|     $SYS/broker/load/messages/received/1min: 0.00
|     $SYS/broker/heap/current: 47240
|     $SYS/broker/load/messages/sent/1min: 0.00
|     $SYS/broker/clients/active: 0
|     $SYS/broker/load/connections/15min: 0.00
|_    $SYS/broker/load/bytes/received/5min: 0.00
MAC Address: 02:69:25:F5:C9:35 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 7.46 seconds

```

```
mosquitto_sub -h 10.10.188.102 -t '#' -d
Client mosqsub|11652-ip-10-10- sending CONNECT
Client mosqsub|11652-ip-10-10- received CONNACK
Client mosqsub|11652-ip-10-10- sending SUBSCRIBE (Mid: 1, Topic: #, QoS: 0)
Client mosqsub|11652-ip-10-10- received SUBACK
Subscribed (mid: 1): 0
Client mosqsub|11652-ip-10-10- sending PINGREQ
Client mosqsub|11652-ip-10-10- received PINGRESP


```