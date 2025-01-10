## Active Directory

_Difficulty:_ 

Go to Steampunk Island and help Ribb Bonbowford audit the Azure AD environment. What's the name of the secret file in the inaccessible folder on the _FileShare_?


## Resolviendo

```
alabaster@ssh-server-vm:~$ cd impacket/
alabaster@ssh-server-vm:~/impacket$ ls
DumpNTLMInfo.py     addcomputer.py   dpapi.py           getPac.py     keylistattack.py  mqtt_check.py     nmapAnswerMachine.py  psexec.py      registry-read.py  secretsdump.py  smbrelayx.py  ticketConverter.py  wmiquery.py
Get-GPPPassword.py  atexec.py        esentutl.py        getST.py      kintercept.py     mssqlclient.py    ntfs-read.py          raiseChild.py  rpcdump.py        services.py     smbserver.py  ticketer.py
GetADUsers.py       certipy          exchanger.py       getTGT.py     lookupsid.py      mssqlinstance.py  ntlmrelayx.py         rbcd.py        rpcmap.py         smbclient.py    sniff.py      tstool.py
GetNPUsers.py       changepasswd.py  findDelegation.py  goldenPac.py  machine_role.py   net.py            ping.py               rdp_check.py   sambaPipe.py      smbexec.py      sniffer.py    wmiexec.py
GetUserSPNs.py      dcomexec.py      getArch.py         karmaSMB.py   mimikatz.py       netview.py        ping6.py              reg.py         samrdump.py       smbpasswd.py    split.py      wmipersist.py
alabaster@ssh-server-vm:~/impacket$
```


```
certipy
Certipy v4.8.2 - by Oliver Lyak (ly4k)

usage: certipy [-v] [-h] {account,auth,ca,cert,find,forge,ptt,relay,req,shadow,template} ...

Active Directory Certificate Services enumeration and abuse

positional arguments:
  {account,auth,ca,cert,find,forge,ptt,relay,req,shadow,template}
                        Action
    account             Manage user and machine accounts
    auth                Authenticate using certificates
    ca                  Manage CA and certificates
    cert                Manage certificates and private keys
    find                Enumerate AD CS
    forge               Create Golden Certificates
    ptt                 Inject TGT for SSPI authentication
    relay               NTLM Relay to AD CS HTTP Endpoints
    req                 Request certificates
    shadow              Abuse Shadow Credentials for account takeover
    template            Manage certificate templates

options:
  -v, --version         Show Certipy's version number and exit
  -h, --help            Show this help message and exit
```




## Referencias
- https://github.com/ly4k/Certipy
