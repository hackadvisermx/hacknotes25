# Notas

- A dynamically linked ELF binary uses a look-up table called the Global Offset Table (GOT) to dynamically resolve functions that are located in shared libraries. 


## Forma de protección 
  
- **RELRO stands for Relocation Read-Only.** which makes the global offset table (GOT) read-only after the linker resolves functions to it. The GOT is important for techniques such as the ret-to-libc attack, although this is outside the scope of this room. 
   
    - https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro 

- **Stack canaries are tokens placed after a stack to detect a stack overflow.** Stack canaries sit beside the stack in memory (where the program variables are stored), and if there is a stack overflow, then the canary will be corrupted. This allows the program to detect a buffer overflow and shut down.
  
    - https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/ 

- **NX is short for non-executable.** If this is enabled, then memory segments can be either writable or executable, but not both. This stops potential attackers from injecting their own malicious code (called shellcode) into the program, because something in a writable segment cannot be executed.

    - https://en.wikipedia.org/wiki/Executable_space_protection 

- **PIE stands for Position Independent Executable.** this loads the program dependencies into random locations, so attacks that rely on memory layout are more difficult to conduct. 
  
    - https://access.redhat.com/blogs/766093/posts/1975793 

Notas
- 
- 