## **How does it happen?**

Injection attacks are probably among the oldest API/web-based attacks and are still being carried out by hackers on real-world applications. Injection flaws occur when user input is **not filtered and is directly processed by an API**; thus enabling the attacker to perform unintended API actions without authorisation. An injection may come from [Structure Query Language (SQL)](https://tryhackme.com/room/sqlinjectionlm), operating system (OS) commands, Extensible Markup Language (XML) etc. Nowadays, frameworks offer functionality to protect against this attack through automatic sanitisation of data; however, applications built in custom frameworks like core PHP are still susceptible to such attacks. 


## **Likely Impact** 

Injection flaws may lead to **information disclosure, data loss, DoS, and complete account takeover**. The successful injection attacks may also cause the intruders to access the sensitive data or even create new functionality and perform remote code execution. 

## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.  
-   A few users of company MHT reported that their account password had changed, and they could not further log in to their original account. Consequently, the dev team found that Bob had developed a vulnerable login API endpoint `/apirule8/user/login_v` that is not filtering user input.  
-   A malicious attacker requires the username of the target, and for the password, they can use the payload `' OR 1=1--'` and get an authorisation key for any account (as shown below).
-   Bob immediately realised his mistake; he updated the API endpoint to `/apirule8/user/login_s` and used parameterised queries and built-in filters of Laravel to sanitise user input.
-   As a result, all malicious payloads on username and password parameters were effectively mitigated (as shown below)

```
curl http://localhost/MHT/apirule8/user/login_v -d "username=admin&password=admin"
{"success":"false","cause":"IncorrectUsernameOrPassword"}
```

```
curl http://localhost/MHT/apirule8/user/login_v -d "username=admin&password='%20OR%201=1--'"
{"success":"true","authkey":"oWsZ8vWNuECjCAiZVJHOzsNsNH08zWRZ"}
```