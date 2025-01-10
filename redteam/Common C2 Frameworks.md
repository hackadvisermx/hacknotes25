## Free

### Metasploit

The Metasploit Framework, developed and maintained by Rapid7, is one of the most popular Exploitation and Post Exploitation frameworks (C2) that is publicly available and is installed on most penetration testing distributions.

### Armitage

Armitage is an extension of the Metasploit Framework - it adds a Graphical user interface and is written in Java, and is incredibly similar to Cobalt Strike. This is because they were both developed by Raphael Mudge. Armitage offers an easy way to enumerate and visualize all of your targets. Aside from looking a lot like Cobalt Strike, it even offers some unique features. One of the most popular can be found in the “Attacks” menu; This feature is known as the Hail Mary attack, which attempts to run all exploits for the services running on a specific workstation. Armitage really is “Fast and Easy Hacking”.


### Powershell Empire/Starkiller

Powershell Empire and Starkiller is another incredibly popular C2 originally created by Harmjoy, Sixdub, and Enigma0x3 from Veris Group. Currently, the project has been discontinued and has been picked up by the BC Security team (Cx01N, Hubbl3, and _Vinnybod). Empire features agents written in various languages compatible with multiple platforms, making it an incredibly versatile C2.v

### Covenant

Covenant by Ryan Cobb is the last free C2 Framework we will be covering - By far, it is one of the most unique C2 Frameworks being written in C#. Unlike Metasploit/Armitage, It’s primarily used for post-exploitation and lateral movement with HTTP, HTTPS, and SMB listeners with highly customizable agents.

### Sliver

Sliver by Bishop Fox is an advanced, highly customizable multi-user, CLI-based C2 framework. Sliver is written in Go, which makes reverse engineering the C2 "implants" incredibly difficult. It supports various protocols for C2 communications like WireGuard, mTLS, HTTP(S), DNS, and much more. Additionally, it supports BOF files for additional functionality, DNS Canary Domains for masking C2 communications, automatic Let's Encrypt certificate generation for HTTPS beacons, and much more.  


## Paid

### Cobalt Strike

Cobalt Strike by Help Systems (Formerly created by Raphael Mudge) is arguably one of the most famous Command and Control frameworks next to Metasploit. Much like Artimage, it is written in Java and designed to be as flexible as possible

### Brute Ratel

Brute Ratel by Chetan Nayak or Paranoid Ninja is a Command and Control framework marketed as a “Customizable Command and Control Center” or “C4” framework that provides a true adversary simulation-like experience with being a unique C2 framework. For more information about the Framework, the author has provided a Video Training Page that demonstrates many of the capabilities within the framework.

## Other C2 Frameworks

For a more comprehensive list of C2 Frameworks and their capabilities, check out the “C2 Matrix”, a project maintained by Jorge Orchilles and Bryson Bort. It has a far more comprehensive list of almost all C2 Frameworks that are currently available. We highly recommend that after this room, you go check it out and explore some of the other C2 Frameworks that were not discussed in this room. 




## Referencias 
- tryhackme
	- https://tryhackme.com/room/rppsempire
- otros
	- https://bc-security.gitbook.io/empire-wiki/
	- https://github.com/BC-SECURITY/Starkiller
	- https://howto.thec2matrix.com/