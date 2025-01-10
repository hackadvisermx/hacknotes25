Several of the challenges are dynamic and require you to talk to our challenge servers over the network. This allows you to perform man-in-the-middle attacks on people trying to communicate, or directly attack a vulnerable service. To keep things consistent, our interactive servers always send and receive JSON objects.  
  
Such network communication can be made easy in Python with the `pwntools` module. This is not part of the Python standard library, so needs to be installed with pip using the command line `pip install pwntools`.  
  
For this challenge, connect to `socket.cryptohack.org` on port `11112`. Send a JSON object with the key `buy` and value `flag`.

Connect at `socket.cryptohack.org 11112`  
  
**Challenge files:**  
  - [pwntools_example.py](https://cryptohack.org/static/challenges/pwntools_example_72a60ff13df200692898bb14a316ee0b.py)
## Solve

```python
#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)


```

- ejecutar
```
 python3 pwntools_example_72a60ff13df200692898bb14a316ee0b.py 
[+] Opening connection to socket.cryptohack.org on port 11112: Done
b"Welcome to netcat's flag shop!\n"
b'What would you like to buy?\n'
b"I only speak JSON, I hope that's ok.\n"
b'\n'
{'flag': 'crypto{sh0pp1ng_f0r_fl4g5}'}
[*] Closed connection to socket.cryptohack.org port 11112
```