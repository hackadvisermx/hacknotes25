# Cesar
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext).

## Solucion
- Google: Cesar y explicarlos

###  way 1

Cyberchef > rotado 19 veces

### way 2
```python
import string
import re 

def cesar(frase,rot):
    abc = string.ascii_letters
    frase_salida = ""
    for car in frase:  
        frase_salida += abc[ (abc.find(car) + rot) % 26 ]
    return frase_salida

encrypted = open('ciphertext','r').read()
encrypted =  re.findall('\{(.*?)\}', encrypted)[0]

rot = 25
plain_text =  cesar(encrypted,rot)

print(f'Codificado   : {encrypted}')
print(f'DeCodificado : {plain_text}')
```
- https://blog.finxter.com/how-to-use-rot13-in-python/