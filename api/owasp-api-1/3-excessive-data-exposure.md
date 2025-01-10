
## **How does it happen?**

Excessive data exposure occurs when applications tend to **disclose more than desired information** to the user through an API response. The application developers tend to expose all object properties (considering the generic implementations) without considering their sensitivity level. They leave the filtration task to the front-end developer before it is displayed to the user. Consequently, an attacker can intercept the response through the API and quickly extract the desired confidential data. The runtime detection tools or the general security scanning tools can give an alert on this kind of vulnerability. However, it cannot differentiate between legitimate data that is supposed to be returned or sensitive data. 

## **Likely Impact** 

A malicious actor can successfully sniff the traffic and easily access confidential data, including personal details, such as account numbers, phone numbers, access tokens and much more. Typically, APIs respond with sensitive tokens that can be later on used to make calls to other critical endpoints.

## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.  
    
-   The company MHT launched a comment-based web portal that takes users' comments and stores them in the database and other information like location, device info, etc., to improve the user experience.  
    
-   Bob was tasked to develop an endpoint for showing users' comments on the company's main website. He developed an endpoint `apirule3/comment_v/{id}` that fetches all information available for a comment from the database. Bob assumed that the front-end developer would filter out information while showing it on the company's main website.

```
curl http://localhost/MHT/apirule3/comment_v/1
{"id":1,"postid":"1","deviceid":"Android 12.0","latitude":"45.5426274","longitude":"-122.7944111","commenttext":"This is my First Post","username":"baduser007"}
```


## **Mitigation Measures** 

-   Never leave sensitive data filtration tasks to the front-end developer. 
-   Ensure time-to-time review of the response from the API to guarantee it returns only legitimate data and checks if it poses any security issue. 
-   Avoid using generic methods such as `to_string() and to_json()`. 
-   Use API endpoint testing through various test cases and verify through automated and manual tests if the API leaks additional data.