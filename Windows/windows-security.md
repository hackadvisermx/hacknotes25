# Windows Security

Security Identifier (SID)

```powershell
PS C:\Users\htb-student> whoami /user

USER INFORMATION
----------------

User Name        SID
================ ==============================================
ws01\htb-student S-1-5-21-2614195641-1726409526-3792725429-1002
PS C:\Users\htb-student>
```

```cmd
(SID)-(revision level)-(identifier-authority)-(subauthority1)-(subauthority2)-(etc)
```

```powershell
Get-WmiObject win32_useraccount -Filter "name = 'bob.smith'" 
```

## El registro

La estrucgura consiste en carpetas principales (root keys), en las cuales hay sub carpetas (subkeys) on sus valores.

El registro es almacenado en `C:\Windows\System32\Config\`

Las claves del registro del usuario esta almacenadas en: `C:\Windows\Users\<USERNAME>\Ntuser.dat`

- Run and RunOnece

Las claves del registro Run y RunOnce  hacen que los programas se ejecuten cada vez que un usuario inicia sesión. El valor de datos de una clave es una línea de comandos que no tiene más de 260 caracteres.

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
```

```powershell
reg query HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```


## Windows Defender

- Revisar que configuraciones de seguridad estan habilitadas

```powershell
PS C:\htb> Get-MpComputerStatus | findstr "True"
````




[Referencia del Registro](https://docs.microsoft.com/es-mx/windows/win32/sysinfo/registry-reference)