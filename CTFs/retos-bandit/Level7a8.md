# Bandit Level 7 → Level 8
The password for the next level is stored in the file **data.txt** next to the word **millionth**

## Datos de Acceso
level7
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## Solucion
```bash
bandit7@bandit:~$ ls -la
total 4108
drwxr-xr-x  2 root    root       4096 Sep  1 06:30 .
drwxr-xr-x 49 root    root       4096 Sep  1 06:30 ..
-rw-r--r--  1 root    root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root    root       3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit8 bandit7 4184396 Sep  1 06:30 data.txt
-rw-r--r--  1 root    root        807 Jan  6  2022 .profile
bandit7@bandit:~$ cat data.txt | grep millionth
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
```
