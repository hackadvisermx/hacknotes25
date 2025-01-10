# Web Proxy Zap


## Zap Replacer

Para activarlo `Ctrl+R` o hacer click en `Replacer` en el menú opciones

- Remplazar en base al ecabezado del Request
  
```
Description: HTB User-Agent.
Match Type: Request Header (will add if not present).
Match String: User-Agent. We can select the header we want from the drop-down menu, and ZAP will replace its value.
Replacement String: HackTheBox Agent 1.0.
Enable: True.
```

- Remplazar en base a encabezado del Response

```
Change input type to text:
Match Type: Response Body String.
Match Regex: False.
Match String: type="number".
Replacement String: type="text".
Enable: True.
```

```
Change max length to 100:
Match Type: Response Body String.
Match Regex: False.
Match String: maxlength="3".
Replacement String: maxlength="100".
Enable: True. 
```

## Repetir Request  

Empezamos por ir al historial, al fondo de la página en ZAP HUD UID hacer click al botón `History` o en el Tab de History en la parte inferor en la aplicación principal ZAP.

Editamos la Rquest con botón derecho `Open/Resend with Request Editor`


## Encoding / Decoding

Para codificar o decodificar, seleccionamos cadena y hacemos click derecho, podemos ir a `Encoder/Decoder/Hash`

Se pueden agregar mas Tabs y aprtados dentro de cada Tab para otros tipos de codificación y decodificación con los botones de +.



## ZAP Shortcuts

```
Shortcut 	Description
[CTRL+B] 	Toggle intercept on/off
[CTRL+R] 	Go to replacer
[CTRL+E] 	Go to encode/decode/hash
```
