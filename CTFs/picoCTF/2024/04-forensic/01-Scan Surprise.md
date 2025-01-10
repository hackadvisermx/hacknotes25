#qrcode

- QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too.
- Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11
- If you don't have access to a phone, you can also use zbar-tools to convert an image to text

## Solve

```
apt install zbar-tools

zbarimg home/ctf-player/drop-in/flag.png
Connection Error (Failed to connect to socket /run/dbus/system_bus_socket: No such file or directory)
Connection Null
QR-Code:picoCTF{p33k_@_b00_0194a007}
scanned 1 barcode symbols from 1 images in 0.08 seconds
```