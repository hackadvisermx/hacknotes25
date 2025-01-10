# James Harold Japp

## Objetivo
 need to be able to log in to this website. Can you tell me how to do it? [mhsctf-jamesharoldjapp.0xmmalik.repl.co](https://mhsctf-jamesharoldjapp.0xmmalik.repl.co) (you may need to wait for the site to wake up)
 
## Solucion
- ver codigo: view-source:https://mhsctf-jamesharoldjapp.0xmmalik.repl.co/
```javascript
<script>
      function validatepwd() {
        var x = document.getElementById("pwd").value;
        if (x == "this_is_a_really_secure_password") {
          window.open("/weirdpage.php?pwd=doublepassword")
        }
      }
    </script>
```
- ver codigo: view-source:https://mhsctf-jamesharoldjapp.0xmmalik.repl.co/weirdpage.php?pwd=doublepassword
```html
<!doctype html><html><head><!--lol gottem here's the flag: flag{1n$p3ct0r_g3n3r@l}--><title>404 Not Found</title><style> body { background-color: #fcfcfc; color: #333333; margin: 0; padding:0; }
```

## Flag
```bash
flag{1n$p3ct0r_g3n3r@l}
```

## Referencias