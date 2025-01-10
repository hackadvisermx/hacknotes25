
# Name

## Objetivo
I want to join this secret club, but they have the weirdest passwords! I've managed to intercept the program they use to authenticate the passwords, but I don't know how to figure it out. Can you figure out the password for me?

## Solucion

```python
def roll(text):
	return text[::-1]

def swoop(text):
	text = list(text)
	for i in range(len(text)):
		text[i] = chr(ord(text[i]) + (i % 5))
	return ''.join(text)


def tswoop(text):
	text = list(text)
	for i in range(len(text)):
		text[i] = chr(ord(text[i]) - (i % 5))
	return ''.join(text)

print(roll(tswoop('}12u7#dvl{$`fos_4jwchb}jelg')))

#password = input("Enter the password: ")
#if swoop(roll(password)) == "}12u7#dvl{$`fos_4jwchb}jelg":
#	print("Welcome in!")
#else:
#s	print("Sorry, wrong password.")```
```
## Flag
python3 d17d3daad85fb5fd1fb849c5e4d63d9e.py
flag{ah_th3_old_$witc#3r00}
## Referencias