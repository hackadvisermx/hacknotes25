# DNS
## Jerarquia de los Dominios

### TLD ( Top-Leve Domain )

gTLD (Generic)
ccTLD (Counry Code)

### Second-Level Domain

63 Caracteres + TLD ( a-z 0-9 -)
- no puede empezar o terminar el nombre

### Subdomain

- 63 caracteres (a-z 0-9 -)
- multiples subdominios separados por . sin exceder 253 caracreres

## Tipos de registros DNS

A		Resuelven direcciones IPV4
AAAA	Resuelven IPV6
CNAME	Resuelven algun otro nombre de domino
MX		Resuelven servidores de correos
TXT		Texto libre
PTR		Reverse

## Solicitud DNS


Cuando solicitas un nombre de dominio, tu computadora revisa:

1. cache local
2. dns ISP o el que elijas (Recursive DNS Server)
3. internet  (DNS backbone)

Authoritative DNS . Responsable de almacenar los registros DNS de un dominio particular, 
tambien conosido como Nameserver

TTL especifica que tanto tiempo estaran en el cache los registros DNS
