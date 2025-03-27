Run the Python script `code.py` in the same directory as `codebook.txt`.

- [Download code.py](https://artifacts.picoctf.net/c/3/code.py)
- [Download codebook.txt](https://artifacts.picoctf.net/c/3/codebook.txt)

Hint:
1. On the webshell, use `ls` to see if both files are in the directory you are in
2. The `str_xor` function does not need to be reverse engineered for this challenge.

## Solucion

- El programa lee el archivo y desencripata la banera
- Solo hay que correrlo de manera normal
```
castr-picoctf@webshell:~/coodebook$ python code.py 
picoCTF{c0d3b00k_455157_197a982c}
```