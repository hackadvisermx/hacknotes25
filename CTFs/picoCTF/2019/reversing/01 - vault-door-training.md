# vault-door-training

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/1afdf83322ee9c0040f8e3a3c047e18b/VaultDoorTraining.java)

## Solucion

- examinamos el codigo

```bash
┌──(kali㉿kali)-[~/picoctf/reversing/vaultdoor]
└─$ cat VaultDoorTraining.java
```

```java
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
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

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_eec0716b713");
    }
}

```

- verificamos version de Java
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/vaultdoor]
└─$ java --version
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
openjdk 11.0.14 2022-01-18
OpenJDK Runtime Environment (build 11.0.14+9-post-Debian-1)
OpenJDK 64-Bit Server VM (build 11.0.14+9-post-Debian-1, mixed mode, sharing)
```

- instalar java por defecto (11)
```bash
sudo apt install default-jdk
```

- instalar vsual code para una mejor edicion
`https://code.visualstudio.com/download`

- compilamos
```bash
──(kali㉿kali)-[~/picoctf/reversing/vaultdoor]
└─$ javac VaultDoorTraining.java 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true

```

- ejecutamos con pass incorrecto y falla
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/vaultdoor]
└─$ java VaultDoorTraining
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: pass
Exception in thread "main" java.lang.StringIndexOutOfBoundsException: begin 8, end 3, length 4
	at java.base/java.lang.String.checkBoundsBeginEnd(String.java:3319)
	at java.base/java.lang.String.substring(String.java:1874)
	at VaultDoorTraining.main(VaultDoorTraining.java:9)
```

- ejecutamos con el password
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/vaultdoor]
└─$ java VaultDoorTraining      
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}
Access granted.

```