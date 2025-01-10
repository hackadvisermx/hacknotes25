Santa was on the way to your home. But, in the way he lost his vehicle's key. Help him find the key & reach your home.

## Solucion
- se nos da un codigo python a corregir
```python


def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
      new_key = new_key + key[i]
      i = (i + 1) % len(key)
    a = []
    for (secret_c,new_key_c) in zip(secret,new_key):
        a.append(chr(ord(secret_c) ^ ord(new_key_c)))
    return ''.join(a)


flag_enc = 0x1d,0x24,0x2d,0x20,0x27,0x28,0x32,0x2e,0x1a,0x35,0x32,0x46,0x1d,0x2b,0xa,0x60,0x18,0x31,0x1c,0x52,0x21,0x52,0x13
flag = str_xor(flag_enc, 'Santa')
print('That is correct! Here\'s your flag: ' + flag)


```
- le agregamos el chr

```python
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
      new_key = new_key + key[i]
      i = (i + 1) % len(key)
    a = []
    for (secret_c,new_key_c) in zip(secret,new_key):
        a.append(chr(ord(secret_c) ^ ord(new_key_c)))
    return ''.join(a)


flag_enc = chr(0x1d)+chr(0x24)+chr(0x2d)+chr(0x20)+chr(0x27)+chr(0x28)+chr(0x32)+chr(0x2e)+chr(0x1a)+chr(0x35)+chr(0x32)+chr(0x46)+chr(0x1d)+chr(0x2b)+chr(0xa)+chr(0x60)+chr(0x18)+chr(0x31)+chr(0x1c)+chr(0x52)+chr(0x21)+chr(0x52)+chr(0x13)
flag = str_xor(flag_enc, 'Santa')
print('That is correct! Here\'s your flag: ' + flag)
```

NECTF{S@nTa's_k3y_h3r3}