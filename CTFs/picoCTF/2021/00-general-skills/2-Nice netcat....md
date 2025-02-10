
# Nice netcat...

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 21135`, but it doesn't speak English...

Hints:
1. You can practice using netcat with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)
2. You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solucion 1

Desde el shell

```
nc mercury.picoctf.net 21135 > ascii
cat ascii | awk '{ printf "%c", $i }'

nc -w 1 mercury.picoctf.net 21135  | awk '{ printf "%c", $i }'
picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}



```

## Solucion 2

Desde cyberchef

