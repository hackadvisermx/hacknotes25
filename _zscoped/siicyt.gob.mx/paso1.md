
```bash
# whois.mx


Domain Name:       siicyt.gob.mx

Created On:        2001-07-27
Expiration Date:   2023-07-26
Last Updated On:   2022-07-27
Registrar:         AKKY ONLINE SOLUTIONS, S.A. DE C.V.
URL:               http://www.akky.mx
Whois TCP URI:     whois.akky.mx
Whois Web URL:     http://www.akky.mx/herramientas/whois.jsf

Registrant:
   Name:           CONACYT  Sistema Integrado de Informacion sobre investigacion Cientifica y Tecno
   City:           No hay informacion
   State:          No hay informacion
   Country:        No Information

Administrative Contact:
   Name:           Jesus Monreal
   City:           Ciudad de Mexico
   State:          Distrito Federal
   Country:        Mexico

Technical Contact:
   Name:           Jesus Monreal
   City:           Ciudad de Mexico
   State:          Distrito Federal
   Country:        Mexico

Billing Contact:
   Name:           Jesus Monreal
   City:           Ciudad de Mexico
   State:          Distrito Federal
   Country:        Mexico

Name Servers:
   DNS:            dns1.buap.mx
   DNS:            dns3.conacyt.mx       148.228.31.20
   DNS:            dns4.conacyt.mx       148.207.151.16
   DNS:            dns5.conacyt.mx       148.207.151.17
```


```bash
dig a siicyt.gob.mx @1.1.1.1

; <<>> DiG 9.10.6 <<>> a siicyt.gob.mx @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48702
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;siicyt.gob.mx.			IN	A

;; ANSWER SECTION:
siicyt.gob.mx.		60	IN	A	45.60.113.125
siicyt.gob.mx.		60	IN	A	45.60.86.125

;; Query time: 3091 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Tue Jan 03 19:37:05 CST 2023
;; MSG SIZE  rcvd: 74
```

```bash
dig ns siicyt.gob.mx @1.1.1.1

; <<>> DiG 9.10.6 <<>> ns siicyt.gob.mx @1.1.1.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16829
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;siicyt.gob.mx.			IN	NS

;; ANSWER SECTION:
siicyt.gob.mx.		60	IN	NS	dns5.conacyt.mx.
siicyt.gob.mx.		60	IN	NS	dns1.buap.mx.
siicyt.gob.mx.		60	IN	NS	dns3.conacyt.mx.
siicyt.gob.mx.		60	IN	NS	dns4.conacyt.mx.

;; Query time: 3031 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Tue Jan 03 19:40:32 CST 2023
;; MSG SIZE  rcvd: 131
```

```bash
dig ns  siicyt.gob.mx @148.207.151.17

; <<>> DiG 9.10.6 <<>> ns siicyt.gob.mx @148.207.151.17
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21721
;; flags: qr aa rd; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 4
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;siicyt.gob.mx.			IN	NS

;; ANSWER SECTION:
siicyt.gob.mx.		60	IN	NS	dns1.buap.mx.
siicyt.gob.mx.		60	IN	NS	dns3.conacyt.mx.
siicyt.gob.mx.		60	IN	NS	dns5.conacyt.mx.
siicyt.gob.mx.		60	IN	NS	dns4.conacyt.mx.

;; ADDITIONAL SECTION:
dns3.conacyt.mx.	60	IN	A	148.228.31.20
dns4.conacyt.mx.	60	IN	A	148.207.151.16
dns5.conacyt.mx.	60	IN	A	148.207.151.17

;; Query time: 3026 msec
;; SERVER: 148.207.151.17#53(148.207.151.17)
;; WHEN: Tue Jan 03 19:41:47 CST 2023
;; MSG SIZE  rcvd: 179
```