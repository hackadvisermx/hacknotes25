# Piece It Together

## Objetivo
My friend dared me to find the secret password to their website, but their code is so messy! It's impossible to see what's what! Can you help me? [mhsctf-pieceittogether.0xmmalik.repl.co](https://mhsctf-pieceittogether.0xmmalik.repl.co) (you may need to wait for the site to wake up)


## Solucion
- Tomar del codigo solo el html
- Ir a cyberfcheff y decodificar (from HTML Entity /from HTML Entity )

```javascript
</head>

<body>
  <div class="w3-content">

    <h2>Login</h2>
    <script>

var _0xa8fe=["\x34\x77","\x64\x7D","\x67\x7B","\x6A","\x7D","\x31\x67","\x77\x30","\x72","\x61\x6C","\x73","\x68\x37","\x61\x67\x7B","\x66\x6C","\x6D\x33\x74","\x76\x61\x6C\x75\x65","\x70\x77\x64","\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64","\x59\x65\x70\x2C\x20\x74\x68\x61\x74\x27\x73\x20\x74\x68\x65\x20\x66\x6C\x61\x67\x21","\x53\x6F\x72\x72\x79\x2C\x20\x74\x68\x61\x74\x27\x73\x20\x6E\x6F\x74\x20\x74\x68\x65\x20\x66\x6C\x61\x67\x21"];function checkpwd(){if(document[_0xa8fe[16]](_0xa8fe[15])[_0xa8fe[14]]== 
																																																																																																																							  (_0xa8fe[12]+ _0xa8fe[11]+ _0xa8fe[3]+ _0xa8fe[5]+ _0xa8fe[9]+ _0xa8fe[0]+ _0xa8fe[4])
																																																																																																																							  ){alert(_0xa8fe[17])}else {alert(_0xa8fe[18])}}

    </script>

    <label for="pwd">Password:</label>
    <input type="text" id="pwd" name="pwd">
    <button onclick="checkpwd()">Submit</button>

  </div>

</body>
```

## Flag

## Referencias
- https://gchq.github.io/CyberChef
- 