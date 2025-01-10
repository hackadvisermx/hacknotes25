
## The Email Where It Happens [Forensics]

### 150

Howdy Truth Seekers! It seems that some malware that was strategically shared has begun to phone back home! We believe that this might have some very important information that could help lead us to finally getting to the bottom of this conspiracy regarding extraterrestrial life. Unfortunately the original developer of this _tool_ was recently promoted to customer status and is no longer on good terms with the orginization. This means that we don't have any information on how to decode this traffic. Unfortunately all I have is a PCAP. Can you help us out here?


- Exportar los paquetes en el .pcap

- filtrar el query dns

## Solve

```
cat dns.txt | grep DNS | awk '{print $11}' | cut -d'.' -f1
```


```
FIQSUIJKEEVCCKRBFIQSUIJKEEVAUSKOKRCVEQ2FKBKE
KRBAIVGEKQ2UKJHU4SKDEBGUCSKMEBBU6TKNKVHESQ2B
KREU6TQKFIQSUIJKEEVCCKRBFIQSUIJKEEVAUVCPHIQG
E4TJMFXC44TJM5TXGQDBOJSWCNJRFZRWY33VMQFEMUSP
JU5CA2LMNR2W22LOMF2GSQDTMVRXEZLUOMXHK4YKIRAV
IRJ2EA2S6MJUF4ZDAMRUIAYTMORTGMFFGVKCJI5CAUSF
HIQEGT2OIZEVETKFIQQEKWCUKJAVIRKSKJCVGVCSJFAU
YICMJFDEKCSCJ5CFSOQKJBSWY3DPEBBHE2LBNYWAUCSX
MUQGC4DQOJSWG2LBORSSA5DIMUQGS3TGN5ZG2YLUNFXW
4IDZN52SA2DBOZSSA4DSN53GSZDFMQQHK4ZAOJSWOYLS
MRUW4ZZAPFXXK4RAMRUXGY3POZSXE6JAMFXGIIDQOJXW
24DUEBSGK5DFNZ2GS33OEBXWMIDFPB2HEYLUMVZHEZLT
ORZGSYLMEBWGSZTFEBXW4ICFMFZHI2BOEBKGQ2LTEBUX
GIDGMFXHIYLTORUWGIDOMV3XGIDBNZSCA4DVORZSA5LT
EBUW4IDQN5ZWS5DJN5XCAZTPOIQHK4ZAORXSAYTFM5UW
4IDQNBQXGZJAOR3W6IDPMYQG65LSEBYGYYLOEBTG64RA
O5XXE3DEEBSG63LJNZQXI2LPNYXCAV3FEB2W4ZDFOJZX
IYLOMQQHS33VEBUGC5TFEBZXI33SMVSCA5DIMUQGY2LG
MVTG64TNEBUW4IDUNBSSAYLHOJSWKZBAOVYG63RANRXW
GYLUNFXW4IDBNZSCA43FOQQHI2DFEBWG6Y3LEB2G6IDV
ORUWY2L2MUQHI2DFEBYGC43TO5XXEZBAORXSAISTJFLE
ER2SPN3WQMC7NYZTGZDTL4ZTEX3CGRZTG435EIXCAV3F
EB3WS3DMEBTG63DMN53SA5LQEBQWM5DFOIQGS3TWMVZX
I2LHMF2GS3THEB2GQZJAOBZG65TJMRSWIIDMNFTGKZTP
OJWSA53JORUCAZTVOJ2GQZLSEBUW443UOJ2WG5DJN5XH
GLQKBJJWC3DVORQXI2LPNZZSYCSUOJUWC3THNRSSAQTP
NFZQUKRBFIQSUIJKEEVCCKRBFIQSUIJKBJCU4RBAKRJE
CTSTJVEVGU2JJ5HAUKRBFIQSUIJKEEVCCKRBFIQSUIJ
```

- base32
```
*!*!*!*!*!*!*!*!*
INTERCEPTED ELECTRONIC MAIL COMMUNICATION
*!*!*!*!*!*!*!*!*
TO: brian.riggs@area51.cloud
FROM: illuminati@secrets.us
DATE: 5/14/2024@16:33
SUBJ: RE: CONFIRMED EXTRATERRESTRIAL LIFE
BODY:
Hello Brian,

We appreciate the information you have provided us regarding your discovery and prompt detention of extraterrestrial life on Earth. This is fantastic news and puts us in position for us to begin phase two of our plan for world domination. We understand you have stored the lifeform in the agreed upon location and set the lock to utilize the password to "SIVBGR{wh0_n33ds_32_b4s3s}". We will follow up after investigating the provided lifeform with further instructions.

Salutations,
Triangle Bois
*!*!*!*!*!*!*!*!*
END TRANSMISSION
*!*!*!*!*!*!*!*! 
```