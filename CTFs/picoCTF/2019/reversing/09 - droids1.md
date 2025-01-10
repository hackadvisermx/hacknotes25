
# droids1
Find the pass, get the flag. Check out this file.

hint> Try using apktool and an emulator
hint> https://ibotpeaches.github.io/Apktool/
hint> https://developer.android.com/studio


## Solucion
- Instalar apktool
```bash
sudo apt install apktool
```

- Decompilamos la apk, usando apktool
```bash
apktool d one.apk 
```

- Haemos un rep sobre el contenio decompilado en busca de `flag` o `password`:
```bash
grep -r password
smali/com/hellocmu/picoctf/R$string.smali:.field public static final password:I = 0x7f0b002f
smali/com/hellocmu/picoctf/FlagstaffHill.smali:    .local v0, "password":Ljava/lang/String;
smali/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.smali:    .param p1, "password"    # Z
smali/androidx/core/view/accessibility/AccessibilityNodeInfoCompat.smali:    const-string v2, "; password: "
res/values/strings.xml:    <string name="password">opossum</string>
res/values/public.xml:    <public type="string" name="password" id="0x7f0b002f" />

```

- vamos emulador y ponemos el password `opossum`

picoCTF{pining.for.the.fjords}



- Instalar apk del reto
```bash
adb shell pm list packages | grep pico
package:com.svox.pico
package:com.hellocmu.picoctf

adb uninstall com.hellocmu.picoctf

adb install one.apk                   
Performing Streamed Install
Success


```