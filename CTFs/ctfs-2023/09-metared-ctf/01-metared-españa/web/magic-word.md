
# Magic word

## Solve

```
cat server.js
'use strict';
const express = require('express');

const PORT = 8080;
const HOST = '0.0.0.0';
const FLAG = process.env.CHALLENGE_FLAG || "flag{empty_flag}"

const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send(`

  <h1>Welcome to the first Spanish Metared stage!</h1>
  <h2>Respect the rules, and have fun!</h2>
  <iframe src="https://giphy.com/embed/4Zo41lhzKt6iZ8xff9" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
  `);
});

app.get('/health', (req, res) => {
  res.status(200).send('Ok');
});

app.get('/givemeflag', (req, res) => {
  res.status(200).send('Are you sure you want to GET the flag?');
});

app.post('/givemeflag', (req, res) => {
  const {user, magicword} = req.body;
  console.log(`Recv req with user ${user} and magicword ${magicword}`);
  if(!user || user !== "admin"){
	  res.status(401).send("<p>I dont trust you</p>");
  } else if(!magicword || btoa(magicword) !== "cHJldHR5IHBsZWFzZSA6Mw==") {
	  res.status(403).send("<p>I do not like your attitude</p>");
  } else {
	  res.status(200).send(`<p>${FLAG}</p>`);
  }
});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});
```



```
curl -X POST http://chall-server-1.numa.host:8081/givemeflag  -d '{"user":"admin","magicword":"pretty please :3"}' -H "Content-Type: application/json"
<p>flag{Y0u_4r3_w3lc0m3_h4v3_fun}</p>%
```