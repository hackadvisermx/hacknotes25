# Crackear el password de un .zip 

## Usando john

- sacar el hash del zip
```
/tools/cracking/john/run/zip2john backup.zip > hash
```
- fuerza bruta con john
```
john hash -w=/tools/wordlists/rockyou.txt
```
