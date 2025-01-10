# Improper Assets Management

## **How does it happen?**
Inappropriate Asset Management refers to a scenario where we have **two versions of an API available in our system**; let's name them APIv1 and APIv2. Everything is wholly switched to APIv2, but the previous version, APIv1, has not been deleted yet. Considering this, one might easily guess that the older version of the API, i.e., APIv1, doesn't have the updated or the latest security features. Plenty of other obsolete features of APIv1 make it possible to find vulnerable scenarios, which may lead to data leakage and server takeover via a shared database amongst API versions.

It is essentially about not properly tracking API endpoints. The potential reasons could be incomplete API documentation or absence of compliance with the [Software Development Life Cycle](https://tryhackme.com/room/securesdlc). A properly maintained, up-to-date API inventory and proper documentation are more critical than hardware-based security control for an organisation.  

## **Likely Impact** 

The older or the **unpatched API versions** can allow the intruders to get unauthorised access to confidential data or even complete control of the system. 

## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.  
-   During API development, the company MHT has developed different API versions like v1 and v2. The company ensured to use the latest versions and API calls but forgot to remove the old version from the server.  
-   Consequently, it was found that old API calls like `apirule9/v1/user/login` return more information like balance, address etc., against the user (as shown below).

```
curl http://localhost/MHT/apirule9/v1/user/login -d "username=alice&password=##!@#!!"
{"id":1,"username":"alice"," Balance":"100","country":"USA"}
```

```
curl http://localhost/MHT/apirule9/v2/user/login -d "username=alice&password=##!@#!!"
{"id":1,"username":"alice"}
```