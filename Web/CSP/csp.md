# Content Security Policy (CPS)

La política de seguridad de contenido (CPS) es una política que generalmente se envía a través de un encabezado de respuesta de HTTP desde el servidor web a su nevegador cuando solicita una página que describe en qué fuentes de contenido debe permitir que se cargue el navegador y cuáles deben bloquearse. En caso de que se encuentre una vulnerabilidad XSS o de inyección de datos en un sitio web, CSP está diseñado para evitar que esta vulnerabilidad sea explotada hasta que se haya parcheado adecuadamente y debería servir como una capa adicional de protección, no como su única línea de defensa.

También se puede incluir una política de CSP dentro del código fuente HTML de la página, utilizando la etiqueta <meta>, como esta:
```
<meta http-equiv="Content-Security-Policy" content="script-src 'none'; object-src 'none';">
```

- Directivas comúnmente usadas:

| Directiva | Significado |
|---------|---------------------------------------------------------------------|
|default-src| Se usa como predeterminada, lo que significa que si un determinado recurso está intentando cargarse y no hay una directiva especificada para su tipo, recurre a default-src para verificar si está permitido cargar.
| script-src  | Especifica las fuentes desde las que se pueden cargar y ejecutar scripts JavaScript.
| connect-src | Especifica a qué ubicaciones el código JavaScript puede realizar solicitudes AJAX (piense en XMLHTTPRequest o fetch). 
|style-src / img-src / font-src / media-src | Especifican desde qué ubicaciones se pueden cargar hojas de estilo CSS, imágenes, fuentes y archivos multimedia (audio / video) respectivamente.
| frame-src / child-src | Define qué ubicaciones se pueden incrustar en la página web a través de iframes.
| report-uri | Indicará al navegador que informe todas las violaciones de su Política de seguridad de contenido a través de una solicitud POST a una URL en particular.

- Fuentes (sources)

| Directiva  | Significado |
|-----------------|-------------------------------|
| *               | es un comodín, lo que significa que el contenido de esa directiva específica se puede cargar desde cualquier lugar |
| 'none'          | no permite cargar recursos del tipo de directiva especificado desde cualquier lugar (media-src 'none') |
| 'self'          | le permite cargar recursos que están alojados en el mismo protocolo, nombre de host y puerto que el sitio web |
| 'unsafe-inline' | permite el uso de hojas de estilo en línea, JavaScript en línea y atributos de eventos como onclick |
| 'unsafe-eval'   | permite que se ejecute código JavaScript adicional utilizando funciones como eval () mediante código JS que ya está permitido dentro de la política |
| example.com     | le permite cargar recursos del dominio example.com, pero no de sus subdominios 
|  '*'*.example.com   |  le permite cargar recursos de todos los subdominios de example.com, pero no del dominio base |
| data:           | permitir que los recursos se carguen desde un data: url |
| nonce -         | permite que un recurso se cargue si tiene un atributo nonce coincidente
| sha256-         | hash SHA256 codificado a través de Base64 que se usa como suma de comprobación para verificar que el contenido del recurso coincide con lo que permite el servidor |


- JSONP
JSON con padding es una técnica usada para solicitar  obtener datos de un servidor sin preocuparse acerca del cross-domain, sobrepasando SOP



## Recursos:
- https://tryhackme.com/room/csp
- [Generate a policy for u](https://report-uri.com/home/generate)
- [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/)
- [JSONBee](https://github.com/zigoo0/JSONBee)
- [Beecptor](https://beeceptor.com/)
