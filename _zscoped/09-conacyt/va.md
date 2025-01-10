```
host svrtmp.main.conacyt.mx
svrtmp.main.conacyt.mx has address 148.228.31.19
```

```
 whois 148.228.31.19

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2023, American Registry for Internet Numbers, Ltd.
#


NetRange:       148.222.252.0 - 148.250.255.255
CIDR:           148.240.0.0/13, 148.223.0.0/16, 148.248.0.0/15, 148.224.0.0/12, 148.222.252.0/22, 148.250.0.0/16
NetName:        LACNIC-ERX-148-201-0-0
NetHandle:      NET-148-222-252-0-1
Parent:         NET148 (NET-148-0-0-0-0)
NetType:        Transferred to LACNIC
OriginAS:
Organization:   Latin American and Caribbean IP address Regional Registry (LACNIC)
RegDate:        2003-10-29
Updated:        2023-06-30
Ref:            https://rdap.arin.net/registry/ip/148.222.252.0

ResourceLink:  http://lacnic.net/cgi-bin/lacnic/whois
ResourceLink:  whois.lacnic.net


OrgName:        Latin American and Caribbean IP address Regional Registry
OrgId:          LACNIC
Address:        Rambla Republica de Mexico 6125
City:           Montevideo
StateProv:
PostalCode:     11400
Country:        UY
RegDate:        2002-07-27
Updated:        2018-03-15
Ref:            https://rdap.arin.net/registry/entity/LACNIC

ReferralServer:  whois://whois.lacnic.net
ResourceLink:  http://lacnic.net/cgi-bin/lacnic/whois

OrgTechHandle: LACNIC-ARIN
OrgTechName:   LACNIC Whois Info
OrgTechPhone:  +598-2604-2222
OrgTechEmail:  whois-contact@lacnic.net
OrgTechRef:    https://rdap.arin.net/registry/entity/LACNIC-ARIN

OrgAbuseHandle: LWI100-ARIN
OrgAbuseName:   LACNIC Whois Info
OrgAbusePhone:  +598-2604-2222
OrgAbuseEmail:  abuse@lacnic.net
OrgAbuseRef:    https://rdap.arin.net/registry/entity/LWI100-ARIN


#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2023, American Registry for Internet Numbers, Ltd.
#



Found a referral to whois.lacnic.net.

% IP Client: 200.92.164.11

% Joint Whois - whois.lacnic.net
%  This server accepts single ASN, IPv4 or IPv6 queries

% LACNIC resource: whois.lacnic.net


% Copyright LACNIC lacnic.net
%  The data below is provided for information purposes
%  and to assist persons in obtaining information about or
%  related to AS and IP numbers registrations
%  By submitting a whois query, you agree to use this data
%  only for lawful purposes.
%  2023-09-13 15:05:51 (-03 -03:00)

inetnum:     148.228.0.0/16
status:      assigned
aut-num:     N/A
owner:       Benemerita Universidad Autonoma de Puebla
ownerid:     MX-BUAP1-LACNIC
responsible: HOSTMASTER SIU-BUAP
address:     4 Sur Centro, 104,
address:     72000 - Puebla - PU
country:     MX
phone:       +52 222 2295500 [5119]
owner-c:     HOS
tech-c:      HOS
abuse-c:     HOS
inetrev:     148.228.0.0/16
nserver:     NS1.BUAP.MX
nsstat:      20230913 AA
nslastaa:    20230913
nserver:     NS2.BUAP.MX [lame - not published]
nsstat:      20230913 UH
nslastaa:    20110621
nserver:     NS3.BUAP.MX [lame - not published]
nsstat:      20230913 UH
nslastaa:    20081021
nserver:     NS4.BUAP.MX
nsstat:      20230913 AA
nslastaa:    20230913
created:     19930326
changed:     20020717

nic-hdl:     HOS
person:      HOSTMASTER SIU-BUAP
e-mail:      hostmaster@buap.mx
address:     4 Sur Centro, 104,
address:     72000 - Puebla - PU
country:     MX
phone:       +52 222 2295500 [5119]
created:     20031105
changed:     20031105

% whois.lacnic.net accepts only direct match queries.
% Types of queries are: POCs, ownerid, CIDR blocks, IP
% and AS numbers.
```




```
 host -t ns conacyt.mx
conacyt.mx name server dns3.conacyt.mx.
conacyt.mx name server dns5.conacyt.mx.
conacyt.mx name server dns4.conacyt.mx
```




```
 dig any conacyt.mx

; <<>> DiG 9.18.16-1-Debian <<>> any conacyt.mx
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 40305
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: de247bdb0940545d (echoed)
;; QUESTION SECTION:
;conacyt.mx.                    IN      ANY

;; ANSWER SECTION:
conacyt.mx.             77      IN      TXT     "083U5SQ+fA4D/fbbW2OFM+7JZAHfxAoL3TsDQ8em6y14GpebeTkrgqegGbsRaxDvHerdm72vewiBv+GmZAzTvw=="
conacyt.mx.             77      IN      TXT     "v=spf1 include:spf.protection.outlook.com ~all"
conacyt.mx.             77      IN      TXT     "google-site-verification=8BEXbdLq9TB2kK16YmBHsgXceym6dNO0vJGjOA8oD8Y"
conacyt.mx.             77      IN      TXT     "google-site-verification=Qf6YPGrhYZre2UfeaVAS33uEV2UEmjGvYFWdxLDvs00"
conacyt.mx.             77      IN      NS      dns4.conacyt.mx.
conacyt.mx.             77      IN      NS      dns3.conacyt.mx.
conacyt.mx.             77      IN      NS      dns5.conacyt.mx.
conacyt.mx.             77      IN      NS      dns1.buap.mx.

;; Query time: 6 msec
;; SERVER: 192.168.65.7#53(192.168.65.7) (TCP)
;; WHEN: Wed Sep 13 17:57:43 UTC 2023
;; MSG SIZE  rcvd: 566
```

```
dig mx conacyt.mx

; <<>> DiG 9.18.16-1-Debian <<>> mx conacyt.mx
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27559
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: a5ad4b7cfa481992 (echoed)
;; QUESTION SECTION:
;conacyt.mx.                    IN      MX

;; ANSWER SECTION:
conacyt.mx.             77      IN      MX      0 conacyt-mx.mail.protection.outlook.com.

;; Query time: 83 msec
;; SERVER: 192.168.65.7#53(192.168.65.7) (UDP)
;; WHEN: Wed Sep 13 17:55:00 UTC 2023
;; MSG SIZE  rcvd: 115
```

```
dig ns conacyt.mx

; <<>> DiG 9.18.16-1-Debian <<>> ns conacyt.mx
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 19171
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 10ff0aa2a20080a0 (echoed)
;; QUESTION SECTION:
;conacyt.mx.                    IN      NS

;; ANSWER SECTION:
conacyt.mx.             77      IN      NS      dns4.conacyt.mx.
conacyt.mx.             77      IN      NS      dns3.conacyt.mx.
conacyt.mx.             77      IN      NS      dns5.conacyt.mx.
conacyt.mx.             77      IN      NS      dns1.buap.mx.

;; Query time: 106 msec
;; SERVER: 192.168.65.7#53(192.168.65.7) (UDP)
;; WHEN: Wed Sep 13 17:56:48 UTC 2023
;; MSG SIZE  rcvd: 204
```