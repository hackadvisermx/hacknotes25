Analisis de trafico

Se ha detectado un incidente crítico en nuestras redes de comunicación. Un atacante desconocido logró infiltrarse en el sistema y ha comenzado a exfiltrar información confidencial relacionada con investigaciones de energía solar y radiación cósmica. La transmisión fue interrumpida, pero logramos interceptar una serie de archivos y el tráfico de red asociado. Sabemos que uno de los archivos contiene una clave crítica que podría ayudarnos a rastrear al atacante y prevenir futuros ataques, pero los demás son señuelos diseñados para confundir a nuestros analistas.

 [KreeTransmition.zip](https://scilabs.ctfd.io/files/3fa7f99232aa4cb6f42234721d0eb3ae/KreeTransmition.zip?token=eyJ1c2VyX2lkIjoxMDY5LCJ0ZWFtX2lkIjozNzQsImZpbGVfaWQiOjEzNn0.Z820RQ.dcqZq8MkVrj4iNDz3urgSoctQkY "KreeTransmition.zip")

## Solucion

- Descargamos y desempaquetamos el archivo
```
┌──(kali㉿kali)-[~/tmp/themarvels/forensic/alerta-de-sword]
└─$ ls
KreeTransmition.zip
                                                                                                                                                                                                              
┌──(kali㉿kali)-[~/tmp/themarvels/forensic/alerta-de-sword]
└─$ unzip KreeTransmition.zip            
Archive:  KreeTransmition.zip
  inflating: KreeTransmition.pcapng  
                                                                                                                                                                                                              
┌──(kali㉿kali)-[~/tmp/themarvels/forensic/alerta-de-sword]
└─$ ls -la
total 558432
drwxr-xr-x 4 kali kali       128 Mar  9 11:16 .
drwxr-xr-x 6 kali kali       192 Mar  9 10:39 ..
-rw-rw-rw- 1 kali kali 284109388 Jan 29 15:15 KreeTransmition.pcapng
-rw-r--r-- 1 kali kali 278333078 Mar  9 10:38 KreeTransmition.zip
                                                                                                                                                                                                              
┌──(kali㉿kali)-[~/tmp/themarvels/forensic/alerta-de-sword]
└─$ 


```

- Abrimos con wireshark para analizar
```
┌──(kali㉿kali)-[~/tmp/themarvels/forensic/alerta-de-sword]
└─$ wireshark KreeTransmition.pcapng &                                                                                              


```