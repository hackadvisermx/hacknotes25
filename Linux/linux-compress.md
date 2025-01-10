# Linux Compress - Decompress


- Unzip con python

```python
import zipfile

with zipfile.ZipFile('test.zip', "r") as z:
  z.extractall("/home/user/directory")
```
