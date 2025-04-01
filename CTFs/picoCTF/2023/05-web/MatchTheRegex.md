# MatchTheRegex

How about trying to match a regular expression The website is running [here](http://saturn.picoctf.net:58599/).

## Solucion

### Intro

- Introducimos un par de palabras cortas para probar la interfaz

### Revisamos código fuente de la página
- Al revisar el codigo fuente nos encontramos una probable regex con la que se valida lo que tecleamos
```
<script>
	function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}
</script>
```

###  Qué son las expresiones regulares ?

Las expresiones regulares son patrones de búsqueda de texto que se usan en lenguajes de programación y en el cómputo teórico. También se les conoce como regex o regexp. 
. Explicarlo en el código

### Sitio regexr.com 

- Ir al sitio> https://regexr.com/ y construirla
- explicar la expresión regular que ya aparece ahí
- en la parte izquierda explicar el Cheatsheet

### Obtener la bandera

- Poner la regex del código y ver como logramos un 

```
^p.....F!?    o   picoCTF{.*?}

p12345F
```

- probar la solución en la pagina del reto
#### Otras expresiones regulares

 - Probar la expresión regular de un telefono, que chatgpt la genere ,

```
Crea una expresion regular para que coincida con las siguientes entradas: 
123-123-999 
(123)-999-999 
123.999.123
```

 -  y la probamos en  regexr.com 
```
\(?\d{3}\)?[-.]\d{3}[-.]\d{3}


123-123-999 
(123)-999-999 
123.999.123
```

- terminar con la broma
https://www.reddit.com/r/ProgrammerHumor/comments/c9e0n4/regex_is_so_easy/




## Bandera

picoCTF{succ3ssfully_matchtheregex_f89ea585}

## Referencias

https://www.youtube.com/watch?v=V4GBvLuByd8
https://www.reddit.com/r/ProgrammerHumor/comments/c9e0n4/regex_is_so_easy/