# Bandit Level 9 → Level 10

## Objetivo
The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

## Datos de acceso

bandit9
EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## Solucion

```bash
bandit9@bandit:~$ ls -la
total 40
drwxr-xr-x  2 root     root     4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root     4096 Sep  1 06:30 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit10 bandit9 19379 Sep  1 06:30 data.txt
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit9@bandit:~$ strings data.txt | grep ==
========== the
bu========== password
4iu========== is
b~==P
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$ 
```

## Notas:

strings         imprime las cadenas (ascii) en un archivo binario
-n              permite especificar el tamano de la cadena
grep            filtra lineas en base a un patron
