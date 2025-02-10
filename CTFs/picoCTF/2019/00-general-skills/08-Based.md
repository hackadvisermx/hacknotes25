
# Based

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29221`.

Hints:
1. I hear python can convert things.
2. It might help to have multiple windows open.


## Solucion

- Hay que abrir 3 ventanas en cyberchef, y resolverlo en 45 segundos
	- Binario
	- Octal
	- Hexadecimal

```
castr-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 29221
Let us see how data is stored
container
Please give the 01100011 01101111 01101110 01110100 01100001 01101001 01101110 01100101 01110010 as a word.
...
you have 45 seconds.....

Input:
container
Please give me the  163 154 165 144 147 145 as a word.
Input:
sludge
Please give me the 7461626c65 as a word.
Input:
table
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_00a975ff}

```