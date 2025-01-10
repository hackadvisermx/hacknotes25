
# FakePGPX10

The PGP file header is weird, can you decode the message?

# Solucion

- Lo mismo que el anterior

```bash
─(kali㉿kali)-[~/…/ctfs2022/metared-5-ecuador/misc/fakepgp]
└─$ cat Fakepgp.txt 
-----BEGIN PGP MESSAGE-----
Charset: ISO-8859-1
Version: GnuPG v1.2.5 (MingW32)
Comment: Using GnuPG with Thunderbird - http://enigmail.mozdev.org - 10 TIMES ENCODE


Vm0wd2QyVkhVWGhVYmxKV1YwZDRXRmxVUm5kVlJscHpXa2M1VjFKdGVGWlZNbmhQWVd4S2MxTnNXbGRTTTFKUVdWY3hTMUl4WkhWalJtUk9ZV3RhU1ZadGNFdFRNVWw0Vkc1T1lWSnRVbGhVVkVwdlpWWmFkR05GZEZSTlZXdzFWa2QwWVZkSFNrZGpTRUpYWVRGYWFGVXhXbUZqTVZaeVpFWlNUbFpYZHpCV01uUnZWakpHYzFOdVVsWmlSMmhXVm10V1lWUkdVblJsUjBaclVqRktTVlZ0ZUhkV01rcEpVV3hzVjJGcmEzaFZla1pUWXpGa2RWVnNXbWxXUjNoWFZtMHhOR1F3TUhoVmJHaHNVakJhV1ZWc1VrZFdiRnBZWlVoa1YwMXJWalpWVm1oclZqRmFObEpZWkZoV2JWSklXWHBHVDJSV1VuTmhSMnhYVWpOb1dGWnRNWGRVTWtsNFZXdGtXR0pzU25OVmFrNVRZMnhXY1ZKdFJsTk5WbXcxV2xWV1QxWXdNWEpXYWs1YVRVWndWRlpxUm1GV01rNUhWRzFHVTFKV2NFVldiR1EwVVRGYVZrMVZWazVTUkVFNQ==
-----END PGP MESSAGE-----

```

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-5-ecuador/misc/fakepgp]
└─$ nano hackme0.txt
                                                                                                                    
┌──(kali㉿kali)-[~/…/ctfs2022/metared-5-ecuador/misc/fakepgp]
└─$ for i in {1..10}; do base64 -d hackme$((i-1)).txt > hackme$i.txt; done
                                                                                                                    
┌──(kali㉿kali)-[~/…/ctfs2022/metared-5-ecuador/misc/fakepgp]
└─$ cat hackme10.txt 
flag{DONTOVERTHINKTHETHINGS}   
```