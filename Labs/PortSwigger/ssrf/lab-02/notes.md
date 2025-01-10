# Lab #2 - Basic SSRF against another back-end system

https://portswigger.net/web-security/ssrf#ssrf-attacks-against-other-back-end-systems
https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system

https://www.youtube.com/watch?v=DKCVDS7c7-4&list=PLuyTk2_mYISIlDtWBIqmgJgn6CYlzHVsQ&index=3
https://github.com/rkhal101/Web-Security-Academy-Series/tree/main/ssrf/lab-02

Vulnerable feature - stock check functionality

Goal -  use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos. 

## Analysis:

application running on: http://192.168.0.190:8080/admin

delete carlos: http://192.168.0.190:8080/admin/delete?username=carlos

python3 script.py <url>

192.168.0.255