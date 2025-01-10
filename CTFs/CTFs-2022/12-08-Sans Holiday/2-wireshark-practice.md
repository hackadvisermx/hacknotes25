

1.  `HTTP`
2.  `app.php`
3.  `687`
4. What is the ip of Apache Server : 192.185.57.242
5. What file is saved to the infected host? :  Ref_Sept24-2020.zip
6. Attackers used bad TLS certificates in this traffic. Which countries weere they registred to? : Israel, South Sudan
8. Ys

- Usar filetro : `ssl.handshake.type == 11`
-



- Extraer el certificado del pcap
```
> How to obtain the SSL certificate from a Wireshark packet capture:
> 
> 1.  From the Wireshark menu choose Edit > Preferences and ensure that “Allow subdissector to reassemble TCP streams” is ticked in the TCP protocol preferences
> 2.  Find “Certificate, Server Hello” (or Client Hello if it is a client-side certificate that you are interested in obtaining.
> 3.  In the packet detail pane, expand the Secure Sockets Layer protocol
> 4.  Expand the “TLSv1 Record Layer: Handshake Protocol: Certificate” field
> 5.  Expand the “Handshake Protocol: Certificate” field
> 6.  Expand the list of certificates. There may be one or more certificates depending upon whether a chain of trust is present. The first certificate is the server certificate, the second is the signing Certificate Authority, the third the CA that trusted/signed that Certificate Authority and so on.
> 7.  Right-click on the on the certificate that you wish to obtain then choose “Export selected packet bytes…” and name the file with a .der extension.
```




- Extraer datos del certificado
```
openssl x509 -in cert.der -inform der -text

Issuer: C = IL, ST = Anourd Thiolaved Thersile5 Fteda8, L = Tel Aviv, O = Wemadd Hixchac GmBH, OU = moasn@emanc, CN = heardbellith.Icanwepeh.nagoya

```
- Los paises:   Israel, São Tomé and Príncipe

IL SS

- Observando 

Israel, South Sudan

## Referencias 
- https://cheatography.com/mbwalker/cheat-sheets/tshark-wireshark-command-line/
- https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/
- https://security.stackexchange.com/questions/123851/how-can-i-extract-the-certificate-from-this-pcap-file
- https://www.ssl.com/country-codes/
