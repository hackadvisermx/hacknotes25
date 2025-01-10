## Network

```shell-session
netstat -na
arp -a
```

## AD Environment
```cmd
systeminfo | findstr Domain
 
Get-ADUser  -Filter *

Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"

Get-ADUser -Filter * -SearchBase "OU=THM,DC=THMREDTEAM,DC=COM"
 
```

## Host Security Solutions

### Antivirus Software (AV)

```cmd
Get-Service windefend

Get-MpComputerStatus | select RealTimeProtectionEnabled

Get-NetFirewallProFile | Format-Table Name,Enabled

Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct

Get-MpThreat
 
```

## Firewall

```
Get-NetFirewallRule | select DisplayName, Enabled, Description

Test-NetConnection -ComputerName 127.0.0.1 -Port 80

(New-Object System.Net.Sockets.TcpClient("127.0.0.1","80")).Connected

Get-NetFirewallRule | select DisplayName,Enabled,Description | findstr "THM"

```

- https://github.com/PwnDexter/SharpEDRChecker
- https://github.com/PwnDexter/Invoke-EDRChecker

## Application and Services

### Instaled applications

```cmd
wmic product get name,version

```