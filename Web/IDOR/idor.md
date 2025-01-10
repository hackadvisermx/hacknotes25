# Insecure Direct Object Reference (IDOR)

Es el acto de explotar una configuración incorrecta en la forma en que se maneja la entrada del usuario para acceder a recursos a los que normalmente no podría acceder.


- Ejemplo 1, cambiando el parameto note 
```
http://10.10.102.104/note.php?note=0
```


