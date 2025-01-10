# María ART CLASS
 María’s Art Class
500

For María’s art class the teacher ask for a MASTERPIECE that combains history and feelings, so María decided to créate a painting that describes an event in history close to her heart and her roots. She decided to paint a piece of Yucatán that everyone can relate to, so she paint the kukulkan pirámide. María says that she hide a Little message in the painting but I guess the teacher never find it because María got an F. Help María to pass de class, find the message and send it to the teacher:3

## Solucion
- nos dan una imagen y le aplicamos strings:
	- 
```bash
──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/crypto/mariaartclass]
└─$ strings KUKULKAN.jpg -n15
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
_I LOVE FLAGS :3 
.MY FAVOURITE WORD IS FLAG 
THIS IS NOT THE FLAG, KEEP LOOKING BRO! 
/ FLAG Un PAso mas  BRO{Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalJsSlZVMnhPVlUxV2NEQlVWbEpUWVdzeFYxTnNhRmRpVkZaUVZrUktTMUl5VGtsaVJtUk9ZbTFvZVZadE1YcGxSbGw0Vkc1V2FsSnNXazlXYlRWRFYxWmFkR1JIUmxSTlZYQjVWR3hhYjFSc1duTmpSVGxhWWxoU1RGWnNXbUZXVmtaMFVteHdWMkpJUWpaV1ZFa3hWREZhV0ZOclpHcFNWR3hZV1ZSS1VrMUdWWGRYYlVacVZtdHdlbGRyV210VWJGcDFVV3R3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ==} 
```


- despues de 6 pasadas de base64, econtramos la bandera con cyberchef: https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base64('A-Za-z0-9-_',true,false)From_Base64('A-Za-z0-9-_',true,false)From_Base64('A-Za-z0-9-_',true,false)From_Base64('A-Za-z0-9-_',true,false)From_Base64('A-Za-z0-9-_',true,false)From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalJsSlZVMnhPVlUxV2NEQlVWbEpUWVdzeFYxTnNhRmRpVkZaUVZrUktTMUl5VGtsaVJtUk9ZbTFvZVZadE1YcGxSbGw0Vkc1V2FsSnNXazlXYlRWRFYxWmFkR1JIUmxSTlZYQjVWR3hhYjFSc1duTmpSVGxhWWxoU1RGWnNXbUZXVmtaMFVteHdWMkpJUWpaV1ZFa3hWREZhV0ZOclpHcFNWR3hZV1ZSS1VrMUdWWGRYYlVacVZtdHdlbGRyV210VWJGcDFVV3R3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTA
- 
flagMX{R3TURN_TH3_J4GUARS_EYES}