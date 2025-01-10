
# Task 19  [Day 13] Intrusion detection To the Pots, Through the Walls





## Configuring Firewalls to Block Traffic
```
sudo ufw status
Status: inactive


sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)


udo ufw default deny incoming
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)

sudo ufw  allow 22/tcp
Rules updated
Rules updated (v6)

sudo ufw deny from 192.168.100.25
Rules updated

sudo ufw deny in on eth0 from 192.168.100.26
Rules updated

sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup


sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                  
Anywhere                   DENY IN     192.168.100.25            
Anywhere on eth0           DENY IN     192.168.100.26            
22/tcp (v6)                ALLOW IN    Anywhere (v6)       


sudo ufw reset
Resetting all rules to installed defaults. This may disrupt existing ssh
connections. Proceed with operation (y|n)? y
Backing up 'user.rules' to '/etc/ufw/user.rules.20231213_195810'
Backing up 'before.rules' to '/etc/ufw/before.rules.20231213_195810'
Backing up 'after.rules' to '/etc/ufw/after.rules.20231213_195810'
Backing up 'user6.rules' to '/etc/ufw/user6.rules.20231213_195810'
Backing up 'before6.rules' to '/etc/ufw/before6.rules.20231213_195810'
Backing up 'after6.rules' to '/etc/ufw/after6.rules.20231213_195810'


sudo ufw status verbose
Status: inactive


```


## Honeypot

```
sudo ./pentbox.rb 

 PenTBox 1.8 
         __
        U00U|.'@@@@@@`.
        |__|(@@@@@@@@@@)
             (@@@@@@@@)
             `YY~~~~YY'
              ||    ||

--------- Menu          ruby2.7.0 @ x86_64-linux-gnu

1- Cryptography tools

2- Network tools

3- Web

4- Ip grabber

5- Geolocation ip

6- Mass attack

7- License and contact

8- Exit

   -> 

```

```
 -> 2 

1- Net DoS Tester
2- TCP port scanner
3- Honeypot
4- Fuzzer
5- DNS and host gathering
6- MAC address geolocation (samy.pl)

0- Back

   -> 
-> 3

// Honeypot //

You must run PenTBox with root privileges.

 Select option.

1- Fast Auto Configuration
2- Manual Configuration [Advanced Users, more options]

-> 2

 Insert port to Open.

   -> 8080

 Insert false message to show.

   -> Santa has gone for the Holidays. Tough luck.

 Save a log with intrusions?

 (y/n)   -> y

 Log file name? (incremental)

Default: */pentbox/other/log_honeypot.txt

   -> 

 Activate beep() sound when intrusion?

 (y/n)   -> y

  HONEYPOT ACTIVATED ON PORT 8080 (2023-12-13 20:07:28 +0000)

```

- vamos al navegador y probamos entrar al puerto 8080 y obtenemos eso
```
  INTRUSION ATTEMPT DETECTED! from 10.2.6.197:37386 (2023-12-13 20:08:21 +0000)
 -----------------------------
GET / HTTP/1.1
Host: 10.10.234.155:8080
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```


## Respuestas

 Which security model is being used to analyse the breach and defence strategies? 
 diamond model
 
Which defence capability is used to actively search for signs of malicious activity?
Threat hunting


What are our main two infrastructure focuses? (Answer format: answer1 and answer2)
firewall and honeypot


Which firewall command is used to block traffic?
deny


There is a flag in one of the stories. Can you find it?
THM{P0T$_W@11S_4_S@N7@} 

