# Applications and Services

We will continue learning more about the system
-   Installed applications  
-   Services and processes
-   Sharing files and printers      
-   Internal services: DNS and local web applications

It is necessary to understand what the system provides in order to get the benefit of the information.

## Installed Applications

First, we start enumerating the system for installed applications by checking the application's name and version. As a red teamer, this information will benefit us. We may find vulnerable software installed to exploit and escalate our system privileges. Also, we may find some information, such as plain-text credentials, is left on the system that belongs to other systems or services.

We will be using the wmic Windows command to list all installed applications and their version.

```shell-session
wmic product get name,version

Name                                                            Version
Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.28.29910     14.28.29910
AWS Tools for Windows                                           3.15.1248
Amazon SSM Agent                                                3.0.529.0
aws-cfn-bootstrap                                               2.0.5
AWS PV Drivers                                                  8.3.4
Microsoft Visual C++ 2019 X64 Additional Runtime - 14.28.29910  14.28.29910
```

Another interesting thing is to look for particular text strings, hidden directories, backup files. Then we can use the PowerShell cmdlets, Get-ChildItem, as follow:

```shell-session
 Get-ChildItem -Hidden -Path C:\Users\kkidd\Desktop\


    Directory: C:\Users\kkidd\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        12/1/2021   4:53 PM            282 desktop.ini
```

## Services and Process  

Windows services enable the system administrator to create long-running executable applications in our own Windows sessions. Sometimes Windows services have misconfiguration permissions, which escalates the current user access level of permissions. Therefore, we must look at running services and perform services and processes reconnaissance.  For more details, you can read about process discovery on [Attack MITRE](https://attack.mitre.org/techniques/T1057/).

Process discovery is an enumeration step to understand what the system provides. The red team should get information and details about running services and processes on a system. We need to understand as much as possible about our targets. This information could help us understand common software running on other systems in the network. For example, the compromised system may have a custom client application used for internal purposes. Custom internally developed software is the most common root cause of escalation vectors. Thus, it is worth digging more to get details about the current process.  

For more details about core Windows processes from the blue team perspective, check out the TryHackMe room: [Core Windows Process](https://tryhackme.com/room/btwindowsinternals).

## Sharing files and Printers

Sharing files and network resources is commonly used in personal and enterprise environments. System administrators misconfigure access permissions, and they may have useful information about other accounts and systems. For more information on printer hacking, we suggest trying out the following TryHackMe room: [Printer Hacking 101](https://tryhackme.com/room/printerhacking101).

## Internal services: DNS, local web applications, etc

Internal network services are another source of information to expand our knowledge about other systems and the entire environment. To get more details about network services that are used for external and internal network services, we suggest trying out the following rooms: [Network Service](https://tryhackme.com/room/networkservices), [Network Service2](https://tryhackme.com/room/networkservices2).

The following are some of the internal services that are commonly used that we are interested in:

-   DNS Services
-   Email Services
-   Network File Share
-   Web application
-   Database service


## Ejemplo

```
C:\Users\kkidd>net start | findstr /s "THM"
   THM Service


PS C:\Users\kkidd> wmic service where "name like 'THM Service'" get Name,PathName
Name         PathName
THM Service  c:\Windows\thm-service.exe


PS C:\Users\kkidd> Get-Process -Name thm-service
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
     78       9    12664       5684              2772   0 thm-service


PS C:\Users\kkidd> netstat -noa |findstr "LISTENING" |findstr "2772"
  TCP    0.0.0.0:13337          0.0.0.0:0              LISTENING       2772
  TCP    [::]:13337             [::]:0                 LISTENING       2772

C:\Users\kkidd>curl http://10.10.169.152:13337
Hi the flag is: THM{S3rv1cs_1s_3numerat37ed}

C:\Users\kkidd>nslookup
Default Server:  ip-10-0-0-2.eu-west-1.compute.internal
Address:  10.0.0.2

> server 10.10.169.152
Default Server:  ip-10-10-169-152.eu-west-1.compute.internal
Address:  10.10.169.152

> ls -d thmredteam.com
[ip-10-10-169-152.eu-west-1.compute.internal]
 thmredteam.com.                SOA    ad.thmredteam.com hostmaster.thmredteam.com. (749 900 600 86400 3600)
 thmredteam.com.                A      10.10.129.59
 thmredteam.com.                NS     ad.thmredteam.com
 _msdcs                         NS     ad.thmredteam.com

```