Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam. Can you help us identify whose mail server the email actually originated from? Download the email file [here](https://artifacts.picoctf.net/c/363/email-export.eml). Flag: picoCTF{FirstnameLastname}

Hint: whois can be helpful on IP addresses also, not only domain names

## Solucion

- Podemos usar una pagina para leer encabezados > https://mxtoolbox.com/Public/Tools/EmailHeaders.aspx
- Se trata de indetificar una dirección IP de acuerdo a la pista, y hacer un whois sobre ella para sacar un nombre

```
whois 173.249.33.206
 

person:         Wilhelm Zwalina
 
```

## Bandera

`picoCTF{WilhelmZwalina}