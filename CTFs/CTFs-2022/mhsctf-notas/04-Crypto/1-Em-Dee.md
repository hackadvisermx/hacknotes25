### Em Dee

## Objetivo
 have a good friend named Em. She loves secret codes, so when she challenged me this time, I was well up for it! She told me that she encoded the word "happy" as "56ab24c15b72a457069c5ea42fcfc640" and "sad" as "49f0bad299687c62334182178bfd75d8" (without the quotes) and challenged me to encode "mhsctf" using her method! I can't figure it out! What would it be? Enter your answer in flag format: "flag{...}"

 ## Solucion

 ```bash
┌──(kali㉿kali)-[~/hacking/mhsctf2022]
└─$ hash-identifier 
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: 56ab24c15b72a457069c5ea42fcfc640

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))

 (kali㉿kali)-[~/hacking/mhsctf2022]
└─$ printf '%s' "mhsctf" | md5sum
fc3e3c405a66f8fe7cb7f17a838ea88c  -

echo -n mhsctf | md5sum
fc3e3c405a66f8fe7cb7f17a838ea88c  -


 ```

 ## Flag
```bash
flag{fc3e3c405a66f8fe7cb7f17a838ea88c}
```

 