# Scavenger Hunt
There is some interesting information hidden around this site [http://mercury.picoctf.net:27278/](http://mercury.picoctf.net:27278/). Can you find it?

Hint: You should have enough hints to find the files, don't run a brute forcer.

## Solución
- Una pagina HTML inocente en apariencia
- Vamos al codigo fuente
	- En html : <!-- Here's the first part of the flag: picoCTF{t -->
	- En css: `/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */`
	- En js: y manda al robots

```
	User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```
- siguiente parte
`http://mercury.picoctf.net:27278/.htaccess`

```html
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

-  última parte
```
Congrats! You completed the scavenger hunt. Part 5: _a69684fd}
```


picoCTF{th4ts_4_l0t_0f_pl4c_a69684fd}


## Ligas
- .htaccess Apache Server : https://httpd.apache.org/docs/2.4/en/howto/htaccess.html
- .DS_Store mac file: https://en.wikipedia.org/wiki/.DS_Store






## Referencias
picoCTF{th4ts_4_l0t_0f_pl4c
