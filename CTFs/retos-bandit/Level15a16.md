## Bandit Level 15 → Level 16
## Objetivo
The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL encryption.

**Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…**

## Datos de acceso

bandit15
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

## Solucion

 
```
bandit15@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root     4096 Sep  1 06:30 ..
-rw-r-----  1 bandit15 bandit15   33 Sep  1 06:30 .bandit14.password
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Sep  1 06:31:12 2022 GMT
verify return:1
depth=0 CN = localhost
notAfter=Sep  1 06:31:12 2022 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Sep  1 06:30:12 2022 GMT; NotAfter: Sep  1 06:31:12 2022 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEHn8h8jANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjIwOTAxMDYzMDEyWhcNMjIwOTAxMDYzMTEyWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDK
u/UD6yArwj259J4o2IVQQGvM/oGVIiYYppFd1jxltmQ03SOUVg+4px+7qOJuCbxA
AH9NCAl55r7v/VDlwGkpu4c2GaqR3zSAlidrtJjrVFZP/QilXdv0uV35N4i30BuT
DdI+FzlYcQx7ztZdtDxp61FTjET4BIcFmSzMQLitpYeeiVcKLXTPnsF8216drWjQ
0Ucb+3RvGgPo/rKPra8/7WYFa8ALdnu2rwP07ndtMDL3iJF9VMuBsr8UuTdsktwa
174QGx0f3RFkcKJ1foxYnSoHvy0BhxVGguMKuinY6cyLELwnjcAp4A2oGI438GnV
whe39ZlCkGved612QLhDAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQDE
2X2mgxYDvujnIAL2Qbs8JnUBFe3lZsRZJbPgko3MZ4lScB5Rbz+vb6q6s0KGGMjh
sKweg4BtG4sQWDIwX2yd4XwJa8rrGWuoA4kgCQ/jJhFZrbCPbDN3sbzX8Tql+epd
oJyQcvLOkWDazRPgx0i4dMXIgUv0kbE+NCvj2waXHldMyjT6GFL2bdv/Xd8ffnXg
wlggJKKIzl0RMp/5z5n1bPMoLVl5HcUG3UzOsTcqcSThTr3JXeWLjaL0qJfAfcw5
V+GM2tGTQB3c4jvISAl5RAARpvFUMc4d4hKd6aesRcFHZfbtSjxglPFmeL1VGxJ9
EIg5c/xwHOE6dgDA2WdS
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 5F32B5DB906F5A2B5367675C4B0D47DD37BCD51B95A4F904BDD0B2D503EC880C
    Session-ID-ctx: 
    Resumption PSK: 2558E6A88828EF48ED9C87693D7381B2617044878B4829B1B0E20146A81B33740AAFD96944A069FA42CDDDDB8290646D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 09 86 a0 aa 25 48 38 1d-0e b1 8d f8 fa 82 ac 33   ....%H8........3
    0010 - c8 0c 4b 4f f3 e8 8b 08-43 f4 54 c5 66 e1 e7 c8   ..KO....C.T.f...
    0020 - 32 3e fa 82 c3 1d 78 7b-41 74 c2 06 56 bc 15 49   2>....x{At..V..I
    0030 - d0 3e 27 e8 6b 12 fd dd-20 78 cf 7f 9f 5c ca 48   .>'.k... x...\.H
    0040 - 57 23 f0 c6 e1 86 8b 37-b2 0b a4 d7 c4 c0 39 1c   W#.....7......9.
    0050 - 9f 57 5b 28 20 51 2f 50-d0 2e ab 57 96 9a c6 60   .W[( Q/P...W...`
    0060 - ce bd 98 f4 6a 9f c5 f2-40 bd d6 ea 14 84 a0 77   ....j...@......w
    0070 - c1 b7 01 df 1a b8 47 e2-bb ac 37 71 8b f1 f5 44   ......G...7q...D
    0080 - ee fe 2c 77 c4 0f 1b 07-f5 88 94 19 90 85 78 0b   ..,w..........x.
    0090 - 16 1e fd 4a c4 9d 42 f0-9a 0e 63 ca 75 00 13 7f   ...J..B...c.u...
    00a0 - cd 5a 42 47 90 6a 51 56-c8 d8 12 4b 86 22 6f d9   .ZBG.jQV...K."o.
    00b0 - 77 76 47 88 56 0b 81 bd-08 4b e4 91 2f 23 3b 8d   wvG.V....K../#;.
    00c0 - d8 ba 71 76 f6 4f 7c ce-bd 05 75 f6 2c 43 60 df   ..qv.O|...u.,C`.

    Start Time: 1662244709
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: CC8E325A2904141F7357EE429F1D4C1FC7148E9CB65001FB2F77939DF5E97663
    Session-ID-ctx: 
    Resumption PSK: F848D0D8E072F15843E4B502B0230420B562E2456E8004FD5039216DAE9458297022EB580E83D3A2D9DC7CF20A9758DE
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 09 86 a0 aa 25 48 38 1d-0e b1 8d f8 fa 82 ac 33   ....%H8........3
    0010 - 6e f7 57 e7 ab 4c e5 5d-43 b7 3f 30 35 9d d0 e2   n.W..L.]C.?05...
    0020 - 06 92 e7 18 c9 e5 6d 49-b9 64 95 6f 4b 52 2b 7f   ......mI.d.oKR+.
    0030 - a5 67 ed f1 ee a9 2d f9-92 21 5b 8f 80 18 b5 d6   .g....-..![.....
    0040 - c9 84 fe 3e 51 2b 20 c7-fe fa 82 ce 8b 1c 8d 03   ...>Q+ .........
    0050 - 25 10 8c b1 fa 9f 56 71-3d 80 fa be 09 ea 82 cb   %.....Vq=.......
    0060 - 88 e8 43 42 2a 25 d0 ba-54 9f 47 a8 a0 51 eb 73   ..CB*%..T.G..Q.s
    0070 - a4 b7 5e 94 34 48 c8 10-83 46 69 91 69 2c 24 49   ..^.4H...Fi.i,$I
    0080 - d7 2d 4e a9 df cf 4d 86-b1 82 54 50 7d 53 58 c3   .-N...M...TP}SX.
    0090 - 09 df fc ca e5 b0 26 cd-0c 1f fa 15 29 0e f2 e0   ......&.....)...
    00a0 - a5 55 f5 4c 8d 9e f1 02-9c 6f 17 17 56 ef 1c 03   .U.L.....o..V...
    00b0 - f3 5c aa b4 b9 a4 7a ad-5f d0 04 98 14 f6 47 4e   .\....z._.....GN
    00c0 - 07 9d b9 0d c3 5f 9a 5d-8b 39 41 b7 74 89 b7 3b   ....._.].9A.t..;

    Start Time: 1662244709
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt         
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
bandit15@bandit:~$
```

## Notas

SSL     Es un conjuto de protocolos que permiten realizar conexiones en red de manera segura

openssl Es una utileria que permite implementar SSL en nuestro servidor (librerias)

s_client    Es un cliente SSL/TLS 
-connect    Permite especificar el servidor y el puerto al que me voy conectar

## Referencias 
- https://en.wikipedia.org/wiki/Secure_Socket_Layer
- https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html
















