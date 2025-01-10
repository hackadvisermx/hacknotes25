
https://suricata.io/

Suricata is a high performance, open source network analysis and threat detection software used by most private and public organizations, and embedded by major vendors to protect their assets.

```
suricata -r suspicious.pcap -S suricata.rules -l logs
```

- El SID es un identificador unico para cada regla

- First rule:
	- First, please create a Suricata rule to catch DNS lookups for adv.epostoday.uk. Whenever there's a match, the alert message (msg) should read _Known bad DNS lookup, possible Dridex infection_

```
alert dns any any -> any any (msg:"Known bad DNS lookup, possible Dridex infection"; dns.query; content:"adv.epostoday.uk"; nocase; sid:1;)
```


- Second rule: 

Develop a Suricata rule that alerts whenever the infected IP address 192.185.57.242 communicates with internal systems over HTTP.
When there's a match, the message (msg) should read _Investigate suspicious connections, possible Dridex infection_



```
alert ip $EXTERNAL_NET any -> $HOME_NET any (msg:"Investigate suspicious connections, possible Dridex infection";)
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"Investigate suspicious connections, possible Dridex infection";)
alert ip $EXTERNAL_NET any -> $HOME_NET 80 (msg:"Investigate suspicious connections, possible Dridex infection";)
alert HTTP $EXTERNAL_NET any -> $HOME_NET any (msg:"Investigate suspicious connections, possible Dridex infection";)

alert http any any -> any any (msg:"Investigate suspicious connections, possible Dridex infection";)
```

- third rule: 
We heard that some naughty actors are using TLS certificates with a specific CN.
Develop a Suricata rule to match and alert on an SSL certificate for heardbellith.Icanwepeh.nagoya.
When your rule matches, the message (msg) should read _Investigate bad certificates, possible Dridex infection_

```
alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection";)
alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection";tls.cert_subject; content:"CN=heardbellith.Icanwepeh.nagoya";)
alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection";tls.subject; content:"CN=heardbellith.Icanwepeh.nagoya";)
alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection";tls.issuerdn:!"CN=Gheardbellith.Icanwepeh.nagoya";)
alert tls $EXTERNAL_NET any -> $HOME_NET any (msg:"Investigate bad certificates, possible Dridex infection";)

 
alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection";tls.cert_subject;content:"CN=heardbellith.Icanwepeh.nagoya";sid:3;)
```

- fourth
Let's watch for one line from the JavaScript: let byteCharacters = atob
Oh, and that string might be GZip compressed - I hope that's OK!
Just in case they try this again, please alert on that HTTP data with message _Suspicious JavaScript function, possible Dridex infection_

```
alert http any any -> any any (msg:"Suspicious JavaScript function, possible Dridex infection";http.accept_enc; content:"gzip"; sid:4;)


alert http any any -> any any (msg:"Suspicious JavaScript function, possible Dridex infection";http.response_body;content:"let byteCharacters = atob";sid:4;)


```



- Todas las reglas:
-
alert dns any any -> any any (msg:"Known bad DNS lookup, possible Dridex infection"; dns.query; content:"adv.epostoday.uk"; nocase; sid:1;)
alert http any any -> any any (msg:"Investigate suspicious connections, possible Dridex infection";)
alert tls any any -> any any (msg:"Investigate bad certificates, possible Dridex infection";tls.cert_subject;content:"CN=heardbellith.Icanwepeh.nagoya";sid:3;)

## Referencias
- https://suricata.readthedocs.io/en/suricata-6.0.0/rules/dns-keywords.html
