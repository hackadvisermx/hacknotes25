# Bandit Level 2 → Level 3

## Objetivo
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

## Datos de acceso
bandit2
rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Solución
```bash
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces in this filename
cat: spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filename: No such file or directory
bandit2@bandit:~$ cat "spaces in this filename" 
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
bandit2@bandit:~$
```

## Notas adicionales
Cuando un archivo tiene espacios en el nombre, se pueden usar "" para delimitarlo o bien \ en los lugares donde hay espacio.


## Referencias
https://linuxhint.com/reference-filename-with-spaces-linux/