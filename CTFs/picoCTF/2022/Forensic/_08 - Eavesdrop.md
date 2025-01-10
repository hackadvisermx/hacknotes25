# Eavesdrop

Download this packet capture and find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/362/capture.flag.pcap)

hint> All we know is that this packet capture includes a chat conversation and a file transfer.

# Solucion

- tcp stream

```bash

Salted__....,.._5*...1W
cl..g.&H.bZ.H.T.........

```

```bash
  

Hey, how do you decrypt this file again?

You're serious?

Yeah, I'm serious

*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123

Ok, great, thanks.

Let's use Discord next time, it's more secure.

C'mon, no one knows we use this program like this!

Whatever.

Hey.

Yeah?

Could you transfer the file to me again?

Oh great. Ok, over 9002?

Yeah, listening.

Sent it

Got it.

You're unbelievable

```

- aplicamos

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/eavesdrop]
└─$ openssl des3 -d -salt -in salted -out flag.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
140584414631296:error:0606506D:digital envelope routines:EVP_DecryptFinal_ex:wrong final block length:../crypto/evp/evp_enc.c:599:
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/eavesdrop]
└─$ cat flag.txt         
�N(�
�D�j?�                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/eavesdrop]
└─$ file flag.txt 
flag.txt: OpenPGP Secret Key


```


- importamos la llave pgp
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/eavesdrop]
└─$ gpg --import flag 
gpg: keybox '/home/kali/.gnupg/pubring.kbx' created
gpg: packet(5) with unknown version 40
gpg: Total number processed: 0


```

