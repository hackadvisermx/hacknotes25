Take a tour of the deep sea! Explore the depths of webpage secrets and find the hidden treasure. Pro tip: Zoom out!

#### Resources:

Web servers:

[challs.bcactf.com:31314](http://challs.bcactf.com:31314/)


## Solve


```
http://challs.bcactf.com:31314/shark
<div class="notFlagPartTrust">
            <!-- You found the shark! Part 1 of the flag: "bcactf{b3" -->
        </div>
```


```
view-source:http://challs.bcactf.com:31314/squid
view-source:http://challs.bcactf.com:31314/static/squid.js
console.log("You found it! Here's the second part of the flag: \"t_y0u_d1\"");
```

```
http://challs.bcactf.com:31314/clam
view-source:http://challs.bcactf.com:31314/static/clam.js
document.cookie = "flag part 3:=dnt_f1n";

window.onbeforeunload = function() {
    document.cookie = "flag part 3:=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
};  

console.log("Hint: how do websites remember you? Where do websites store things?")
```

```
curl http://challs.bcactf.com:31314/shipwreck -I
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.12.3
Date: Sat, 08 Jun 2024 20:06:29 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1266
Flag_Part_4: d_th3_tr
Connection: close
```

```
http://challs.bcactf.com:31314/whale
// Part 5 of the flag: "e4sur3"
```

```
view-source:http://challs.bcactf.com:31314/treasure

view-source:http://challs.bcactf.com:31314/static/treasure.js
console.log("Hint: what's robots.txt?");
console.log("Another hint: I don't think the robots found the root! Check under /treasure");
console.log("Also- this one isn't just about clicking around...");

view-source:http://challs.bcactf.com:31314/treasure/robots.txt
You found the rest of the flag!

_t336e3}

```

```
bcactf{b3t_y0u_d1dnt_f1nd_th3_tre4sur3_t336e3}
```