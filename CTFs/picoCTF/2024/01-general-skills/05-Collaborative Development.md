My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/177/challenge.zip)

## Hints

- `git branch -a` will let you see available branches
- How can file 'diffs' be brought to the main branch? Don't forget to `git config`!
- Merge conflicts can be tricky! Try a text editor like nano, emacs, or vim.

## Solve

```
git branch -a

  feature/part-1
  feature/part-2
* feature/part-3
  main


castr@mymac drop-in % git checkout feature/part-1
Switched to branch 'feature/part-1'
castr@mymac drop-in % cat flag.py
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')%


print("Printing the flag...")
print("m@k3s_th3_dr3@m_", end='')%


castr@mymac drop-in % git checkout feature/part-3
Switched to branch 'feature/part-3'
castr@mymac drop-in % cat flag.py
print("Printing the flag...")

print("w0rk_7ae8dd33}")


picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ae8dd33}



```