# basic-mod2

A new modular challenge! Download the message [here](https://artifacts.picoctf.net/c/503/message.txt). Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

# Solucion 
```python
import string

def modInverse(a, m): 
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

# Mapear letras 27-36 y numeros 1-26, 37 es _
k = 1
map = {}
for c in string.ascii_lowercase:
    map[k]=c
    k+=1
for c in string.digits:
    map[k]=c
    k+=1
map[37]='_'

# Leer data y procesar
data = open('message.txt','r').readlines()[0].strip().split(' ')
for c in data:
    modinv = modInverse(int(c),41)
    print(map[modinv], end='')
```

picoCTF{1nv3r53ly_h4rd_f6747912}
