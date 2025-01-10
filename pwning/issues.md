
El problema es que al mandar una cadena de caracteres con las direcciones para desbordar el buffer el pyhton aveces no lo hace


https://security.stackexchange.com/questions/212036/buffer-overflow-exploit-with-python3-wrong-return-address-written

Pero se puede usar perl tambien 

```
perl -e 'print "A"x4 . "\x48\x49\x90\x84\xe3\xe9";' |xxd
```

otro recurso
https://stackoverflow.com/questions/54550845/strange-behaviour-of-python3-in-hex


```python
python3 -c "import sys;sys.stdout.buffer.write(b'A' * 44 + b'\xcb\x85\x04\x08')"
```

```python
b'A' * 44 + b'\xcb\x85\x04\x08'
```