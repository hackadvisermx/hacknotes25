# Comandos Linux


## Gestionar permisos

- Se dividen en tres grupos, u, g, o:

```
 u   g   o
 rwx rwx rwx
```

|Letra | Significado|
|:---|:-------------|
| u  | user
| g  | group
| o  | others

|Letra | Significado|
|:---|:-------------|
| r  | read
| w  | write
| x  | execute 

- cambiar los permisos usando letras

Pone permisos rwx al usuario y quite permisos rx a otros en la misma linea

```
chmod u+rwx,o-rx file.txt
```
- cambiar permisos usando numeros

Las letras se pueden convertir en numeros de acuerdo a su posicion en binario
```
rwx     111     7 
rw-     110     6
r-x     101     5
r--     100     4
-wx     011     3
-w-     010     2
--x     001     1
```

## Gestion de permisos especiales

Existen algunos permisos que no se enumeran de manera simple, 
```
lsattr
```
| Permiso               | Significado |
|:----------------------|:-----------------------------------------------------------|
| SUID (Set User ID)    | permite ejecutar como si fuese el propietario (4XXX)
| SGID (Set group ID)   | permite ejecutar como si fuese del grupo porpiedad del archivo
|                       | en un directorio los archivos nuevos son asignados al grupo del directorio
| Sticky bit            | evita que los usuarios no propietarios borren
|                       | en un dir, los archivos solo pueden ser borrados o renombrados por su propietario
