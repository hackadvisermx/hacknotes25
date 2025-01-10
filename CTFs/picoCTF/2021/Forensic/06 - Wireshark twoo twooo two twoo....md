# Wireshark twoo twooo two twoo...

Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng).

Hint 1: Did you really find _the_ flag?
Hint 2: Look for traffic that seems suspicious.
## Solucion
- examinamos los paquetes TCP y HTTP en busca de la bandera

- la solucion esta en los paquetes DNS

``` cmd
dns && ip.dst==18.217.1.57 && dns.qry.name contains local
```

- File - Export - Packet Disection - cvs y parsearlo, quitando linea 1 y ultima para limpiar

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/wiresharktwo]
└─$ cat cvs.csv | cut -d ' ' -f 5 | cut -d '.' -f 1 | tr -d '\n' | base64 -d
picoCTF{dns_3xf1l_ftw_deadbeef}                                                                                                                                                                                 

```

- Copiarlos como texto del query de cada paquete

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/wiresharktwo]
└─$ cat exifil | cut -d '.' -f 1 | tr -d '\n' | base64 -d
picoCTF{dns_3xf1l_ftw_deadbeef}                                                                                       
```

