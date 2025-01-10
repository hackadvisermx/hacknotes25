# tr

Traduce de diferentes formas la fuente con el destino

- Sintaxis
```bash
tr [flags] [source]/[find]/[select] [destination]/[replace]/[change]
```

| Bandera | Descripción |
|---------|---------------|
| -d | Borra un cnjunto de caracteres |
| -s | Remplaza la fuente con el destino |
| -c | Hace todo en reversa
| :lower: | Minúsculas |
| :upper: | Mayúsculas |
| :digit: | Números o dígtos |
| :alpha: | Alfanumérico |
| :xdigit: | Dígito hexadecimal |



- Convierte minúsculas a mayúsculas
```bash
cat file.txt | tr -s '[a-z]' '[A-Z]'
cat file.txt | tr -s '[:lower:]' '[:upper:]'
```

- Eliminar letras, :, espacio
```bash
cat creds.txt | tr -d [a-zA-Z: ]
```


