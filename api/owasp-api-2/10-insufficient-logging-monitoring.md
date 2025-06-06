
# Insufficient Logging & Monitoring

## **How does it happen?**

Insufficient logging & monitoring reflects a scenario when an attacker conducts malicious activity on your server; however, when you try to track the hacker, **there is not enough evidence available due to the absence of logging and monitoring mechanisms**. Several organisations only focus on infrastructure logging like network events or server logging but lack API logging and monitoring. Information like the visitor's IP address, endpoints accessed, input data etc., along with a timestamp, enables the identification of threat attack patterns. If logging mechanisms are not in place, it would be challenging to identify the attacker and their details. Nowadays, the latest web frameworks can automatically log requests at different levels like error, debug, info etc. These errors can be logged in a database or file or even passed to a [SIEM solution](https://tryhackme.com/room/defensivesecurity) for detailed analysis.

## **Likely Impact** 

Inability to identify attacker or hacker behind the attack. 

## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.  
-   In the past, the company MHT has been susceptible to multiple attacks, and the exact culprit behind the attacks could not be identified. Therefore, Bob was assigned to make an API endpoint `/apirule10/logging` (GET) that will log users' metadata (IP address, browser version etc.) and save it in the database as well (as shown below)

```
curl http://localhost/MHT/apirule10/logging
{"message":"Hi, an abnormal activity has been detected. Your IP address 127.0.0.1 Browser: curl\/7.55.1 Timestamp: 2023-01-27 20:45:11 has been logged"}
```

-   Later, it was also decided that the same would be forwarded to a SIEM solution for correlation and analysis.

## **Mitigation Measures** 

-   Ensure use of the Security Information and Event Management (SIEM) system for log management. 
-   Keep track of all denied accesses, failed authentication attempts, and input validation errors, using a format imported by SIEM and enough detail to identify the intruder.
-   Handle logs as sensitive data and ensure their integrity at rest and transit. Moreover, implement custom alerts to detect suspicious activities as well.

