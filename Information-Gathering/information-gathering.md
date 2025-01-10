# Informaton Gatherig 

# whois

```
whois thmredteam.com
```

# Query A Recrds

```
nslookup target
dig cafe.thmredteam.com @1.1.1.1
```

## Query MX , NS Records

```
nslookup -query=MX target
dig mx target @1.1.1.1
```

```
nslookup -type=ns inlanefreight.htb ns.inlanefreight.htb
dig ns inlanefreight.htb @ns.inlanefreight.htb
dig ns inlanefreight.htb @ns.inlanefreight.htb +short

```

## Query A Records for Subdoman

```
nslookup -query=A target
dig a target @1.1.1.1
```


## Query PTR Records

```
nslookup -query=PTR 31.13.92.36
dig -x 31.13.92.36 @1.1.1.1
```

## Query ANY Records

```
nslookup -query=ANY target
dig any google.com @8.8.8.8
```

# Query TXT Records

```
nslookup -query=TXT $target
dig txt target @1.1.1.1
```

## Zone transfer

```
nslookup -type=any -query=axfr inlanefreight.htb ns.inlanefreight.htb

dig axfr inlanefreight.htb @ns.inlanefreight.htb

host -l inlanefreight.htb root.inlanefreight.htb

dig axfr internal.inlanefreight.htb @ns.inlanefreight.htb
```

## SMB


Nota:
    - Algunas veces los DNS tienen varias zonas, aglgunas pueden ser internas