# Windows event logs

- Event Logs
Event logs record events taking place in the execution of a system to provide an audit trail that can be used to understand the activity of the system and to diagnose problems. They are essential to understand the activities of complex systems, particularly in applications with little user interaction (such as server applications).

- SIEMs (Security information and event management)
  - Ejemplos: splunk y elastic
  - Algunas características de un SIEM son:
    - Threat detection
    - Investigation
    - Time to respond
  - Algunas otras son:
    - basic security monitoring
    - advaced threeat detection
    - forensic & incident responde
    - log collection
    - normalization
    - notificarion and alerts
    - security incident detection
    - threar response workflow

## Eventos en Widnows

- [Tipos de evento en windows](https://docs.microsoft.com/en-us/windows/win32/eventlog/event-types)
- [Tipos de logs en windows](https://docs.microsoft.com/en-us/windows/win32/eventlog/eventlog-key)

## Herramientas

### wevtutil.exe

- [wevtutil](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)

- Contar cuantos tipos de logs:
```
wevtutil el | Measure-Object -line
```
- Consulta 3 elementos de log Application leyendolos en reversa y mostrando el resultado en modo texto
```
wevtutil qe Application /c:3 /rd:true /f:text
```

### powershell Get-WinEvent

- obtener todos los logs en una computadora local : ```Get-WinEvent -ListLog *```
- obtener los nombres de los proveedores de log que contienen una cadena especifica ```Get-WinEvent -ListProvider *PowerShell*```





```
Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS' }
Get-WinEvent -FilterHashtable @{LogName='Application';ProviderName='MsiInstaller'}
```

(Get-WinEvent -ListProvider Microsoft-Windows-PowerShell).Events | Format-Table Id, Description | Measure-Object -line

### xpath

- [Xpath](https://docs.microsoft.com/en-us/windows/win32/wes/consuming-events#xpath-10-limitations)
- [Xpath Reference](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100))
```
Get-WinEvent -Logname Application -FilterXpath '*/System/EventID=100'
wevtutil qe Application /q:*/System[EventID=100] /f:text /c:1
Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"]'
Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=101 and */System/Provider[@Name="WLMS"]'
Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="System"'
```


 Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4724'
 Get-WinEvent -LogName Application -FilterXPath '*/System/Provider[@Name="WLMS"] and System/TimeCreated[@SystemTime="2020-12-15T01:09:08.940277500Z"]]'

- Powershell downgrade atack
```
Get-WinEvent -path 'C:\Users\Administrator\Desktop\merged.evtx' -FilterXPath '*/System/EventID=400'
```

- Application log clear
```
Get-WinEvent -path 'C:\Users\Administrator\Desktop\merged.evtx' -FilterXPath '*/System/EventID=104'
Get-WinEvent -path 'C:\Users\Administrator\Desktop\merged.evtx' -FilterXPath '*/*/EventID=104' | Format-List *
Get-WinEvent -path 'C:\Users\Administrator\Desktop\merged.evtx' -FilterXPath '*/*/EventID=4104' -oldest -maxevents 1 | Format-List *
```


