# Comandos shell windows ejemplos


- Agregar lineas a hosts y luego quitar la ultima
```
AC C:\Windows\System32\drivers\etc\hosts "10.10.163.131   overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm" 
(GC C:\Windows\System32\drivers\etc\hosts | select -Skiplast 1) | SC C:\Windows\System32\drivers\etc\hosts
```