# Play Nice

Not all ancient ciphers were so bad... The flag is not in standard format. `nc mercury.picoctf.net 33686` [playfair.py](https://mercury.picoctf.net/static/aec5fd7b1ec96307c4eda752a3353f68/playfair.py)


# Solucion
- Explicacion teorica

https://es.wikipedia.org/wiki/Cifrado_de_Playfair

- nos pide plain
```bash
┌──(kali㉿kali)-[~/picoctf/crypto/playnice]
└─$ nc mercury.picoctf.net 33686
Here is the alphabet: v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp
Here is the encrypted message: 4celvfdkoq5a0dx7pr40ifzctd8488
What is the plaintext message
```

- nos dan un código, lo copiamos para ir tratando de decifrarlo

```bash
[['v', '6', '0', 'u', 'f', 'm'], 
['k', '7', 'e', 'd', 'g', '4'], 
['z', '1', '3', 'h', '2', 'o'], 
['y', 'q', 'a', '9', 'i', 'b'], 
['5', '8', 'n', 't', 'w', 'x'], 
['l', 'r', 's', 'c', 'j', 'p']]

```

- reverciamos encrypt_string como decrypt_string

```pyhon
def decrypt_string(s, matrix):
        result = ""
        for i in range(0, len(s), 2):
                result += decrypt_pair(s[i:i + 2], matrix)
        return result

```

- reversiamos encryt_pair a decrytp_pair
- restamos 1 en lugar de sumar 1
```python
def decrypt_pair(pair, matrix):
        p1 = get_index(pair[0], matrix)
        p2 = get_index(pair[1], matrix)

        if p1[0] == p2[0]:
                return matrix[p1[0]][(p1[1] -1 )  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUAR>
        elif p1[1] == p2[1]:
                return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE]>
        else:
                return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]
```

- modificamos la cabecera

```python
alfabeto =  'v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp'
m = generate_square(alfabeto)

print(m)

msg = sys.argv[1]
print( decrypt_string(msg, m) )

```

- ejecutamos ya todo modificado para sacar el texto plano

```bash
┌──(kali㉿kali)-[~/picoctf/crypto/playnice]
└─$ python3 exp.py 4celvfdkoq5a0dx7pr40ifzctd8488
dpksmue41bnyue84jlem2jhl9ux755


```


- obtenemos la bandera

```bash
┌──(kali㉿kali)-[~/picoctf/crypto/playnice]
└─$ nc mercury.picoctf.net 33686
Here is the alphabet: v60ufmk7edg4z13h2oyqa9ib58ntwxlrscjp
Here is the encrypted message: 4celvfdkoq5a0dx7pr40ifzctd8488
What is the plaintext message? dpksmue41bnyue84jlem2jhl9ux755
Congratulations! Here's the flag: 3a64de31e7b5acb6c87ae45050e187ee

```

## Referencias

https://ctftime.org/writeup/28931

https://www.dcode.fr/playfair-cipher

- https://github.com/HHousen/PicoCTF-2021/blob/master/Cryptography/Play%20Nice/README.md

- playfair cipher : https://en.wikipedia.org/wiki/Playfair_cipher