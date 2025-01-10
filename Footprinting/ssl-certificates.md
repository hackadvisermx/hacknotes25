# ssl-certificates

- [crt.sh Certificate Search](https://crt.sh/)

 ```bash
curl -s https://crt.sh/\?q\=uaz.edu.mx\&output\=json | jq .
 ```

 ```bash
curl -s https://crt.sh/\?q\=uaz.edu.mx\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u > subdomains
```

```bash
for i in $(cat subdomains);do host $i | grep "has address" | grep uaz.edu.mx | cut -d" " -f1,4;done 

for i in $(cat subdomains);do host $i | grep "has address" | grep uaz.edu.mx | cut -d" " -f4 >> ipaddresses;done 
```

```bash

```