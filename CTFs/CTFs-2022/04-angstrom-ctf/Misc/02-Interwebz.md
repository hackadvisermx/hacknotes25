# Interwebz
Clam's super powerful mega server of doom is running all of ångstromCTF's infrastructure! For many challenges, it's important that you're able to connect to it. Get a free flag by connecting to `nc challs.actf.co 31335`.

Author: aplet123

hint: On Linux and macOS, you just need to install netcat and you can use the nc command. On Windows, you can either install the Windows Subsystem for Linux (WSL) and use nc from there, or find some way to make raw TCP connections, like with PuTTY.

## Solucion
```bash
nc challs.actf.co 31335

actf{plugged_in_and_ready_to_go}
```