# Comandos de red en mac


- Apagar y encender adaptador de red
```
sudo ifconfig en0 down
sudo ifconfig en0 up
```

- Apagar y encender el wifi
```
sudo networksetup -setairportpower en0 off
sudo networksetup -setairportpower en0 on
```


- Ver estatus de inrefaz de red
```
sudo ifconfig -u en0
```

- Ver puertos abiertos

```bash
netstat -anvp tcp | awk 'NR<3 || /LISTEN/'
```

- Obtener la ip de la interfaz de red
```
ipconfig getifaddr en4
```
 
```bash
ifconfig -l | xargs -n1 ipconfig getifaddr
```