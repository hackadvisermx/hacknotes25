## Bandit Level 14 → Level 15
## Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.

## Datos de aceso
bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq


## Solucion

```bash 
bandit14@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 Sep  1 06:30 .
drwxr-xr-x 49 root root 4096 Sep  1 06:30 ..
-rw-r--r--  1 root root  220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root 3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root root  807 Jan  6  2022 .profile
drwxr-xr-x  2 root root 4096 Sep  1 06:30 .ssh
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
```


### Notas

nc      Utileria de red en linea de comando que permite abrir o conectarse a un puerto TCP / UDP
-v      Me da informacion del estado del puerto al que me estoy conectando

