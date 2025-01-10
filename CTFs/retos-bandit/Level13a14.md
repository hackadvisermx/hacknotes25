cat ## Bandit Level 13 → Level 14
## Objetivo
The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. **Note:** **localhost** is a hostname that refers to the machine you are working on

## Datos de acceso
bandit13
wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

## Solucion

```bash
bandit13@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root     4096 Sep  1 06:30 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
-rw-r-----  1 bandit14 bandit13 1679 Sep  1 06:30 sshkey.private
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost -p 2220
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?

bandit14@bandit:~$ 
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
bandit14@bandit:~$
```

### Notas


ssh-keygen          Permite generar el par de llaves ssh (publica y privada) usando el algortimo RSA

llave privada       Se debe mantener del lado del cliente (no exponer)
llave publica       Se pone en el archivo authorized_keys del lado del servidor 


## Referencias
- https://help.ubuntu.com/community/SSH/OpenSSH/Keys
- 


















