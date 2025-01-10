# Baby RSA Quiz
Author: @Gary#4657  
  
A nictn e RSA warmup for you crypto nerds. If you are new to RSA, this challenge is for you :)  
  
**Press the `Start` button on the top-right to begin this challenge.**

**Connect with:**  

nc challenge.nahamcon.com 30380

## Solucion
```
┌──(kali㉿kali)-[~/…/ctfs2022/nahamconctf/crypto/xorrox]
└─$ nc challenge.nahamcon.com 30380

Welcome to the Baby RSA Quiz! 

Choose Option 0 if you're asking yourself "what in the world is RSA?" or maybe want to run through the basics.
Choose Option 1 if you're comfortable with RSA, feel free to skip to the quiz
Choose Option 2 if Rivest, Shamir, or Adleman hurt your feelings, feel free to exit the program 


/------------------------\
| Baby RSA MENU:         |
| (0) Teach me some RSA! | 
| (1) Skip to quiz       |
| (2) Quit               |
\------------------------/

Choice: 1

___________________________________________________________________________________

I see you are ready to take my quiz! This quiz is comprised of three parts with 
each part giving you a poor implementation of RSA. If you are unfamiliar with any 
of these values given, it might be worthwhile to check out option 0 in the main 
menu.

 ---------
| Part 1: |
 ---------
n = 136435867896173
e = 65537
ct = ct,

What is the plaintext (in integer form)? 


>> factorizar
>> -   136 435867 896173 = 9 517139 × 14 335807

Number of divisors: 4

Sum of divisors: 136 435891 749120

Euler's totient: 136 435844 043228


R




```


```
Nice job on the first part! Those numbers weren't really as big as we thought. 

 ---------
| Part 2: |
 ---------
n = 16297901560355814157879251441813580353618104143874500955196235279539209335405689086548831416542651529301298254506633936393705394898591507022718671563360898649614243564991075140140076695679190044521345189824516990432122723141337500554469072627093616813792490493387203856175986354511390313657094591092434592041184777001184145102100392186304181749885131565356779699553824787014716689516388425452159392256307323805588057062574520340690422944471709022217783836517903872439753985223094360528941579708142735516789669943165344709406315471859047417000187346031241101347250157641097913200481113354085315637206038554450434237269
e = 3
ct = 26480272848384180570411447917437668635135597564435407928130220812155801611065536704781892656033726277516148813916446180796750368332515779970289682282804676030149428215146347671350240386440440048832713595112882403831539777582778645411270433913301224819057222081543727263602678819745693540865806160910293144052079393615890645460901858988883318691997438568705602949652125
```