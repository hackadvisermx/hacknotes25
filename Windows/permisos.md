# Permisos

## Permisos NTFS basicos

Los permisos pueden ser establecidos por un administrador o una cuenta con privilegios, los permisos pueden ser aplicados a:

- Usuarios
- Grupos

Los permisos que pueden ser establecidos son:

| Permiso                       |  Permite
|:------------------------------|:--------------------
| Full Control                  | Tomar propiedad de la carpeta, establecer permisos para otros, modificar, leer, escribir y ejecutar
| Modificar                     | Modificar, leer, escribir y ejecutar archivos
| Leer & Ejecutar               | Leer y ejecutar archivos
| Listar contenido de carpetas  | Listar el contenido de las carpetas y subcarpetas
| Leer                          | Leer archivos
| Escribir                      | Escrbir datos en el folder especificado 
| Permisos especiales           | Una variedad de permisos avanzados
|


Nota: Puedes permitir o denegar permisos para usuarios o grupos

## Usar la utilería : _icals_

Se puede usar **icacls** para revisar los permisos de una carpeta
```
icacls c:\important
``` 
| Permiso                       |  Permite
|:------------------------------|:--------------------
| I     | permiso herado del contenedor padre
| F     | acceso completo
| M     | permiso de modificación / acceso
| OI    | herencia de objeto
| IO    | solo herencia
| RX    | leer y ejecutar
| AD    | agregar datos (agregar subdirectorios)
| WD    | escribir datos y agregar archivos

Se puede usar **icacls** también para remover o denegr permisos o establecer la propuedad de una carpeta, ejemplo:

```cmd
icacls c:\important\ /setowner Users
```

```cmd
icacls c:\users /remove joe
```

## Permisos para compartir

- Full Control
- Change
- Read