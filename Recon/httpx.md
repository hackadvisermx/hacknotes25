# httpx



- Un solo dominio
```
 echo www.uaz.edu.mx | httpx -silent
```

- Un subrango de red
```
 echo 148.217.50.1/24 | httpx -silent
```
- Algunas banderas utiles
```
echo 148.217.50.1/24 | httpx -silent -status-code -title
```


Referencias
- [HOW TO FIND XXE BUGS: SEVERE, MISSED AND MISUNDERSTOOD](https://www.bugcrowd.com/blog/how-to-find-xxe-bugs/)
- [XML External Entity (XXE) Processing](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing)