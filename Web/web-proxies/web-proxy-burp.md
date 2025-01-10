# Burpsuite

## Burp Match and Replace

Para acceder a esta funcionalidad ir a `Proxy - Options - Match and Replace`.

- Remplazar en base al ecabezado del Request

```cmd
Type: Request header
Match: ^User-Agent.*$
Replace: User-Agent: HackTheBox Agent 1.0
Regex match: True
```

- Remplazar en base a encabezado del Response

```cmd
Type: Response body.
Match: type="number".
Replace: type="text".
Regex match: False.
```


## Repetir Request  

Empezamos por ir al historial y elegir una request `Proxy - Http History` 

Enviamos la solicitud al `Repeater` con `CTRL*R` o botón derecho y `Send To Repeater` y luego movernos a la pestaña Repeater con click o con `Ctrl-Shift+R`


## Encoding / Decoding

Para **codiicar** una cadena, boton derecho luego `Convert Selection>URL>URL encode key characters` o `Ctrl+U`, hay otros tipos de codificación como `Full URL-Encoding` o `Unicode URL`que pueden ser ùtiles con Requests que tienen caractéres adicionales

Para decodificar puedoemos usar el Tab `Decoder`.

## Burp Shortcuts

```
[CTRL+R] 	    Send to repeater
[CTRL+SHIFT+R] 	Go to repeater
[CTRL+I] 	    Send to intruder
[CTRL+SHIFT+B] 	Go to intruder
[CTRL+U] 	    URL encode
[CTRL+SHIFT+U] 	URL decode
```
