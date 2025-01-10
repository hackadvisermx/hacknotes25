# timer
You will find the flag after analysing this apk Download [here](https://artifacts.picoctf.net/c/327/timer.apk).

hints
- decompile
- mobsf or jadx

## Solucion
- decompilar la apk


```
jd-gui

sudo apt install jd-gui

jadx-gui
sudo apt install jadx

```





- buscar la cadena pico en el código con la función de busqueda
```
package com.example.timer;  
  
/* loaded from: classes3.dex */  
public final class BuildConfig {  
    public static final String APPLICATION_ID = "com.example.timer";  
    public static final String BUILD_TYPE = "debug";  
    public static final boolean DEBUG = Boolean.parseBoolean("true");  
    public static final int VERSION_CODE = 1;  
    public static final String VERSION_NAME = "picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}";  
}
```




## Bandera
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}