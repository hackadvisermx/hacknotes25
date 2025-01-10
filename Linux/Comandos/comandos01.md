# Comandos Basicos Parte 1

- Buscar un archivo
  
```bash
find . -type f -readable ! -executable -size 1033c
```

- Cambia si inicia por espacio y seguido de lo que sea, por nada
  
```bash
 sed 's/^ *//'
```

- Mostrar linea especifica con awk
```
awk 'NR=1234'
```
- Mandar la salida de error (2) a /dev/null
```
find / -name hola 2>/dev/null
```
- Redirigir el stdin a stderr y todo a dev/null para iniciar de consola con ifaz grafica sin verbose
```
firefox > /dev/null 2>&1
```
- Des asociar un proceso que se habre por ejemplo desde consola
```
disown -a
disown
```
- awk para filtrar
```
awk 'word' file.txt
cat file.txt | awk 'word' | awk '{print $1}' # campo 1
cat file.txt | awk 'word' | awk 'NF{print $NF}' # ultimo elemento de la linea
``` 

- Monitorear cada determinado tiempo
```
watch -n 1 ls -la
```

- ver en que shell estas
```
echo $0
```

 