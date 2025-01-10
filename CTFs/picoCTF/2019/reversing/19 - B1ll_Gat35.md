#  B1ll_Gat35

Can you reverse this [Windows Binary](https://jupiter.challenges.picoctf.org/static/0ef5d0d6d552cd5e0bd60c2adbddaa94/win-exec-1.exe)?


## Solucion
- instalaar wine
```bash

sudo dpkg --add-architecture i386 
sudo apt update 
sudo apt install wine
sudo apt install wine32:i386
```
- que tenemos
```bash
wine win-exec-1.exe 
Input a number between 1 and 5 digits: 1
Initializing...
Enter the correct key to get the access codes: 22
Incorrect key. Try again
```

- Decompilams con ghidra

I found `main()` by going to `Search > Program Text` and searching for `Initializing` in "All Fields" since that was a string that appears when the program launches. Clicking the one with the "PUSH" in the preview goes right to the `main()` function.



## Referencias

https://picoctf2019.haydenhousen.com/reverse-engineering/b1ll_gat35