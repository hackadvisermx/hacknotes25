


- La funcion win no es accesible, nos muestra una ayuda

```
──(kali㉿kali)-[~/picoctf/reversing/picker3]
└─$ nc saturn.picoctf.net 53282
==> win
Did not understand "win" Have you tried "help"?
==> help

This program fixes vulnerabilities in its predecessor by limiting what
functions can be called to a table of predefined functions. This still puts
the user in charge, but prevents them from calling undesirable subroutines.

* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 




```

- intentamos imprimir variables, cada funcion se puede imprimir su nombre
```
==> 2
Please enter variable name to read: func_table
print_table                     read_variable                   write_variable                  getRandomNumber                 
==> 

==> 2
Please enter variable name to read: func_table[0]
Illegal variable name
==> 

==> 2
Please enter variable name to read: check_table
<function check_table at 0x796b8c359550>
==> 2
Please enter variable name to read: win
<function win at 0x796b8c359dc0>

```

- cambiamos el nombre de las variables
```
Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 3
Please enter variable name to write: getRandomNumber
Please enter new value of variable: win
==> 2
Please enter variable name to read: win
<function win at 0x796b8c359dc0>
==> 4
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d 
==>                
```

- sacamos la flag
```
┌──(kali㉿kali)-[~/picoctf/reversing/picker3]
└─$ python3
Python 3.12.6 (main, Sep  7 2024, 14:20:15) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> cars = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d".split()
>>> cars
['0x70', '0x69', '0x63', '0x6f', '0x43', '0x54', '0x46', '0x7b', '0x37', '0x68', '0x31', '0x35', '0x5f', '0x31', '0x35', '0x5f', '0x77', '0x68', '0x34', '0x37', '0x5f', '0x77', '0x33', '0x5f', '0x67', '0x33', '0x37', '0x5f', '0x77', '0x31', '0x37', '0x68', '0x5f', '0x75', '0x35', '0x33', '0x72', '0x35', '0x5f', '0x31', '0x6e', '0x5f', '0x63', '0x68', '0x34', '0x72', '0x67', '0x33', '0x5f', '0x32', '0x32', '0x36', '0x64', '0x64', '0x32', '0x38', '0x35', '0x7d']
>>> [ chr(int(x,16)) for x in cars ].join()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'join'
>>> [ chr(int(x,16)) for x in cars ]
['p', 'i', 'c', 'o', 'C', 'T', 'F', '{', '7', 'h', '1', '5', '_', '1', '5', '_', 'w', 'h', '4', '7', '_', 'w', '3', '_', 'g', '3', '7', '_', 'w', '1', '7', 'h', '_', 'u', '5', '3', 'r', '5', '_', '1', 'n', '_', 'c', 'h', '4', 'r', 'g', '3', '_', '2', '2', '6', 'd', 'd', '2', '8', '5', '}']
>>> 

>>> ''.join( [ chr(int(x,16)) for x in cars ] )
'picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_226dd285}'
>>> 


```