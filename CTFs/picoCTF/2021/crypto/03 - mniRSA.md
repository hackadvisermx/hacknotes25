# Mini RSA

What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: [ciphertext](https://mercury.picoctf.net/static/e7e63a387acc347648918f419d1ae438/ciphertext)


## Solucion

¿Qué pasa si tienes un exponente pequeño? Sin embargo, hay un giro, rellenamos el texto sin formato para que (M ** e) sea apenas más grande que N. Vamos a descifrar esto


c = m ^ e ( mod n )

Caso 1 (ataque de raiz cubica)

c = m ^ e
c = m ^ 3
m = 3 raiz c

Sin embargo no lo podemos usar

Caso 2 

m ^ e >= n
c = m ^ e - xn
m = raiz e (c + xn)

El algortimo agrega n a x hasta que se sea un cubo valido. En este punto , estarems en condicones de obtener el mensaje en texto plano, 

``` python
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

n=161576568432146305407822605195988788423367831773489290174076332113521363679607546240195027460240509>
e=3
co=12200123185888718861325247578988844221745345580555937133090883049102739910735547326599771339806853>

c = co
while True:
        m = iroot(c, 3)[0]
        if pow(m, 3, n) == co :
                print('Pwned')
                print(long_to_bytes(m))
        c += n

```

```bash
Pwned
b'                                                                                                        picoCTF{e_sh0u1d_b3_lArg3r_85d643d5}'

```

# Referencias

