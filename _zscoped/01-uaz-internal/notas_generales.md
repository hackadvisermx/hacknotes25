# Notas Generales

- Parece ser el rango de conexión por VPN

10.1.233.1/24

echo 10.1.0.0/16 | httpx -title -web-server -status-code

- Telefonos : `10.1.240`
- switches : `10.2.192`
- aps : `10.3.x.x`
- 10.1.254  > equipos de conectividad entre campus

```
187.191.46.70 / parecer ser acceso externo a los sitios remotos
148.217.201.14 / a la par con la interna
201.117.251.4/24 / esto parece iigual
```


## Busquedas 
```
nmap --script smb-os-discovery -p 445 10.2.21.1/24 -n -Pn --open -v
echo 10.1.0.0/16 | httpx-toolkit -title -web-server -status-code
echo 10.2.1.1/16 | httpx-toolkit -title -web-server -status-code -follow-redirects -vhost -ip
for i in {0..254}; do nbtscan -r 10.1.$i.1/24; done | grep 10
```


| Grupo                | Subgrupo                | Ip             | pwned |
| -------------------- | ----------------------- | -------------- |-------|
| Equipo de telefonia  | Call Manager Principal  | 148.217.240.11 |  |
| Equipo de telefonia  | Call Manager Secundario | 148.217.196.11 | yes! |
| Políticas y permisos | Fortigate Siglo XXI     | 10.1.254.233   | |
| Políticas y permisos | Fortigate CUC           | 10.1.254.225   | |
| Routers              | 6500 Siglo XXI          | 10.2.192.1               | |
| Routers              | 6500 CUC                | 148.217.254.1|  |


