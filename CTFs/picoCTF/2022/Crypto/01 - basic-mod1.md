	# basic-mod1

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message [here](https://artifacts.picoctf.net/c/397/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

# Solucion

```python
data = open('message.txt','r').read().strip().split(' ')

print(data)
flag = ''
for c in data:
        char = int(c) % 37
        print(f'{c:<5} - {char:<5} - ',end='')
        if char>=0 and char<=25:
                s = chr(char+65)
        elif char>=26 and char<=35:
                s= chr(char+22)
        elif char==36:
                s = '_'
        flag += s
        print(s)
print(f'\n{flag}')


```

```bash
R0UND_N_R0UND_8C863EE7
```

picoCTF{R0UND_N_R0UND_8C863EE7}


```python

mensaje = open('message.txt').read().strip().split(' ')
#print(mensaje)

numeros = [ int(n)%37 for n in mensaje ]
print(numeros)
flag = ''

for n in numeros:
   if n>=0 and n<=25:
      s = chr(n+65)
   elif n>=26 and n<=35:
      s = chr(n+22)
   else: 
      s = '_'
   flag += s
 
print(f"picoCTF{{{flag}}}"
	  
)

```