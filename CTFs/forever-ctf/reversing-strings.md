
I think the flag is hardcoded in the binary. If only there was a way to look at the text data in a binary file.

## solucion

```
strings strings reversing-strings -n 15 | grep utf
utflag{plaintext_str1ngs_aRe_b3St_Str1ngs
```