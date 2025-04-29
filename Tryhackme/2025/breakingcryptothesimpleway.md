

# Breaking Crypto the Simple Way


```
ython 3.13.2 (main, Mar 13 2025, 14:29:07) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> p = 205237461320000835821812139013267110933
>>> q = 214102333408513040694153189550512987959
>>> tn = (1-p)  * (1-q)
>>> tn
43941819371451617899582143885098799360487795145142432760613501190745566156856
>>> n = p * q
>>> tn = (p-1)  * (q-1)
>>> tn
43941819371451617899582143885098799360487795145142432760613501190745566156856
>>> d = pow(e,-1,tn)
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    d = pow(e,-1,tn)
            ^
NameError: name 'e' is not defined
>>> e = 65537
>>> d = pow(e,-1,tn)
>>> c = 9002431156311360251224219512084136121048022631163334079215596223698721862766
>>> t = pow(c, d, n)
>>> t
2066599226201921488518166332774002961446565564615335572349
 
>>> bytes.fromhex(hex(t)[2:]).decode()
'THM{Psssss_4nd_Qsssssss}'
>>> 

```

## Task 3 Breaking Hashes


```
┌──(kali㉿kali)-[~/tmp/tryhackme/breakingcryptothesimpleway]
└─$ echo -n "1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGuessMySecret" > digest.txt
                                                                                       
┌──(kali㉿kali)-[~/tmp/tryhackme/breakingcryptothesimpleway]
└─$ cat digest.txt            
1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGuessMySecret                                                                                       
┌──(kali㉿kali)-[~/tmp/tryhackme/breakingcryptothesimpleway]
└─$ hashcat -a 0 -m 150 digest.txt /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 18.1.8, SLEEF, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================
* Device #1: cpu--0x000, 1435/2935 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGuessMySecret:sunshine
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 150 (HMAC-SHA1 (key = $pass))
Hash.Target......: 1484c3a5d65a55d70984b4d10b1884bda8876c1d:CanYouGues...Secret
Time.Started.....: Tue Apr  8 21:24:37 2025 (0 secs)
Time.Estimated...: Tue Apr  8 21:24:37 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    22314 H/s (0.16ms) @ Accel:256 Loops:1 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 1024/14344385 (0.01%)
Rejected.........: 0/1024 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> bethany

Started: Tue Apr  8 21:24:15 2025
Stopped: Tue Apr  8 21:24:38 2025
                                                                                       
┌──(kali㉿kali)-[~/tmp/tryhackme/breakingcryptothesimpleway]
└─$ 

```

## Task 4 Exposed Keys


- exploit
```
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Configuration
url = "http://bcts.thm/labs/lab3/process.php"
encryption_key = b"1234567890123456"  # Must be 16 bytes (same as in the JavaScript)
wordlist_path = "wordlist.txt"        # Path to the wordlist

# Function to encrypt a message
def encrypt_message(message, iv):
    # Pad the message to a multiple of the block size (16 bytes for AES)
    padded_message = pad(message.encode(), AES.block_size)
    # Encrypt using AES-CBC
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_message)
    # Encode ciphertext and IV in Base64 for transmission
    return base64.b64encode(ciphertext).decode(), base64.b64encode(iv).decode()

# Function to send the payload
def send_payload(ciphertext, iv):
    payload = {"data": ciphertext, "iv": iv}
    response = requests.post(url, json=payload)
    return response.text

# Main bruteforce function
def bruteforce():
    with open(wordlist_path, "r") as f:
        words = f.readlines()

    for word in words:
        word = word.strip()
        print(f"Trying: {word}")
        # Generate a random IV (16 bytes)
        iv = AES.get_random_bytes(16)
        # Encrypt the current word
        ciphertext, iv_base64 = encrypt_message(word, iv)
        # Send the payload to the server
        response = send_payload(ciphertext, iv_base64)
        print(f"Response: {response}")
        # Check if the response indicates success
        if "Access granted!" in response:
            print(f"[+] Found the correct message: {word}")
            break

if __name__ == "__main__":
    bruteforce()

```

- iniciamos ataque de fuerza bruta
```
┌──(.venv)─(kali㉿kali)-[~/tmp/tryhackme/breakingcryptothesimpleway]
└─$ python exp2.py 
Trying: jadmxqtideg
Response: Message jadmxqtideg is invalid!
Trying: pyasosedg
 
Response: Access granted! Here's your flag: THM{3nD_2_3nd_is_n0t_c0mpl1c4ted}
[+] Found the correct message: ankhzljjgu
                                               
```

##  Task 5 Bit Flipping **Attacks**

```python
import base64, sys
from binascii import unhexlify, hexlify

original_token = sys.argv[1] # Your encrypted role token goes here

try:
    cipher_bytes = bytearray(unhexlify(original_token))
except ValueError:
    print("Invalid token format! Make sure it's a valid hex string.")
    exit(1)

# AES block size
block_size = 16

# Debug: Print IV (first 16 bytes) before modification
print("\n[DEBUG] Original IV (First 16 Bytes):", hexlify(cipher_bytes[:block_size]).decode())

guest_offset = 0

xor_diff = [
    0x01,  # '0' -> '1'
]

# Apply bit flipping to the IV (first 16 bytes)
for i, diff in enumerate(xor_diff):
    print(f"[DEBUG] Modifying byte at offset {guest_offset + i}: {hex(cipher_bytes[guest_offset + i])} XOR {hex(diff)}")
    cipher_bytes[guest_offset + i] ^= diff

print("\n[DEBUG] Modified IV (First 16 Bytes):", hexlify(cipher_bytes[:block_size]).decode())

# Encode the modified token back to hex
modified_token = hexlify(cipher_bytes).decode()

print("\nModified Token:")
print(modified_token)
print("\nUse this token as the new 'role' cookie in your browser to log in as admin.")

```