# Mind your Ps and Qs

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/3cfeb09681369c26e3f19d886bc1e5d9/values)


## solucion
- verificar la instalacion de librerias para RSA

```bash
python3 -m pip install gmpy2
python3 -m pip install pycryptodome
```

- formulas

n = p * q
c = m ^ e (mod n)

tn = (p-1)(q-1)
d = inv_mod[e,tn]
m = c ^ d (mod n)

- Tenemos

```bash 
┌──(kali㉿kali)-[~/picoctf/crypto/mind]
└─$ cat values 
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537  
```

### way 0
- facttorizamos n 
http://factordb.com 


```python
from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import inverse
>>> 
>>> p = 1617549722683965197900599011412144490161
>>> q = 475693130177488446807040098678772442581573
>>> n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
>>> p * q == n
True
>>> c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
>>> e = 65537
>>> 
>>> tn = (p-1)*(q-1)
>>> d = inverse(e, tn)
>>> m = pow(c, d, n)
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_45369387}'


>>> bytes.fromhex(hex(m)[2:])
b'picoCTF{sma11_N_n0_g0od_05012767}'
```




### way 2

- instalamos rsactftool

```bash
┌──(kali㉿kali)-[/opt]
└─$ sudo git clone https://github.com/Ganapati/RsaCtfTool.git
Cloning into 'RsaCtfTool'...
remote: Enumerating objects: 3254, done.
remote: Counting objects: 100% (592/592), done.
remote: Compressing objects: 100% (304/304), done.
remote: Total 3254 (delta 376), reused 353 (delta 284), pack-reused 2662
Receiving objects: 100% (3254/3254), 17.60 MiB | 3.19 MiB/s, done.
Resolving deltas: 100% (2187/2187), done.

┌──(kali㉿kali)-[/opt/RsaCtfTool]
└─$ python3 -m pip install -r requirements.txt


┌──(kali㉿kali)-[/opt/RsaCtfTool]
└─$ sudo ln -s /opt/RsaCtfTool/RsaCtfTool.py /usr/bin/rsactftool


```

```bash
┌──(kali㉿kali)-[~/picoctf/crypto/mind]
└─$ rsactftool -n 769457290801263793712740792519696786147248001937382943813345728685422050738403253 -e 65537 --uncipher 8533139361076999596208540806559574687666062896040360148742851107661304651861689 
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmpdn2dkdxo.
[*] Performing mersenne_primes attack on /tmp/tmpdn2dkdxo.
 24%|██████████████                                              | 12/51 [00:00<00:00, 234100.69it/s]
[*] Performing smallq attack on /tmp/tmpdn2dkdxo.
[*] Performing system_primes_gcd attack on /tmp/tmpdn2dkdxo.
100%|███████████████████████████████████████████████████████| 7007/7007 [00:00<00:00, 1018770.39it/s]
[*] Performing factordb attack on /tmp/tmpdn2dkdxo.
[*] Attack success with factordb method !

Results for /tmp/tmpdn2dkdxo:

Unciphered data :
HEX : 0x7069636f4354467b736d6131315f4e5f6e305f67306f645f34353336393338377d
INT (big endian) : 13016382529449106065927291425342535437996222135352905256639629442503647501498237
INT (little endian) : 14498987658303720244605374829370395583378376448083098194788817536789828969130352
utf-8 : picoCTF{sma11_N_n0_g0od_45369387}
STR : b'picoCTF{sma11_N_n0_g0od_45369387}'
HEX : 0x007069636f4354467b736d6131315f4e5f6e305f67306f645f34353336393338377d
INT (big endian) : 13016382529449106065927291425342535437996222135352905256639629442503647501498237
INT (little endian) : 3711740840525752382618975956318821269344864370709273137865937289418196216097370112
utf-8 : picoCTF{sma11_N_n0_g0od_45369387}
utf-16 : 瀀捩䍯䙔獻慭ㄱ也湟弰で摯㑟㌵㤶㠳紷
STR : b'\x00picoCTF{sma11_N_n0_g0od_45369387}'

```

## Ligas
- factordb : http://factordb.com 
- RsaCtfTool: https://github.com/RsaCtfTool/RsaCtfTool