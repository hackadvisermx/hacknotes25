## All Hashed Out [Crypto]

### 150


## Solve


```
fcrackzip -b -c 'Aa1!:' -l 1-5 -u short_n_sweet.zip
PASSWORD FOUND!!!!: pw == B!p*3
```

```
unzip short_n_sweet.zip        
Archive:  short_n_sweet.zip
[short_n_sweet.zip] build_different.7z password: 
 extracting: build_different.7z      
  inflating: built_different.txt  
```

```
cat built_different.txt 
290c5768c4c300bb5d94c5e48566d940
4878e6f0309cb4c0b1653d540fde005e
6c851b965778e56409a4963807c11122
edfa12078ab7c689e2e5a37e30220a737505301ef06bc7f8bdf24c89c7cc7689
9d5e6dd6e9432865dd6a5ded27682705d2a4ef1a
55732c74c1d2dadd52c36e2f4ca6031e041ab0ce
977802f5a40c482b13508874af6f12c3ec2f096db6fc598bbc95754c
30a09df5dc99880273cfc6dbcd4b48c35e5111082260d23442740ecc21d56e19
02812275fad36de5b71f1baecd48f685d4f1d64c9f1ed200a981f870cb3a9899befdb3bb597b394dc97ab9b12566e2a7f4e5587dce267ff02f0f4050fdd6baf8

```

- crackstation

|                                                                                                                                        |         |            |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| 290c5768c4c300bb5d94c5e48566d940                                                                                                       | md2     | Matamoros  |
| 4878e6f0309cb4c0b1653d540fde005e                                                                                                       | md4     | Matamoros  |
| 6c851b965778e56409a4963807c11122                                                                                                       | md5     | Matamoros  |
| edfa12078ab7c689e2e5a37e30220a737505301ef06bc7f8bdf24c89c7cc7689                                                                       | Unknown | Not found. |
| 9d5e6dd6e9432865dd6a5ded27682705d2a4ef1a                                                                                               | Unknown | Not found. |
| 55732c74c1d2dadd52c36e2f4ca6031e041ab0ce                                                                                               | sha1    | Matamoros  |
| 977802f5a40c482b13508874af6f12c3ec2f096db6fc598bbc95754c                                                                               | sha224  | Matamoros  |
| 30a09df5dc99880273cfc6dbcd4b48c35e5111082260d23442740ecc21d56e19                                                                       | sha256  | Matamoros  |
| 02812275fad36de5b71f1baecd48f685d4f1d64c9f1ed200a981f870cb3a9899  <br>befdb3bb597b394dc97ab9b12566e2a7f4e5587dce267ff02f0f4050fdd6baf8 | sha512  | Matamoros  |
- cracker hascat
```
hashcat -m100 h2 -a3 -1?l?u?d?s ?1?1?1?1?1
```

-m100 sha1
-m1400 sha-256

- 8 a la vez no de 1 a 8
```
hashcat -m1400 h1 -a3 -1?a ?1?1?1?1?1?1?1?1 -i --increment-min=8
```

- sacamos lo que hay en .7z
```
7z x build_different.7z
Pass:Matamoros
```
- Sacamos el pass de 
```
zip2john common_passwords_rock.zip > h3
ver 1.0 efh 5455 efh 7875 common_passwords_rock.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=37, decmplen=25, crc=45549CEC ts=A645 cs=a645 type=0


john h3 -w=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
123456789123456789 (common_passwords_rock.zip/flag.txt)     
1g 0:00:00:00 DONE (2024-06-03 16:09) 50.00g/s 4915Kp/s 4915Kc/s 4915KC/s 123456..Donovan
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 


unzip common_passwords_rock.zip  
Archive:  common_passwords_rock.zip
[common_passwords_rock.zip] flag.txt password: 
password incorrect--reenter: 
 extracting: flag.txt  


cat flag.txt 
SIVBGR{P@SSW0RDZ_R_H@RD}

```




## Referencias
- https://security.stackexchange.com/questions/201931/hashcat-specify-number-of-characters
- 