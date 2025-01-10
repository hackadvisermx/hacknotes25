# XORROX

We are exclusive -- you can't date anyone, not even the past! And don't even think about looking in the mirror!  
**Download the files below.**

## Archivos
- output.txt

```txt
xorrox=[1, 209, 108, 239, 4, 55, 34, 174, 79, 117, 8, 222, 123, 99, 184, 202, 95, 255, 175, 138, 150, 28, 183, 6, 168, 43, 205, 105, 92, 250, 28, 80, 31, 201, 46, 20, 50, 56]
enc=[26, 188, 220, 228, 144, 1, 36, 185, 214, 11, 25, 178, 145, 47, 237, 70, 244, 149, 98, 20, 46, 187, 207, 136, 154, 231, 131, 193, 84, 148, 212, 126, 126, 226, 211, 10, 20, 119]
```

- xorrox.py
```python
#!/usr/bin/env python3

import random

with open("flag.txt", "rb") as filp:
    flag = filp.read().strip()

key = [random.randint(1, 256) for _ in range(len(flag))]

xorrox = []
enc = []
for i, v in enumerate(key):
    k = 1
    for j in range(i, 0, -1):
        k ^= key[j]
    xorrox.append(k)
    enc.append(flag[i] ^ v)

with open("output.txt", "w") as filp:
    filp.write(f"{xorrox=}\n")
    filp.write(f"{enc=}\n")

```



# Solucion

