## **How does it happen?**

Broken Function Level Authorisation reflects a scenario where a low privileged user (e.g., sales) bypasses system checks and gets access to **confidential data by impersonating a high privileged user (Admin)**. Consider a scenario of complex access control policies with various hierarchies, roles, and groups and a vague separation between regular and administrative functions leading to severe authorisation flaws. By taking advantage of these issues, the intruders can easily access the unauthorised resources of another user or, most dangerously – the administrative functions.   

Broken Function Level Authorisation reflects IDOR permission, where a user, most probably an intruder, can perform administrative-level tasks. APIs with complex user roles and permissions that can span the hierarchy are more prone to this attack. 

## **Likely Impact** 

The attack primarily targets the authorisation and non-repudiation principles of security. Broken Functional Level Authorisation can lead an intruder to impersonate an authorised user and let the malicious actor get administrative rights to perform sensitive tasks. 


## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.  
-   Bob has been assigned another task to develop an admin dashboard for company executives so that they can view all employee's data and perform specific tasks.  
-   Bob developed an endpoint `/apirule5/users_v` to fetch data of all employees from the database. To add protection, he added another layer to security by adding a special header `isAdmin` in each request. The API only fetches employee information from the database if `isAdmin=1` and `Authorization-Token` are correct. The authorisation token for HR user Alice is `YWxpY2U6dGVzdCFAISM6Nzg5Nzg=`.

