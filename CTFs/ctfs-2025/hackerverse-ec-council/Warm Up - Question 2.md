
**Question 2**

What is the correct password for binary1? (The answer is case-sensitive)

https://ctf.hackerverse.com/files/6d002f40223758cf1f43699075bb00df/binary1?token=eyJ1c2VyX2lkIjoxOTg0LCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoxNn0.aAsPXw.IhbsKRfxPdiYliAab5lS5L2TV6I


## Solve

- Decodificamos con ghidra la función chida es:

```c
bool verify_password(long ppass)

{
  int iVar1;
  long in_FS_OFFSET;
  int i;
  undefined8 local_38;
  undefined8 local_30;
  byte local_28 [24];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x673a257671212f28;
  local_30 = 0x3131122d140d2d2d;
  for (i = 0; (i < 0x10 && (*(char *)(ppass + i) != '\0')); i = i + 1) {
    local_28[i] = *(byte *)(ppass + i) ^ 0x42;
  }
  iVar1 = memcmp(local_28,&local_38,0x10);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar1 == 0;
}

```

- Valores codificados
```c
local_38 = 0x673a257671212f28;
local_30 = 0x3131122d140d2d2d;
```

- Al convertirlos a bytes en **little endian**, obtenemos:
```
local_38 = b'(/!qv%:g'    # 0x673a257671212f28 → b'(/!qv%:g'
local_30 = b'---\r\x14-11'  # 0x3131122d140d2d2d → b'---\r\x14-11'

```

- Concatenados
```
coded = b'(/!qv%:g---\r\x14-11'

```
- Sabemos que el XOR que aplicó el programa fue:

```
local_28[i] = ppass[i] ^ 0x42;

```

- Entonces para revertilos
```
ppass[i] = local_28[i] ^ 0x42

```


- plicamos XOR inverso byte por byte sobre los 16 bytes codificados:
```
decoded = bytes([b ^ 0x42 for b in coded])

```


Todo

```python
import struct

# Hardcoded values extraídos del análisis del binario (en hexadecimal)
local_38 = 0x673a257671212f28
local_30 = 0x3131122d140d2d2d

# Convertimos a bytes en orden little endian (como lo hace el binario)
bytes_38 = struct.pack("<Q", local_38)  # 8 bytes
bytes_30 = struct.pack("<Q", local_30)  # 8 bytes

# Concatenamos ambos para obtener la cadena codificada completa (16 bytes)
encoded_password = bytes_38 + bytes_30

# Invertimos el XOR aplicado (XOR con 0x42)
decoded_password = bytes([b ^ 0x42 for b in encoded_password])

# Mostramos el resultado como texto
print("Password recuperado:")
print(decoded_password.decode('utf-8', errors='replace'))

```

- otra forma
```python
from pwn import *

# Valores hardcodeados (como en el binario)
local_38 = 0x673a257671212f28
local_30 = 0x3131122d140d2d2d

# Unimos ambos en formato little endian (Q = 8 bytes)
encoded = p64(local_38) + p64(local_30)

# Revertimos el XOR con 0x42
decoded = xor(encoded, 0x42)

# Mostramos el password
print("Password recuperado:")
print(decoded.decode('utf-8', errors='replace'))

```

- Password recuperado
```
Password recuperado:
jmc34gx%ooOVoPss

```