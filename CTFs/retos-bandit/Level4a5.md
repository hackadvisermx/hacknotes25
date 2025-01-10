# Bandit Level 4 → Level 5
The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

## Datos de acceso
bandit4
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

## Solucion
```bash
bandit4@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 Sep  1 06:30 .
drwxr-xr-x 49 root root 4096 Sep  1 06:30 ..
-rw-r--r--  1 root root  220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root 3771 Jan  6  2022 .bashrc
drwxr-xr-x  2 root root 4096 Sep  1 06:30 inhere
-rw-r--r--  1 root root  807 Jan  6  2022 .profile
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ file ./*
./-file00: OpenPGP Public Key
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
bandit4@bandit:~/inhere$ 
```

