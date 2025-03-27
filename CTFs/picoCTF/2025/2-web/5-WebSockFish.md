# WebSockFish

Can you win in a convincing manner against this chess bot? He won't go easy on you!You can find the challenge [here](http://verbal-sleep.picoctf.net:61344/).

1. Try understanding the code and how the websocket client is interacting with the server

## Solucion 1

- Mover una pieza envia eval ##
- Si modificamos el ## y ponemos algo como -5000 nos da la bandera

### Narativa

#### Intentar ganar por las buenas:
 - Un tablero de ajedrez y un pez parlante nos reciben cuando ingresamos al sitio web del desafío.
 - Lo obvio aquí es jugar e intentar ganar…
 - Pero es más difícil de lo que parece. Usar un motor de ajedrez en línea tampoco servirá de nada. Aunque ganes, no conseguirás la bandera.
 - Sigamos la pista y revisemos el código fuente del sitio web usando Ctrl+U.

#### Explorar el codigo fuente
- Primero vemos referencias a varias hojas de estilo CSS y scripts de JavaScript. Esta sección carga scripts para la apariencia del sitio web y el juego de ajedrez.
- Un poco más abajo encontramos un código que crea un WebSocket.

```javascript
<script>
      var ws_address = "ws://" + location.hostname + ":" + location.port + "/ws/";
      const ws = new WebSocket(ws_address);

      ws.onmessage = (event) => {
        const message = event.data;
        updateChat(message);
      };

      function sendMessage(message) {
        ws.send(message);
      }

      function updateChat(message) {
        const chatText = $("#chatText");
        chatText.text(message);
      }
    </script>

```
- Un WebSocket es un protocolo de comunicación que crea una conexión bidireccional persistente entre un cliente y un servidor a través de un único socket TCP. A diferencia de HTML, un WebSocket permite que el servidor y el cliente se intercambien datos en cualquier momento sin iniciar una nueva solicitud.

- Este script crea un WebSocket que escucha los mensajes del servidor y luego actualiza el cuadro de chat azul con el mensaje. También crea una función para enviar mensajes. Interesante.

- En la parte inferior, pasando un código que maneja el movimiento de las piezas, encontramos otra sección de interés.

```javascript
function makeBestMove() {
        var moves = "";
        var history = game.history({ verbose: true });
        for (var i = 0; i < history.length; i++) {
          var move = history[i];
          moves +=
            " " + move.from + move.to + (move.promotion ? move.promotion : "");
        }

        stockfish.postMessage("position fen " + STARTPOS + " moves" + moves);
        stockfish.postMessage("go depth " + DEPTH);
      }

      stockfish.onmessage = function (event) {
        var message;
        // console.log(event.data);
        if (event.data.startsWith("bestmove")) {
          var bestMove = event.data.split(" ")[1];
          var srcSq = bestMove.slice(0, 2);
          var dstSq = bestMove.slice(2, 4);
          var promotion = bestMove.slice(4);

          game.move({ from: srcSq, to: dstSq, promotion: promotion });
          board.position(game.fen());
        } else if (event.data.startsWith(`info depth ${DEPTH}`)) {
          var splitString = event.data.split(" ");
          if (event.data.includes("mate")) {
            message = "mate " + parseInt(splitString[9]);
          } else {
            message = "eval " + parseInt(splitString[9]);
          }
          sendMessage(message);
        }
      };
```

- Esta sección muestra la posición actual del tablero con Stockfish y gestiona su respuesta. Más importante aún, toma la evaluación del juego (quién gana y por cuánto) y la envía al servidor mediante la función sendMessage(). Cuando el servidor responde, el mensaje se envía al chat, como vimos anteriormente.

- Descubrimos que el sitio web usa WebSocket para enviar la evaluación del juego a un servidor, que responde con un mensaje en el chat. Veamos si podemos aprovecharlo.

### Explotación de WebSockets y la solución

- Intentemos enviar mensajes al servidor con las Herramientas de Desarrollo. Haga clic derecho y seleccione Inspeccionar o presione F12. Seleccione la pestaña de la consola.

- Sabemos que el mensaje debe tener el formato "eval/mate [entero]". Empecemos con algo sencillo.
```
sendMessage("eval 0")
I think this position is pretty equal

```
- ¡Enviar "eval 0" actualizó el chat! Ahora que sabemos que funciona, intentemos avisar al servidor de que Stockfish está a punto de perder.
- 
```
sendMessage("mate 1")
Haha I think you're gonna drown in 1 moves.
```
- Mmm, eso no se ve bien. Intentemos añadir un signo negativo.

```
 
sendMessage("mate -1")
You may eventually checkmate me, but you will never break my spirit as a fish!!

```
- Listo. Dado que el puesto se evalúa desde la perspectiva de Stockfish, cuando la evaluación es positiva, Stockfish gana.

- Probemos con numeros mas grandes:
```
sendMessage("eval -100000000000000000000000000000")

Huh???? How can I be losing this badly... I resign... here's your flag: picoCTF{c1i3nt_s1d3_w3b_s0ck3t5_a2a9bbe9}
```


- ¡Ajá! ¡Eso funcionó! Informarle al servidor que Stockfish perdía por -100,000 hizo que abandonara y nos diera la bandera.

- Ten en cuenta que Stockfish no ha abandonado el juego (aún puedes seguir jugando). También puedes usar ws.send() en lugar de sendMessage().

- Este desafío es bastante simple, pero también muy difícil si no conoces el método de ataque. Seguir la pista es crucial para resolverlo. ¡No lo pienses demasiado! Simplemente intenta cosas sencillas antes de pasar a ataques más complejos.
## Referencias
- https://medium.com/@acamq/picoctf2025-websockfish-7be8d26e847e