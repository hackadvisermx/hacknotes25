
```cmd
arp -a
```

```cmd
C:\Windows\System32\drivers\etc\hosts
```

```cmd
ipconfig /all
```


## System
- Systeminfo
```
PS C:\Users\user> systeminfo 

PS C:\Users\user> systeminfo | findstr /s 'os'
Host Name:                 RED-WIN-ENUM
OS Name:                   Microsoft Windows Server 2019 Datacenter
OS Manufacturer:           Microsoft Corporation
PS C:\Users\user>

PS C:\Users\user> systeminfo | findstr /I /C:'version'
OS Version:                10.0.17763 N/A Build 17763
BIOS Version:              Amazon EC2 1.0, 10/16/2017


```
- Installed updates
```cmd
PS C:\Users\user> wmic qfe get Caption,Description
Caption                                     Description
http://support.microsoft.com/?kbid=5015731  Update
http://support.microsoft.com/?kbid=4470502  Update
http://support.microsoft.com/?kbid=4470788  Security Update
http://support.microsoft.com/?kbid=4480056  Update
http://support.microsoft.com/?kbid=4486153  Update

PS C:\Users\user> (wmic qfe get Caption,Description | Measure-Object -line).Lines 
31 

PS C:\Users\user> wmic qfe get Caption,Description | Measure-Object -line         

Lines Words Characters Property 
----- ----- ---------- -------- 
   31     
```

- Runnning 
```cmd
PS C:\Users\user> net start
These Windows services are started: 

   Amazon SSM Agent
   Application Host Helper Service
   Background Tasks Infrastructure Service
   Base Filtering Engine
   Certificate Propagation
   CNG Key Isolation
   COM+ Event System
   Computer Browser
   Connected Devices Platform Service
   CoreMessaging
   Cryptographic Services
   Data Sharing Service
   DCOM Server Process Launcher
   Device Setup Manager



PS C:\Users\user> wmic product get name,version,vendor
Name                                                            Vendor
Version      
Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.28.29910     Microsoft Corporation
14.28.29910  
AWS Tools for Windows                                           Amazon Web Services Developer Relations  
3.15.1248    
Amazon SSM Agent                                                Amazon Web Services
3.0.529.0    
aws-cfn-bootstrap                                               Amazon Web Services
2.0.5        
AWS PV Drivers                                                  Amazon Web Services
8.3.4        
Microsoft Visual C++ 2019 X64 Additional Runtime - 14.28.29910  Microsoft Corporation
14.28.29910 
```


## Users

- whoami
```cmd
PS C:\Users\user> whoami
red-win-enum\user

PS C:\Users\user> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description
    State
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Enabled
SeSecurityPrivilege                       Manage auditing and security log                                   Enabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Enabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Enabled


PS C:\Users\user> whoami /groups

GROUP INFORMATION
-----------------

Group Name                                                    Type             SID                                          Attributes
============================================================= ================ ============================================ ===============================================================
Everyone                                                      Well-known group S-1-1-0                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114                                    Mandatory group, Enabled by default, Enabled group
RED-WIN-ENUM\sshusers                                         Alias            S-1-5-21-1966530601-3185510712-10604624-1016 Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                                        Alias            S-1-5-32-544                                 Mandatory group, Enabled by default, Enabled group, Group  

```

- net user

```cmd
PS C:\Users\user> net user

User accounts for \\RED-WIN-ENUM

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest
jane                     michael                  peter
randa                    sshd                     strategos
user                     WDAGUtilityAccount
The command completed successfully.

PS C:\Users\user> net group
This command can be used only on a Windows Domain Controller.

More help is available by typing NET HELPMSG 3515.

PS C:\Users\user> net localgroup

Aliases for \\RED-WIN-ENUM

-------------------------------------------------------------------------------
*Access Control Assistance Operators
*Administrators
*Backup Operators


PS C:\Users\user> net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
peter
strategos
user
The command completed successfully.

```

- net accounts
```cmd
PS C:\Users\user> net accounts
Force user logoff how long after time expires?:       Never
Minimum password age (days):                          0
Maximum password age (days):                          42
Minimum password length:                              0
Length of password history maintained:                None
Lockout threshold:                                    Never
Lockout duration (minutes):                           30
Lockout observation window (minutes):                 30
Computer role:                                        SERVER
The command completed successfully.

PS C:\Users\user> net accounts /domain
The request will be processed at a domain controller for domain WORKGROUP.

System error 1355 has occurred.

The specified domain either does not exist or could not be contacted.

PS C:\Users\user>

```

## Networking

- IP
```cmd
PS C:\Users\user> ipconfig

Windows IP Configuration


Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . : eu-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::3984:bb:6f55:c6d0%4
   IPv4 Address. . . . . . . . . . . : 10.10.220.93
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 10.10.0.1
PS C:\Users\user> ipconfig /all

Windows IP Configuration

   Host Name . . . . . . . . . . . . : RED-WIN-ENUM
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : eu-west-1.ec2-utilities.amazonaws.com
                                       eu-west-1.compute.internal

Ethernet adapter Ethernet 3:

   Connection-specific DNS Suffix  . : eu-west-1.compute.internal
   Description . . . . . . . . . . . : Amazon Elastic Network Adapter
   Physical Address. . . . . . . . . : 02-E2-0A-CF-29-3D
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::3984:bb:6f55:c6d0%4(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.10.220.93(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Lease Obtained. . . . . . . . . . : Wednesday, December 21, 2022 3:30:22 AM
   Lease Expires . . . . . . . . . . : Wednesday, December 21, 2022 5:00:22 AM
   Default Gateway . . . . . . . . . : 10.10.0.1
   DHCP Server . . . . . . . . . . . : 10.10.0.1
   DHCPv6 IAID . . . . . . . . . . . : 134353458
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-E3-D1-2B-0E-F8-30-D0-72-3F
   DNS Servers . . . . . . . . . . . : 10.0.0.2
   NetBIOS over Tcpip. . . . . . . . : Enabled
PS C:\Users\user>

```

- Ports

```cmd
PS C:\Users\user> netstat -an | findstr /c:"TCP"
  TCP    0.0.0.0:22             0.0.0.0:0              LISTENING
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:5357           0.0.0.0:0              LISTENING
```


```cmd
PS C:\Users\user> arp -a

Interface: 10.10.220.93 --- 0x4
  Internet Address      Physical Address      Type
  10.10.0.1             02-c8-85-b5-5a-aa     dynamic
  10.10.187.227         02-1f-1a-73-55-c5     dynamic
  10.10.255.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
PS C:\Users\user>

```

```cmd
PS C:\Users\user> netstat -abno

Active Connections

  Proto  Local Address          Foreign Address        State           PID  
  TCP    0.0.0.0:22             0.0.0.0:0              LISTENING       2064 
 [sshd.exe]
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       4   
 Can not obtain ownership information
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       848 
  RpcSs
 [svchost.exe]
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4   
 Can not obtain ownership information
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       964 
  TermService
 [svchost.exe]
  TCP    0.0.0.0:5357           0.0.0.0:0              LISTENING       4   
 Can not obtain ownership information
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4 
 Can not obtain ownership information
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4 
 Can not obtain ownership information
  TCP    0.0.0.0:49664          0.0.0.0:0              LISTENING       484 
 Can not obtain ownership information
  TCP    0.0.0.0:49665          0.0.0.0:0              LISTENING       316 

```







