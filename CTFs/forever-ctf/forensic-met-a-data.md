#  Met A Data

See if you can find the flag hidden in this picture. Well, I guess it isn't really _in_ the picture, just part of the file.

## Hints
- Are there any commands or programs you can use to see the [metadata](https://en.wikipedia.org/wiki/Metadata) of a file/image?
- Try running the command line program `strings` on the image and looking for the file. You can also use an online tool like [this one](https://www.exifdata.com/index.php).

## Solución

### Forma 1
```
strings strings.jpg -n 20
utflag{stringy_thingies}
*9*-13666 (;?:4>0563
"33333333333333333333333333333333333333333333333333
```

### Forma 2
```
exiftool strings.jpg
ExifTool Version Number         : 12.60
File Name                       : strings.jpg
Directory                       : .
File Size                       : 534 kB
File Modification Date/Time     : 2023:05:17 20:19:41-06:00
File Access Date/Time           : 2023:05:17 20:20:23-06:00
File Inode Change Date/Time     : 2023:05:17 20:19:46-06:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : utflag{stringy_thingies}
Image Width                     : 1920
Image Height                    : 2560
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1920x2560
Megapixels                      : 4.9
```


