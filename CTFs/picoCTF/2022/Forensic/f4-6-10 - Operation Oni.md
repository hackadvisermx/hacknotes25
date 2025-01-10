# Operation Oni

Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download disk image](https://artifacts.picoctf.net/c/374/disk.img.gz)
-   Remote machine: `ssh -i key_file -p 50406 ctf-player@saturn.picoctf.net`

# solucion
- Informacion de la imagen

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/operationoni]
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)

```

- ver los archivos
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/operationoni]
└─$ fls -o 206848 disk.img
d/d 458:	home
d/d 11:	lost+found
d/d 12:	boot
d/d 13:	etc
d/d 79:	proc
d/d 80:	dev
d/d 81:	tmp
d/d 82:	lib
d/d 85:	var
d/d 94:	usr
d/d 104:	bin
d/d 118:	sbin
d/d 464:	media
d/d 468:	mnt
d/d 469:	opt
d/d 470:	root
d/d 471:	run
d/d 473:	srv
d/d 474:	sys
V/V 33049:	$OrphanFile

```

- listamos cotenido de la carpet root y luego .ssh
```bash
┌──(kali㉿kali)-[~/picoctf/forensic/operationoni]
└─$ fls -o 206848 disk.img 470
r/r 2344:       .ash_history
d/d 3916:       .ssh

┌──(kali㉿kali)-[~/picoctf/forensic/operationoni]
└─$ fls -o 206848 disk.img 3916
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
```

- luego listamos el contenido del archivo

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/operationoni]
└─$ icat -o 206848 disk.img 2346
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGCtd7hso2E7OQItY6aTjMMyKZb1FVmeBfnVjyHcGYos root@localhost
                                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/operationoni]
└─$ icat -o 206848 disk.img 2345
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```


- Montar la particon

```bash
sudo losetup loop0 disk.img
sudo kpartx -av /dev/loop0 
sudo mount -r /dev/mapper/loop0p2 tmp

```

- encontrar la ssh key

``` bash
┌──(root㉿kali)-[/home/…/operationoni/tmp/root/.ssh]
└─# ls -la
total 4
drwx------ 2 root root 1024 Oct  6 10:30 .
drwx------ 3 root root 1024 Oct  6 10:30 ..
-rw------- 1 root root  411 Oct  6 10:30 id_ed25519
-rw-r--r-- 1 root root   96 Oct  6 10:30 id_ed25519.pub

```

- acceder al server
```bash
──(root㉿kali)-[/home/…/operationoni/tmp/root/.ssh]
└─# cat id_ed25519 
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
                                                                                                      
┌──(root㉿kali)-[/home/…/operationoni/tmp/root/.ssh]
└─# ssh -i id_ed25519 -p 50279 ctf-player@saturn.picoctf.net

```

- obtener la bandera

```bash
ctf-player@challenge:~$ ls -la
total 4
drwxr-xr-x 1 ctf-player ctf-player 20 Mar 17 17:14 .
drwxr-xr-x 1 root       root       24 Mar 15 06:58 ..
drwx------ 2 ctf-player ctf-player 34 Mar 17 17:14 .cache
drwxr-xr-x 2 ctf-player ctf-player 29 Mar 15 06:58 .ssh
-rw-r--r-- 1 root       root       28 Mar 15 06:58 flag.txt
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_af277f77}ctf-player@challenge:~$ Connection to saturn.picoctf.net closed by remote host.

```

