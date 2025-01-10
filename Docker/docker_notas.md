
# Docker

## Iniciales
 
```
docker info 
docker version
```
## Publicar imagen
```
docker login
docker tag hackadviser/docker-ofensivo
```
## Contenedores
- ver contenedores
```
docker ps -a 
```
- ejecutar contenedor y autoborrar
```
docker run -it --rm contenedor bash
```
- entrar a un contenedor ya existente
```
docker exec -it contenedor bash
```
- borrrar contenedor
```
docker rm contenedor
```
- borrar todos los contenedores
```
docker ps -a -q
```
```
docker rm $(docker ps -a -q)
```

- borrar imagenes excepto una
```
 docker rmi $(docker images -a | grep -v 'kalidocker' | awk 'NR>1 {print $3}')
```