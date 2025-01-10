# Reconocimiento dns



- Enumerar hosts con wfuzz
```bash
wfuzz --hl 320 -c -w /tools/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "HOST:FUZZ.mafialive.thm" http://mafialive.thm/
```


- Enumerar don dnsenum
```bash
dnsenum --noreverse oxxo.com
```

