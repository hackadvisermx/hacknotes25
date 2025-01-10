
## Baby's First RSA [Crypto]

### 150

I learned just learned about RSA and I am pretty sure that I implemented it right. It should be impossible to get my flag.

## Solve

```
from gmpy2 import * 

gmpy2.get_context().precision=2048
n=  546355920998555652385674298161560893770338220027595474110827644>
e = 3
c = 113208879218657079704171317074893049412137373443727725602962320>

for t in range(10000):
    m, tr = iroot(t*n + c, e)
    if tr:   
        print(f"Encontre t = {t}")
        print(f"Mensaje    = {bytes.fromhex(hex(m)[2:]).decode()}")
        break

```

```
python3 exp.py
Encontre t = 0
Mensaje    = SIVBGR{D0nt_F0rg37_T0_P4D!!!}

```