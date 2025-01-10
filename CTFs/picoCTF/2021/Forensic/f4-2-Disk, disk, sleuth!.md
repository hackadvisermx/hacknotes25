Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/f63e4eba644c99e92324b65cbd875db6/dds1-alpine.flag.img.gz)

Have you ever used `file` to determine what a file was?
Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
Using your own computer, you could use qemu to boot from this disk!


# Solucion

```
file dds1-alpine.flag.img.gz 
dds1-alpine.flag.img.gz: gzip compressed data, was "dds1-alpine.flag.img", last modified: Tue Mar 16 00:19:51 2021, from Unix, original size modulo 2^32 134217728

┌──(kali㉿kali)-[~/picoctf/forensic/disk-disk-sleuth]
└─$ gzip -d dds1-alpine.flag.img.gz        


┌──(kali㉿kali)-[~/picoctf/forensic/disk-disk-sleuth]
└─$ ls -la
total 131084
drwxrwxr-x 2 kali kali      4096 Oct 11 12:58 .
drwxrwxr-x 3 kali kali      4096 Oct 11 12:54 ..
-rw-rw-r-- 1 kali kali 134217728 Mar 15  2021 dds1-alpine.flag.img
                                                                                             
┌──(kali㉿kali)-[~/picoctf/forensic/disk-disk-sleuth]
└─$ file dds1-alpine.flag.img 
dds1-alpine.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x10,81,1), startsector 2048, 260096 sectors


```

### Forma 1
```
strings dds1-alpine.flag.img |  grep pico
ffffffff81399ccf t pirq_pico_get
ffffffff81399cee t pirq_pico_set
ffffffff820adb46 t pico_router_probe
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_ad5c96c0}

```

### Forma 2
```
sudo apt install autopsy

sudo autopsy

>> Modo autopsy

sudo autopsy 

============================================================================

                       Autopsy Forensic Browser 
                  http://www.sleuthkit.org/autopsy/
                             ver 2.24 

============================================================================
Evidence Locker: /var/lib/autopsy
Start Time: Fri Oct 11 16:20:21 2024
Remote Host: localhost
Local Port: 9999

Open an HTML browser on the remote host and paste this URL in it:

    http://localhost:9999/autopsy

Keep this process running and use <ctrl-c> to exit
Invalid magic value (raw_open: image "/home/kali/picoctf/forensic/disk-disk-sleuth" - is a directory)

>> vamos al web

http://localhost:9999/autopsy

- creamos el proyecto
- creamos el host
- agregamos la imagen
- buscammos la cadena


```

### Forma 3

```
Booting a raw disk image in QEMU

qemu-system-x86_64 -drive format=raw,file=dds1-alpine.flag.img

root
root


cd boot
cat syslinux.cgf


```

- https://unix.stackexchange.com/questions/276480/booting-a-raw-disk-image-in-qemu