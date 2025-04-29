#pipenv

Es un administrador de ambientes virtuales de python3, actualmente ya no es compatible con Python2

- Crea un ambiente virtual dependiendo la carpeta donde te encuentras
- Los almacena en .local/share/virutalenvs
- Crea un archivo de seguimiento en la carpeta del proyecto : PipFile

Es mas bien para ambientes de desarrollo:

# 📦 Pipenv: Qué es, cómo funciona y ejemplos

## ✅ ¿Qué es Pipenv?

`Pipenv` es una herramienta para gestionar **dependencias** y **entornos virtuales** en proyectos de Python. Combina lo mejor de `pip` y `virtualenv` en una sola herramienta más automatizada y organizada.

##  ¿Cómo funciona?

Cuando usas `pipenv`, este:

1. **Crea un entorno virtual** (si no existe uno).
2. **Instala las dependencias** y las registra en archivos:
    - `Pipfile`: lista de paquetes que necesita tu proyecto. 
    - `Pipfile.lock`: versiones exactas para asegurar entornos reproducibles.
        
## ¿Para qué se utiliza?

- Aislar dependencias por proyecto.
- Evitar conflictos entre paquetes.
- Facilitar despliegues y compartir entornos.
- Reemplazar el uso manual de `requirements.txt` y `virtualenv`.
    
---

## 📌 Comandos Básicos

###  Crear un entorno y archivo Pipfile

`pipenv install`

Esto crea un `Pipfile` y un entorno virtual.

###  Instalar una librería

`pipenv install requests`

Instala `requests` y la registra en el `Pipfile`.

### Desinstalar una librería

`pipenv uninstall requests`

###  Ejecutar un script dentro del entorno virtual

`pipenv run python script.py`

###  Entrar al entorno virtual

`pipenv shell`

Esto te coloca dentro del entorno virtual activado.

---

## 📄 Archivos importantes

- `Pipfile`: define las dependencias del proyecto.
- `Pipfile.lock`: guarda versiones exactas para entornos reproducibles.
    

---

## 📘 Ejemplo sencillo

### Paso 1: Crear carpeta y moverte a ella

`mkdir mi_proyecto cd mi_proyecto`

### Paso 2: Crear entorno e instalar dependencias

`pipenv install requests`

### Paso 3: Crear un archivo Python

**script.py**:

`import requests  response = requests.get('https://httpbin.org/get') print(response.json())`

### Paso 4: Ejecutarlo

`pipenv run python script.py`

---
##  Para limpiar el entorno

`pipenv --rm`

Esto elimina el entorno virtual del proyecto.
