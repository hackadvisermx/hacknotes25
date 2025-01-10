# vault-door-6
This vault uses an XOR encryption scheme. The source code for this vault is here: VaultDoor6.java

Hint: 

If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.

## Solucion

- Analizamos la pista
```python

>>> 45 ^ 0x55
120
>>> 120 ^ 0x55
45

>>> 45 ^ 45
0
```

- Programa orginal
```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
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

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}

```

- Programa modificado para imprimir la flag
```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        //System.out.print("Enter vault password: ");
        //String userInput = scanner.next();
	//String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword()) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword() {
     /*    if (password.length() != 32) {
            return false;
        } */
        byte[] flagBytes = new byte[32];
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
        };
       
        for (int i=0; i<32; i++) {
            flagBytes[i] = (byte) (myBytes[i] ^  0x55);
            /* if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            } */
        }
        String flag = new String(flagBytes);
        System.out.println(flag);
        return true;
    }
}

```

## Forma 2
```python
>>> mybytes = [ 0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
              0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
              0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
              0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36]
 

flag = [i^0x55 for i in mybytes]
flag = [chr(i) for i in flag]

''.join(flag)


```