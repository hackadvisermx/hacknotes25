# Wordpres

- wpscan recon
```bash
wpscan --url http://10.10.237.142/wordpress -e u,ap,t
```


- wpscan brute 
```
wpscan --url http://10.10.10.120/wp/wordpress -P   -U admin -t 50
```

- reverse shell modificando un tema


```bash
http://internal.thm/wordpress/wp-content/themes/twentyseventeen/404.php
```