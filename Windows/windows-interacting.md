# Interacting with the Windows Operating System

Se puede interactuar con windows de diversas formas:

## Remote Desktop Protocol (RDP)

## Windows Command Line

### CMD

- Pedir ayuda de un comando:

```cmd
help
help vol
ipconfig /?
```

### PowerShell

#### Cmdlets

Powershell utiliza cmdlets, un cmdlet es un comando ligero que se usa en el entorno de PowerShell, los cmdlets realizan una acción y suelen devolver un objeto de Microsoft .NET, por ejemplo:

```powershell
Get-ChildItem 
Get-ChildItem -Recurese
Get-ChildItem -Path c:\users\administrator
Get-ChildItem -Path c:\users\administrator -Recurse
```

#### Aliases

Muchos cmdlets en powershell tienen también alias. Por ejemplo `Set-Location` es `cd` o `sl`, o para `Get-ChildItem` es `ls` o `gci`.

- Para obtener los alias:

```powershell
get-alias
```

- Crear un alias

```powershell
New-Alias -Name "Show-Files" Get-ChildItem
```

- Obtener ayuda

```powershell
Get-Help Get-AppPackage
```

#### Ejecutar Scripts

Podemos ejecutar scripts en powershell de dierentes maneras

```powershell
PS C:\htb> .\PowerView.ps1;Get-LocalGroup |fl
```

- Importar todas las funciones de un modulo, listar los modulos cargados

```powersh
Import-Module .\PowerView.ps1
Get-Module | select Name,ExportedCommands | fl
```

#### **Execution Policy**

Algunas veces nos encontramos con que no podemos ejecutar los scripts esto debido a una catacterística de seguridad que prevene de la ejecución maliciosa de scripts, llamada `Execution Policy`.

```powershell
Get-ExecutionPolicy -List
```




Referencias:
- [Información general del cmdlet](https://docs.microsoft.com/es-mx/powershell/scripting/developer/cmdlet/cmdlet-overview?view=powershell-7)