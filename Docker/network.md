# Redes en docker


- Saber si un puerto est expusto en un contenedor
```
docker port pentestdocker 80 
```

- Listar las redes existentes
```
docker network ls
docker network inspect host
```

- Conectar el contenedor a la red local
```
 docker run --rm -it --network host --name pt hackadvisermx/pentestdocker /bin/zsh
```