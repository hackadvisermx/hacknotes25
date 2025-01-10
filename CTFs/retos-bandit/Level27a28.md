# Bandit Level 27 → Level 28

There is a git repository at `ssh://bandit27-git@localhost/home/bandit27-git/repo`. The password for the user `bandit27-git` is the same as for the user `bandit27`.

Clone the repository and find the password for the next level.

## Datos de acceso
bandit27
YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

## Solucion

 
```bash
bandit27@bandit:~$ ls -la
total 20
drwxr-xr-x  2 root root 4096 Sep  1 06:29 .
drwxr-xr-x 49 root root 4096 Sep  1 06:30 ..
-rw-r--r--  1 root root  220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root 3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root root  807 Jan  6  2022 .profile
bandit27@bandit:~$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
fatal: could not create work tree dir 'repo': Permission denied
bandit27@bandit:~$ 
bandit27@bandit:~$ 
```
 

- Clonamos el repo en una carpeta temporal
- Usamos git clone en el puerto 2220
- 
```bash
bandit27@bandit:~$ mkdir /tmp/kgit
bandit27@bandit:~$ cd /tmp/kgit
bandit27@bandit:/tmp/kgit$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo 
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory /home/bandit27/.ssh (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhosts password:  YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
Permission denied, please try again.
bandit27-git@localhosts password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
Receiving objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
```

- entramos al repo y mostramos al README

```bash
bandit27@bandit:/tmp/kgit$ cd repo/
bandit27@bandit:/tmp/kgit/repo$ ls
README
bandit27@bandit:/tmp/kgit/repo$ cat README
The password to the next level is: AVanL161y9rsbcJIsFHuw35rjaOM19nR
```