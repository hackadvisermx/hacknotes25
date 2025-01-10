# Actvive Reconnaissance

>> Room: Active Reconnaissance

:: Task 1 :

~ herramientas: ping, traceroute, telnet, nc
 

:: Task 2 : Web Browser

~ Developer Tools: Ctrl + Shift + I

~ Firefox Addons

-> FoxyProxy:
-> User-Agent Switcher and Manager
-> Wappalyzer



Browse to the following website and ensure that you have opened your Developer Tools on AttackBox Firefox, or the browser on your computer. Using the Developer Tools, figure out the total number of questions. : Cuantas preguntas hay en el sitio > https://static-labs.tryhackme.cloud/sites/networking-tcp/

8


:: Task 3 : Ping

~ ejecutar comandos:

	ping ip/host
 	ping 10.10.134.28
	ping -c 10.10.134.28


~ tecnico
	ICMP echo type 8
	ICMP echo reply type 0
	Tamaño del paquete 64 bytes




Which option would you use to set the size of the data carried by the ICMP echo request?

-s 

What is the size of the ICMP header in bytes?

8

Does MS Windows Firewall block ping by default? (Y/N)

Y

Deploy the VM for this task and using the AttackBox terminal, issue the command ping -c 10 10.10.167.123. How many ping replies did you get back?

10




:: Task 4 :  Traceroute 

~ Traza la ruta que siguen los paquetes 

traceroute 10.10.167.123
traceroute www.uaz.edu.mx


In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com?

172.67.69.208


In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com?

104.26.11.229

In Traceroute B, how many routers are between the two systems?

26


Start the attached VM from Task 3 if it is not already started. On the AttackBox, run traceroute 10.10.167.123. Check how many routers/hops are there between the AttackBox and the target VM.





:: Task 5 : Telnet

telnet 10.10.134.28 80                                                                       1 ⨯
Trying 10.10.134.28...
Connected to 10.10.134.28.
Escape character is '^]'.
GET / HTTP/1.1
Host:10.10.134.28

HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 14:46:24 GMT
Server: Apache/2.4.10 (Debian)
Last-Modified: Mon, 30 Aug 2021 12:09:24 GMT
ETag: "15-5cac5b436ddfa"
Accept-Ranges: bytes
Content-Length: 21
Content-Type: text/html

Telnet to port 80...
Connection closed by foreign host.

- Start the attached VM from Task 3 if it is not already started. On the AttackBox, open the terminal and use the telnet client to connect to the VM on port 80. What is the name of the running server?

Apache

- What is the version of the running server (on port 80 of the VM)?

2.4.10


:: Task 6 : Netcat. >> OJO Hay que iniciar la otra maquina virtual >>>


~ una forma

nc 10.10.18.176 80                                                                                        GET / HTTP/1.1
Host: 10.10.18.176
<Enter>
<Enter>
^C

~ otra forma

echo -e "GET / HTTP/1.1\r\nHost:10.10.18.176\t\n" | nc 10.10.18.176 80
^C


~ otra forma

$ cat req                                                                                                 127 ⨯
GET / HTTP/1.1
Host: unkwonk

nc 10.10.18.176 80 < req 

~ netcat modo chat

$ escucha
	nc -lnvp 1234
$ conecta
	nc localhost 1234

~ Escaneo de puertos >>

nc -z -v 10.10.18.176 21
nc -z -v 10.10.18.176 1-80


~ Flags

- Start the VM and open the AttackBox. Once the AttackBox loads, use Netcat to connect to the VM port 21. What is the version of the running server?

nc 10.10.18.176 21                                                                                        
220 debra2.thm.local FTP server (Version 6.4/OpenBSD/Linux-ftpd-0.17) ready.

0.17




:: Task 7 : 

