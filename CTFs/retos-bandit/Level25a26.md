# Bandit Level 25 → Level 26

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

## Datos de acceso
bandit25
p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

## Solucion

```bash
bandit25@bandit:~$ ls -la
total 32
drwxr-xr-x  2 root     root     4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root     4096 Sep  1 06:30 ..
-rw-r-----  1 bandit25 bandit25   33 Sep  1 06:30 .bandit24.password
-r--------  1 bandit25 bandit25 1679 Sep  1 06:30 bandit26.sshkey
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit25 bandit25    4 Sep  1 06:30 .pin
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost -p2220

```

```bash
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost -p2220
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory /home/bandit25/.ssh (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames


..
..
..

  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/ 
Connection to localhost closed.
```

El shell no es un shell tradicional
```bash
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
bandit25@bandit:~$
```

- El archivo es abierto por el comando more
- La solucion pasa por reducr el tam de la pantalla
- Luego iniciar el editor desde more

```
   v
           Start up an editor at current line. The editor is taken from the environment variable VISUAL if defined, or EDITOR if VISUAL is not defined, or defaults to vi(1) if neither VISUAL nor EDITOR
           is defined.
```

- Presonamos `v` e iniciamos el editor vi
- Presionamos `:` y editamos el archivo

```
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
:e /etc/bandit_pass/bandit26
```

- el archiv se abre y muestre el password 
```bash
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
~                                                                                                                                                                                                               
~                                                                                                                                                                                                               
~                                                                                                                                                                                                               
"/etc/bandit_pass/bandit26" [readonly] 1L, 33B
```

. salimos del editor
```
:!q
```

. regresamos
```
  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
--More--(66%)
```


