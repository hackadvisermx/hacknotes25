```
 whois provident.com.mx

Domain Name:       provident.com.mx

Created On:        2000-03-08
Expiration Date:   2025-03-07
Last Updated On:   2024-03-03
Registrar:         CSC Corporate Domains, Inc
URL:               http://cscglobal.com

Registrant:
   Name:           Domain Administrator
   City:           Leeds
   State:          ENG
   Country:        United Kingdom

Administrative Contact:
   Name:           Domain Administrator
   City:           Leeds
   State:          ENG
   Country:        United Kingdom

Technical Contact:
   Name:           DNS Administrator
   City:           Wilmington
   State:          Delaware
   Country:        United States

Billing Contact:
   Name:           ccTLD Billing
   City:           Wilmington
   State:          Delaware
   Country:        United States

Name Servers:
   DNS:            ns1.netnames.net
   DNS:            ns2.netnames.net
   DNS:            ns5.netnames.net
   DNS:            ns6.netnames.net

DNSSEC DS Records:
```

```
subfinder -d prvident.com.mx

               __    _____           __
   _______  __/ /_  / __(_)___  ____/ /__  _____
  / ___/ / / / __ \/ /_/ / __ \/ __  / _ \/ ___/
 (__  ) /_/ / /_/ / __/ / / / / /_/ /  __/ /
/____/\__,_/_.___/_/ /_/_/ /_/\__,_/\___/_/

		projectdiscovery.io

[INF] Current subfinder version v2.6.6 (latest)
[INF] Loading provider config from /root/.config/subfinder/provider-config.yaml
[INF] Enumerating subdomains for prvident.com.mx
^C
➜  ~ subfinder -d provident.com.mx

               __    _____           __
   _______  __/ /_  / __(_)___  ____/ /__  _____
  / ___/ / / / __ \/ /_/ / __ \/ __  / _ \/ ___/
 (__  ) /_/ / /_/ / __/ / / / / /_/ /  __/ /
/____/\__,_/_.___/_/ /_/_/ /_/\__,_/\___/_/

		projectdiscovery.io

[INF] Current subfinder version v2.6.6 (latest)
[INF] Loading provider config from /root/.config/subfinder/provider-config.yaml
[INF] Enumerating subdomains for provident.com.mx
global.provident.com.mx
wac.provident.com.mx
pool1.provident.com.mx
webconf.provident.com.mx
correo.provident.com.mx
dialin.provident.com.mx
lsmeet.provident.com.mx
Lyncdiscover.provident.com.mx
sstats.provident.com.mx
ns0.correo.provident.com.mx
prov-pue-ocs.provident.com.mx
adminlc.provident.com.mx
json.provident.com.mx
mail.provident.com.mx
sentryn.provident.com.mx
www.provident.com.mx
prelaunch.provident.com.mx
www.socios.provident.com.mx
www.sstats.provident.com.mx
ns1.correo.provident.com.mx
lsweb.provident.com.mx
meet.provident.com.mx
LyncdiscoverInternal.provident.com.mx
admin.provident.com.mx
sip.provident.com.mx
lyncdiscoverinternal.provident.com.mx
lyncdiscover.provident.com.mx
blog.provident.com.mx
lyncwac.provident.com.mx
provident.com.mx
socios.provident.com.mx
```

```
cat provident | httpx -title -web-server -status-code -follow-redirects -vhost -ip

    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\__/\__/ .___/_/|_|
             /_/

		projectdiscovery.io

[INF] Current httpx version v1.6.0 (outdated)
https://blog.provident.com.mx [200] [Finanzas personales, de negocios y consejos | Blog Provident] [Apache] [vhost] [173.236.220.114]
https://prelaunch.provident.com.mx [200] [IIS Windows Server] [Microsoft-IIS/10.0] [vhost] [45.223.50.234]
https://www.socios.provident.com.mx [200] [IIS Windows Server] [Microsoft-IIS/8.5] [vhost] [45.223.50.234]
https://correo.provident.com.mx [200] [] [nginx] [vhost] [185.154.150.15]
https://www.provident.com.mx [200] [Préstamos personales | Provident México] [Microsoft-IIS/8.5] [vhost] [45.60.192.234]
https://provident.com.mx [301,200] [Préstamos personales | Provident México] [Microsoft-IIS/8.5] [vhost] [149.126.72.234] [https://www.provident.com.mx/]
```