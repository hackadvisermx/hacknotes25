# Un archivo que ha sido codificado 
# 5 veces base64, 5 veces base32, 5 veces base16

import base64

f=open('encodedflag.txt','r')
flag=f.read()
#print(flag)
res=''

for i in range(0,5):
    res=base64.b16decode(flag)
    flag=res

for i in range(0,5):
    res=base64.b32decode(flag)
    flag=res

for i in range(0,5):
    res=base64.b64decode(flag)
    flag=res


print(flag)

f.close() 
