# Bandit Level 11 → Level 12

bandit11
6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM


## Solucion
```bash
bandit11@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 Sep  1 06:30 .
drwxr-xr-x 49 root     root     4096 Sep  1 06:30 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit12 bandit11   49 Sep  1 06:30 data.txt
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$ 

```

- act con new
```
bandit11@bandit:~$ python
Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import codecs
>>> codecs.decode('Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh','rot13')
u'The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'
>>> 
bandit11@bandit:~$ exit
logout
```

## Notas

tr          transforma una entrada (modificandola de algina forma) y genera una salida

python
codecs          es una libreria que incluye difrentes metodos de codificacion usadados comunmente
codecs.decode   metodo que se invoca para llevar a cabo la decodificacion


Referencias
https://rot13.com/