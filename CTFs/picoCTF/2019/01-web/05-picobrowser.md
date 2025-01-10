# picobrowser

This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/26704/` ([link](https://jupiter.challenges.picoctf.org/problem/26704/)) or http://jupiter.challenges.picoctf.org:26704
- Hint: You don't need to download a new web browser

## Solución
#### Explicar antes
- Que es el user-agent : https://developer.mozilla.org/es/docs/Web/HTTP/Headers/User-Agent

### Desde la consla
```bash
curl https://2019shell1.picoctf.com/problem/12255/flag -H 'User-Agent: picobrowser' -s | grep pico
```
- -s Curl en modo silent

### Firefox
- Abrir el inspector
- Modificar el encabesado

## Referencias:
- user-agent : https://developer.mozilla.org/es/docs/Web/HTTP/Headers/User-Agent