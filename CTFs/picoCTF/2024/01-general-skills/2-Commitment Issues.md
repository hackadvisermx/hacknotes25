I accidentally wrote the flag down. Good thing I deleted it!You download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/137/challenge.zip)

### Hints
- Version control can help you recover files if you change or lose them!
- Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control)
- You can 'checkout' commits to see the files inside them

## Solucion

```
git log -p

commit 3899edb7f3110d613c72ad40083fd8feeef703d0 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:58 2024 +0000

    remove sensitive info

diff --git a/message.txt b/message.txt
index ed59373..d552d1e 100644
--- a/message.txt
+++ b/message.txt
@@ -1 +1 @@
-picoCTF{s@n1t1z3_9539be6b}
+TOP SECRET

commit 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:58 2024 +0000

    create flag

diff --git a/message.txt b/message.txt
new file mode 100644
index 0000000..ed59373
--- /dev/null
+++ b/message.txt
@@ -0,0 +1 @@
+picoCTF{s@n1t1z3_9539be6b}
```