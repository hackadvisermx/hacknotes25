# find


- Archivos anteriores a una fecha de modificación

```bash
find / ! -newermt 2000-12-31 -type f -exec ls -la {} \; 2>/dev/null
```

- Archivos modificados en un rango de fechas

```bash
 find /path/to/dir -newermt yyyy-mm-dd ! -newermt yyyy-mm-dd -ls
```

- Archivos con permisos de escritura que se llaman vsftpd*

```bash
find / -writable -name vsftpd* -type f -ls 2>/dev/nul
```

- Encontrar y mostrar el contenido de un archivo

```bash
find . -name file01
find . -name file01 | xargs cat
cat $(find . -name file01)
```
