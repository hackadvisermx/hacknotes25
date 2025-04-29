## Escaneo inicial


```
┌──(kali㉿kali)-[~]
└─$ nmap -n -Pn -T5 -v 10.10.88.195 --open -p0-9500 -sV 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-29 11:26 CST
NSE: Loaded 46 scripts for scanning.
Initiating Connect Scan at 11:26
Scanning 10.10.88.195 [9501 ports]
Discovered open port 80/tcp on 10.10.88.195
Discovered open port 22/tcp on 10.10.88.195
Discovered open port 443/tcp on 10.10.88.195
Discovered open port 1443/tcp on 10.10.88.195
Discovered open port 9007/tcp on 10.10.88.195
Discovered open port 8000/tcp on 10.10.88.195
Discovered open port 1338/tcp on 10.10.88.195
Discovered open port 1883/tcp on 10.10.88.195
Completed Connect Scan at 11:26, 17.65s elapsed (9501 total ports)
Initiating Service scan at 11:26
Scanning 8 services on 10.10.88.195
Completed Service scan at 11:27, 42.77s elapsed (8 services on 1 host)
NSE: Script scanning 10.10.88.195.
Initiating NSE at 11:27
Completed NSE at 11:27, 7.83s elapsed
Initiating NSE at 11:27
Completed NSE at 11:27, 3.29s elapsed
Nmap scan report for 10.10.88.195
Host is up (0.19s latency).
Not shown: 9475 closed tcp ports (conn-refused), 18 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE                 VERSION
22/tcp   open  ssh                     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http                    lighttpd 1.4.55
443/tcp  open  ssl/http                Apache httpd 2.4.41
1338/tcp open  ftp                     vsftpd 2.0.8 or later
1443/tcp open  ssl/http                Apache httpd 2.4.41 ((Ubuntu))
1883/tcp open  mosquitto version 1.6.9
8000/tcp open  http                    Apache httpd 2.4.41 ((Ubuntu))
9007/tcp open  http                    Apache httpd 2.4.41
Service Info: Hosts: ip-10-10-88-195.eu-west-1.compute.internal, myblog.thm; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 71.63 seconds

```


**What is the version of the Apache server?**

```
curl 10.10.159.248:443 -I
HTTP/1.1 400 Bad Request
Date: Wed, 28 Feb 2024 23:02:44 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Length: 472
Connection: close
Content-Type: text/html; charset=iso-8859-1

Respuesta: 2.4.41
```
 

What is the port number of the FTP service?

```
Nos lo dice el escaneo de nmap

 1338
```

**What is the FQDN for the website hosted using a self-signed certificate and contains critical server information as the homepage?**

```
openssl s_client -connect 10.10.159.248:443

Respuesta: dev.probe.thm
```

**What is the email address associated with the SSL certificate used to sign the website mentioned in Q3?**

```
openssl s_client -connect 10.10.159.248:443
probe@probe.thm
```

What is the value of the **PHP Extension Build** on the server?

```
https://10.10.88.195:1443/

PHP Extension Build 	API20190902,NTS 


Respuesta: API20190902,NTS
```

What is the banner for the FTP service?

```
┌──(kali㉿kali)-[~]
└─$ nc -nv 10.10.88.195 1338               
(UNKNOWN) [10.10.88.195] 1338 (?) open
220 THM{WELCOME_101113}


Respuesta: THM{WELCOME_101113}
```

What software is used for managing the database on the server?

```
sudo apt install gobuster

gobuster dir -u http://10.10.88.195:8000/ -w /usr/share/wordlists/dirb/big.txt      
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.88.195:8000/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/contactus            (Status: 301) [Size: 323] [--> http://10.10.88.195:8000/contactus/]
/javascript           (Status: 301) [Size: 324] [--> http://10.10.88.195:8000/javascript/]
/phpmyadmin           (Status: 301) [Size: 324] [--> http://10.10.88.195:8000/phpmyadmin/]
/server-status        (Status: 403) [Size: 279]
Progress: 20469 / 20470 (100.00%)
===============================================================
Finished
===============================================================



http://10.10.88.195:8000/phpmyadmin/

```


```
ffuf -u http://10.10.88.195:8000/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -ic  
```

```

Respuesta> phpmyadmin


```

What is the Content Management System (CMS) hosted on the server?

```
https://10.10.88.195:9007/

```

```
┌──(kali㉿kali)-[~]
└─$ nikto -h https://10.10.88.195:9007/
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.88.195
+ Target Hostname:    10.10.88.195
+ Target Port:        9007
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /C=US/ST=Some-State/O=Internet Widgits Pty Ltd/CN=myblog.thm/emailAddres
                   Ciphers:  TLS_AES_256_GCM_SHA384
                   Issuer:   /C=US/ST=Some-State/O=Internet Widgits Pty Ltd/CN=myblog.thm/emailAddres
+ Start Time:         2024-02-29 11:32:52 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/
+ /: Drupal Link header found with value: <https://myblog.thm:9007/index.php?rest_route=/>; rel="http
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://dev
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the conty-scanner/vulnerabilities/missing-content-type-header/
+ /index.php?: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ No CGI Directories found (use '-C all' to force check all possible dirs)

```

```
Respuesta> Wordpress
```


What is the version number of the CMS hosted on the server?

 ```
wpscan --url https://10.10.88.195:9007/ --disable-tls-checks
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.25
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: https://10.10.88.195:9007/ [10.10.88.195]
[+] Started: Thu Feb 29 11:36:52 2024

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.41 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: https://10.10.88.195:9007/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: https://10.10.88.195:9007/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] WordPress version 6.2.2 identified (Insecure, released on 2023-05-20).
 | Found By: Emoji Settings (Passive Detection)
 |  - https://10.10.88.195:9007/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=6.2.2'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - https://10.10.88.195:9007/, Match: 'WordPress 6.2.2'

[+] WordPress theme in use: twentytwentythree
 | Location: https://10.10.88.195:9007/wp-content/themes/twentytwentythree/
 | Last Updated: 2023-11-07T00:00:00.000Z
 | Readme: https://10.10.88.195:9007/wp-content/themes/twentytwentythree/readme.txt
 | [!] The version is out of date, the latest version is 1.3
 | [!] Directory listing is enabled
 | Style URL: https://10.10.88.195:9007/wp-content/themes/twentytwentythree/style.css
 | Style Name: Twenty Twenty-Three
 | Style URI: https://wordpress.org/themes/twentytwentythree
 | Description: Twenty Twenty-Three is designed to take advantage of the new design tools introduced in WordPress 6....
 | Author: the WordPress team
 | Author URI: https://wordpress.org
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.1 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - https://10.10.88.195:9007/wp-content/themes/twentytwentythree/style.css, Match: 'Version: 1.1'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:06 <======================> (137 / 137) 100.00% Time: 00:00:06

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu Feb 29 11:38:27 2024
[+] Requests Done: 168
[+] Cached Requests: 5
[+] Data Sent: 43.542 KB
[+] Data Received: 191.175 KB
[+] Memory used: 254.105 MB
[+] Elapsed time: 00:01:35

```

```
 |  - https://10.10.88.195:9007/, Match: 'WordPress 6.2.2'
```

```
Respuesta> 6.2.2
```

What is the username for the admin panel of the CMS?

 ```
wpscan --url https://10.10.88.195:9007/ --disable-tls-checks -e u

[+] joomla
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

```

```
Respuesta: joomla
```

During vulnerability scanning, **OSVDB-3092** detects a file that may be used to identify the blogging site software. What is the name of the file?

```
─$ nikto -h https://10.10.88.195:9007/
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.88.195
+ Target Hostname:    10.10.88.195
+ Target Port:        9007
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /C=US/ST=Some-State/O=Internet Widgits Pty Ltd/CN=myblog.thm/emailAddres
                   Ciphers:  TLS_AES_256_GCM_SHA384
                   Issuer:   /C=US/ST=Some-State/O=Internet Widgits Pty Ltd/CN=myblog.thm/emailAddres
+ Start Time:         2024-02-29 11:32:52 (GMT-6)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/
+ /: Drupal Link header found with value: <https://myblog.thm:9007/index.php?rest_route=/>; rel="http
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://dev
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the conty-scanner/vulnerabilities/missing-content-type-header/
+ /index.php?: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Hostname '10.10.88.195' does not match certificate's names: myblog.thm. See: https://cwe.mitre.org/data/definitions/297.html
+ Apache/2.4.41 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: The Content-Encoding header is set to "deflate" which may mean that the server is vulnerable to the BREACH attack. See: http://breachattack.com/
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.

... Por aqui aparecera solo que nikto se tarda de a madre

```

```
Resuesta> license.txt
```


**What is the name of the software being used on the standard HTTP port?** 

```
 curl 10.10.159.248 -I
HTTP/1.1 403 Forbidden
Content-Type: text/html
Content-Length: 341
Date: Wed, 28 Feb 2024 23:01:33 GMT
Server: lighttpd/1.4.55

Respuesta: lighttpd

```

What is the flag value associated with the web page hosted on port 8000?

```
http://10.10.88.195:8000/contactus/

Flag: THM{CONTACT_US_1100}
```