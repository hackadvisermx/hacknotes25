	In this [article](https://docs.google.com/document/d/1WFGIA2Dovt_CwuNBpFoYsxukrQEnBvoD/edit?usp=sharing&ouid=116503409028827144644&rtpof=true&sd=true) you can read the history of the Incas

## Solucion

- Descargar el archivo, hacerle strings y ya
```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-4-stage-peru/stego/historyofperu]
└─$ strings -n10 LA\ HISTORIA\ DE\ LOS\ INCAS.doc | grep {   
Fl@g{M@chu_Picchu}
```