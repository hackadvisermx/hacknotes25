



## Naughty IP

Use [the artifacts](https://storage.googleapis.com/hhc22_player_assets/boriaArtifacts.zip) from Alabaster Snowball to analyze this attack on the Boria mines. Most of the traffic to this site is nice, but one IP address is being naughty! Which is it? Visit Sparkle Redberry in the Web Ring for hints.

18.222.86.32


## Credential Mining

The first attack is a [brute force](https://owasp.org/www-community/attacks/Brute_force_attack) login. What's the first username tried?

`http.request.method==POST`
alice

## 404 FTW
```
cat weberror.log | grep '18.222.86.32' | less

18.222.86.32 - - [05/Oct/2022 16:48:17] "GET /proc HTTP/1.1" 200 -
18.222.86.32 - - [05/Oct/2022 16:48:27] "POST /proc HTTP/1.1" 200 -
```

## IMDS, XXE, and Other Abbreviations

strings victim.pcap | grep -i 'XML' -A 30 -B 30

http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance/


