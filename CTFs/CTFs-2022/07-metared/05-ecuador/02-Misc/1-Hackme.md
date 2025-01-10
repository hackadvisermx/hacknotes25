
# Hackme

Before being captured, our informant told us the following: "To get to base #64 you must make 30 laps in a row"

# Solucion

- Es un archivo que ha sido codificado base64 30 veces

```bash
cp hackme.txt hackme0.txt
for i in {1..30}; do base64 -d hackme$((i-1)).txt > hackme$i.txt; done
```

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-5-ecuador/misc/hackme]
└─$ cat hackme30.txt         
flag{BASE64_BEST_ENCODE}
```