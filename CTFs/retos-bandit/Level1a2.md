# Bandit Level 1 → Level 2

## Objetivo
The password for the next level is stored in a file called **-** located in the home directory

## Datos de acceso
bandit1
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

## Solución
```bash
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat -
^C
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit1@bandit:~$ pwd
/home/bandit1
bandit1@bandit:~$ cat /home/bandit1/-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit1@bandit:~$ 
```

## Notas adicionales
El comando cat confunde al - como parte la entrada estandar, por lo tanto hay que anteponer ./ al nombre del archivo.

## Referencias
https://www.google.com/search?q=dashed+filename

