- Al acceder
```
######################################################
Sun Dec 11 14:11:33 UTC 2022
On attempt [7] of trying to connect.
If no connection is made after [60] attempts
contact the holidayhack sys admins via discord.
######################################################
 
Greetings Noble Player, 

Many thanks for answering our desperate cry for help!

You may have heard that some evil Sporcs have opened up a web-store selling 
counterfeit banners and flags of the many noble houses found in the land of 
the North! They have leveraged some dastardly technology to power their 
storefront, and this technology is known as PHP! 

***gasp*** 

This strorefront utilizes a truly despicable amount of resources to keep the 
website up. And there is only a certain type of Christmas Magic capable of 
powering such a thing… an Elfen Ring!

Along with PHP there is something new we've not yet seen in our land. 
A technology called Continuous Integration and Continuous Deployment! 

Be wary! 

Many fair elves have suffered greatly but in doing so, they've managed to 
secure you a persistent connection on an internal network. 

BTW take excellent notes! 

Should you lose your connection or be discovered and evicted the 
elves can work to re-establish persistence. In fact, the sound off fans
and the sag in lighting tells me all the systems are booting up again right now.  

Please, for the sake of our Holiday help us recover the Ring and save Christmas!
grinchum-land:~$ 
```

- reconocemos terremo
```
grinchum-land:~# nmap 172.18.0.1/24 -p- -T4
Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-12 02:52 GMT
Nmap scan report for 172.18.0.1
Host is up (0.0000070s latency).
Not shown: 65529 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
2222/tcp  open  EtherNetIP-1
8080/tcp  open  http-proxy
8088/tcp  open  radan-http
10022/tcp open  unknown
MAC Address: 02:42:7E:59:A7:BB (Unknown)

Nmap scan report for wordpress-db.local_docker_network (172.18.0.87)
Host is up (0.0000090s latency).
Not shown: 65534 closed tcp ports (reset)
PORT     STATE SERVICE
3306/tcp open  mysql
MAC Address: 02:42:AC:12:00:57 (Unknown)

Nmap scan report for wordpress.local_docker_network (172.18.0.88)
Host is up (0.0000090s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:42:AC:12:00:58 (Unknown)

Nmap scan report for gitlab.local_docker_network (172.18.0.150)
Host is up (0.0000090s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8181/tcp open  intermapper
MAC Address: 02:42:AC:12:00:96 (Unknown)

Nmap scan report for grinchum-land.flag.net.internal (172.18.0.99)
Host is up (0.0000040s latency).
Not shown: 65534 closed tcp ports (reset)
PORT     STATE SERVICE
2222/tcp open  EtherNetIP-1

Nmap done: 256 IP addresses (5 hosts up) scanned in 7.11 seconds
grinchum-land:~# 

```

- Lista de los repos:
```jquery 
grinchum-land:/app# curl --silent http://gitlab.local_docker_network/api/v4/projects | jq .
[
  {
    "id": 2,
    "description": null,
    "name": "Wordpress.Flag.Net.Internal",
    "name_with_namespace": "Rings of Powder / Wordpress.Flag.Net.Internal",
    "path": "wordpress.flag.net.internal",
    "path_with_namespace": "rings-of-powder/wordpress.flag.net.internal",
    "created_at": "2022-10-27T01:08:54.411+05:30",
    "default_branch": "main",
    "tag_list": [],
    "topics": [],
    "ssh_url_to_repo": "ssh://git@gitlab.flag.net.internal:10022/rings-of-powder/wordpress.flag.net.internal.git",
    "http_url_to_repo": "http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal.git",
    "web_url": "http://gitlab.flag.net.internal/rings-of-powder/wordpress.flag.net.internal",
    "readme_url": null,
    "avatar_url": null,
    "forks_count": 0,
    "star_count": 0,
    "last_activity_at": "2022-10-27T02:28:21.672+05:30",
    "namespace": {
      "id": 5,
      "name": "Rings of Powder",
      "path": "rings-of-powder",
      "kind": "group",
      "full_path": "rings-of-powder",
      "parent_id": null,
      "avatar_url": null,
      "web_url": "http://gitlab.flag.net.internal/groups/rings-of-powder"
    }
  }
]
```

- Clonamos el repo
```
git clone http://gitlab.local_docker_network/rings-of-powder/wordpress.flag.net.internal.git
```

- Hacer un tar recursivo a lo clonado
```

```



## Referencias

- https://bytefreaks.net/gnulinux/bash/gitlab-com-get-a-list-with-the-names-of-all-repositories-in-your-account
- 