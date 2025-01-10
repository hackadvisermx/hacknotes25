# Cache Poisoning

## Qué es **web cache poisoning**?

El **web cache poisoning** es una técnica avanzada mediante la cual un atacante explota el comportamiento de un servidor web y la caché para que otros usuarios reciban una respuesta HTTP dañina.

Básicamente, el **web cache poisoning** implica dos fases:

- En primer lugar, el atacante debe averiguar cómo obtener una respuesta del servidor back-end que, inadvertidamente, contiene algún tipo de carga útil peligrosa.
- Una vez que tengan éxito, deben asegurarse de que su respuesta se almacene en caché y, posteriormente, se sirva a las víctimas previstas.

Un cache web envenenado puede ser un medio potencialmente devastador para distribuir numerososo ataques, explotando vulnerabilidades como XSS, JavaScript Injection, open redirecton, etc.

Referencias:
- [Web cache poisoning - portswigger](https://portswigger.net/web-security/web-cache-poisoning)
- [2021 - Cache Poisoning at Scale](https://youst.in/posts/cache-poisoning-at-scale/)
- [2020 - Web Cache Entanglement: Novel Pathways to Poisoning](https://portswigger.net/research/web-cache-entanglement)
- [2018 - Practical Web Cache Poisoning](https://portswigger.net/research/practical-web-cache-poisoning)
