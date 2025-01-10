# Mysterious Broadcast 
There used to be 8 Models of humanoid cylon but now there are only 7. We've located one of their broadcast nodes but we can't decode it. Are you able to decipher their technologies?

http://173.230.134.127

## Solucion

http://173.230.134.127/seq/3f9d5166-b4c4-4322-bdc0-5055407fcc6c 


```python
import requests

url = 'http://173.230.134.127/seq/3f9d5166-b4c4-4322-bdc0-5055407fcc6c'
s = requests.Session()
while True:
	r = s.get(url)
	if '~' in r.text:
		print(r.text)
		break
x = 0
for i in range(224):
	r = s.get(url)
	if x % 7 == 0 and x!=0:
		print('')
		x = 0
	else:
		print(r.text, end='')
		x += 1

```

```bash
~
1100011
1100101
0100011
1010110
1001000
1110110
0011011
1010001
0110001
0111011
1010110
0011010
1111011
0100101
1100011
1100001
0010101
0011101
0011101
0111011
0011000
1010101
1100111
1001011
1000110
0101101
0110100
0110100
1100011
1011011
1001001
1001100
0111100
1101111
1011110
```


## Sol 1
```python
import requests
f = open("mys.txt", "w")
for y in range(40):
    f.write(" ")
    for x in range(7):
      url = requests.get("http://173.230.134.127/seq/8bfeb90d-15d1-4b03-9757-f338520b60a1")
      htmltext = url.text
      print(htmltext)
      f.write(url.text)
f.close()
```

