# vault-door-7
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java

## Solucion

- codigo original
```java
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class VaultDoor7 {
    public static void main(String args[]) {
        VaultDoor7 vaultDoor = new VaultDoor7();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Each character can be represented as a byte value using its
    // ASCII encoding. Each byte contains 8 bits, and an int contains
    // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
    // example: if the hex string is "01ab", then those can be
    // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
    // bytes are represented as binary, they are:
    //
    // 0x30: 00110000
    // 0x31: 00110001
    // 0x61: 01100001
    // 0x62: 01100010
    //
    // If we put those 4 binary numbers end to end, we end up with 32
    // bits that can be interpreted as an int.
    //
    // 00110000001100010110000101100010 -> 808542562
    //
    // Since 4 chars can be represented as 1 int, the 32 character password can
    // be represented as an array of 8 ints.
    //
    // - Minion #7816
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734291511
            && x[6] == 960049251
            && x[7] == 1681089078;
    }
}

```

### Forma 2 - python
```python
from pwn import * 
>>> a = [1096770097,1952395366,1600270708,1601398833,1716808014,1734305381,828716089,895562083]


>>> ''.join([ p32(x, endian='big').decode() for x in a ])
'A_b1t_0f_b1t_sh1fTiNg_fe1e495a1c'

```

### Forma 3 - python
```python
```python
x =[0] * 8

x[0] = 1096770097
x[1] = 1952395366
x[2] = 1600270708
x[3] = 1601398833
x[4] = 1716808014
x[5] = 1734293603
x[6] = 959591523
x[7] = 842097204

ch = [None] * 4
buffer = ""

for i in range(0,8):
	tmp = str(bin(x[i])[2:].zfill(32))
	ch[0] = chr(int(hex(int(tmp[:8], 2)), 16))
	ch[1] = chr(int(hex(int(tmp[8:16], 2)), 16))
	ch[2] = chr(int(hex(int(tmp[16:24], 2)), 16))
	ch[3] = chr(int(hex(int(tmp[24:32], 2)), 16))
	buffer += ch[0] + ch[1] + ch[2] + ch[3]

print("picoCTF{{{}}}".format(buffer))
```
```



- Referencias

- https://stackoverflow.com/questions/35731543/how-to-extract-and-display-each-of-the-four-bytes-of-an-integer-individually-as

- https://mkyong.com/java/java-convert-byte-to-int-and-vice-versa/

- https://captainmich.github.io/programming_language/CTF/Challenge/picoCTF2019/reverse_engineering.html#vault-door-7