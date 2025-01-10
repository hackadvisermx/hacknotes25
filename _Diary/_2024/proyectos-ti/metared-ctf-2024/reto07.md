
Since start of this year, we are receiving reports about suspicious activity coming from a company called Monster Inc. Our blue team has tracked down their secret company portal and cracked the admin account password's, however, couldn't bypass the 2FA security. Can you break in?

username: admin
password: admin

## Construir la imagen


```
docker build -t monster-inc .

docker run --name monster -p3000:3000 monster-inc
```

## Correr la solución

```
virtualenv env
source .venv/bin/activate

pip install pyotp==2.3.0
pip install requests


source deactivate 
```

## Referencias
- https://github.com/BCACTF/bcactf-5.0/tree/main/moc-inc
- 