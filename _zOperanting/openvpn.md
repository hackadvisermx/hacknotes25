
- Problema al conectar a la vpn
https://bugzilla.redhat.com/show_bug.cgi?id=2093069

- Basicamente es agregar las lineas 
```
cipher AES-256-CBC
data-ciphers AES-256-GCM:AES-128-GCM:AES-256-CBC
```

La cosa es en windows, solo dejar esta linea y asi funciona

```
cipher AES-256-CBC
```