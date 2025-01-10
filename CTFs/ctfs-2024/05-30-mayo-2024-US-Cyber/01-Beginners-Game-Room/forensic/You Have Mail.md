

# You Have Mail [Forensics]

### 150

This challenge is composed of an email, more specifically a .eml file. The email introduces the theme for the forensics group, which is a whistleblower announcing that alien life exists on Earth, and the government knows about it.

 [URGENT_Proof_of_UFO_Read_in_a_secure_location.eml](https://ctfd.uscybergames.com/files/3679aeb619d8182d54e43d4d46b0b4fc/URGENT_Proof_of_UFO_Read_in_a_secure_location.eml?token=eyJ1c2VyX2lkIjoxNzE0LCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoyMzN9.ZlvkDQ.ZxsRV-eWI-UKCN21csbqWh8amu4)

## Solve
- El mensaje descargado trae un zip en base 64 y el password esta en numeros hen ex

```
UEsDBAoACQAAADewp1gfngtKRAAAADgAAAAMABwAZXZpZGVuY2UudHh0VVQJAAMZ6zpm6Oo6ZnV4
CwABBOgDAAAEAAAAADeIlKHufvfLJvJ/Ed32cRwF755eiG+bw1NAIL3UPKn+4WIMkSPXJInVFxLM
CrGuacbTdG6AcqrqzDiXWVhqKv6WuHlKUEsHCB+eC0pEAAAAOAAAAFBLAQIeAwoACQAAADewp1gf
ngtKRAAAADgAAAAMABgAAAAAAAEAAACkgQAAAABldmlkZW5jZS50eHRVVAUAAxnrOmZ1eAsAAQTo
AwAABAAAAABQSwUGAAAAAAEAAQBSAAAAmgAAAAAA
```

```
Please see the attachment for my first piece of evidence. I am not
very good at understanding encryption details, but I did password
protect the file. The password is 53 65 63 75 72 65 5f 43 6f 64 65 3a
4f 72 64 65 72 5f 36 36.
```

```
Secure_Code:Order_66

 7z x download.zip
```


```
 cat evidence.txt
You found the evidence!

 SIVBGR{th3_ev1d3nc3_1s_h3r3}
```