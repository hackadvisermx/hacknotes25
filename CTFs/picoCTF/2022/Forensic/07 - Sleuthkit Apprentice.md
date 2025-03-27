mm# Sleuthkit Apprentice

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download compressed disk image](https://artifacts.picoctf.net/c/334/disk.flag.img.gz)

## Solucion
- desempacamos la magen

``` bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ gzip -d disk.flag.img.gz 
```

- examinamos con fdisk

```
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ fdisk -l disk.flag.img 
Disk disk.flag.img: 300 MiB, 314572800 bytes, 614400 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x7389e82d

Device         Boot  Start    End Sectors  Size Id Type
disk.flag.img1 *      2048 206847  204800  100M 83 Linux
disk.flag.img2      206848 360447  153600   75M 82 Linux swap / Solaris
disk.flag.img3 

```

```bash

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ sudo apt install kpartx      

```

- Montar la imagen

```bash

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ sudo losetup loop0 disk.flag.img
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ losetup -l
NAME SIZELIMIT OFFSET AUTOCLEAR RO BACK-FILE                                               DIO LOG-SEC
/dev/loop0
             0      0         0  0 /home/kali/hacking/ctfs2022/picoctf2022/forensic/sleuthkit-app/disk.flag.img
                                                                                             0     512
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ kpartx -av /dev/loop0
/dev/mapper/control: open failed: Permission denied
Failure to communicate with kernel device-mapper driver.
Incompatible libdevmapper 1.02.175 (2021-01-08) and kernel driver (unknown version).
device mapper prerequisites not met
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ sudo kpartx -av /dev/loop0
add map loop0p1 (254:0): 0 204800 linear 7:0 2048
add map loop0p2 (254:1): 0 153600 linear 7:0 206848
add map loop0p3 (254:2): 0 253952 linear 7:0 360448
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ mount -r /dev/mapper/loop0p1 tmp 
mount: /home/kali/hacking/ctfs2022/picoctf2022/forensic/sleuthkit-app/tmp: must be superuser to use mount.
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ sudo mount -r /dev/mapper/loop0p1 tmp
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ 



```

## Sleuth
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ mmls -V                         
The Sleuth Kit ver 4.11.1
```

- info de las particiones

```
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ mmls disk.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)


```

- tipo de particion en ese offset

```
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ fsstat -o 360448 disk.flag.img

```

- ver archivos en la particion
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ fls -o 360448 disk.flag.img
d/d 451:	home
d/d 11:	lost+found
d/d 12:	boot
d/d 1985:	etc
d/d 1986:	proc
d/d 1987:	dev
d/d 1988:	tmp
d/d 1989:	lib
d/d 1990:	var
d/d 3969:	usr
d/d 3970:	bin
d/d 1991:	sbin
d/d 1992:	media
d/d 1993:	mnt
d/d 1994:	opt
d/d 1995:	root
d/d 1996:	run
d/d 1997:	srv
d/d 1998:	sys
d/d 2358:	swap
V/V 31745:	$OrphanFiles
```

- ver en un directorio determinao

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ fls -o 360448 disk.flag.img 31745


```

- archivos borrados recursivo

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ fls -o 360448 disk.flag.img -r -d | grep flag
r/r * 2082(realloc):	root/my_folder/flag.txt


```

- montar particion o imagen

```
sudo kpartx -av disk.flag.img 
sudo losetup -P --show -f disk.flag.img

sudo mount /dev/mapper/loop2p1 tmp


┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ sudo kpartx -lav disk.flag.img
add map loop1p1 (254:3): 0 204800 linear 7:1 2048
add map loop1p2 (254:4): 0 153600 linear 7:1 206848
add map loop1p3 (254:5): 0 253952 linear 7:1 360448

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ sudo mount /dev/mapper/loop1p3 tmp

testdisk



```

## Todo el pedo era por aca

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ fls -o 360448 disk.flag.img -r | grep flag 
++ r/r * 2082(realloc):	flag.txt
++ r/r 2371:	flag.uni.txt

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ icat -o 360448 disk.flag.img 2371 > f        
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/sleuthkit-app]
└─$ cat f
picoCTF{by73_5urf3r_42028120}



```


## Referencias

- https://askubuntu.com/questions/184414/recover-data-from-image-file-usb-disk
- 