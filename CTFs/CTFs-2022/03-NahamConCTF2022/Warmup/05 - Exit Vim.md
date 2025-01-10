# Exit Vim
Author: @JohnHammond#6971  
  
Ah yes, a bad joke as old as time... can you exit `vim`?  
  
PS (not challenge related), _thank you_ so much to **[Paranoids](https://theparanoids.com)** for supporting NahamCon 2022!

## Solucion
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/nahamconctf/warmup/quirky]
└─$ ssh -p 31072 user@challenge.nahamcon.com
The authenticity of host '[challenge.nahamcon.com]:31072 ([34.123.79.100]:31072)' can't be established.
ED25519 key fingerprint is SHA256:FgKWMWi6vCPV2fv3tNKdEzyQKnmFXS4oXncEgDjRLhc.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[challenge.nahamcon.com]:31072' (ED25519) to the list of known hosts.
user@challenge.nahamcon.com's password: 

flag{ccf443b43322be5659150eac8bb2a18c}
Connection to challenge.nahamcon.com closed.
```
