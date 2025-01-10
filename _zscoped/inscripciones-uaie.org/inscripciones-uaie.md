# Analisis Incial

## Curl

```
curl -I http://inscripciones-uaie.org
HTTP/1.1 200 OK
Date: Thu, 20 Jan 2022 19:34:13 GMT
Server: Apache
X-Powered-By: PHP/7.4.26
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: PHPSESSID=13101365b7f66754be813d23ea6688ea; path=/
Upgrade: h2,h2c
Connection: Upgrade
Content-Type: text/html; charset=UTF-8
```

```
whatweb http://inscripciones-uaie.org
/usr/lib/ruby/vendor_ruby/target.rb:188: warning: URI.escape is obsolete
http://inscripciones-uaie.org/ [200 OK] Apache, Cookies[PHPSESSID], Country[UNITED STATES][US], Frame, HTML5, HTTPServer[Apache], IP[72.167.68.58], PHP[7.4.26], Script[text/javascript], Title[Selección de Horario], UncommonHeaders[upgrade], X-Powered-By[PHP/7.4.26], YouTube
```

## whois


``` whois inscripciones-uaie.org
Domain Name: INSCRIPCIONES-UAIE.ORG
Registry Domain ID: D402200000017365155-LROR
Registrar WHOIS Server: whois.godaddy.com
Registrar URL: http://www.whois.godaddy.com
Updated Date: 2021-09-19T03:50:09Z
Creation Date: 2021-07-20T17:03:00Z
Registry Expiry Date: 2022-07-20T17:03:00Z
Registrar Registration Expiration Date:
Registrar: GoDaddy.com, LLC
Registrar IANA ID: 146
Registrar Abuse Contact Email: abuse@godaddy.com
Registrar Abuse Contact Phone: +1.4806242505
Reseller:
Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
Domain Status: clientRenewProhibited https://icann.org/epp#clientRenewProhibited
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
Registrant Organization: UNIVERSIDAD AUTONOMA DE ZACATECAS &quot;FRANCISCO GARCIA SALINAS
Registrant State/Province: Zacatecas
Registrant Country: MX
Name Server: NS03.DOMAINCONTROL.COM
Name Server: NS04.DOMAINCONTROL.COM
DNSSEC: unsigned
URL of the ICANN Whois Inaccuracy Complaint Form https://www.icann.org/wicf/)
>>> Last update of WHOIS database: 2022-01-20T19:43:01Z <<<

For more information on Whois status codes, please visit https://icann.org/epp
```

## ffuf

```ffuf -u http://inscripciones-uaie.org/FUZZ -w /tools/wordlists/seclists/Discovery/Web-Content/big.txt -t 10 -ic                                                                                    

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://inscripciones-uaie.org/FUZZ
 :: Wordlist         : FUZZ: /tools/wordlists/seclists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 10
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.htpasswd               [Status: 403, Size: 318, Words: 29, Lines: 10]
.htaccess               [Status: 403, Size: 318, Words: 29, Lines: 10]
cgi-bin                 [Status: 301, Size: 246, Words: 14, Lines: 8]
cgi-bin/                [Status: 403, Size: 318, Words: 29, Lines: 10]
cgi-sys                 [Status: 301, Size: 246, Words: 14, Lines: 8]
common                  [Status: 301, Size: 245, Words: 14, Lines: 8]
controlpanel            [Status: 200, Size: 33978, Words: 1364, Lines: 330]
cpanel                  [Status: 200, Size: 33978, Words: 1364, Lines: 330]
demo                    [Status: 301, Size: 243, Words: 14, Lines: 8]
font                    [Status: 301, Size: 243, Words: 14, Lines: 8]
mailman                 [Status: 301, Size: 246, Words: 14, Lines: 8]
pipermail               [Status: 301, Size: 248, Words: 14, Lines: 8]
webmail                 [Status: 200, Size: 33983, Words: 1364, Lines: 330]
whm                     [Status: 200, Size: 33963, Words: 1364, Lines: 330]
:: Progress: [20476/20476] :: Job [1/1] :: 174 req/sec :: Duration: [0:01:58] :: Errors: 0 ::```


## Misc

https://inscripciones-uaie.org/cgi-bin/

Notice: Trying to access array offset on value of type null in /home/gqx6l8666xfx/public_html/gatejo/index.php on line 21

Notice: Undefined index: Id in /home/gqx6l8666xfx/public_html/gatejo/index.php on line 9

Notice: Undefined index: User in /home/gqx6l8666xfx/public_html/gatejo/index.php on line 10

Notice: Undefined index: Programa in /home/gqx6l8666xfx/public_html/gatejo/index.php on line 11

Notice: Trying to access array offset on value of type null in /home/gqx6l8666xfx/public_html/gatejo/index.php on line 21

