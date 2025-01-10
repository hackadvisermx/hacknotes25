# Wireshark doo dooo do doo...

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng).

# Solucion
- En el paquete 827 se intercambia por http la bandera en ROT13

- Se puede descargar el achivo de texto



- En uno de los archivos descargados estaba la bandera

```bash
┌──(kali㉿kali)-[~/picoctf/forensic/wireshark]
└─$ cat %2f            
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}

```

The flag is picoCTF{p33kab00_1_s33_u_deadbeef}