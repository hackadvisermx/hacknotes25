
# [Day 7] Log analysis ‘Tis the season for log chopping!



- Se trata de parsear un archivo de logs con comandos de consola

|   |   |   |
|---|---|---|
|**Position**|**Field**|**Value**|
|1|Timestamp|[2023/10/25:16:17:14]|
|2|Source IP|10.10.140.96|
|3|Domain and Port|storage.live.com:443|
|4|HTTP Method|GET|
|5|HTTP URI|/|
|6|Status Code|400|
|7|Response Size|630|
|8|User Agent|"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  <br>(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"|


```
cat access.log | cut -d ' ' -f 1,3,6
cat access.log | cut -d '"' -f 2

```

# Respuestas

How many unique IP addresses are connected to the proxy server?
9
```
cat access.log | cut -d ' ' -f2 | sort | uniq -c
   5711 10.10.116.67
   4974 10.10.120.75
   5495 10.10.132.238
   5750 10.10.140.96
   5564 10.10.161.168
   4994 10.10.185.225
   5802 10.10.46.50
   5140 10.10.75.132
   5651 10.10.89.232
```


How many unique domains were accessed by all workstations?
111

```
cat access.log | cut -d ' ' -f3 | cut -d ':' -f1 | sort | uniq -d | wc
 111     111    2376

```



What status code is generated by the HTTP requests to the least accessed domain? 
503
```
cat access.log | cut -d ' ' -f3 | cut -d':' -f1 | sort | uniq -c | sort -nr
grep 'partnerservices.getmicrosoftkey.com' access.log | cut -d ' ' -f 6 | sort | uniq -d
503
```

Based on the high count of connection attempts, what is the name of the suspicious domain?

```
 cat access.log | cut -d ' ' -f3 | cut -d':' -f1 | sort | uniq -c | sort -n 

frostlings.bigbadstash.thm
```

What is the source IP of the workstation that accessed the malicious domain?
```
grep 'frostlings.bigbadstash.thm' access.log| cut -d ' ' -f2 | sort | uniq -d
10.10.185.225

```

How many requests were made on the malicious domain in total? 1581
```
grep 'frostlings.bigbadstash.thm' access.log| cut -d ' ' -f2 | sort | uniq -c
   1581 10.10.185.225

```


Having retrieved the exfiltrated data, what is the hidden flag?
```
grep 'frostlings.bigbadstash.thm' access.log | cut -d'=' -f2| cut -d ' ' -f 1 | base64 -d | grep THM
72703959c91cb18edbefedc692c45204,SOC Analyst,THM{a_gift_for_you_awesome_analyst!}
ubuntu@tryhackme:~/Desktop/artefacts$ 

```