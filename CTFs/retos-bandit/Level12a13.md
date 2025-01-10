# Bandit Level 12 → Level 13

## Datos de acceso

bandit12
JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

## Solucion

```bash
xxd -r data.txt | file -
/dev/stdin: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ 
bandit12@bandit:~$ 
bandit12@bandit:~$ xxd -r data.txt | zcat |file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat |file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat |file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar x0 | file -
tar: Options '-[0-7][lmh]' not supported by *this* tar
Try 'tar --help' or 'tar --usage' for more information.
/dev/stdin: empty
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ 
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat |file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file -
/dev/stdin: ASCII text
bandit12@bandit:~$ xxd -r data.txt | zcat | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat
The password is wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
```

## Referencia

- Algunos tipos de compresion en Linux

```
-----------------------------------------------------
ext	    comp	desc			    desc consola
-----------------------------------------------------
.gz	    gzip	gzip -d	 (gunzip)	zcat
.bz2	bzip2	bzip2 -d (bunzip2)	bzcat
.tar	tar	    tar xf			    tar xO
----------------------------------------------------
```

- otros (instalar) :

.zip	zip	unzip (7z x)	
.rar	rar	unrar (7z x)


apt install zip rar unrar p7zip-full p7zip-rar



