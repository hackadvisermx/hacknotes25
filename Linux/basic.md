# Basic

- Información de un archivo

```bash
ls -lai /etc/sudores
stat /etc/sudoers
```

- Buscar archivo

```bash
find / -name \*\.conf -newermt 2020-03-03 -size +25k -size -28k -exec ls -la {} \; 2>/dev/null
```



- [Generador de prompt PS1](https://bashrcgenerator.com/)
