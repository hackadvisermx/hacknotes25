# Merida Tunnels

A legend of Merida is that under the city there is an underground communication system made up of tunnels that connect the main churches in the heart of the city.

Huay Chivo knows the true answer and hides it in a flag.

## Solucion 
- Identificamos el tipo de archivo y agregamos extension
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/stego/meridatunnels]
└─$ ls

file                                             
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/stego/meridatunnels]
└─$ file file 
file: Microsoft PowerPoint 2007+
                                                 
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/stego/meridatunnels]
└─$ mv file file.pttx                 
                                                 
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/stego/meridatunnels]
└─$ ls
file.pttx

```

- descmprimimos
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-3-mexico/stego/meridatunnels]
└─$ unzip file.pttx  
Archive:  file.pttx
  inflating: docProps/app.xml        
  inflating: docProps/core.xml       
 extracting: ppt/media/image1.png    
 extracting: ppt/media/image2.png    
 extracting: ppt/media/image3.png    
 extracting: ppt/media/image4.png    
 extracting: ppt/media/image5.png    
 extracting: ppt/media/image6.png    
  inflating: ppt/media/images8.png   
  inflating: ppt/presentation.xml    
  inflating: ppt/presProps.xml       
  inflating: ppt/slideLayouts/slideLayout1.xml  
  inflating: ppt/slideLayouts/slideLayout10.xml  
  inflating: ppt/slideLayouts/slideLayout11.xml  
  inflating: ppt/slideLayouts/slideLayout12.xml  
  inflating: ppt/slideLayouts/slideLayout2.xml  
  inflating: ppt/slideLayouts/slideLayout3.xml  
  inflating: ppt/slideLayouts/slideLayout4.xml  
  inflating: ppt/slideLayouts/slideLayout5.xml  
  inflating: ppt/slideLayouts/slideLayout6.xml  
  inflating: ppt/slideLayouts/slideLayout7.xml  
  inflating: ppt/slideLayouts/slideLayout8.xml  
  inflating: ppt/slideLayouts/slideLayout9.xml  
  inflating: ppt/slideLayouts/_rels/slideLayout1.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout10.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout11.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout12.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout2.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout3.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout4.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout5.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout6.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout7.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout8.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout9.xml.rels  
  inflating: ppt/slideMasters/slideMaster1.xml  
  inflating: ppt/slideMasters/_rels/slideMaster1.xml.rels  
  inflating: ppt/slides/slide1.xml   
  inflating: ppt/slides/slide2.xml   
  inflating: ppt/slides/slide3.xml   
  inflating: ppt/slides/slide4.xml   
  inflating: ppt/slides/slide5.xml   
  inflating: ppt/slides/slide8.xml   
  inflating: ppt/slides/_rels/slide1.xml.rels  
  inflating: ppt/slides/_rels/slide2.xml.rels  
  inflating: ppt/slides/_rels/slide3.xml.rels  
  inflating: ppt/slides/_rels/slide4.xml.rels  
  inflating: ppt/slides/_rels/slide5.xml.rels  
  inflating: ppt/tableStyles.xml     
  inflating: ppt/theme/theme1.xml    
  inflating: ppt/viewProps.xml       
  inflating: ppt/_rels/presentation.xml.rels  
  inflating: [Content_Types].xml     
  inflating: _rels/.rels       
```

- Examinamos todas las imagenes en ppt/media y encotramos que images8.png, tiene una frase oculta al subr y bajar el contraste
```
Ichkaansiho
```

- Usamos openstego para sacar los datos embebidos en la imagen con el password encontrado , sale el archivo cripto

```bash
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/media]
└─$ openstego 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
                                                                                                     
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/media]
└─$ ls    
cripto.png  image1.png  image2.png  image3.png  image4.png  image5.png  image6.png  images8.png
                                                                                                     
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/media]
└─$ 

```
- Abrimos cripto.png y viene un algorimo de criptado
```
Citrix ctx1 decode
```

- Seguimos examinando y llegamos a ppt/slides y ahi encontramos el archivo slides8.xml, y al analizarlo nos damos cuenta que es un archivo que es pptx y le cambiamos el nombre

```bash
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/slides]
└─$ ls 
_rels  slide1.xml  slide2.xml  slide3.xml  slide4.xml  slide5.xml  slide8.xml
                                                                                                     
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/slides]
└─$ exiftool slide8.xml
ExifTool Version Number         : 12.44
File Name                       : slide8.xml
Directory                       : .
File Size                       : 453 kB
File Modification Date/Time     : 2022:10:05 21:35:36-04:00
File Access Date/Time           : 2022:10:12 16:08:42-04:00
File Inode Change Date/Time     : 2022:10:05 21:35:36-04:00
File Permissions                : -rwxrwx---
File Type                       : PPTX
File Type Extension             : pptx
MIME Type                       : application/vnd.openxmlformats-officedocument.presentationml.presentation
Zip Required Version            : 20
Zip Bit Flag                    : 0x0808
Zip Compression                 : Deflated
Zip Modify Date                 : 2022:10:06 02:34:48
Zip CRC                         : 0x41e11478
Zip Compressed Size             : 676
Zip Uncompressed Size           : 13115
Zip File Name                   : [Content_Types].xml
Template                        : 
Total Edit Time                 : 7 minutes
Application                     : LibreOffice/6.4.7.2$Linux_X86_64 LibreOffice_project/40$Build-2
Create Date                     : 2022:10:05 21:27:34Z
Creator                         : 
Description                     : 
Language                        : en-US
Last Modified By                : 
Modify Date                     : 2022:10:05 21:34:49Z
Revision Number                 : 3
Subject                         : 
Title                           : Lights
                                                                                                     
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/slides]
└─$ mv slide8.xml slide8.pptx

```

- lo descomprimimos y econtramos ahi ppt/flag
```bash
┌──(kali㉿kali)-[~/…/stego/meridatunnels/ppt/slides]
└─$ unzip slide8.pptx
Archive:  slide8.pptx
  inflating: [Content_Types].xml     
  inflating: _rels/.rels             
  inflating: docProps/app.xml        
  inflating: docProps/core.xml       
  inflating: ppt/_rels/presentation.xml.rels  
  inflating: ppt/flag                
  inflating: ppt/media/image1.jpeg   
  inflating: ppt/media/image2.jpeg   
  inflating: ppt/media/image3.jpeg   
  inflating: ppt/media/image4.png    
  inflating: ppt/presentation.xml    
  inflating: ppt/slideLayouts/_rels/slideLayout1.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout10.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout11.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout12.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout13.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout14.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout15.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout16.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout17.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout18.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout19.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout2.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout20.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout21.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout22.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout23.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout24.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout25.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout26.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout27.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout28.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout29.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout3.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout30.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout31.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout32.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout33.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout34.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout35.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout36.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout4.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout5.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout6.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout7.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout8.xml.rels  
  inflating: ppt/slideLayouts/_rels/slideLayout9.xml.rels  
  inflating: ppt/slideLayouts/slideLayout1.xml  
  inflating: ppt/slideLayouts/slideLayout10.xml  
  inflating: ppt/slideLayouts/slideLayout11.xml  
  inflating: ppt/slideLayouts/slideLayout12.xml  
  inflating: ppt/slideLayouts/slideLayout13.xml  
  inflating: ppt/slideLayouts/slideLayout14.xml  
  inflating: ppt/slideLayouts/slideLayout15.xml  
  inflating: ppt/slideLayouts/slideLayout16.xml  
  inflating: ppt/slideLayouts/slideLayout17.xml  
  inflating: ppt/slideLayouts/slideLayout18.xml  
  inflating: ppt/slideLayouts/slideLayout19.xml  
  inflating: ppt/slideLayouts/slideLayout2.xml  
  inflating: ppt/slideLayouts/slideLayout20.xml  
  inflating: ppt/slideLayouts/slideLayout21.xml  
  inflating: ppt/slideLayouts/slideLayout22.xml  
  inflating: ppt/slideLayouts/slideLayout23.xml  
  inflating: ppt/slideLayouts/slideLayout24.xml  
  inflating: ppt/slideLayouts/slideLayout25.xml  
  inflating: ppt/slideLayouts/slideLayout26.xml  
  inflating: ppt/slideLayouts/slideLayout27.xml  
  inflating: ppt/slideLayouts/slideLayout28.xml  
  inflating: ppt/slideLayouts/slideLayout29.xml  
  inflating: ppt/slideLayouts/slideLayout3.xml  
  inflating: ppt/slideLayouts/slideLayout30.xml  
  inflating: ppt/slideLayouts/slideLayout31.xml  
  inflating: ppt/slideLayouts/slideLayout32.xml  
  inflating: ppt/slideLayouts/slideLayout33.xml  
  inflating: ppt/slideLayouts/slideLayout34.xml  
  inflating: ppt/slideLayouts/slideLayout35.xml  
  inflating: ppt/slideLayouts/slideLayout36.xml  
  inflating: ppt/slideLayouts/slideLayout4.xml  
  inflating: ppt/slideLayouts/slideLayout5.xml  
  inflating: ppt/slideLayouts/slideLayout6.xml  
  inflating: ppt/slideLayouts/slideLayout7.xml  
  inflating: ppt/slideLayouts/slideLayout8.xml  
  inflating: ppt/slideLayouts/slideLayout9.xml  
  inflating: ppt/slideMasters/_rels/slideMaster1.xml.rels  
  inflating: ppt/slideMasters/_rels/slideMaster2.xml.rels  
  inflating: ppt/slideMasters/_rels/slideMaster3.xml.rels  
  inflating: ppt/slideMasters/slideMaster1.xml  
  inflating: ppt/slideMasters/slideMaster2.xml  
  inflating: ppt/slideMasters/slideMaster3.xml  
  inflating: ppt/slides/_rels/slide1.xml.rels  
  inflating: ppt/slides/slide1.xml   
  inflating: ppt/theme/theme1.xml    
  inflating: ppt/theme/theme2.xml    
  inflating: ppt/theme/theme3.xml  
```

- miramos el archivo y vemos que esta encriptado, lo llevams a cyberchef aplicando la receta del algoritmo que nos menciona la imagen anterior

```
┌──(kali㉿kali)-[~/…/meridatunnels/ppt/slides/ppt]
└─$ ls
flag  media  presentation.xml  _rels  slideLayouts  slideMasters  slides  theme
                                                                                                     
┌──(kali㉿kali)-[~/…/meridatunnels/ppt/slides/ppt]
└─$ pwd
/home/kali/hackdata/ctfs2022/metared-3-mexico/stego/meridatunnels/ppt/slides/ppt                                                                               
┌──(kali㉿kali)-[~/…/meridatunnels/ppt/slides/ppt]
└─$ cat flag            
MDGGKPAKMOGLKJAMOEEBLMBJMHGCIKCPOPEKJNDIPEFBJADFPBFENBHELEBBMHGCOHECJCDHPMFJJNDILNBINOHLLHBCMCGHKGADMHGCKDAGIDCGOHECICCHKCAHMOGLKLAONCHHLHBCNJHMLNBINMHJKPAKIOCLPDFG

```

- despues de cyberxhef receta> Citrix ctx1 decode

```
flagMX{Merida es una ciudad de leyendas!}
```

