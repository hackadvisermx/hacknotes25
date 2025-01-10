# Bandit Level 8 → Level 9
The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once

## Datos de acceso
bandit8
TESKZC0XvTetK0S9xNwm25STk5iWrBvP

## Solucion
```bash
bandit8@bandit:~$ ls -la
total 56
drwxr-xr-x  2 root    root     4096 Sep  1 06:30 .
drwxr-xr-x 49 root    root     4096 Sep  1 06:30 ..
-rw-r--r--  1 root    root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root    root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit9 bandit8 33033 Sep  1 06:30 data.txt
-rw-r--r--  1 root    root      807 Jan  6  2022 .profile
bandit8@bandit:~$ cat data.txt | sort | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit8@bandit:~$ 

```