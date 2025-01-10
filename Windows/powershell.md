# Powershell


| Comando                    | Descripcion |
|---------------------------|---------------------------------------------------|
| Set-Location               | Cambiar de directorio
| Get-ChildItem              | Obtener los subdirectorios dentro de un directorio
| Get-Content                | Mostrar el contenido de un archivo
| Select-String              | Selecciona una cadena de texto de acuerdo a un patron
| Get-FileHash               | Obtener el hash de un archivo 
| Get-Item -Path f -Stream * | Mostrar streams ocultos en archivos (ADS)
| wmic process call create   | Ejecutar un stream oculto



- Algunos ejemplos

```
Set-Location .\Documents\
Get-ChildItem -Hidden
Get-Content 
Get-ChildItem -hidden -directory -filter '*3*' 
Get-Content -path .\1.txt | Measure-Object -word 
Get-Content -path .\1.txt | Select -Index 551
(Get-Content .\1.txt)[551,6991]
Get-Content .\2.txt |  Select-String -pattern 'redryder'
```
- Mas ejemplos
```
 Get-FileHash -Algorithm MD5 '.\db file hash.txt'
 Get-Item -Path .\deebee.exe -Stream *
C:\tools\strings64.exe -accepteula .\deebee.exe | Select-String -pattern 'THM'
wmic process call create $(Resolve-Path .\deebee.exe:hidedb)
 ```


```
Get-Content -path .\1.txt | Measure-Object -word 


```
