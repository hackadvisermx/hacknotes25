# flag leak







- Instalar GEF
https://gef.readthedocs.io/en/master/

- checar la seguridad del binario
```bash
checksec
```



```bash
bash -c "$(curl -fsSL http://gef.blah.cat/sh)"
```

- algunos comandos de contexto: https://gef.readthedocs.io/en/master/commands/context/


```bash
memory watch $sp 0x40 byte
memory unwatch
```

- configurar como vemos una seccion ejemplo stack:
```

context stack

```