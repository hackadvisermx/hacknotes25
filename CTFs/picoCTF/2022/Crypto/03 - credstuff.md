# credstuff

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak [here](https://artifacts.picoctf.net/c/534/leak.tar). The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on

## Solucion

```bash
                                                                                                                     
┌──(kali㉿kali)-[~/…/picoctf2022/crypto/credstuff/leak]
└─$ cat usernames.txt | grep -n cultiris
378:cultiris
                                                                                                                     
┌──(kali㉿kali)-[~/…/picoctf2022/crypto/credstuff/leak]
└─$ sed -n '378,378p' passwords.txt     
cvpbPGS{P7e1S_54I35_71Z3}
                                                                                                                     
┌──(kali㉿kali)-[~/…/picoctf2022/crypto/credstuff/leak]
└─$ sed -n '378,378p' passwords.txt | tr [A-Za-z] [N-ZA-Mn-za-m]
picoCTF{C7r1F_54V35_71M3}


```