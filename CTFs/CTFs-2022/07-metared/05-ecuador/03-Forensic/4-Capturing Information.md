
# Capturing Information

Juan our SPY, managed to get information from the criminal's computer. Juan reports that he tries to get away. Help us to discover where thinks intend to escape.

flag{DESTINY}

# Solucion

- se nos da un pcap con informacion de comunicacion usb


usb.transfer_type == 0x01


tshark -r captura.pcapng -T fields -e usbhid.data -Y 'usbhid.data && usb.data_len==8 && usbhid.data!=0000000000000000' | sed 's/.\{2\}/&:/g' > x

- lugo le pase el parser : https://github.com/carlospolop-forks/ctf-usb-keyboard-parser

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/metared-5-ecuador/forensic/capturinginfo]
└─$ python3 usbkeyboard.py x             
Hi Freddy
The music is very good, specially the bachatas
Hello Camilla
I need to travel this friday to Paris
please buy a plane ticket Argentina to Paris
Thanks
          

```

flag{PARIS}

## Referncias
- https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4
- https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/usb-keystrokes
- https://github.com/carlospolop-forks/ctf-usb-keyboard-parser

