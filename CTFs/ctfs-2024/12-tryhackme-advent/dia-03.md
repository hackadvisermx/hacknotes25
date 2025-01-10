# Log analysis - Day 3: Even if I wanted to go, their vulnerabilities wouldn't allow it.



## Log Analysis & Introducing ELK

Log analysis is crucial to blue-teaming work, as you have likely discovered through this year's Advent of Cyber.

Analysing logs can quickly become overwhelming, especially if you have multiple devices and services. ELK, or Elasticsearch, Logstash, and Kibana, combines data analytics and processing tools to make analysing logs much more manageable. ELK forms a dedicated stack that can aggregate logs from multiple sources into one central place.

Explaining how ELK collates and processes these logs is out of the scope of today's task. However, if you wish to learn more, you can check out the [Investigating with ELK 101](https://tryhackme.com/r/room/investigatingwithelk101) room. For now, it's important to note that multiple processes behind the scenes achieve this.

The first part of today's task is to investigate the attack on Frosty Pines Resort's Hotel Management System to see what it looks like to a blue teamer. You will then test your web app skills by recreating the attack.

## Answer the questions below

### **BLUE**: Where was the web shell uploaded to?

**Answer format:** /directory/directory/directory/filename.php

/media/images/rooms/shell.php


### **BLUE**: What IP address accessed the web shell?

10.11.83.34

### **RED**: What is the contents of the flag.txt?
THM{Gl1tch_Was_H3r3}

