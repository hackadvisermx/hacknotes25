# droids3

Find the pass, get the flag. Check out this file.

hint> Try using apktool and an emulator
hint> https://ibotpeaches.github.io/Apktool/
hint> https://developer.android.com/studio


# Solucion
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

- detectams el error getFlag llama a nope, hay que llamar a yep que invoca cilantro la funcion nativa que regresa la flag

```java
package com.hellocmu.picoctf;

import android.content.Context;

public class FlagstaffHill {
    public static native String cilantro(String str);

    public static String nope(String input) {
        return "don't wanna";
    }

    public static String yep(String input) {
        return cilantro(input);
    }

    public static String getFlag(String input, Context ctx) {
        return nope(input);
    }
}
```



- abrir el archivo y detectar el error que es: 
- cambiar la llada none a yep en getFlag

```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ grep -r getFlag
three/smali/com/hellocmu/picoctf/MainActivity.smali:    invoke-static {v0, v2}, Lcom/hellocmu/picoctf/FlagstaffHill;->getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
three/smali/com/hellocmu/picoctf/FlagstaffHill.smali:.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;

nano three/smali/com/hellocmu/picoctf/FlagstaffHill.smali


.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 19
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;-> yep (Ljava/lang/String;)Ljava/lang/Strin>

    move-result-object v0

    .line 20
    .local v0, "flag":Ljava/lang/String;
    return-object v0
.end method

```



- Parcharlo y recompilar

```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ apktool d -r three.apk 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
I: Using Apktool 2.5.0-dirty on three.apk
I: Copying raw resources...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
 
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ nano three/smali/com/hellocmu/picoctf/FlagstaffHill.smali

```

- borrar meta
```bash
  rm three/original/META-INF/MANIFEST.MF
  rm three/original/META-INF/CERT.SF    
  rm three/original/META-INF/CERT.RSA 
```

- reconsruir el paquete 

```
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ apktool b ./three -o three_2.apk                         
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
I: Using Apktool 2.5.0-dirty
I: Checking whether sources has changed...
I: Smaling smali folder into classes.dex...
I: Checking whether resources has changed...
I: Copying raw resources...
I: Copying libs... (/lib)
I: Building apk file...
I: Copying unknown files/dir...
I: Built apk...
 
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ ls    
three  three_2.apk  three.apk

```


- generar llave
```bash
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ keytool -genkey -dname "c=MX" -keypass 123456 -keystore hacker.keystore -storepass 123456 -validity 10000 -alias hackerapp -keyalg RSA
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
 
┌──(kali㉿kali)-[~/picoctf/reversing/droids3]
└─$ ls                                          
hacker.keystore  three  three.apk

```
- firmar apk con la llave
```bash
jarsigner -digestalg SHA1 -verbose -signedjar three2b.apk -keystore hacker.keystore three2.apk hackerapp
```

- insalar apk (des instalar la anteror)
```bash
adb uninstall com.hellocmu.picoctf

adb install three2b.apk           
Performing Streamed Install
Success

```

- Ejecutar la app en el simulador, poner algo en el cuadro de texto y obtener la bandera

picoCTF{tis.but.a.scratch}


- https://tsalvia.haatenablog.com/entry/2019/10/12/053834#droids3---Points-450
- http://teamcryptis.fr/2019/10/28/picoCTF-2019-writeups.html