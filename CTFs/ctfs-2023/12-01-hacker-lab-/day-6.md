

## Solucion


```
sudo vol -f memory.raw windows.filescan | grep png

```

```
─$ sudo vol -f memory.raw windows.filescan | grep png   
0x918b7602a230.0\Program Files\WindowsApps\Microsoft.Windows.Photos_2023.10070.17002.0_x64__8wekyb3d8bbwe\Assets\Blank_PhotosSplashWideTile.png 216
0x918b760e8750  \Users\santa\Pictures\wallpaper.png     216
0x918b760e88e0  \Users\santa\AppData\Local\Packages\Microsoft.Windows.Photos_8wekyb3d8bbwe\LocalState\PhotosAppBackground\wallpaper.png 216
0x918b760ed250  \Users\santa\Pictures\wallpaper.png     216
0x918b760ed3e0  \Users\santa\AppData\Local\Packages\Microsoft.Windows.Photos_8wekyb3d8bbwe\LocalState\PhotosAppBackground\wallpaper.png 216
0x918b76974b60  \Program Files\WindowsApps\Microsoft.MicrosoftStickyNotes_6.0.1.0_x64__8wekyb3d8bbwe\Assets\Devices-light.png   216
0x918b76c517f0  \Users\santa\Pictures\wallpaper.png     216
0x918b76c54860  \Users\santa\AppData\Local\Packages\Microsoft.Windows.Photos_8wekyb3d8bbwe\LocalState\PhotosAppLockscreen\wallpaper.png 216
0x918b76c56160  \Users\santa\AppData\Local\Packages\Microsoft.Windows.Photos_8wekyb3d8bbwe\LocalState\PhotosAppLockscreen\wallpaper.png 216
0x918b771069c0  \Users\santa\Pictures\wallpaper.png     216
0x918b771082c0  \Program Files\WindowsApps\Microsoft.MicrosoftStickyNotes_6.0.1.0_x64__8wekyb3d8bbwe\Assets\NewNotePlaceholder-light.png        216
0x918b7710a840  \Program Files\WindowsApps\Microsoft.MicrosoftStickyNotes_6.0.1.0_x64__8wekyb3d8bbwe\Assets\SearchPlaceholder-light.png 216
0x918b7710d270  \Program Files\WindowsApps\Microsoft.MicrosoftStickyNotes_6.0.1.0_x64__8wekyb3d8bbwe\Assets\SignInUpsellCloud.png       216


```

```
┌──(kali㉿kali)-[~/shared/ctfs-navidad/hacking-lab/06]
└─$ sudo vol -f memory.raw dumpfiles --virtaddr 0x918b760e8750
Volatility 3 Framework 2.5.2
Progress:  100.00               PDB scanning finished                        
Cache   FileObject      FileName        Result

DataSectionObject       0x918b760e8750  wallpaper.png   file.0x918b760e8750.0x918b70a67190.DataSectionObject.wallpaper.png.dat
SharedCacheMap  0x918b760e8750  wallpaper.png   file.0x918b760e8750.0x918b76b2ada0.SharedCacheMap.wallpaper.png.vacb

```

```
sudo apt install zbar-tools 
zbarimg -q --raw file.0x918b760e8750.0x918b70a67190.DataSectionObject.wallpaper.png
HV23{FANCY-W4LLP4p3r}

```
## Referencias

- https://seanthegeek.net/1172/how-to-install-volatility-2-and-volatility-3-on-debian-ubuntu-or-kali-linux/
- https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet
- https://github.com/volatilityfoundation/volatility/wiki/Command-Reference#filescan