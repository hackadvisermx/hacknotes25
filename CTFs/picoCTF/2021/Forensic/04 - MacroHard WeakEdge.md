#  MacroHard WeakEdge
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/52da699e0f203321c7c90ab56ea912d8/Forensics is fun.pptm)


# Solucion
- Desempaquetamos el .ppt

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/macrohard]
└─$ file Forensics\ is\ fun.pptm 
Forensics is fun.pptm: Microsoft PowerPoint 2007+
                                                                                                     
┌──(kali㉿kali)-[~/picoctf/forensic/macrohard]
└─$ unzip Forensics\ is\ fun.pptm 

```

- revisamos las macros ?? pero fail
```bash

```


- El archivo hidden contiene la flag en base64

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/macrohard/ppt]
└─$ cd slideMasters 
                                                                                                     
┌──(kali㉿kali)-[~/…/forensic/macrohard/ppt/slideMasters]
└─$ ls    
hidden  _rels  slideMaster1.xml
                                                                                                     
┌──(kali㉿kali)-[~/…/forensic/macrohard/ppt/slideMasters]
└─$ cat hidden        
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q                                                                                                     
┌──(kali㉿kali)-[~/…/forensic/macrohard/ppt/slideMasters]
└─$ cat hidden | tr -d ' '
ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ                                                                                                     
┌──(kali㉿kali)-[~/…/forensic/macrohard/ppt/slideMasters]
└─$ cat hidden | tr -d ' ' | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input

```