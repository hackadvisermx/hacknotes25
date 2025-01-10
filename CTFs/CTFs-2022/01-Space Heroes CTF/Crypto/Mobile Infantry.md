
# Mobile Infantry

shctf{ABCDEFGHIJKLMNOPQRSTrqponmlkjihgfedcba}

- longitud 38

```python
def len_check(pad):
    if len(pad) != 38:
        return False
    return True
```

- la primera mitad deben ser mayusculas (19)

```python
def check1(pad):
    for i in range(0, int(len(pad)/2)+1):
        if not pad[i].isupper():
            return False
    return True
```

- la segunda mitad deben ser minúsculas

```python
def check2(pad):
    for i in range(int(len(pad)/2)+1, len(pad)):
        if not pad[i].islower():
            return False
    return Tru
```

- la primera parte deben ser consecutivas ABC ...

```python
def check3(pad):
    for i in range(0, int(len(pad)/2)):
        if ord(pad[i]) != ord(pad[i+1])-1:
            return False
    return True
```

- la segunda parte deben ser de reversa 
```python
def check4(pad):
    for i in range(int(len(pad)/2)+1, len(pad)-1):
        if ord(pad[i]) != ord(pad[i+1])+1:
            return False
    return True
```


AAAAAAAAAAAAAAAAAZZ1234567891234567890
12345678901234567891234567891234567890


AAAAAAAAAAAAAAAAAZZaaaaaaaaaaaaaaaaaaa

CARLOSCARLOSCARLOSCAaaaaaaaaaaaaaaaaaa


ABCDEFGHIJKLMNOPQRSTabcdefghjklmnopqrs
ABCDEFGHIJKLMNOPQRSTrqponmlkjihgfedcba