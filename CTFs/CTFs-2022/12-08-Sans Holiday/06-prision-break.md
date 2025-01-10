
- al conectar
```
Greetings Noble Player, 

You find yourself in a jail with a recently captured Dwarven Elf.

He desperately asks your help in escaping for he is on a quest to aid a friend in a search for treasure inside a crypto-mine. 

If you can help him break free of his containment, he claims you would receive "MUCH GLORY!"

Please, do your best to un-contain yourself and find the keys to both of your freedom.
```


- sacamos la ip actual
```
grinchum-land:/# cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.18.0.99     grinchum-land
grinchum-land:/# 
```

- hacemos un nmap
```

grinchum-land:/# nmap 172.18.0.1/24
Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-11 13:18 GMT
Nmap scan report for 172.18.0.1
Host is up (0.0000040s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
2222/tcp open  EtherNetIP-1
MAC Address: 02:42:E0:FD:C9:95 (Unknown)

Nmap scan report for grinchum-land (172.18.0.99)
Host is up (0.0000030s latency).
Not shown: 999 closed tcp ports (reset)
PORT     STATE SERVICE
2222/tcp open  EtherNetIP-1

Nmap done: 256 IP addresses (2 hosts up) scanned in 1.93 seconds
```

- vemos discos montados y montamos en el contenedor
```
grinchum-land:~$ sudo -l
User samways may run the following commands on grinchum-land:
    (ALL) NOPASSWD: ALL
grinchum-land:~$ sudo su
grinchum-land:/home/samways# fdisk -l
Disk /dev/vda: 2048 MB, 2147483648 bytes, 4194304 sectors
2048 cylinders, 64 heads, 32 sectors/track
Units: sectors of 1 * 512 = 512 bytes

Disk /dev/vda doesn't contain a valid partition table
grinchum-land:/home/samways# mount /dev/vda /mnt
grinchum-land:/home/samways# cd /mnt/home
grinchum-land:/mnt/home# ls
jailer
grinchum-land:/mnt/home# 
grinchum-land:/mnt/home# cd jailer/.ssh/
grinchum-land:/mnt/home/jailer/.ssh# ls
jail.key.priv  jail.key.pub
grinchum-land:/mnt/home/jailer/.ssh# cat jail.key.priv 

                Congratulations! 

          You've found the secret for the 
          HHC22 container escape challenge!

                     .--._..--.
              ___   ( _'-_  -_.'
          _.-'   `-._|  - :- |
      _.-'           `--...__|
   .-'                       '--..___
  / `._                              \
   `. `._               one           |
     `. `._                           /
       '. `._    :__________....-----'
         `..`---'    |-_  _- |___...----..._
                     |_....--'             `.`.
               _...--'                       `.`.
          _..-'                             _.'.'
       .-'             step                _.'.'
       |                               _.'.'
       |                   __....------'-'
       |     __...------''' _|
       '--'''        |-  - _ |
               _.-''''''''''''''''''-._
            _.'                        |\
          .'                         _.' |
          `._          closer           |:.'
            `._                     _.' |
               `..__                 |  |
                    `---.._.--.    _|  |
                     | _   - | `-.._|_.'
          .--...__   |   -  _|
         .'_      `--.....__ |
        .'_                 `--..__
       .'_                         `.
      .'_    082bb339ec19de4935867   `-.
      `--..____                        _`.
               ```--...____          _..--'
                     | - _ ```---.._.'
                     |   - _ |
                     |_ -  - |
                     |   - _ |
                     | -_  -_|
                     |   - _ |
                     |   - _ |
                     | -_  -_|
grinchum-land:/mnt/home/jailer/.ssh# 
```

- enviar el secreto en el avatar y listo



## referencias 
- https://tbhaxor.com/container-breakout-part-1/