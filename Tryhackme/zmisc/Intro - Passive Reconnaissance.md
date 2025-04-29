# intro - Passive Reconnaissance

- Que es iana : https://www.iana.org/
	- Administración de direcciones : https://www.iana.org/numbers
	- Adminisración de dominios: https://www.iana.org/domains/root/db

- Control de dominos en MX: https://www.iana.org/domains/root/db/mx.html


> Room: Passive Reconnaissance

https://tryhackme.com/room/passiverecon

: Task 1 :
	whois, nslookup, dig
	dnsdumpster, shodan

: Task 2: passive reconnaissance vs active reconnaissance

- passive , obtener información de fuentes publicas

- active: requiere iteración con el objetivo
  

	
: Task 3: whois

~ administración de dominios internacional:
	https://www.iana.org/
	https://www.iana.org/domains/root/db

~ hay regiones para la administración de ípsilons y dominios
	https://www.iana.org/numbers

~ cuando compramos un dominio tenemos que registrarlo

~ cada país registra y administra sus nombres de dominio
	https://www.iana.org/domains/root/db/mx.html

~ comando whois, para obtener info de un dominio


~ ejemplo: whois tryhackme.com

-> whois.namecheap.com
-> fechas de creación, actualización y vencmiento
-> nombre del que registro e informacion de contacto
-> servidores dns


~ flag: whois tryhackme.com 
	
	When was TryHackMe.com registered?
	20180705
	
	What is the registrar of TryHackMe.com?
	namecheap.com
	
	Which company is TryHackMe.com using for name servers?
	cloudflare.com


 
	
: Task 4: nslookup and ig

~ DNS server (que es ?)

- cloudfare: 1.1.1.1 1.00.1
- google: 8.8.8.8, 8.8.4.4
- quad9: 9.9.9.9 149.112.112.112

~ tabla de registros del dns: A AAAA CNAME MX SOA TXT

~ nslookup
	nslookup -type=a tryhackme.com 1.1.1.1
	nslookup -type=mx tryhackme.com

~ dig
	dig tryhackme.com
	dig tryhackme.com MX

~ ataque de transferencia de zona con dig
	dig uas.edu.mx ns 
	dig AXFR uas.edu.mx @dns-lm.uas.edu.mx  

~ trasferencia de zona con : dnsenum
	dnsenum uas.edu.mx


~ flag:	dig thmlabs.com txt
	THM{a5b83929888ed36acb0272971e438d78}


**Zone Transfer**

dig @dns.uas.edu.mx uas.edu.mx axfr
nslookup -type=any -query=axfr uas.edu.mx dns.uas.edu.mx

: Task 5 : DNSDumpster

~ flag

Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog?

remote



: Task 6 : shodan.io

~ flags

According to Shodan.io, what is the 2nd country in the world in terms of the number of publicly accessible Apache servers? : Apache

Germany

Based on Shodan.io, what is the 3rd most common port used for Apache?

8080

Based on Shodan.io, what is the 3rd most common port used for nginx? : Ngnix

8888
