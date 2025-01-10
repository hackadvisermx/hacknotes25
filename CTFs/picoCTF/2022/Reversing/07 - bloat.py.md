# bloat.py

 Can you get the flag? Run this [Python program](https://artifacts.picoctf.net/c/432/bloat.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/432/flag.txt.enc).

# solucion

```python

print(a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])
```

 ```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/bloat]
└─$ python3 bloat.flag.py
happychance
                                                                                                                                                                                                         
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/bloat]
└─$ python3 bloat.flag.py
Please enter correct password for flag: happychance
picoCTF{d30bfu5c4710n_f7w_c47f9e9c}

 ```