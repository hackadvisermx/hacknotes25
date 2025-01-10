Beautiful place to visit in Peru



Do you know the beautiful places that Peru has? I'll give you some clues so you can discover them. A file has been transferred with the list of some interesting places in Peru that you should know. Find out which place we recommend you visit.

Locate a clue that will lead you to discover the chosen place

## Solucion
- Abrir con whireshark
- Exportar los archivos FPT transferidos
- El Zip tiene contrasena y viene en el otro archivo
```bash
┌──(kali㉿kali)-[~/…/metared-4-stage-peru/forensic/beatiful/ortro]
└─$ ls -la
total 404
drwxrwx--- 1 root vboxsf  16384 Nov  8 09:57 .
drwxrwx--- 1 root vboxsf  16384 Nov  8 09:57 ..
-rwxrwx--- 1 root vboxsf     54 Nov  8 09:57 informacon1.txt
-rwxrwx--- 1 root vboxsf 375907 Nov  8 09:57 turismo.zip
                                                                                                                            
┌──(kali㉿kali)-[~/…/metared-4-stage-peru/forensic/beatiful/ortro]
└─$ cat informacon1.txt 
Contraseña para descomprimir 

HQbNh:YXS$cgDegdUcV1                                                                                                                            
┌──(kali㉿kali)-[~/…/metared-4-stage-peru/forensic/beatiful/ortro]
└─$ unzip turismo.zip
Archive:  turismo.zip
[turismo.zip] Flag.jpg password: 
  inflating: Flag.jpg                
  inflating: Lista de lugares por visitar.txt  
                                                                                                                            
┌──(kali㉿kali)-[~/…/metared-4-stage-peru/forensic/beatiful/ortro]
└─$  
```