# How to catch snakes
## Descripción del reto

Nos deslizamos como una serpiente y accedimos a información confidencial disponible en un carpeta copartida, para poder extraerla sin ser descubiertos la hemos encriptado forma muy sencilla

We slipped like a snake and accessed confidential information available in a shared folder, in order to extract it without being discovered we have encrypted it in a simple way.

## Creación del reto

- la bandera original

flagMX{hiddenmessagewitholdstuff}

- quitamos las llaves de la bandera para convertir a ascii con caracteres validos

 flagMXhiddenmessagewitholdstuff

- Use cyberchef para convertir la bandera a morse
..-. .-.. .- --. -- -..- .... .. -.. -.. . -. -- . ... ... .- --. . .-- .. - .... --- .-.. -.. ... - ..- ..-. ..-.

- Luego converti la cadena a hex

0a2e2e2d2e202e2d2e2e202e2d202d2d2e202d2d202d2e2e2d202e2e2e2e202e2e202d2e2e202d2e2e202e202d2e202d2d202e202e2e2e202e2e2e202e2d202d2d2e202e202e2d2d202e2e202d202e2e2e2e202d2d2d202e2d2e2e202d2e2e202e2e2e202d202e2e2d202e2e2d2e202e2e2d2e

- Luego convertimos 20 a 7c , 2e a 20, 2d a 09

202009207c200920207c20097c0909207c09097c092020097c202020207c20207c0920207c0920207c207c09207c09097c207c2020207c2020207c20097c0909207c207c2009097c20207c097c202020207c0909097c200920207c0920207c2020207c097c2020097c202009207c20200920

- Luego todo a ascii
  	 | 	  | 	|		 |		|	  	|    |  |	  |	  | |	 |		| |   |   | 	|		 | | 		|  |	|    |			| 	  |	  |   |	|  	|  	 |  	

Para resolver solo hacer 
- hacer el proceso inverso

- reseta usada
https://gchq.github.io/CyberChef/#recipe=To_Morse_Code('-/.','Space','Line%20feed')To_Hex('None',0)Find_/_Replace(%7B'option':'Simple%20string','string':'20'%7D,'7c',true,false,true,false)Find_/_Replace(%7B'option':'Simple%20string','string':'2e'%7D,'20',true,false,true,false)Find_/_Replace(%7B'option':'Simple%20string','string':'2d'%7D,'09',true,false,true,false)From_Hex('None')&input=ZmxhZ01YaGlkZGVubWVzc2FnZXdpdGhvbGRzdHVmZg

- receta en reversa
https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Extended%20(%5C%5Cn,%20%5C%5Ct,%20%5C%5Cx...)','string':'%5C%5Cx20'%7D,'.',true,false,true,false)Find_/_Replace(%7B'option':'Extended%20(%5C%5Cn,%20%5C%5Ct,%20%5C%5Cx...)','string':'%5C%5Cx09'%7D,'-',true,false,true,false)Find_/_Replace(%7B'option':'Extended%20(%5C%5Cn,%20%5C%5Ct,%20%5C%5Cx...)','string':'%5C%5Cx7c'%7D,'%20',true,false,true,false)From_Morse_Code('Space','Line%20feed')&input=ICAJIHwgCSAgfCAJfAkJIHwJCXwJICAJfCAgICB8ICB8CSAgfAkgIHwgfAkgfAkJfCB8ICAgfCAgIHwgCXwJCSB8IHwgCQl8ICB8CXwgICAgfAkJCXwgCSAgfAkgIHwgICB8CXwgIAl8ICAJIHwgIAkg 

- meter el archivo al zip sin la ruta
```
zip -jrm msg.zip msg.txt
```

Referencias

- original: https://github.com/daffainfo/ctf-writeup/tree/main/BxMCTF%202023/Where%20Snakes%20Die
- https://string-functions.com/string-hex.aspx
- 