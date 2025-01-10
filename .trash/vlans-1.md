# vlans 1

```
interface Vlan1
 description NATIVA
 ip address 10.1.0.1 255.255.252.0
 no ip redirects
 ip route-cache flow
!
interface Vlan5
 ip address 10.1.5.1 255.255.255.0
!
interface Vlan8
 description Biologia_Exp_Alumnos
 ip address 10.1.8.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan9
 description Biologia_Exp_Docentes
 ip address 10.1.9.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan10
 description Biologia_Exp_Libre1
 ip address 10.1.10.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan11
 description Biologia_Exp_Libre2
 ip address 10.1.11.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan12
 description Estudios Nuclueares Alumnos
 ip address 10.1.12.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan13
 description Estudios_Nucleares_Docentes
 ip address 10.1.13.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan14
 ip address 10.1.14.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan15
 description Estudios Nuclueares Libre2
 ip address 10.1.15.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan16
 description Fisica Alumnos
 ip address 10.1.16.1 255.255.255.0
 ip access-group global1 in
 no ip redirects
 ip route-cache flow
!
interface Vlan17
 description Fisica_Docentes
 ip address 10.1.17.1 255.255.255.0
 no ip redirects
 ip route-cache flow
!
interface Vlan18
 description SERVIDORES INSTITUCIONALES
 no ip address
 ip route-cache flow
!
interface Vlan19
 description FISICA_19
 ip address 10.1.19.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 ip route-cache flow
!
interface Vlan20
 description Matematicas_Alumnos
 ip address 10.1.20.1 255.255.255.0
 ip access-group globall in
 ip helper-address 10.1.205.15
!
interface Vlan21
 description Matematicas_Docentes
 ip address 10.1.21.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan22
 description Matematicas_Libres1
 ip address 10.1.22.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan23
 description Matematicas_Libres2
 ip address 10.1.23.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan24
 description Alumnos_PrepaII
 ip address 10.1.24.1 255.255.255.0
 ip access-group global1 in
 ip route-cache flow
 shutdown
!
interface Vlan25
 description Docentes_PrepaII
 ip address 10.1.25.1 255.255.255.0
 ip access-group global1 in
 no ip redirects
 ip route-cache flow
 shutdown
!
interface Vlan26
 description Wireless_PrepaII
 ip address 10.1.26.1 255.255.255.0
 ip access-group global1 in
 no ip redirects
 ip route-cache flow
 shutdown
!
interface Vlan32
 description PROMEP
 ip address 10.1.32.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan36
 description Clinica_Universitaria_Alumnos
 ip address 10.1.36.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan39
 description Clinica_Universitaria_Libre2
 ip address 10.1.39.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan40
 description Odontopediatria
 ip address 10.1.40.1 255.255.255.0
 ip access-group globall in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan41
 description ETIAE
 ip address 10.1.41.1 255.255.255.0
 ip access-group globall in
 ip helper-address 10.1.205.15
!
interface Vlan44
 description Odontologia Alumnos
 ip address 10.1.44.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan45
 description Odontologia_Docentes
 ip address 10.1.45.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan46
 description Odontologia Libre1
 ip address 10.1.46.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan47
 description Odontologia Libre2
 ip address 10.1.47.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan50
 description PS_CE_II
 ip address 148.217.50.1 255.255.255.0
!
interface Vlan51
 description Mecanica
 ip address 10.1.51.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan52
 description Mecanica_II
 ip address 10.1.52.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan53
 description Mecanica_III
 ip address 10.1.53.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan54
 description Comun_Electronica
 ip address 10.1.54.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan55
 description Comun_Electronica_II
 ip address 10.1.55.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan56
 description Comun_Electronica_III
 ip address 10.1.56.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan57
 description Electrica
 ip address 10.1.57.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan58
 description Electrica_II
 ip address 10.1.58.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan59
 description Electrica_III
 ip address 10.1.59.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan60
 description Derecho-Alumnos
 ip address 10.1.60.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan61
 description Derecho-Docentes
 ip address 10.1.61.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan62
 description Derecho-Libre1
 ip address 10.1.62.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan63
 description Derecho-Libre2
 ip address 10.1.63.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan64
 description Lab_Control-Maest_Procesos
 ip address 10.1.64.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan65
 description Lab_Control-Maest_Procesos_II
 ip address 10.1.65.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan68
 description Psicologia-Alumnos
 ip address 10.1.68.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan69
 description Psicologia-Docentes
 ip address 10.1.69.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan70
 description Psicologia-Libre1
 ip address 10.1.70.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan71
 description Psicologia-Libre2
 ip address 10.1.71.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan72
 description Ciencias Politicas Alumnos
 ip address 10.1.72.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan73
 description Ciencias Politicas Docentes
 ip address 10.1.73.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan74
 description Ciencias Politicas Libres1
 ip address 10.1.74.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan75
 description Ciencias Politicas Libres2
 ip address 10.1.75.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan76
 description Ciencias Sociales Alumnos
 ip address 10.1.76.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan77
 description Ciencias Sociales Docentes
 ip address 10.1.77.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan78
 description Ciencias Sociales Libre1
 ip address 10.1.78.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan79
 description Ciencias Sociales Libre2
 ip address 10.1.79.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan80
 description FCA_Alumnos
 ip address 10.1.80.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan81
 description FCA_Docentes
 ip address 10.1.81.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan82
 description FCA_Libre1
 ip address 10.1.82.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan83
 description FCA_Libre2
 ip address 10.1.83.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan84
 description Economia-Alumnos
 ip address 10.1.84.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan85
 description Economia-Docentes
 ip address 10.1.85.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan86
 description Economia-Libre1
 ip address 10.1.86.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan87
 description Economia-Libre2
 ip address 10.1.87.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan88
 description Antrolopologia Alumnos
 ip address 10.1.88.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan89
 description Antrolopologia Docentes
 ip address 10.1.89.1 255.255.255.0
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan90
 description VLAN VIDEOCONFERENCIA
 ip address 148.217.90.1 255.255.255.0
!
interface Vlan91
 no ip address
 ip helper-address 10.1.205.15
 shutdown
!
interface Vlan92
 description Centro_Idiomas
 ip address 10.1.92.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 ip route-cache flow
!
interface Vlan93
 description Centro_Idiomas_Docentes
 ip address 10.1.93.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan94
 description SERVIDORES ESCUELAS
 no ip address
 ip route-cache flow
!
interface Vlan95
 description Centro_Idiomas_Libre1
 ip address 10.1.95.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 ip route-cache flow
!
interface Vlan96
 description Docencia Superior Alumnos
 ip address 10.1.96.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 ip route-cache flow
!
interface Vlan97
 description Docencia Superior Docentes
 ip address 10.1.97.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 ip route-cache flow
!
interface Vlan98
 description Docencia Superior Libre 1
 ip address 10.1.98.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan99
 description Docencia Superior Libre 2
 ip address 10.1.99.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan100
 description Dr Estudios del Desarrollo Alumnos
 ip address 10.1.100.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan101
 description Dr Estudios del Desarrollo Docentes
 ip address 192.168.101.1 255.255.255.0 secondary
 ip address 10.1.101.1 255.255.255.0
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan102
 description Dr Estudios del Desarrollo Libre1
 ip address 10.1.102.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan103
 description Dr Estudios del Desarrollo Libre3
 ip address 10.1.103.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan104
 description Estudio Humanidades y Artes - Alumnos
 ip address 10.1.104.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan105
 description Estudio Humanidades y Artes - Docentes
 ip address 10.1.105.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan106
 description Estudio Humanidades y Artes - Libre1
 ip address 10.1.106.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan107
 description Estudio Humanidades y Artes - Libre2
 ip address 10.1.107.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan108
 description Filosofia Alumnos
 ip address 10.1.108.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan109
 description Filosofia_Docentes
 ip address 10.1.109.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan110
 description Filosofia Libre1
 ip address 10.1.110.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan111
 description Filosofia Libre2
 ip address 10.1.111.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.153
 ip helper-address 10.1.205.15
!
interface Vlan112
 description Historia - Alumnos
 ip address 10.1.112.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan113
 description Historia - Docentes
 ip address 10.1.113.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan114
 description Historia - Libre1
 ip address 10.1.114.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan115
 description Historia - Libre2
 ip address 10.1.115.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan116
 description Letras Alumnos
 ip address 10.1.116.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan117
 description Letras Docentes
 ip address 10.1.117.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan118
 description Letras Libre1
 ip address 10.1.118.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan119
 description Letras Libre2
 ip address 10.1.119.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan120
 description Minas-Alumnos
 ip address 10.1.120.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan121
 description Minas-Docentes
 ip address 10.1.121.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan122
 description Minas-Libre1
 ip address 10.1.122.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan123
 description Minas-Libre2
 ip address 10.1.123.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan124
 description Ingenieria_Civil_Alumnos
 ip address 10.1.124.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan125
 description Ingenieria_Civil_Docentes
 ip address 10.1.125.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan126
 description Ingenieria_Civil_Libre1
 ip address 10.1.126.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan127
 description Ingenieria_Civil_Libre2
 ip address 10.1.127.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan128
 description Ingenieria_Electronica_ALumnos
 ip address 10.1.128.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan129
 description Ingenieria_Electronica_Docentes
 ip address 10.1.129.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan130
 description Ingenieria_Electronica_Libre1
 ip address 10.1.130.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan131
 description Ingenieria_Electronica_Libre2
 ip address 10.1.131.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan133
 description Topografia II
 ip address 10.1.133.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan134
 description Topo - Hidroinf
 ip address 10.1.134.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan135
 description CIDTE
 ip address 10.1.135.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan136
 description Secundaria-Alumnos
 ip address 10.1.136.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan137
 description Secundaria-Docentes
 ip address 10.1.137.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan138
 description Secundaria-Libre1
 ip address 10.1.138.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan139
 description Secundaria-Libre2
 ip address 10.1.139.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan140
 description Musica-Alumnos
 ip address 10.1.140.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan141
 description Musica-Docentes
 ip address 10.1.141.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan142
 description Musica-Libre1
 ip address 10.1.142.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan143
 description Musica-Libre2
 no ip address
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan144
 description Biblioteca_FCA
 ip address 10.1.144.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan145
 description Biblioteca_FCA
 ip address 10.1.145.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan146
 description Biblioteca_FCA
 ip address 10.1.146.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan147
 description WLS-4-UACYA
 ip address 10.1.147.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan148
 description WLS-5-UACYA
 ip address 10.1.148.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan149
 description WLS-6-UACYA
 ip address 10.1.149.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan150
 description CC-1-UACYA
 ip address 10.1.150.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan151
 description Fisica-Wireless
 ip address 10.1.151.1 255.255.255.0
!
interface Vlan152
 description STUAZ
 ip address 10.1.152.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan200
 description INFRA WIRELESS
 ip address 10.1.200.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan205
 description Servidores Internos
 no ip address
 ip route-cache flow
!
interface Vlan210
 description CIT
 ip address 10.1.210.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan211
 description Departamento_Escolar
 ip address 10.1.211.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan212
 description Bilbioteca
 ip address 10.1.212.1 255.255.255.0
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan213
 description Bilbioteca_II
 ip address 10.1.213.1 255.255.255.0
 ip helper-address 10.1.205.15
 no ip redirects
!
interface Vlan214
 description Licenciatura en Lenguas
 ip address 10.1.214.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan215
 no ip address
 shutdown
!
interface Vlan216
 description CIT2
 ip address 10.1.216.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan217
 description NIVA-CIT
 ip address 10.1.217.1 255.255.255.0
!
interface Vlan218
 description Biblioteca Central II
 ip address 10.1.218.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan220
 ip address 10.1.220.1 255.255.255.0
 ip helper-address 10.1.205.15
!
interface Vlan230
 description SPAUAZ
 ip address 10.1.230.1 255.255.255.0
 ip access-group global1 in
 ip helper-address 10.1.205.15
!
interface Vlan240
 description Telefonia
 ip address 10.1.240.1 255.255.255.0 secondary
 ip address 148.217.240.2 255.255.255.0
 ip helper-address 10.1.205.15
 no ip redirects
 ip route-cache flow
!
interface Vlan241
 no ip address
 shutdown
!
interface Vlan300
 description CE
 ip address 172.16.39.1 255.255.255.0
 ip access-group global1 in
 no ip redirects
 ip route-cache flow
!
interface Vlan302
 no ip address
!
interface Vlan400
 description UAZ-VISITAS
 ip address 10.254.0.2 255.255.252.0
!
interface Vlan888
 no ip address
 ip route-cache flow
!
interface Vlan901
 description VLAN SALIDA E1
 no ip address
!
interface Vlan903
 description VLAN SALIDA E3
 no ip address
!
interface Vlan999
 description VLAN INTERNET LINK_6500-FGT_Internal
 ip address 148.217.254.1 255.255.255.248
 ip route-cache flow
 ip ospf network point-to-point

```