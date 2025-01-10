
# Data breach poem

Una breacha de datos es tan romantica que hasta podría escribir un poema para narrar lo que hemos sufrido al perder nuestra privacidad. Tanto en Linux como en Windows, solo el final de la linea es diferente, pero la perdida es la misma.

A data breach is so romantic that I could even write a poem to narrate what we have suffered when losing our privacy. On both Linux and Windows, only the end of the line is different, but the loss is the same.

## generar el archivo

- se genera los bits de la banera
- luego se inserta un \\n cuando es 1 y un  \\n \\r  cuando es 0
- la bandera queda codificada al final de cada linea

```python

flag = b'rbd'

flag_bits = ''.join(f'{x:08b}' for x in flag)

dbpoem = """When hackers strike and networks fall
Our data's left exposed to all
They steal our secrets, our lifeblood too
And leave us reeling, not knowing what to do
But hope is not lost, there is a way
To stop the bleed and save the day
It starts with a plan, a team in place
Ready to respond with skill and grace
First we must identify, contain the threat
Cut off the source, lest it spread
Isolate the damage, secure the breach
And limit the fallout, within our reach
Next comes eradication, fixing the flaw
Closing the gap, with no pause or flaw
We must restore our systems, our digital space
And ensure our security, a safer place
Last comes recovery, returning to the norm
Testing and validating, until we're reborn
The bleed has stopped, our wounds are healed
And our defenses are stronger, our data shielded
So let us work together, with focus and care
Stopping the bleed, ensuring we're prepared
For the hackers will come, of this we know
But we'll be ready, and our data will glow.""".split('\n')

with open('dbrpoem.txt', 'wb') as f:
    for i in range(len(dbpoem)):
        f.write(dbpoem[i].encode('utf-8') + (b'\r\n' if flag_bits[i] == '1' else b'\n'))

```

-
# Solucion

- leer los saltos, convertirlos a binario e obtenemos la bandera
```python
import binascii

dbpoem = open('dbrpoem.txt','r',newline='').read()

binflag = ''.join(['1' if x[-1] == '\r' else '0' for x in dbpoem.split('\n') if len(x) > 0])
 
n = int(binflag,2)

print(binascii.unhexlify('%x' % n).decode())
```


## Referencias
	- https://www.linkedin.com/pulse/stopping-bleed-poem-cybersecurity-incident-response-matthew-smith
	- https://github.com/WolvSec/WolvCTF-2023-Challenges-Public/blob/main/forensics/elytra/solution/gen.py
