


## Solucion

### informacion de las particiones con mmls
-

```
mmls disk.flag.img 
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

### Determinar el tipo de particiones con fsstat

```
 fsstat -o 2048 disk.flag.img 
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: Ext4
Volume Name: 
Volume ID: 8e023955b4e7dab7e04b7643076ccf0f

Last Written at: 2021-09-29 13:10:02 (CDT)
Last Checked at: 2021-09-29 10:57:16 (CDT)

Last Mounted at: 2021-09-29 13:06:00 (CDT)
Unmounted properly
Last mounted on: /mnt/boot

Source OS: Linux
Dynamic Structure
Compat Features: Journal, Ext Attributes, Resize Inode, Dir Index
InCompat Features: Filetype, Extents, Flexible Block Groups, 
Read Only Compat Features: Sparse Super, Large File, Huge File, Extra Inode Size

Journal ID: 00
Journal Inode: 8

METADATA INFORMATION
--------------------------------------------
Inode Range: 1 - 25585
Root Directory: 2
Free Inodes: 25560
Inode Size: 256

CONTENT INFORMATION
--------------------------------------------
Block Groups Per Flex Group: 16
Block Range: 0 - 102399
Block Size: 1024
Reserved Blocks Before Block Groups: 1
Free Blocks: 74579

BLOCK GROUP INFORMATION
--------------------------------------------
Number of Block Groups: 13
Inodes per group: 1968
Blocks per group: 8192

Group: 0:
  Inode Range: 1 - 1968
  Block Range: 1 - 8192
  Layout:
    Super Block: 1 - 1
    Group Descriptor Table: 2 - 2
    Group Descriptor Growth Blocks: 3 - 258
    Data bitmap: 259 - 259
    Inode bitmap: 272 - 272
    Inode Table: 285 - 776
    Data Blocks: 777 - 8192
  Free Inodes: 1944 (98%)
  Free Blocks: 1498 (18%)
  Total Directories: 2

Group: 1:
  Inode Range: 1969 - 3936
  Block Range: 8193 - 16384
  Layout:
    Super Block: 8193 - 8193
    Group Descriptor Table: 8194 - 8194
    Group Descriptor Growth Blocks: 8195 - 8450
    Data bitmap: 260 - 260
    Inode bitmap: 273 - 273
    Inode Table: 777 - 1268
    Data Blocks: 1269 - 16384
  Free Inodes: 1968 (100%)
  Free Blocks: 7548 (92%)
  Total Directories: 0

Group: 2:
  Inode Range: 3937 - 5904
  Block Range: 16385 - 24576
  Layout:
    Data bitmap: 261 - 261
    Inode bitmap: 274 - 274
    Inode Table: 1269 - 1760
    Data Blocks: 1761 - 24576
  Free Inodes: 1968 (100%)
  Free Blocks: 4644 (56%)
  Total Directories: 0

Group: 3:
  Inode Range: 5905 - 7872
  Block Range: 24577 - 32768
  Layout:
    Super Block: 24577 - 24577
    Group Descriptor Table: 24578 - 24578
    Group Descriptor Growth Blocks: 24579 - 24834
    Data bitmap: 262 - 262
    Inode bitmap: 275 - 275
    Inode Table: 1761 - 2252
    Data Blocks: 2253 - 32768
  Free Inodes: 1968 (100%)
  Free Blocks: 1884 (22%)
  Total Directories: 0

Group: 4:
  Inode Range: 7873 - 9840
  Block Range: 32769 - 40960
  Layout:
    Data bitmap: 263 - 263
    Inode bitmap: 276 - 276
    Inode Table: 2253 - 2744
    Data Blocks: 2745 - 40960
  Free Inodes: 1968 (100%)
  Free Blocks: 2436 (29%)
  Total Directories: 0

Group: 5:
  Inode Range: 9841 - 11808
  Block Range: 40961 - 49152
  Layout:
    Super Block: 40961 - 40961
    Group Descriptor Table: 40962 - 40962
    Group Descriptor Growth Blocks: 40963 - 41218
    Data bitmap: 264 - 264
    Inode bitmap: 277 - 277
    Inode Table: 2745 - 3236
    Data Blocks: 3237 - 49152
  Free Inodes: 1968 (100%)
  Free Blocks: 7934 (96%)
  Total Directories: 0

Group: 6:
  Inode Range: 11809 - 13776
  Block Range: 49153 - 57344
  Layout:
    Data bitmap: 265 - 265
    Inode bitmap: 278 - 278
    Inode Table: 3237 - 3728
    Data Blocks: 3729 - 57344
  Free Inodes: 1968 (100%)
  Free Blocks: 4096 (50%)
  Total Directories: 0

Group: 7:
  Inode Range: 13777 - 15744
  Block Range: 57345 - 65536
  Layout:
    Super Block: 57345 - 57345
    Group Descriptor Table: 57346 - 57346
    Group Descriptor Growth Blocks: 57347 - 57602
    Data bitmap: 266 - 266
    Inode bitmap: 279 - 279
    Inode Table: 3729 - 4220
    Data Blocks: 4221 - 65536
  Free Inodes: 1968 (100%)
  Free Blocks: 7934 (96%)
  Total Directories: 0

Group: 8:
  Inode Range: 15745 - 17712
  Block Range: 65537 - 73728
  Layout:
    Data bitmap: 267 - 267
    Inode bitmap: 280 - 280
    Inode Table: 4221 - 4712
    Data Blocks: 4713 - 73728
  Free Inodes: 1968 (100%)
  Free Blocks: 8192 (100%)
  Total Directories: 0

Group: 9:
  Inode Range: 17713 - 19680
  Block Range: 73729 - 81920
  Layout:
    Super Block: 73729 - 73729
    Group Descriptor Table: 73730 - 73730
    Group Descriptor Growth Blocks: 73731 - 73986
    Data bitmap: 268 - 268
    Inode bitmap: 281 - 281
    Inode Table: 4713 - 5204
    Data Blocks: 5205 - 81920
  Free Inodes: 1968 (100%)
  Free Blocks: 7934 (96%)
  Total Directories: 0

Group: 10:
  Inode Range: 19681 - 21648
  Block Range: 81921 - 90112
  Layout:
    Data bitmap: 269 - 269
    Inode bitmap: 282 - 282
    Inode Table: 5205 - 5696
    Data Blocks: 5697 - 90112
  Free Inodes: 1968 (100%)
  Free Blocks: 8192 (100%)
  Total Directories: 0

Group: 11:
  Inode Range: 21649 - 23616
  Block Range: 90113 - 98304
  Layout:
    Data bitmap: 270 - 270
    Inode bitmap: 283 - 283
    Inode Table: 5697 - 6188
    Data Blocks: 6189 - 98304
  Free Inodes: 1968 (100%)
  Free Blocks: 8192 (100%)
  Total Directories: 0

Group: 12:
  Inode Range: 23617 - 25584
  Block Range: 98305 - 102399
  Layout:
    Data bitmap: 271 - 271
    Inode bitmap: 284 - 284
    Inode Table: 6189 - 6680
    Data Blocks: 6681 - 102399
  Free Inodes: 1968 (100%)
  Free Blocks: 4095 (99%)
  Total Directories: 0

```

### Listar los archivos y nombres de directorios con fls

```
fls -i raw -f ext4 -o 2048 -r disk.flag.img 
d/d 11: lost+found
r/r 12: ldlinux.sys
r/r 13: ldlinux.c32
r/r 15: config-virt
r/r 16: vmlinuz-virt
r/r 17: initramfs-virt
l/l 18: boot
r/r 20: libutil.c32
r/r 19: extlinux.conf
r/r 21: libcom32.c32
r/r 22: mboot.c32
r/r 23: menu.c32
r/r 14: System.map-virt
r/r 24: vesamenu.c32
V/V 25585:      $OrphanFiles

```
#### vemos info en la otra particion
```
fsstat -o 360448 disk.flag.img         
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: Ext4
Volume Name: 
Volume ID: 3c054136f02898b3224bd632cbd6c255

Last Written at: 2021-09-29 10:57:31 (CDT)
Last Checked at: 2021-09-29 10:57:16 (CDT)

Last Mounted at: 2021-09-29 13:06:00 (CDT)
Unmounted properly
Last mounted on: /

```

```
fls -o 360448 -r disk.flag.img

+ r/r 2363:     .ash_history
+ d/d 3981:     my_folder
++ r/r * 2082(realloc): flag.txt
++ r/r 2371:    flag.uni.txt

```

## Visualizamos el conteido de los archivos con icat

```
> puras mamadas
 icat -o 360448 disk.flag.img 2082
            3.449677            13.056403


> vemos el otro y andale

icat -o 360448 disk.flag.img 2371
picoCTF{by73_5urf3r_2f22df38}


```