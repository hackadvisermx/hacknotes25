
Hey there, welcome. This is a warmup, enjoy. You intercepted a communication upon entering the virtual world. A file has been downloaded; you might find an answer in it.

### Support of Challenges

Use this information to achieve the resolution of the challenge

[

Download

](https://cdn.cattheflag.org/Warmup)


## Solve

```

```

```
 /tmp/pycdc/pycdc Warmup.pyc
# Source Generated with Decompyle++
# File: Warmup.pyc (Python 3.10)


def encrypt(input):
    output = ''
    for i in range(len(input)):
        output += chr(ord(input[i]) + 2)
    return output

input = input('Enter a string to encrypt: ')
if encrypt(input) == 'j6emavj5arn5vj2t6a2ha5pet{rv32p':
    print(f'''CAT{{{input}}}''')
    return None
None('NO invalid flag !')
```




## REferencuas

- https://stackoverflow.com/questions/71278961/how-can-i-decompile-pyc-files-from-python-3-10
- https://github.com/zrax/pycdc
- 