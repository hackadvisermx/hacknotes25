# Process and Services

## Procesos

- Listando los procesos en powershell

```cmd
Get-Process | select-object Processname
```



## Servicios 

- Listado de servicios, corriendo, los 2 primeros, formato de lista (fl)

```cmd
Get-Service | ? {$_.Status -eq "Running"} | select -First 2 |fl
```

- Listando servicios que tienen la palabra fox
```cmd
 Get-Service | ? {$_.DisplayName -like "*fox*"} | fl
```


- Iniciar el administrador de servicios

```cmd
services.msc
```

Cuentas integradas de windows que tienen que ver con servicios:

- LocalService
- NetworkService
- LocalSystem

### Manejo de servicios con utileria: sc

- Información de un servicio

```cmd
sc qc wuauserv
```

- Iniciar o parar servicios con sc

```cmd
sc stop wuauserv
```

- Configurar servicios 

```cmd
sc config wuauserv binPath=C:\Winbows\Perfectlylegitprogram.exe
```

- Mostrar permisos

```cmd
sc sdshow wuauserv
```

Discretionary Access Control List (DACL) - Controlar el acceso a un objeto
System Access Control List (SACL) - controlar los accesos a una cuenta

- **Security Descriptor Definition Language (SDDL).**

Lenguaje de definición del descriptor de seguridad, El lenguaje de definición de descriptores de seguridad (SDDL) define el formato de cadena que las funciones ConvertSecurityDescriptorToStringSecurityDescriptor y ConvertStringSecurityDescriptorToSecurityDescriptor usan para describir un descriptor de seguridad como una cadena de texto. El lenguaje también define elementos de cadena para describir información en los componentes de un descriptor de seguridad.

- Examinar los permisos de un servicio desde PowerShell

```cmd
Get-ACL -Path HKLM:\System\CurrentControlSet\Services\wuauserv | Format-List
```


Recursos

- [Acerca de los Servicios ](https://docs.microsoft.com/en-us/windows/win32/services/about-services)

- [Servicios críticos del sistema](https://docs.microsoft.com/es-mx/windows/win32/rstmgr/critical-system-services)

- [Componentes de Windows - Servicios](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_components#Services)
  
  