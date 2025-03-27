Dear Threat Intelligence Analyst,Quick heads up - we stumbled upon a shady executable file on one of our employee's Windows PCs. Good news: the employee didn't take the bait and flagged it to our InfoSec crew.Seems like this file sneaked past our Intrusion Detection Systems, indicating a fresh threat with no matching signatures in our database.Can you dive into this file and whip up some YARA rules? We need to make sure we catch this thing if it pops up again.Thanks a bunch!The suspicious file can be downloaded [here](https://challenge-files.picoctf.net/c_standard_pizzas/f2f491f317b5d905b50463fbf42feaa409a15219d57d9e085123a43feac5c53f/suspicious.zip). Unzip the archive with the password `picoctf`

Additional details will be available after launching your challenge instance.

1. The test cases will attempt to match your rule with various variations of this suspicious file, including a packed version, an unpacked version, slight modifications to the file while retaining functionality, etc.
2. Since this is a Windows executable file, some strings within this binary can be "wide" strings. Try declaring your string variables something like `$str = "Some Text" wide ascii` wherever necessary.
3. Your rule should also not generate any false positives (or false negatives). Refine your rule to perfection! One YARA rule file can have multiple rules! Maybe define one rule for Packed binary and another rule for Unpacked binary in the same rule file?

Additional details will be available after launching your challenge instance

## Solucion

```
upx -d suspicious.exe -o unpacked.exe 
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     40960 <-     26624   65.00%    win32/pe     unpacked.exe

Unpacked 1 file.

```


## Referencias
- https://www.winitor.com/download2
- https://www.varonis.com/blog/yara-rules