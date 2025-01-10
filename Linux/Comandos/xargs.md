# xargs

| Bandera | Descripción |
|---------|---------------|
| -I str | Crea una variable para posterior uso |
| -p | Pregunta antes de ejecutar el comando |
| -t  | Modo verbose del comando |



- Ejecutar varios comandos a las vez
 ```bash
 echo "ids.txt allports" | xargs -p -I arch bash -c '{ ls arch; wc arch; }'
```

 |