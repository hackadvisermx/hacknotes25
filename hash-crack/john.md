# John the ripper




## Crack hash single mode

Es un ataque de fuerza bruta

```
cat hash7.txt 
Joker:7bf6d9bb82bed1302f331fc6b816aada

john --single --format=raw-md5 hash7.txt
```

nota: si no tiene nombre de usuario hay que agregarlo antes para poder usar sigle mode


## Custom rule attack

Permite explotar: password complexity predictability

Estan guardadas en _/etc/john/john.conf_

- Modificadores de posición

| Modificador   | Significado
|:--------------|:--------------------------------------------------|
| Az            | Toma la palabra y agrega a esta un caracter definido
| A0            | Toma la palabra y antepone esta un caracter definido
| c             | Capitaliza la posición del caracter 

Estos modificadores pueden ser usados en combinación para definir donde y que de la palabra quieres modificar.

- Modificadores de caracter

| Modificador   | Significado
|:--------------|:--------------------------------------------------|
| [0-9]         | Incluira números del 0 al 9
| [0]           | Incluye solo el número 0
| [A-z]         | Incluye mayúsculas y minúsculas
| [A-Z]         | Incluye solo mayúsculas
| [a-z]         | Incluye solo minúsculas
| [a]           | Incluye solo la a
| [!@$%]        | Incluye solo los símbolos !@$%

- Crear la regla

  - pone en mayúsculas la primera letra, 
  - agrega al final de la palabra, 
  - números del 0 al 9, 
  - y algunos de los simbolos !£$%@

Poner esto en el archivo _/etc/john/john.conf_ o _/opt/john/john.conf_

[List.Rules:PoloPassword]
cAz"[0-9] [!£$%@]"


## Crack rar file

- Primero convertir a formato de john 
```
rar2john [rar file] > [output file]
```

- Luego ya aplicar el crack
```
john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt
```

