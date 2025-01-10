# Mass Assignment

## **How does it happen?**

Mass assignment reflects a scenario where **client-side data is automatically bound with server-side objects or class variables**. However, hackers exploit the feature by first understanding the **application's business logic** and sending specially crafted data to the server, acquiring administrative access or inserting tampered data. This functionality is widely exploited in the latest frameworks like Laravel, Code Ignitor etc.  

Consider a user's profiles dashboard where users can update their profile like associated email, name, address etc. The username of the user is a read-only attribute and cannot be changed; however, a malicious actor can edit the username and submit the form. If necessary filtration is not enabled on the server side (model), it will simply insert/update the data in the database. 

## **Likely Impact** 

The attack may result in **data tampering and privilege escalation** from a regular user to an administrator. 

## Practical Example  

-   Open the VM. You will find that the Chrome browser and Talend API Tester application are running automatically, which we will be using for debugging the API endpoints.  
-   Bob has been assigned to develop a signup API endpoint `/apirule6/user` that will take a name, username and password as input parameters (POST). The user's table has a `credit column` with a default value of `50`. Users will upgrade their membership to have a larger credit value.
-   Bob has successfully designed the form and used the mass assignment feature in Laravel to store all the incoming data from the client side to the database (as shown below).

-   What is the problem here? Bob is not doing any filtering on the server side. Since using the **mass assignment feature**, he is also inserting credit values in the database (malicious actors can update that value).  
    
-   The solution to the problem is pretty simple. Bob must ensure necessary filtering on the server side (`apirule6/user_s`) and ensure that the default value of credit should be inserted as `50`, even if more than 50 is received from the client side (as shown below).

```
curl http://localhost/MHT/apirule6/user -d "user=bob&username=bob_thm&password=pass&credit=110"
{"username":"bob_thm","credit":"110","id":5}
```


## **Mitigation Measures** 

-   Before using any framework, one must study how the backend insertions and updates are carried out. In the Laravel framework, [fillable and guarded](https://laravel.com/docs/9.x/eloquent#inserts) arrays mitigate the above-mentioned scenarios. 
-   Avoid using functions that bind an input from a client to code variables automatically.
-   Allowlist those properties only that need to get updated from the client side.

```
curl http://localhost/MHT/apirule6/user_s -d "user=bob&username=bob_thm&password=pass&credit=110"
{"username":"bob_thm","credit":50,"id":6}
```