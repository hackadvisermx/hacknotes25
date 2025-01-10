# where are the robots

Can you find the robots? `https://jupiter.challenges.picoctf.org/problem/36474/` ([link](https://jupiter.challenges.picoctf.org/problem/36474/)) or http://jupiter.challenges.picoctf.org:36474

- Hint: What part of the website could tell you where the creator doesn't want you to look?


## Solución
https://jupiter.challenges.picoctf.org/problem/36474/
https://jupiter.challenges.picoctf.org/problem/36474/robots.txt

- Existe un estandar de esclusión: google: robots.txt
```
User-agent: *
Disallow: /477ce.html
```
https://jupiter.challenges.picoctf.org/problem/36474/477ce.html
```
Guess you found the robots  
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
```


## Notas adicionales
- que es el archivo robots.txt

## Referencias

- https://es.wikipedia.org/wiki/Robot
- https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjZuoeBvpT6AhVoFNQBHaNOD34YABAAGgJvYQ&ohost=www.google.com&cid=CAESbOD2SMcDmYzEnk4lXODxA9BwVhVWCgP_xXuOVH52bPISDIhg5pMGK-ypRqx1nsw_LAbKsBrLSj84wcA7EKMA78tHmWpE38lutV3tDSh_nJn10ZBodKN-MPhrAzPF553G4A5Q9zeqkrgLGgDtKQ&sig=AOD64_2OA1rpFApKkYk2fybCtTIeyO9KMg&q&adurl&ved=2ahUKEwjd6f2AvpT6AhVZL0QIHdJADtAQ0Qx6BAgEEAE