To avoid leak the flag, i hashed it , can you uncover it and win the game ? Keep it small and simple, take a closer look.

##  hashed world

## Creamos un archivo zip con password con la bandera: common_pass_rules.zip 

- tenemos la bandera
```
castr@mymac reto6 % cat flag.txt
flagmx{hashes_r_hard_to_crack}
```

- la comprimimos
```
 zip -er common_pass_rules.zip flag.txt
Enter password:
Verify password: 01234567891234
  adding: flag.txt (stored 0%)
```

## Crackeamos el archivo creado para probar

- creamos el hash de john
```
zip2john common_pass_rules.zip > cp                         
ver 1.0 efh 5455 efh 7875 common_pass_rules.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=43, decmplen=31, crc=B68D4530 ts=AE5B cs=ae5b type=0
```

- usamos diccionario rockyou
```
john cp -w=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
01234567891234   (common_pass_rules.zip/flag.txt)     
1g 0:00:00:00 DONE (2024-06-19 09:27) 1.694g/s 24159Kp/s 24159Kc/s 24159KC/s 02123475679..01/18/05nk
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```


## Creamos un archivo con hashes: made_unlike.txt

aqui: https://www.browserling.com/tools/all-hashes
los 2 ultimos en cmd

```
┌──(kali㉿kali)-[~/shared/us-iv-cybergames/crypto]
└─$ echo -n "vivamexico" | sha256sum 
bac3892c9d315805228e664b5bca24bedbdb645273e787b8a940cec5adac95f5  -
                                                                                                                                          
┌──(kali㉿kali)-[~/shared/us-iv-cybergames/crypto]
└─$ echo -n "vivamexico" | sha512sum               
1ddd4b8acdc9e7be1732e41a8ff0a2a406706a311d0270b78578d0c3c19a89b44e390b0ab3f5e7bc517e6fc2728a24e9264fb062142bbb7669d21c0d30ece2c6  -
                                                   
```
- el archivo se llamara :  made_unlike.txt
```
vivamexico


e5cbca412cf5e9815806565295bc3ca2
2e09fe210082602ec73aafeb4aad59cc
9a5a7f2bf1273ae46cf8181f47a0a02f
edfa120998a7c689e2e5a37e30220a737505301ef06bc7f8bdf24c89c7cc768923
9d5e6de6e9432865dd6a5ded27682705d2a4ef1a
2db2f4ebd5241da27c2d83260481411daeb9d9a1
e58a5a8dd18696e99a1458350e81da644136eb0e86754fbfa25fb3a0
bac3892c9d315805228e664b5bca24bedbdb645273e787b8a940cec5adac95f5
1ddd4b8acdc9e7be1732e41a8ff0a2a406706a311d0270b78578d0c3c19a89b44e390b0ab3f5e7bc517e6fc2728a24e9264fb062142bbb7669d21c0d30ece2c6
```
## Creamos un .7z con el 

```
7z a make_unlike.7z common_pass_rules.zip -pvivamexico
```

## Creamos un zip con password donde esta todo: 

```
C*z!7

 zip -er small_r_good.zip m*


```
