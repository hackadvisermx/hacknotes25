https://assets.tryhackme.com/js/api-requests.js?v=2.2

```
curl https://tryhackme.com/api/site-stats

{"publicRooms":806,"totalUsers":2861042,"totalUsersForRanking":953172}

```


```
curl https://tryhackme.com/api/new-rooms 

[{"type":"walkthrough","code":"requestsmugglingbrowserdesync","title":"HTTP Browser Desync","description":"Learn about Request Smuggling Browser Desync.","imageURL":"https://tryhackme-images.s3.amazonaws.com/room-icons/d28eeb115d0cc7cf43776e8b4dc84153.png","creator":"l4m3r8"},{"type":"walkthrough","code":"http2requestsmuggling","title":"HTTP/2 Request Smuggling","description":"Exploit HTTP Request Smuggling in HTTP/2 environments.","imageURL":"https://tryhackme-images.s3.amazonaws.com/room-icons/0e5ada0b18268959026e492c74b9f9b0.svg","creator":"munra"},{"type":"challenge","code":"chrome","title":"Chrome","description":"Let us place all of our trust in a password manager.","imageURL":"https://tryhackme-images.s3.amazonaws.com/room-icons/a0f4ee76b9228435f15a4a89b0c8b9fd.png","creator":"hadrian3689"},{"type":"challenge","code":"exfilibur","title":"Exfilibur","description":"You’ve been asked to exploit all the vulnerabilities present.","imageURL":"https://tryhackme-images.s3.amazonaws.com/room-icons/ec6a4ab94c6bf994398938839bce48ab.png","creator":"l4m3r8"},{"type":"walkthrough","code":"monikerlink","title":"Moniker Link (CVE-2024-21413)","description":"Leak user's credentials using CVE-2024-21413 to bypass Outlook's Protected View.","imageURL":"https://tryhackme-images.s3.amazonaws.com/room-icons/f733b93431c63c39d9eac0e5c0065b8a.png","creator":"cmnatic"},{"type":"walkthrough","code":"cloudbasediac","title":"Cloud-based IaC","description":"Learn about infrastructure as code (IaC) using tools for cloud deployment.","imageURL":"https://tryhackme-images.s3.amazonaws.com/room-icons/0719ee1c2ee2d370c4feaf82cbc859e7.png","creator":"melmols"}]**%**
```

```
curl https://tryhackme.com/api/networks

{"success":true,"rooms":[{"title":"Holo","description":"Holo is an Active Directory (AD) and Web-App attack lab that aims to teach core web attack vectors and more advanced AD attack techniques. This network simulates an external penetration test on a corporate network.","streak":{"enabled":true,"accessTime":10,"number":{"freeUser":7,"subUser":-1}},"freeToUse":false,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/79023e1ed4c207bc52b7dfee208c80a5.png","code":"hololive"},{"title":"Wreath","description":"Learn how to pivot through a network by compromising a public facing web machine and tunnelling your traffic to access other machines in Wreath's network. (Streak limitation only for non-subscribed users)","streak":{"enabled":true,"number":{"freeUser":7,"subUser":-1},"accessTime":10},"freeToUse":true,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/ffa81460a5c1487dd7bb43d0ca0735a1.png","code":"wreath"},{"title":"Breaching Active Directory","description":"This network covers techniques and tools that can be used to acquire that first set of AD credentials that can then be used to enumerate AD.","streak":{"enabled":true,"accessTime":4,"number":{"freeUser":7,"subUser":-1}},"freeToUse":true,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/a936e45c948fb10f2eec7768c7a32e66.png","code":"breachingad"},{"title":"Enumerating Active Directory","description":"This room covers various Active Directory enumeration techniques, their use cases as well as drawbacks.","streak":{"enabled":true,"accessTime":10,"number":{"freeUser":7,"subUser":-1}},"freeToUse":true,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/aab8209b616e6e146df6ceaf7bda48d5.png","code":"adenumeration"},{"title":"Lateral Movement and Pivoting","description":"Learn about common techniques used to move laterally across a Windows network.","streak":{"enabled":true,"accessTime":3,"number":{"freeUser":7,"subUser":-1}},"freeToUse":false,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/2c164794fa55d4805f01fbc5eef79017.png","code":"lateralmovementandpivoting"},{"title":"Exploiting Active Directory","description":"Learn common AD exploitation techniques that can allow you to reach your goal in an AD environment.","streak":{"enabled":true,"accessTime":3,"number":{"freeUser":7,"subUser":-1}},"freeToUse":false,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/9975bcee38db4eff87972247f8895e40.png","code":"exploitingad"},{"title":"Persisting Active Directory","description":"Learn about common Active Directory persistence techniques that can be used post-compromise to ensure the blue team will not be able to kick you out during a red team exercise.","streak":{"enabled":true,"accessTime":4,"number":{"freeUser":7,"subUser":-1}},"freeToUse":false,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/df8f584cce98cbf00bbd8a4da5cc4a09.png","code":"persistingad"},{"title":"Red Team Capstone Challenge","description":"This room is the capstone challenge for the red team learning pathway.","streak":{"enabled":true,"accessTime":7,"number":{"freeUser":7,"subUser":-1}},"freeToUse":false,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/19300c6a4e14181b945aac5104d08c9d.png","code":"redteamcapstonechallenge"},{"title":"Bandit","description":"You’ve been asked to exploit all the vulnerabilities on multiple systems.","streak":{"enabled":true,"accessTime":4,"number":{"freeUser":7,"subUser":-1}},"freeToUse":true,"imageUrl":"https://tryhackme-images.s3.amazonaws.com/room-icons/602513b69ffd0bb6e7d2dd7899816661.png","code":"bandit"}]}%
```



https://assets.tryhackme.com/js/script.js?v=3.12

```
curl https://tryhackme.com/api/user/rank/hackuaz2024
{"userRank":209773}%
```

```
curl https://tryhackme.com/api/server-time
{"datetime":"2024-03-06T16:45:45.060Z"}**%**
```


https://assets.tryhackme.com/js/pages/hacktivities/content.js?v=0.7

```
curl https://tryhackme.com/api/content/hacktivities
```
```

## explorar

```
/api/v2/users/saved-rooms?code=
castr@mymac ~ % curl https://tryhackme.com/api/v2/users/saved-rooms
{"status":"error","message":"Unauthorized"}%

```


