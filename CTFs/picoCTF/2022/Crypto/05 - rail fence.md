# rail fence

A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? Download the message [here](https://artifacts.picoctf.net/c/276/message.txt). Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.

# solucion

The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_55228140
```bash

─(kali㉿kali)-[~/hacking/ctfs2022/picoctf2022/railfence]
└─$ echo 'WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_55228140' | tr [A-Z] [a-z]
wh3r3_d035_7h3_f3nc3_8361n_4nd_3nd_55228140

```
 
## referencias

- [rail fence]((https://cryptii.com/pipes/rail-fence-cipher)