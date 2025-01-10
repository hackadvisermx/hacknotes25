

## Super Duper Quick Maths [MISC]

### 150

Solve my math test and you'll get my flag!

_nc 0.cloud.chals.io 15072_

## Solve

```
from pwn import *

p =  remote('0.cloud.chals.io',15072)

print(p.recvuntil(b'!').decode())
p.readline()

for i in range(50):
        op = p.readline()
        sol = int(util.safeeval.expr(op))
        p.sendline(str(sol).encode())
        log.info('Reto {}: {} = {}'.format(i, op.decode(), sol))
        print(p.readline().decode())

print(p.recvall().decode())
```

```
SIVBGR{L00kM0m!_ICANDO_m4th}
```