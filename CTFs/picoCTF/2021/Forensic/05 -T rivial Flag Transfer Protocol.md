# Trivial Flag Transfer Protocol

Figure out how they moved the [flag](https://mercury.picoctf.net/static/b686a99ec088f10b324cfe963bd32dab/tftp.pcapng).

Hint> What are some other ways to hide data?

# Solucion

- datos en el pcap hay que extrearlos con whiresjark

- decodificar mensajes

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/trivialflag/data]
└─$ cat instructions.txt | tr [A-Za-z] [N-ZA-M]
TFTP DOESNT ENCRYPT OUR TRAFFIC SOWE MUST DISGUISE OUR FLAG TRANSFER .FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

```

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/trivialflag/data]
└─$ cat plan | tr [A-Za-z] [N-ZA-M] 
I USED THE PROGRAM AND HID IT WITH- DUE DILIGENCE. CHECKOUT THE PHOTOS

```

- ver el contendo del paquete
```bash
┌──(kali㉿kali)-[~/picoctf/forensic/trivialflag/data]
└─$ dpkg-deb -I program.deb 
 new Debian package, version 2.0.
 size 138310 bytes: control archive=1250 bytes.
     826 bytes,    18 lines      control              
    1184 bytes,    17 lines      md5sums              
 Package: steghide
 Source: steghide (0.5.1-9.1)
 Version: 0.5.1-9.1+b1
 Architecture: amd64
 Maintainer: Ola Lundqvist <opal@debian.org>
 Installed-Size: 426
 Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
 Section: misc
 Priority: optional
 Description: A steganography hiding tool
  Steghide is steganography program which hides bits of a data file
  in some of the least significant bits of another file in such a way
  that the existence of the data file is not visible and cannot be proven.
  .
  Steghide is designed to be portable and configurable and features hiding
  data in bmp, wav and au files, blowfish encryption, MD5 hashing of
  passphrases to blowfish keys, and pseudo-random distribution of hidden bits
  in the container data.

```



-  Instalar steghide
```bash
┌──(kali㉿kali)-[~/picoctf/forensic/trivialflag/data]
└─$ sudo apt install steghide

```

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/trivialflag/data]
└─$ steghide --extract -sf picture3.bmp -p DUEDILIGENCE
wrote extracted data to "flag.txt".
                                                                                       
┌──(kali㉿kali)-[~/picoctf/forensic/trivialflag/data]
└─$ cat flag.txt                   
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

```