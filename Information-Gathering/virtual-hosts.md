# Virtual Hosts


```
ffuf -u http://inlanefreight.htb -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.inlanefreight.htb' -fs 10918
```
