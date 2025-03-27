# hashcrack

 A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?Access the server using `nc verbal-sleep.picoctf.net 57819`

1. Understanding hashes is very crucial. [Read more here](https://primer.picoctf.org/#_hashing).
2. Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.
3. Tried using any hash cracking tools?

## Solucion
- Los crackeamos con crackstation

```
❯ nc verbal-sleep.picoctf.net 57819
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_869e658e}
```

- Cual es la longitud de los passwords
```
echo -n 482c811da5d5b4bc6d497ffa98491e38 | wc -m 
32

echo -n b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 | wc -m
40

echo -n 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 | wc -m
64

```

- Como calcular los hash de una palabra
```
echo "picoCTF 2025" | md5sum
echo "picoCTF 2025" | sha1sum 
echo "picoCTF 2025" | sha256sum 

```

## Referencias
- https://crackstation.net/
