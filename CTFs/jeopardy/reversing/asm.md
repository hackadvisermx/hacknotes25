# ASM



# x86 - 64

- Flags register

bit | sym | name
------------------
  0 |  CF | carry
  1 |  -- | (always 1)
  2 |  PF | parity
  3 |  -- | (always 0)
  4 |  AF | adjust
  5 |  -- | (always 0)
  6 |  ZF | zero
  7 |  SF | sign
  8 |  TF | trap
  9 |  IF | interrupt
 10 |  DF | direction
 11 |  OF | overflow

 rightmost most digit is CF

31337

  1   0  1   1   0   0  0  0  1  1 despues
  1   0  1   0   0   0  0  0  1  1 antes

  1   0  1   1   0   1  0  1  1  1 despues
  1   0  1   0   0   1  0  1  1  1 antes
  IF TF SF  ZF  --  AF -- PF -- CF
  

 


 JNE        - salta si zf=0
 JE         - salta si zf=1

 1011000011 - 2c3
1011010111  - 2d7

https://exploit.courses/files/bfh2017/day5/0x44_RemoteExploit.pdf


[Flags register](https://en.wikipedia.org/wiki/FLAGS_register)