# GET aHEAD

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:53554/](http://mercury.picoctf.net:53554/)
- Hints:
	- Maybe you have more than 2 choices
	- Check out tools like Burpsuite to modify your requests and look at the responses

## Solución

http://mercury.picoctf.net:53554/

- Tiene dos botones, que cargan el index.php y cambian de rojo a azul
- Uno lo hace con GET el otro con POST
- La pista nos dice que tenemos mas opciones> https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- El titulo del reto sugiere HEAD puede ser el metodo

## Web
- Puedo ir a firefox y editar el request de uno de los botones
- Cambiar a HEAD, volver a enviar
- Examinar luego los Response headers, ahi estará la bandera

### Consola rules
- Para ver los encabezados en CURL concretamente el HEAD usamos -I

```
curl -I http://mercury.picoctf.net:53554/
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}
Content-type: text/html; charset=UTF-8


```

## Con Burp
- Explicar que es un proxy web
	- google> webhacking tools proxy
		- https://learn.onemonth.com/web-hacking-tools-proxies/

- configurar burp para inceptar
- instalar foxyproxy
- instalar certificado
- resolver el reto modificand el encabezado 


## Referencias
- http methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- web proxy : https://learn.onemonth.com/web-hacking-tools-proxies/