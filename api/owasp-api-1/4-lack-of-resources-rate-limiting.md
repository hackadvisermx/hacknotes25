## **How does it happen?**

Lack of resources and rate limiting means that **APIs do not enforce any restriction on** the frequency of clients' requested resources or the files' size, which badly affects the API server performance and leads to the DoS (Denial of Service) or non-availability of service. Consider a scenario where an API limit is not enforced, thus allowing a user (usually an intruder) to upload several GB files simultaneously or make any number of requests per second. Such API endpoints will result in excessive resource utilisation in network, storage, compute etc.

Nowadays, attackers are using such attacks to **ensure the non-availability of service for an organisation**, thus tarnishing the brand reputation through increased downtime. A simple example is non-compliance with the Captcha system on the login form, allowing anyone to make numerous queries to the database through a small script written in Python.

## **Likely Impact** 

The attack primarily targets the **Availability** principles of security; however, it can tarnish the brand's reputation and cause financial loss.  

### Practical Example

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.  
-   The company MHT purchased an email marketing plan (20K emails per month) for sending marketing, password recovery emails etc. Bob realised that he had successfully developed a login API, but there must be a "Forgot Password" option that can be used to recover an account.  
-   He started building an endpoint `/apirule4/sendOTP_v` that will send a 4-digit numeric code to the user's email address. An authenticated user will use that One Time Password (OTP) to recover the account.

```
curl http://localhost:80/MHT/apirule4/sendOTP_v -d "email=test@gmail.com"
{"success":"true","msg":"4 Digit OTP sent on Email."}

```

## **Mitigation Measures** 

-   Ensure using a captcha to avoid requests from automated scripts and bots.
-   Ensure implementation of a limit, i.e., how often a client can call an API within a specified time and notify instantly when the limit is exceeded. 
-   Ensure to define the maximum data size on all parameters and payloads, i.e., max string length and max number of array elements.

```
curl http://localhost:80/MHT/apirule4/sendOTP_s -d "sales@gmht.com"
{"success":"false","msg":"Invalid Email"}
```