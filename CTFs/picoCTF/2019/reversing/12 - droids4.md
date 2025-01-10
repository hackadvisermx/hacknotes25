# droids4
Reverse the pass, patch the file, get the flag. Check out this file.


## Solucion
- abrimos la apk con jdx-gui


- reversamos el password

```java
import java.util.*;
class pass {
    public static void main(String args[]) {
        StringBuilder ace = new StringBuilder("aaa");
        StringBuilder jack = new StringBuilder("aaa");
        StringBuilder queen = new StringBuilder("aaa");
        StringBuilder king = new StringBuilder("aaa");
        ace.setCharAt(0, (char) (ace.charAt(0) + 4));
        ace.setCharAt(1, (char) (ace.charAt(1) + 19));
        ace.setCharAt(2, (char) (ace.charAt(2) + 18));
        jack.setCharAt(0, (char) (jack.charAt(0) + 7));
        jack.setCharAt(1, (char) (jack.charAt(1) + 0));
        jack.setCharAt(2, (char) (jack.charAt(2) + 1));
        queen.setCharAt(0, (char) (queen.charAt(0) + 0));
        queen.setCharAt(1, (char) (queen.charAt(1) + 11));
        queen.setCharAt(2, (char) (queen.charAt(2) + 15));
        king.setCharAt(0, (char) (king.charAt(0) + 14));
        king.setCharAt(1, (char) (king.charAt(1) + 20));
        king.setCharAt(2, (char) (king.charAt(2) + 15));
        System.out.println("".concat(queen.toString()).concat(jack.toString()).concat(ace.toString())>
}
}
```

- compilamos
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids4]
└─$ javac pass.java
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
 
┌──(kali㉿kali)-[~/picoctf/reversing/droids4]
└─$ java pass             
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
alphabetsoup

```

- desempacamos
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids4]
└─$ apktool d -r four.apk 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
I: Using Apktool 2.5.0-dirty on four.apk
I: Copying raw resources...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```

- buscamos el punto de patching
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids4]
└─$ grep -r 'call it'
four/smali/com/hellocmu/picoctf/FlagstaffHill.smali:    const-string v5, "call it"

```

- editamos 
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids4]
└─$ nano four/smali/com/hellocmu/picoctf/FlagstaffHill.smali
```
- el cambio, es esto
```bash
	const-string v5, "call it"

    return-object v5

```

- por esto
```bash
	invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cardamom(Ljava/lang/String;)Ljava/lang/String;
	
	move-result-object v0
	
	return-object v0
```

- borrar meta
```bash
  rm four/original/META-INF/MANIFEST.MF
  rm four/original/META-INF/CERT.SF    
  rm four/original/META-INF/CERT.RSA 
```

- recompilamos y firmamos
```
apktool b ./four -o four2.apk

keytool -genkey -dname "c=MX" -keypass 123456 -keystore hacker.keystore -storepass 123456 -validity 10000 -alias hackerapp -keyalg RSA

jarsigner -digestalg SHA1 -verbose -signedjar four2b.apk -keystore hacker.keystore four2.apk hackerapp

```


```bash
jarsigner -digestalg SHA1 -verbose -signedjar four2b.apk -keystore hacker.keystore four2.apk hackerapp

```

- vamos al emulador, ponemos pass y click al boton
alphabetsoup

picoCTF{not.particularly.silly}