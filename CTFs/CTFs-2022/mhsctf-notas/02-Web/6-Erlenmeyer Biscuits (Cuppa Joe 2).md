# Erlenmeyer Biscuits (Cuppa Joe 2)

## Objetivo
You remember that coffee shop that just opened up, Cuppa Joe? Well there's now a competitor shop that's opening up across from them! It's called Erlenmeyer Biscuits, and here is their website. I really don't want Cuppa Joe to go out of business, so do you think you could dig up some dirt on Erlenmeyer Biscuits to stop them from opening? mhsctf-erlenmeyer-biscuits.0xmmalik.repl.co (you may need to wait for the site to wake up)

## Solucion
      
```
curl https://mhsctf-erlenmeyer-biscuits.0xmmalik.repl.co/ -I    
HTTP/2 200 
content-type: text/html; charset=utf-8
date: Sat, 19 Feb 2022 01:29:49 GMT
expect-ct: max-age=2592000, report-uri="https://sentry.repl.it/api/10/security/?sentry_key=615192fd532445bfbbbe966cd7131791"
replit-cluster: hacker
server: Werkzeug/1.0.1 Python/3.8.12
set-cookie: session=eyJmbGFnIjoiZmxhZ3tmbDQ1a19zMzU1MTBuX2MwMGsxM3NfNHIzXzFuNTNjdXJlfSJ9.YFLMhA.xt_8C0BrPHl2HDm9yIRffDhK7Ow; Path=/
strict-transport-security: max-age=6640751; includeSubDomains
content-length: 668

```

- La cosa va por la cookie
```bash
echo 'eyJmbGFnIjoiZmxhZ3tmbDQ1a19zMzU1MTBuX2MwMGsxM3NfNHIzXzFuNTNjdXJlfSJ9.YFLMhA.xt_8C0BrPHl2HDm9yIRffDhK7Ow' | base64 -d
{"flag":"flag{fl45k_s35510n_c00k13s_4r3_1n53cure}"}base64: invalid input
```


## Flag

## Referencias