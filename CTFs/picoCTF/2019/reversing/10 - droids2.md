# droids2
Find the pass, get the flag. Check out this file.

## Solucion

- Instalar jadx
https://github.com/skylot/jadx

```bash
sudo apt install jadx
```

- abrimos app con jadx para detectar lo que hay que cambiar

```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids2]
└─$ jadx-gui &
```

- detectamos la funcion que genera el pass

```java

package com.hellocmu.picoctf;

import android.content.Context;

public class FlagstaffHill {
    public static native String sesame(String str);

    public static String getFlag(String input, Context ctx) {
        String[] witches = {"weatherwax", "ogg", "garlick", "nitt", "aching", "dismass"};
        int second = 3 - 3;
        int third = (3 / 3) + second;
        int fourth = (third + third) - second;
        int fifth = 3 + fourth;
        if (input.equals("".concat(witches[fifth]).concat(".").concat(witches[third]).concat(".").concat(witches[second]).concat(".").concat(witches[(fifth + second) - third]).concat(".").concat(witches[3]).concat(".").concat(witches[fourth]))) {
            return sesame(input);
        }
        return "NOPE";
    }
}
```

- hacemos reversing al pass en java

```java
import java.util.*;
class pass {
    public static void main(String args[]) {
	String[] witches = {"weatherwax", "ogg", "garlick", "nitt", "aching", "dismass"};
        int second = 3 - 3;
        int third = (3 / 3) + second;
        int fourth = (third + third) - second;
        int fifth = 3 + fourth;
	System.out.println("".concat(witches[fifth]).concat(".").concat(witches[third]).concat(".").concat(witches[second]).concat(".").concat(witches[(fifth + second) - third]).concat(".").concat(witches[3]).concat(".").concat(witches[fourth]));
}
}
```

- compilamos
```bash
──(kali㉿kali)-[~/picoctf/reversing/droids2]
└─$ javac pass.java
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
 
┌──(kali㉿kali)-[~/picoctf/reversing/droids2]
└─$ 

┌──(kali㉿kali)-[~/picoctf/reversing/droids2]
└─$ java pass             
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
dismass.ogg.weatherwax.aching.nitt.garlick


```
- insalar apk (des instalar la anteror)
```bash
adb uninstall com.hellocmu.picoctf

adb install two.apk           
Performing Streamed Install
Success

```

- Ejecutar la app en el simulador, poner algo en el cuadro de texto y obtener la bandera

picoCTF{what.is.your.favourite.colour}
