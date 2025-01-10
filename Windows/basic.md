# Basic


- Verson y build desde powershell
  
```cmd
Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber
```

- Arbol de archivos

```cmd
tree "c:\Program Files"
tree "c:\Program Files" /f | more
```
