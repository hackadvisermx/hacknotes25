
# Just Another Forensics Chall
We received this file, and we don´t know how to manage it, but something was lost in it.

Could you check?

## Solucion

- Son varias capas de un archivo docker, hicmos la busqueda
```
{"created":"2023-09-05T21:19:04.531986036Z","created_by":"RUN /bin/sh -c echo \"ZmxhZ3tkMGNLM3JfZjByM25zMWNzX2xBWTNyMW5nfQ==\" \u003e /tmp/flag.txt # buildkit"
```

- La bandera estaba en base64
```
flag{d0cK3r_f0r3ns1cs_lAY3r1ng}
```