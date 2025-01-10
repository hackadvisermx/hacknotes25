# grep


| Bandera | Descripción |
|---------|---------------|
| -R | Efectua un grep recursivo |
| -h | Deshabilito, en un grep recursivo, el prefijo nombre del archivo
| -c | No lista el pattern como tal si no un NUM de cuantas veces aparece
| -i | Ignora may / min |
| -l | Lista el nombre del archivo en lugar del pattern buscad |
| -n | Lista el número de línea |
| -v | Las lineas que "no coinciden" |
| -E | El pattern como expresión regular (Extended regular Expresion)
| -e | Múltiples patterns (Basic Regular Expresions)|

- [Basic vs Extended (GNU Grep 3.5](https://www.gnu.org/software/grep/manual/html_node/Basic-vs-Extended.html)

grep, egrep, fgrep
grep -E = egrep / machea la expresion regular en la cadena
grep -F = fgrep / machea una cadena fija



- Grep si inicia (^) por root
```bash
 | grep '^root'
```

- Que inicia con hola (^) y termina en a ($) 
```bash
grep '^hola$'
```

- Palabras entre comillas sencillas
```bash
grep -E  "([']*['])" grep.txt
```

