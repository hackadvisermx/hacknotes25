
```
set **NAME**=_myname_  

reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v %NAME% /t REG_DWORD /d 0 /f  
echo this is a dummy line
```


```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v xpc /t REG_DWORD /d 0 /f  
```


- Referencias
- https://morgantechspace.com/2014/11/set-allow-log-on-locally-user-rights-via-powershell-cmd-csharp.html
- https://www.infopackets.com/news/10109/how-fix-hide-user-accounts-windows-7-8-10-login-screen