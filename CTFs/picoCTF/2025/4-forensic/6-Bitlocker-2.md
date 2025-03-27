
# Bitlocker-2

Jacky has learnt about the importance of strong passwords and made sure to encrypt the BitLocker drive with a very long and complex password. We managed to capture the RAM while this drive was opened however. See if you can break through the encryption!Download the disk image [here](https://challenge-files.picoctf.net/c_verbal_sleep/b22e1ca13c0b82bb85afe5ae162f6ecbdf5b651e364e6a2b57c9ad44ae0b3bfd/bitlocker-2.dd) and the RAM dump [here](https://challenge-files.picoctf.net/c_verbal_sleep/b22e1ca13c0b82bb85afe5ae162f6ecbdf5b651e364e6a2b57c9ad44ae0b3bfd/memdump.mem.gz)

1. Try using a volatility plugin

## Solucion





```
BitLocker Recovery Key 2AE26DD3-87AE-4A0F-A380-9848FF6E866D.lnk
BitLocker Recovery Key 2AE26DD3-87AE-4A0F-A380-9848FF6E866D.lnk
BitLocker Drive Encryption.lnk

```


## Solucion 2

- Buscar la banera en el volcado de memoria
```
strings memdump.mem | grep picoCTF
picoCTF{B1tl0ck3r_dr1v3_d3crypt3d_9029ae5b}

```