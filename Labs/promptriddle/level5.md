
```
This is Level 5  
I need more tools  

hackadvisermx@Level5:~$

hackadvisermx@Level5:~$ resources

magnifying-glass.pdf

hackadvisermx@Level5:~$ download magnifying-glass.pdf

Downloading file...

hackadvisermx@Level5:~$


```

- Procesamos el pdf
```
┌──(kali㉿kali)-[~/tmp]
└─$ pdf2john magnifying-glass.pdf > pdfhash
                                                                                                                                           
┌──(kali㉿kali)-[~/tmp]
└─$ john pdfhash -w=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
Cost 1 (revision) is 4 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
unimportant      (magnifying-glass.pdf)     
1g 0:00:00:02 DONE (2025-04-15 23:35) 0.4098g/s 312445p/s 312445c/s 312445C/s urmighty..undaground
Use the "--show --format=PDF" options to display all of the cracked passwords reliably
Session completed. 

```

- al abrir el pdf, un numero que parecen ser coordneadas: Place Basilique Saint Sernin, Toulouse France

```
saintsernin


password toulouse
```

