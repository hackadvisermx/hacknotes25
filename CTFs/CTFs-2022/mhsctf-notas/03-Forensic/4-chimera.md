``` bash
binwalk -e 87122c397ac8b10d53057a2c9ec1834e.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 499 x 389, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
234601        0x39469         PNG image, 499 x 389, 8-bit/color RGBA, non-interlaced
234642        0x39492         Zlib compressed data, compressed

                                                                                       
┌──(kali㉿kali)-[~/hacking/mhsctf2022/forensic/chimera]
└─$ foremost 87122c397ac8b10d53057a2c9ec1834e.png 
Processing: 87122c397ac8b10d53057a2c9ec1834e.png
|*|
                                                                                       
┌──(kali㉿kali)-[~/hacking/mhsctf2022/forensic/chimera]
└─$ cd output    
                                                                                       
┌──(kali㉿kali)-[~/…/mhsctf2022/forensic/chimera/output]
└─$ ls
audit.txt  png
                                                                                       
┌──(kali㉿kali)-[~/…/mhsctf2022/forensic/chimera/output]
└─$ cd png       
                                                                                       
┌──(kali㉿kali)-[~/…/forensic/chimera/output/png]
└─$ open 00000458.png 
                                                                                       
┌──(kali㉿kali)-[~/…/forensic/chimera/output/png]

```

flag{4bs0rb3d}