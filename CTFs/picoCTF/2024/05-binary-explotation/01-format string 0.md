
Can you use your knowledge of format strings to make the customers happy?Download the binary [here](https://artifacts.picoctf.net/c_mimas/77/format-string-0).Download the source [here](https://artifacts.picoctf.net/c_mimas/77/format-string-0.c).

Additional details will be available after launching your challenge instance.

### Hints

- This is an introduction of format string vulnerabilities. Look up "format specifiers" if you have never seen them before.
- Just try out the different options

## Solve

- solo introducir una cadena lo suficientemente larga


```
nc mimas.picoctf.net 64285

Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: skdjasdfjas;ldfj;lkdfja;sdkjf;akdlsjf;alksdfj;alkdsfj;alsdkjf;alsdkjf;alksdjf;alkjsdf;akjsdf;laksdjf;laskdjf
There is no such burger yet!

picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}


picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}
```