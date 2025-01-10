# Bandit Level 3 → Level 4
The password for the next level is stored in a hidden file in the **inhere** directory.

# Datos de acceso
bandit3
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

# Solucion

```bash
bandit3@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root 4096 Sep  1 06:30 .
drwxr-xr-x 49 root root 4096 Sep  1 06:30 ..
-rw-r--r--  1 root root  220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root 3771 Jan  6  2022 .bashrc
drwxr-xr-x  2 root root 4096 Sep  1 06:30 inhere
-rw-r--r--  1 root root  807 Jan  6  2022 .profile
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Sep  1 06:30 .
drwxr-xr-x 3 root    root    4096 Sep  1 06:30 ..
-rw-r----- 1 bandit4 bandit3   33 Sep  1 06:30 .hidden
bandit3@bandit:~/inhere$ cat .hidden 
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
bandit3@bandit:~/inhere$ 
```

