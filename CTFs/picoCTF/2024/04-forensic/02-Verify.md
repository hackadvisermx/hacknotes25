People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.You can download the challenge files here:

- `[challenge.zip](https://artifacts.picoctf.net/c_rhea/21/challenge.zip)`

Additional details will be available after launching your challenge instance.

- Checksums let you tell if a file is complete and from the original distributor. If the hash doesn't match, it's a different file.
- You can create a SHA checksum of a file with `sha256sum <file>` or all files in a directory with `sha256sum <directory>/*`.
- Remember you can pipe the output of one command to another with `|`. Try practicing with the 'First Grep' challenge if you're stuck!

## Solve

```
for i in $(ls -R); do ./decrypt.sh $i ; done | grep pico

bad magic number
bad magic number
bad magic number
picoCTF{trust_but_verify_e018b574}
```