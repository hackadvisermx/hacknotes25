# dont-use-client-side
Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/37821/` ([link](https://jupiter.challenges.picoctf.org/problem/37821/)) or http://jupiter.challenges.picoctf.org:37821
- Hint: Never trust the client

## Solución
#### Primero explicar
- del lado del cliente y del lado del servidor
- depurar: https://developer.mozilla.org/es/docs/Tools/Debugger
	- The Firefox JavaScript Debugger
. podemos deputar algo de prueba para probar

#### Examinamos el código fuente
```javascript
<script type="text/javascript">
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'a3c8') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_1') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '9}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }
</script>
```
- Aquí claro vemos como es que el password se valida, solo hay que armar las piezas en orden

## Referencas
- client-side vs server-side : https://www.educative.io/answers/client-side-vs-server-side
- mozilla debugger:  https://developer.mozilla.org/es/docs/Tools/Debugger
