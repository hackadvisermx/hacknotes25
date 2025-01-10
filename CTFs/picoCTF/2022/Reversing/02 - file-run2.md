# file-run2

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program [here](https://artifacts.picoctf.net/c/355/run).

## solucion

```bash
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/file-run2]
└─$ chmod +x run
                                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/file-run2]
└─$ ./run 
Run this file with only one argument.
                                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/file-run2]
└─$ ./run run 
Won't you say 'Hello!' to me first?
                                                                                                                     
┌──(kali㉿kali)-[~/…/ctfs2022/picoctf2022/reversing/file-run2]
└─$ ./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_981abfb5} 

```