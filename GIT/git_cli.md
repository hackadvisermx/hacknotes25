# GIT


- Mantiene el seguimiento de los cambios al código
- Sincroniza código entre diferentes personas
- Probar cambios al código sin perder el original (branch)
- Regresar a una versión anterior de código


## Manejo de credenciales

- Brrar las credenciales anteriores

```
git config --system --unset credential.helper
```

## Ligar codigo existente a un repositorio vacio en git

```
echo “# sisinfogeo2021 >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/castruaz/sisinfogeo2021.git
git push -u origin master 
```





## Crear un repositorio nuevo, clonarlo y hacer cambios

- Crear el repositorio en github: https://github.com/new
- Clonar el repositorio localmente
```
git clone https://github.com/hackadvisermx/hello.git
```
- Crear un archivo y agregarlo
```
touch index.html
git add index.html
git status
```

- Poner mi archivo(s) agregados en la lista de espera para subir (commit)
```
git commit -m "Inicial"
```

- Subir los cambios
```
git push
```

- Agregar y poner en commit todos los archivos que hayan cambiado
```
git commit -m "los cambios"
git push
```

### Hacer cambios en el repo en github, bajarlos al repo local

- Hacer los cambios requeridos directamente en github
- Sincronizar el repo con la copia local
```
git pull
```

## Branching

Permite trabajar en diferentes partes del repositorio al mismo tiempo

- crear una nueva rama y moverse a ella
```
git checkout -b style
```

- regresarme al branch master
```
git checkout master 
```

- mesclar _style_ en _master_
```
git checkout master
git merge style
```
Nota: Talvez se generen conflitos, se corrigen y se hace push de nuvo


- Borrar una rama
```
git branch -d style
```













