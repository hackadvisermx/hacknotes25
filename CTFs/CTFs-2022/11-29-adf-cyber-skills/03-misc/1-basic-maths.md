
## Solucion
- Resolver 100 ecuaciones para tener la flag

```python
#!/usr/bin/python3.8
from pwn import *

'''
Run the wrapper: python wrapper.py <IP> <port>
e.g. python wrapper.py 0.0.0.0 1337
'''

IP   = str(sys.argv[1]) if len(sys.argv) >= 2 else '0.0.0.0'
PORT = int(sys.argv[2]) if len(sys.argv) >= 3 else 1337
r    = remote(IP, PORT)

for i in range(100):
  r.recvuntil(b'Equation')
  r.recvlines(2)
  equation = r.recvuntil(b' =', drop=True)
  print(f'Equation: {equation.decode()}\n')
  solution = int(util.safeeval.expr(equation))


  # Insert your payload here
  r.sendlineafter('Answer:', str(solution).encode())
  

  # Last equation to get flag
  if i == (99):
    success(f'Flag --> {r.recvline_contains(b"HTB", timeout=0.2).strip().decode()}')
```

```bash
[+] Flag --> HTB{y0uR_EVALuat10n_w45_f45t_45_l1ghtn1ng}
[*] Closed connection to 161.35.173.232 port 31521
```
## Referencias

https://nandynarwhals.org/sieberrsec-ctf-3.0-canyoumathit/
