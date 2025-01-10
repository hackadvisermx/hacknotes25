# Day 16

- en el codigo fuente de la pagina se encuentra
```
<li><a href="http://machine_ip/api/api_key">Modular modern free</a></li>
```

- extraer ligas con python
```
#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

html=requests.get('http://10.10.12.64:8000/static/index.html')
soup=BeautifulSoup(html.text,'html.parser')

links = [a['href'] for a in soup.find_all('a', href=True)]

print(links)
```



- Crear un script para fuzerar del 0 al 100
```
import requests

for i in range(1,101):
    if i%2!=0:  
        r = requests.get('http://10.10.12.64:8000/api/'+str(i))
        print(i)
        print(r.text)   
```
```
/api/57
```
