# Bandit Level 5 → Level 6
The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

-   human-readable
-   1033 bytes in size
-   not executable

## Datos de acceso
bandit5
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

## Solucion
```bash
bandit5@bandit:~$ ls -la
total 24
drwxr-xr-x  3 root root    4096 Sep  1 06:30 .
drwxr-xr-x 49 root root    4096 Sep  1 06:30 ..
-rw-r--r--  1 root root     220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root    3771 Jan  6  2022 .bashrc
drwxr-x--- 22 root bandit5 4096 Sep  1 06:30 inhere
-rw-r--r--  1 root root     807 Jan  6  2022 .profile
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ find . -type f -size 1033c 2>/dev/null
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
```

