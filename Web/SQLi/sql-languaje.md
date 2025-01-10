# SQL Languaje


## INSERT

```cmd
INSERT INTO table_name VALUES (column1_value, column2_value, column3_value, ...);
INSERT INTO logins VALUES(1, 'admin', 'p@ssw0rd', '2020-07-02');
```

## SELECT

```cmd
SELECT column1, column2 FROM table_name;
SELECT * FROM logins;
SELECT username,password FROM logins;
```

### SELECT ... ORDER BY

```cmd
SELECT * FROM logins ORDER BY password;
SELECT * FROM logins ORDER BY password DESC;
SELECT * FROM logins ORDER BY password DESC, id ASC;
```

### SELECT ... LIMIT

```cmd
SELECT * FROM logins LIMIT 2
SELECT * FROM logins LIMIT 1, 2
```

### SELECT ... WHERE

```cmd
SELECT * FROM table_name WHERE <condition>;
SELECT * FROM logins WHERE id > 1;
SELECT * FROM logins where username = 'admin';
```

### SELECT - WHERE .. LIKE

```
SELECT * FROM logins WHERE username LIKE 'admin%';
SELECT * FROM logins WHERE username like '___';
```

## OPERATORS AND / OR / NOT

```cmd
SELECT 1 = 1 AND 'test' = 'test';
SELECT 1 = 1 AND 'test' = 'abc';
SELECT 1 = 1 && 'test' = 'abc';
```

```cmd
SELECT 1 = 1 OR 'test' = 'abc';
SELECT 1 = 2 OR 'test' = 'abc';
SELECT 1 = 1 || 'test' = 'abc';
```

```cmd
SELECT NOT 1 = 1;
SELECT NOT 1 = 2;
SELECT 1 != 1;
```

```cmd
SELECT * FROM logins WHERE username != 'john';
SELECT * FROM logins WHERE username != 'john' AND id > 1;
```



## DROP

```cmd
DROP TABLE logins;
```

### ALTER

```cmd
ALTER TABLE logins ADD newColumn INT;
ALTER TABLE logins RENAME COLUMN newColumn TO oldColumn;
ALTER TABLE logins MODIFY oldColumn DATE;
ALTER TABLE logins DROP oldColumn;
```

## UPDATE

```cmd
UPDATE table_name SET column1=newvalue1, column2=newvalue2, ... WHERE <condition>;
UPDATE logins SET password = 'change_password' WHERE id > 1;
```

## UNION

```cmd
SELECT * FROM ports UNION SELECT * FROM ships;
```
Nota: solo opera con select de igual nuemero de columnas

