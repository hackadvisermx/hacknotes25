# App Engine: Qwik Start - Python

```
gcloud auth list

Credentialed Accounts

ACTIVE: *
ACCOUNT: student-00-9f2b459ff667@qwiklabs.net

To set the active account, run:
    $ gcloud config set account `ACCOUNT`
```

```
gcloud config list project
[core]
project = qwiklabs-gcp-01-5a04f12dac83

Your active configuration is: [cloudshell-19492]
```

- Habilite el API > **App Engine Admin AP**
- Descargamos la aplicación
```
git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
cd python-docs-samples/appengine/standard_python3/hello_world
```

- Probamos la aplicación con: Google Cloud development server
```
dev_appserver.py app.yaml
```

- previsualizamos en el puerto 80:
```
https://8080-cs-25077ca5-32a9-4ad4-9999-ae40377fc513.ql-us-central1-pihl.cloudshell.dev/?authuser=1&redirectedPreviously=true
```

## Tarea 4  Hacer un cambio

- Iniciamos una nueva ventana de consola
- Nos desplazamos a la carpeta y modificamos
```
cd python-docs-samples/appengine/standard_python3/hello_world
nano main.py
```


## Tara 5 - Desplegamos la app

```
gcloud app deploy
```
Seleccionamos la region
Aceptamos el nombre por defecto

## Tarea 6 - Ver la aplicacion

```
gcloud app browse
https://qwiklabs-gcp-01-5a04f12dac83.de.r.appspot.com
```