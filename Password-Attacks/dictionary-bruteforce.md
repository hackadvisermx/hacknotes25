# Dictionary and Brute-Force

## Dictionary attack

A dictionary attack is a technique used to guess passwords by using well-known words or phrases. The dictionary attack relies entirely on pre-gathered wordlists that were previously generated or found. It is important to choose or create the best candidate wordlist for your target in order to succeed in this attack. Let's explore performing a dictionary attack using what you've learned in the previous tasks about generating wordlists. We will showcase an offline dictionary attack using `hashcat`, which is a popular tool to crack hashes.  

Let's say that we obtain the following hash `f806fc5a2a0d5ba2471600758452799c`, and want to perform a dictionary attack to crack it. First, we need to know the following at a minimum:  

1- What type of hash is this?  
2- What wordlist will we be using? Or what type of attack mode could we use?

To identify the type of hash, we could a tool such as `hashid` or `hash-identifier`. For this example, `hash-identifier` believed the possible hashing method is MD5. Please note the time to crack a hash will depend on the hardware you're using (CPU and/or GPU).

`hashcat -a 0 -m 0 f806fc5a2a0d5ba2471600758452799c /usr/share/wordlists/rockyou.txt`

`-a 0 ` sets the attack mode to a dictionary attack
`-m 0 ` sets the hash mode for cracking MD5 hashes; for other types, run hashcat -h for a list of supported hashes.
`f806fc5a2a0d5ba2471600758452799c` this option could be a single hash like our example or a file that contains a hash or multiple hashes.
`/usr/share/wordlists/rockyou.txt` the wordlist/dictionary file for our attack

We run hashcat with `--show `option to show the cracked value if the hash has been cracked:

`hashcat -a 0 -m 0 F806FC5A2A0D5BA2471600758452799C /usr/share/wordlists/rockyou.txt --show`

### Brute-Force attack

Brute-forcing is a common attack used by the attacker to gain unauthorized access to a personal account. This method is used to guess the victim's password by sending standard password combinations. The main difference between a dictionary and a brute-force attack is that a dictionary attack uses a wordlist that contains all possible passwords.

In contrast, a brute-force attack aims to try all combinations of a character or characters. For example, let's assume that we have a bank account to which we need unauthorized access. We know that the PIN contains 4 digits as a password. We can perform a brute-force attack that starts from 0000 to 9999 to guess the valid PIN based on this knowledge. In other cases, a sequence of numbers or letters can be added to existing words in a list, such as admin0, admin1, .. admin9999.

For instance, `hashcat` has charset options that could be used to generate your own combinations. The charsets can be found in hashcat help options.

```     
user@machine$ hashcat --help
 ? | Charset
 ===+=========
  l | abcdefghijklmnopqrstuvwxyz
  u | ABCDEFGHIJKLMNOPQRSTUVWXYZ
  d | 0123456789
  h | 0123456789abcdef
  H | 0123456789ABCDEF
  s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  a | ?l?u?d?s
  b | 0x00 - 0xff   
```

The following example shows how we can use hashcat with the brute-force attack mode with a combination of our choice.
```shell-session
user@machine$ hashcat -a 3 ?d?d?d?d --stdout
1234
0234
2234
```

`-a 3 ` sets the attacking mode as a brute-force attack
`?d?d?d?d` the ?d tells hashcat to use a digit. In our case, ?d?d?d?d for four digits starting with 0000 and ending at 9999
`--stdout `print the result to the terminal

Now let's apply the same concept to crack the following MD5 hash: `05A5CF06982BA7892ED2A6D38FE832D6` a four-digit PIN number.

```shell-session
hashcat -a 3 -m 0 05A5CF06982BA7892ED2A6D38FE832D6 ?d?d?d?d
```

