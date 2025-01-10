
# Not Very Significant Message

They say a picture is worth a thousand words. Well, I certainly think the ISSS logo is saying more than it lets on. Why don't you take a look?

Hints>
- Ever heard of any techniques for hiding secret messages in pictures? I think you might to look just the _least bit_ closer at the picture to decipher the flag.

## Solucion

```
zsteg isss-logo.png
imagedata           .. file: hp300 (68020+68881) BSD
b1,rgb,lsb,xy       .. text: "utflag{st3g0_1$_c0oL}"
b4,r,msb,xy         .. text: ["3" repeated 228 times]
b4,g,msb,xy         .. text: ";;;333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
b4,b,msb,xy         .. text: ["3" repeated 228 times]
b4,rgb,msb,xy       .. text: ["3" repeated 172 times]
b4,bgr,msb,xy       .. text: ["3" repeated 172 times]
b4,abgr,msb,xy      .. text: "?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3?3"
```
