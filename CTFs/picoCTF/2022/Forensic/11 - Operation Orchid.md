# Operation Orchid

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download compressed disk image](https://artifacts.picoctf.net/c/240/disk.flag.img.gz)

# Solucion

- montamos la imagen


- exploramos
```bash
┌──(root㉿kali)-[/home/…/picoctf2022/forensic/operatonorchid/mnt]
└─# cd root       
                                                                                                      
┌──(root㉿kali)-[/home/…/forensic/operatonorchid/mnt/root]
└─# ls -la
total 4
drwx------  2 root root 1024 Oct  6 14:32 .
drwxr-xr-x 22 root root 1024 Oct  6 14:30 ..
-rw-------  1 root root  202 Oct  6 14:33 .ash_history
-rw-r--r--  1 root root   64 Oct  6 14:32 flag.txt.enc
                                                                                                      
┌──(root㉿kali)-[/home/…/forensic/operatonorchid/mnt/root]
└─# cat .ash_history 
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
                                                                                                      
┌──(root㉿kali)-[/home/…/forensic/operatonorchid/mnt/root]
└─# 



```

- desencriptamos

```bash

sudo openssl aes256 -salt -d -in mnt/root/flag.txt.enc -out flag -k unbreakablepassword1234567

┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/operatonorchid]
└─$ ls
disk.flag.img  flag  mnt
                                                                                                      
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/forensic/operatonorchid]
└─$ cat flag 
picoCTF{h4un71ng_p457_17237fce}   
```