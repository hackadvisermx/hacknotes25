
#  Cookie Monster Secret Recipe


Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?You can access the Cookie Monster [here](http://verbal-sleep.picoctf.net:60118/) and good luck

1. Sometimes, the most important information is hidden in plain sight. Have you checked all parts of the webpage?
2. Cookies aren't just for eating - they're also used in web technologies!
3. Web browsers often have tools that can help you inspect various aspects of a webpage, including things you can't see directly.


```
# Access Denied

Cookie Monster says: 'Me no need password. Me just need cookies!'

Hint: Have you checked your cookies lately?

[Go back](http://verbal-sleep.picoctf.net:60118/)
```

```
POST /login.php HTTP/1.1
Host: verbal-sleep.picoctf.net:60118
Content-Length: 29
Cache-Control: max-age=0
Origin: http://verbal-sleep.picoctf.net:60118
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://verbal-sleep.picoctf.net:60118/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Cookie: secret_recipe=cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0E5NjRBMTM0fQ%3D%3D
Connection: keep-alive

username=admin&password=admin
```

- decodificar la cookie
```
Cookie: secret_recipe=cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0E5NjRBMTM0fQ%3D%3D

picoCTF{c00k1e_m0nster_l0ves_c00kies_A964A134}
```