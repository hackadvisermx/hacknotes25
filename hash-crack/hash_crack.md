
# Hashcrack

## MD4

- john
```
john --format=raw-md4 elhash -w /tools/wordlists/rockyou.txt
```

- hashcat
```
hashcat -m 900 elhash /tools/wordlists/rockyou.txt --force
```

## MD5
- hashcat
```
hashcat -m 0 hash /tools/wordlists/rockyou.txt --force
```

## SHA-1 RAW
- john
```
john --format=raw-sha1 hashsha1 -w /tools/wordlists/rockyou.txt
```
```
hashcat -m 100 hashsha1 /tools/wordlists/rockyou.txt --force
```

## SHA-256
```
hashcat -m 1400 hashC.txt ww.mnf --force
hashcat -m 1400 hashC.txt ww.mnf --show
```

## GPG
- John
