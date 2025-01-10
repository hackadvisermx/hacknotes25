# Problemas encontrados en Firefox

## Crear otro perfil

about:profiles



## Habilitar puertos restringidos

- Crear la entrada para permitir puertos si no existe y agregar el puerto

https://support.mozilla.org/en-US/questions/1083282

about:config

network.security.ports.banned.override
6666

- Se puede configurar tambien para chrome
https://www.ookangzheng.com/allow-unsafe-port-on-chrome-mac-version/

 ```
 // nano unsafe-chrome.sh 
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --explicitly-allowed-ports=993,465,110,21,22,3389

// give it permission
chmod +x unsafe-chrome.sh

Done
```
Ponerlo como una App en el docker de mac> https://stackoverflow.com/questions/281372/executing-shell-scripts-from-the-os-x-dock

