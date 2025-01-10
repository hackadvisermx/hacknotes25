How about some hide and seek?Download this file [here](https://artifacts.picoctf.net/c_titan/129/unknown.zip).

- - How can you view the information about the picture?
- If something isn't in the expected form, maybe it deserves attention?

## Solve

```
➜  canyousee exiftool ukn_reality.jpg
ExifTool Version Number         : 12.40
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2024:03:12 00:05:53+00:00
File Access Date/Time           : 2024:03:14 23:24:10+00:00
File Inode Change Date/Time     : 2024:03:14 23:24:08+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
➜  canyousee echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_b32040b8}
```