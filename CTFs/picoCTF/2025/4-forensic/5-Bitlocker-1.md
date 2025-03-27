jo
# Bitlocker-1

Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!Download the disk image [here](https://challenge-files.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd)

1. Hash cracking

# Solucion

- BitLocker es una función de seguridad de Windows que cifra unidades de disco y protege los datos. Esto ayuda a mantener la información confidencial segura si el dispositivo se pierde o es robado.

- examinando la imagen

```
┌──(root㉿kali)-[/home/…/tmp/picoctf2025/forensic/bitlocker]
└─# file bitlocker-1.dd 
bitlocker-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "-FVE-FS-", sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, sectors/track 63, heads 255, hidden sectors 124499968, FAT (32 bit), sectors/FAT 8160, serial number 0, unlabeled; NTFS, sectors/track 63, physical drive 0x1fe0, $MFT start cluster 393217, serial number 02020454d414e204f, checksum 0x41462020
```


- Sacar el hash de bitlocker
```
bitlocker2john -i bitlocker-1.dd > bitlocker-hash
cat bitlocker-hash 
```

```
john bitlocker-hash -w=/usr/share/wordlists/rockyou.txt

Note: This format may emit false positives, so it will keep trying even after finding a possible candidate.
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (BitLocker, BitLocker [SHA-256 AES 32/64])
Cost 1 (iteration count) is 1048576 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
       (?)     
jacqueline       (?)     
2g 0:00:29:51 0.22% (ETA: 2025-03-25 09:58) 0.001116g/s 20.99p/s 41.99c/s 41.99C/s jeremy01..jasonkidd
Session aborted

```

- Use `losetup` to attach the .dd image file: 
- Losetup permite asociar un dispositivo de loop a un archivo regular
- Un dispositivo de loop es metodo usado para adminisrtar y editar imagenes de sistemas de archivo
```
sudo losetup -f -P bitlocker-1.dd                                                                                                        
losetup      
                
NAME       SIZELIMIT OFFSET AUTOCLEAR RO BACK-FILE                                                DIO LOG-SEC
/dev/loop0         0      0         0  0 /home/kali/tmp/picoctf2025/forensic/bitlocker/bitlocker-1.dd
               
```


- - Crear dos directorios uno para dislocker para escribir el volumen desencriptado y el otro para montarlo
```
sudo mkdir /mnt/bitlocker /mnt/decrypted
```

- Usar dislocker para desencriptar la particion
```
sudo dislocker -v -V /dev/loop0 -u -- /mnt/bitlocker

Enter the user password: 
jacqueline
```

- Crear punto de monteje desencriptad
```
sudo mount -o loop /mnt/bitlocker/dislocker-file /mnt/decrypted 
```

- Sacar la flag
```
┌──(root㉿kali)-[/mnt/decrypted]
└─# ls
'$RECYCLE.BIN'   flag.txt  'System Volume Information'
                                                                                                     
┌──(root㉿kali)-[/mnt/decrypted]
└─# cat flag.txt     
picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}   
```

- deshabilitar todo
```
losetup -d /dev/loop0
umount /mnt/decrypted 
umount /mnt/bitlocker

``