## Default Passwords

Before performing password attacks, it is worth trying a couple of default passwords against the targeted service. Manufacturers set default passwords with products and equipment such as switches, firewalls, routers. There are scenarios where customers don't change the default password, which makes the system vulnerable. Thus, it is a good practice to try out admin:admin, admin:123456, etc. If we know the target device, we can look up the default passwords and try them out. For example, suppose the target server is a Tomcat, a lightweight, open-source Java application server. In that case, there are a couple of possible default passwords we can try: admin:admin or tomcat:admin.:

- https://cirt.net/passwords
- https://default-password.info/
- https://datarecovery.com/rd/default-passwords/

## Weak Passwords  
Professionals collect and generate weak password lists over time and often combine them into one large wordlist. Lists are generated based on their experience and what they see in pentesting engagements. These lists may also contain leaked passwords that have been published publically. Here are some of the common weak passwords lists :

-   [https://wiki.skullsecurity.org/index.php?title=Passwords](https://wiki.skullsecurity.org/index.php?title=Passwords)[](https://wiki.skullsecurity.org/index.php?title=Passwords) - This includes the most well-known collections of passwords.
-   [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords) - A huge collection of all kinds of lists, not only for password cracking.

## Leaked Passwords

Sensitive data such as passwords or hashes may be publicly disclosed or sold as a result of a breach. These public or privately available leaks are often referred to as 'dumps'. Depending on the contents of the dump, an attacker may need to extract the passwords out of the data. In some cases, the dump may only contain hashes of the passwords and require cracking in order to gain the plain-text passwords. The following are some of the common password lists that have weak and leaked passwords, including webhost, elitehacker,hak5, Hotmail, PhpBB companies' leaks:  

-   [SecLists/Passwords/Leaked-Databases](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Leaked-Databases)

## Combined wordlists  

Let's say that we have more than one wordlist. Then, we can combine these wordlists into one large file. This can be done as follows using cat:
 `cat file1.txt file2.txt file3.txt > combined_list.txt`
  
To clean up the generated combined list to remove duplicated words, we can use sort and uniq as follows:
 `sort combined_list.txt | uniq -u > cleaned_combined_list.txt`


## Customized Wordlists  

Customizing password lists is one of the best ways to increase the chances of finding valid credentials. We can create custom password lists from the target website. Often, a company's website contains valuable information about the company and its employees, including emails and employee names. In addition, the website may contain keywords specific to what the company offers, including product and service names, which may be used in an employee's password!   

Tools such as `Cewl` can be used to effectively crawl a website and extract strings or keywords. `Cewl` is a powerful tool to generate a wordlist specific to a given company or target. Consider the following example below:

 `cewl -w list.txt -d 5 -m 5 http://thm.labs`
    
`-w` will write the contents to a file. In this case, list.txt.
`-m 5` gathers strings (words) that are 5 characters or more
`-d 5 `is the depth level of web crawling/spidering (default 2)
`- http://thm.labs `is the URL that will be used

As a result, we should now have a decently sized wordlist based on relevant words for the specific enterprise, like names, locations, and a lot of their business lingo. Similarly, the wordlist that was created could be used to fuzz for usernames. 

Apply what we discuss using cewl against `https://clinic.thmredteam.com/` to parse all words and generate a wordlist with a minimum length of 8. Note that we will be using this wordlist later on with another task!

### Username Wordlists

Gathering employees' names in the enumeration stage is essential. We can generate username lists from the target's website. For the following example, we'll assume we have a `{first name} {last name} `(ex: John Smith) and a method of generating usernames.

-   **{first name}:** john
-   **{last name}:** smith
-   **{first name}{last name}:  `johnsmith`** 
-   **{last name}{first name}:  `smithjohn`**  
-   first letter of the **{first name}{last name}: `jsmith`** 
-   first letter of the **{last name}{first name}: `sjohn`**  
-   first letter of the **{first name}.{last name}: `j.smith`** 
-   first letter of the **{first name}-{last name}: `j-smith`** 
-   and so on

Thankfully, there is a tool `username_generator` that could help create a list with most of the possible combinations if we have a first name and last name.

```shell-session
git clone https://github.com/therodri2/username_generator.git
cd username_generator
python3 username_generator.py -h
echo "John Smith" > users.lst
python3 username_generator.py -w users.lst
usage: username_generator.py [-h] -w wordlist [-u]
```

### Keyspace Technique

Another way of preparing a wordlist is by using the key-space technique. In this technique, we specify a range of characters, numbers, and symbols in our wordlist. `crunch` is one of many powerful tools for creating an offline wordlist. With `crunch`, we can specify numerous options, including min, max, and options as follows:

`crunch 2 2 01234abcd -o crunch.txt`

It's worth noting that `crunch` can generate a very large text file depending on the word length and combination options you specify. The following command creates a list with an 8 character minimum and maximum length containing numbers 0-9, a-f lowercase letters, and A-F uppercase letters:

`crunch 8 8 0123456789abcdefABCDEF -o crunch.txt `

the file generated is 459 GB and contains 54875873536 words

`crunch` also lets us specify a character set using the -t option to combine words of our choice. Here are some of the other options that could be used to help create different combinations of your choice:  

`@` - lower case alpha characters
`,` - upper case alpha characters
`%` - numeric characters
`^` - special characters including space

For example, if part of the password is known to us, and we know it starts with pass and follows two numbers, we can use the` %` symbol from above to match the numbers. Here we generate a wordlist that contains pass followed by 2 numbers:

```shell-session
crunch 6 6 -t pass%%
Crunch will now generate the following amount of data: 700 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 100
pass00
pass01
pass02
pass03
```

### CUPP - Common User Passwords Profiler

`CUPP` is an automatic and interactive tool written in Python for creating custom wordlists. For instance, if you know some details about a specific target, such as their birthdate, pet name, company name, etc., this could be a helpful tool to generate passwords based on this known information. `CUPP` will take the information supplied and generate a custom wordlist based on what's provided. There's also support for a `1337/leet mode`, which substitutes the letters a, i,e, t, o, s, g, z  with numbers. For example, replace a  with 4  or i with 1. For more information about the tool, please visit the GitHub repo [here](https://github.com/Mebus/cupp).

To run CUPP, we need python 3 installed. Then clone the GitHub repo to your local machine using git as follows:

CUPP supports an interactive mode where it asks questions about the target and based on the provided answers, it creates a custom wordlist. If you don't have an answer for the given field, then skip it by pressing the Enter key.

`python3 cupp.py -i`

As a result, a custom wordlist that contains various numbers of words based on your entries is generated. Pre-created wordlists can be downloaded to your machine as follows:

`python3 cupp.py -l`

Finally, CUPP could also provide default usernames and passwords from the Alecto database by using the -a option.

`python3 cupp.py -a`


## Referencias
- https://tryhackme.com/room/passwordattacks

- Herramientas
	- [CUPP](https://github.com/Mebus/cupp)

