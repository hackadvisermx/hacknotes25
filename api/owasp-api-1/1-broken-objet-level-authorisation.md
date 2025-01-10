## Broken Object Level Authorisation (BOLA)

## **How does it Happen?**

Generally, API endpoints are utilised for a common practice of retrieving and manipulating data through object identifiers. BOLA refers to Insecure Direct Object Reference (IDOR) - which creates a scenario where the user uses the **input functionality and gets access to the resources they are not authorised to access**. In an API, such controls are usually implemented through programming in Models (Model-View-Controller Architecture) at the code level.

## Likely Impact

The absence of controls to prevent **unauthorised object access can lead to data leakage** and, in some cases, complete account takeover. User's or subscribers' data in the database plays a critical role in an organisation's brand reputation; if such data is leaked over the internet, that may result in substantial financial loss.

## **Practical Example**  

-   Open the VM. You will find that the Chrome browser and Talend API Tester application are running automatically, which we will be using for debugging the API endpoints.
-   Bob is working as an API developer in `Company MHT` and developed an endpoint `/apirule1/users/{ID}` that will allow other applications or developers to request information by sending an employee ID. In the VM, you can request results by sending `GET` requests to `http://localhost:80/MHT/apirule1_v/user/1.`

```
http://127.0.0.1/MHT/apirule1_v/user/1

{
"id": 1,
"username": "John",
"name": "Scott",
"flag": "THM{00123123}"
}
```

- What is the issue with the above API call? The problem is that the endpoint is not validating any incoming API call to confirm whether the request is valid. It is not checking for any authorisation whether the person requesting the API call can ask for it or not.   
-  The solution for this problem is pretty simple; Bob will implement an authorisation mechanism through which he can identify who can make API calls to access employee ID information.  
-  The purpose is achieved through **access tokens or authorisation tokens** in the header. In the above example, Bob will add an authorisation token so that only headers with valid authorisation tokens can make a call to this endpoint.
-  In the VM, if you add a valid `Authorization-Token` and call `http://localhost:80/MHT/apirule1_s/user/1`, only then will you be able to get the correct results. Moreover, all API calls with an invalid token will show `403 Forbidden` an error message (as shown below).


## **Mitigation Measures**

-   An authorisation mechanism that relies on user policies and hierarchies should be adequately implemented. 
-   Strict access controls methods to check if the logged-in user is authorised to perform specific actions. 
-   Promote using completely random values (strong encryption and decryption mechanism) for nearly impossible-to-predict tokens.