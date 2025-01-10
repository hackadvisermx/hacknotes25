# Subdomain Enumeration


## Project Sonar

```cms
https://sonar.omnisint.io/subdomains/{domain} - All subdomains for a given domain
https://sonar.omnisint.io/tlds/{domain}       - All tlds found for a given domain
https://sonar.omnisint.io/all/{domain}        - All results across all tlds for a given domain
https://sonar.omnisint.io/reverse/{ip}        - Reverse DNS lookup on IP address
https://sonar.omnisint.io/reverse/{ip}/{mask} - Reverse DNS lookup of a CIDR range
```

```cmd
curl -s https://sonar.omnisint.io/subdomains/$TARGET | jq -r '.[]' | sort -u
curl -s https://sonar.omnisint.io/tlds/$TARGET | jq -r '.[]' | sort -u
curl -s https://sonar.omnisint.io/all/$TARGET | jq -r '.[]' | sort -u
```


## Certficados

- https://censys.io
- https://crt.sh


```
curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"'
```

```
export TARGET="facebook.com"
export PORT="443"
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "${TARGET}:${PORT}" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u
```

## Theharvester 

- https://github.com/laramies/theHarvester



