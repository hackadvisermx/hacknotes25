# WhitePages

## Solucion
- vemos el tipo de archivo

```bash
──(kali㉿kali)-[~/picoCTF/forensic/whitepages]
└─$ file whitepages.txt 
whitepages.txt: Unicode text, UTF-8 text, with very long lines (1376), with no line terminators
```

- explicar que es UTF8 > https://es.wikipedia.org/wiki/UTF-8
	
- vaciado hexadecimal 
```bash
xxd whitepages.txt e 
xxd -g 1 whitepages.txt 
xxd -g 1 whitepages.txt | tail
```
- tenemos dos opciones asi que lo trataremos como binario

```
e28083	0 
20		1
```


## Forma 1

```
sed 's/ /0/g' whitepages.txt | sed 's/ /1/g'
```
o

```
sed 's/\xe2\x80\x83/0/g' whitepages.txt | sed 's/\x20/1/g'
```

## Forma 2



- migrar a python 3
```
sudo apt install -y python-is-python3	
```

- checar la version de python
```bash
┌──(kali㉿kali)-[~/picoCTF/forensic/whitepages]
└─$ python --version
Python 3.9.10
```

- asegurarnos que tenemos 
```
sudo apt install python3-pip
sudo apt install python3-setuptools
sudo apt install python3-dev libssl-dev libffi-dev build-essential


sudo apt-get install python3-pwntools


python3 -m pip install pwntools
```

- instalar terminator y agregar acceso directo

	nano copiar y duplicar ( alt + 6, ctrl + u)

```python 
#!/usr/bin/python3
from pwn import *
file = open('whitepages.txt','rb')
data = bytearray(file.read())
data = data.replace(b'\xe2\x80\x83', b'0')
data = data.replace(b'\x20', b'1')
data = data.decode('ascii')
data = unbits(data)

print(data)
```

# Referencias

- unicode - https://en.wikipedia.org/wiki/Unicode
- utf-8 - https://en.wikipedia.org/wiki/UTF-8
- unicode space separator - https://www.compart.com/en/unicode/category/Zs
- 