# Cross Site Request Forgery (CSRF)

Ocurre cuando un usuario visita una página en un sitio web, que lleva a cabo una accion en un sitio diferente. Supongamos que la victima hace click en una liga creada por el atacante, lo cual cambiara el correo.
```
<img src="https://vulnerable-website.com/email/change?email=pwned@evil-user.net"> 
```
Funciona por que la victima haciendo la solicitud no el sitio, todo lo que ve el sitio es a un usuario normal haciendo una solicitud normal. Esto abre la puerta para que la cuenta del usuario sea completamente comprometida a través de resetear el password por ejemplo. 

El escenario para que funcion es cuando hay parámetros personalizables y el cookie de sesión es enviado automáticamente. Bastaría con crear un html vulnerable y ponerlo en un servidor web:
```
<img src="http://localhost:3000/transfer?to=alice&amount=100">
```

## Usando XSRFProbe
XSRFProbe is an advanced Cross Site Request Forgery (CSRF/XSRF) Audit and Exploitation Toolkit
- Instalar
```
pip3 install xsrfprobe
```
- Uso
```
xsrfprobe -u <url>/<endpoint>
```



## Referencias

- Herramientas
  - [xsrfprobe](https://github.com/0xInfection/XSRFProbe)

## Tools
- [CSRF POC generator](https://tools.nakanosec.com/csrf/?source=post_page-----db464a61a582--------------------------------)
