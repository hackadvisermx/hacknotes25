#  Insp3ct0r
Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/41511/` ([link](https://jupiter.challenges.picoctf.org/problem/41511/)) or http://jupiter.challenges.picoctf.org:41511

Hints:
How do you inspect web code on a browser?
There's 3 parts

## Solucion
https://jupiter.challenges.picoctf.org/problem/41511/

1.  Ver codigo fuente (ctrl+u)
```html
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

2. Seguir la liga css en el codgo fuente (esta al top)
```html
<head>
    <title>My First Website :)</title>
    <link href="[https://fonts.googleapis.com/css?family=Open+Sans|Roboto](view-source:https://fonts.googleapis.com/css?family=Open+Sans|Roboto)" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="[mycss.css](view-source:https://jupiter.challenges.picoctf.org/problem/41511/mycss.css)">
    <script type="application/javascript" src="[myjs.js](view-source:https://jupiter.challenges.picoctf.org/problem/41511/myjs.js)"></script>
  </head>
```
``/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */``

3. seguir la liga al js
```javascript
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */
```

- Armamos 


## Notas adicionales
- abrir ligas en una nueva pestaña ( ctrl + click)
- ver código fuente de una pagina ( ctrl + u )
html, css, javascript
- barra de desarrollador de google ( ctrl + shift + i )
. partes que la integran (inspector, console, debugger, network, style editor, ....)
. moverla por la pantalla 
