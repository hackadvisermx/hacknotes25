
## El dns no resuelve en la maquina virtual de vmware Kali

- si esta en modo nat , nada
- si esta en modo puente, nada

### Solucion

- Evitar que el administrador de red controle los dens

- Primero editamos
```
cat /etc/resolv.conf
domain localdomain
search localdomain
nameserver 8.8.8.8
nameserver 8.8.8.4
```

- luego editamos: 
```
sudo nano /etc/NetworkManager/NetworkManager.conf

[main]
dns=none


```

- reiniciamos administrador de red
```
sudo systemctl reload NetworkManager.service

```