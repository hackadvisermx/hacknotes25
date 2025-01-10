
# What's Diffie [Crypto]

### 150

Alice and Bob have been experimenting with a way to send flags back and forth securely. Can you intercept their messages?

_nc 0.cloud.chals.io 32820_

## Solve

```
nc 0.cloud.chals.io 32820
g =  12
p =  53
a =  8
b =  67

What is their shared secret?

Enter your input: 47

To find the flag you will need to perform a bitwise XOR operation between each byte of the encrypted message and the corresponding byte of the shared secret key.

7c 66 79 6d 68 7d 54 1b 70 49 43 1b 48 70 49 5d 1f 42 70 1b 43 1e 4c 1c 70 1b 41 4b 70 4d 1f 4d 52
```


```python
from pwn import *

r = remote("0.cloud.chals.io",32820)
l1 = r.recvline()
l2 = r.recvline()
l3 = r.recvline()
l4 = r.recvline()
exec(l1)
exec(l2)
exec(l3)
exec(l4)
log.info('p={} g={} a={} b={}'.format(p,g,a,b))
A = pow(g,a,p)
B = pow(g,b,p)
S1 = pow(B,a,p)
S2 = pow(A,b,p)
log.info('S1={} S2={}'.format(S1,S2))
print(r.recvuntil(b': ').decode())
r.sendline(str(S1).encode())
print(r.recvuntil(b'.\n\n').decode())

data = r.recvline().decode().split()
print(data)

flag=''
for n in data:
        v = int(n,16)
        x = v ^ S1
        flag += chr(x)

print(flag)
```


```
SIVBGR{4_fl4g_fr0m_4l1c3_4nd_b0b}
```