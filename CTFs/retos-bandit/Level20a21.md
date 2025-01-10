# Bandit Level 18 → Level 19

## Objetivo
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think

## Datos de acceso
bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT


## Solucion
 

```bash
bandit20@bandit:~$ nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 3444802
bandit20@bandit:~$ Listening on 0.0.0.0 2020

bandit20@bandit:~$ ./suconnect 2020
Connection received on 127.0.0.1 48964
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[1]+  Done                    nc -lnvp 2020 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$ 


```
 

## Notas

Funcionamiento de tmux 

```tmux commands
---------------------------------------------------
ctrl + b + c    Crear ventana
ctrl + b + %    Split vertical
ctrl + b + "    Split horizontal
ctrl + b + ,    Renombar Panel
ctrl + b + {    Mover pane a la izquierda
ctrl + b + }    Mover pane a la derecha
ctrl + b + sp   Intercambiar entre panes
ctrl + b + z    Zoom pane
ctrl + b + !    Convertir pane en window
ctrl + b + q    Mostrar los numeros de los panes
ctrl + b + n    Ir a una ventana determinada     
ctrl + b + x    Cerrar pane
Ctrl + b, :     setw -g mouse - activar el mouse
----------------------------------------------------```

tmux ls
tmux a -t 1

```
