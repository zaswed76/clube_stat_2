
import requests
import time

USERNAME = 'zaswed' # put correct usename here
PASSWORD = 'fasadAQ9' # put correct password here

LOGINURL = 'http://adminold.itland.enes.tech/index.php/map'
DATAURL = 'http://adminold.itland.enes.tech/index.php/map'

# import requests
# payload = {'Login': USERNAME, 'Password': PASSWORD}
# with requests.Session() as s:
#     p = s.post(LOGINURL, data=payload)
#     print(p.text)
#
#     print("----------------------")
#     r = s.get(DATAURL)
#     print(r.text)

import requests

login_data = {'Login': USERNAME, 'Password': PASSWORD}

s = requests.Session()
r = s.post(LOGINURL, data=login_data)
time.sleep(6)
# print(r.text)
r2 = s.post(DATAURL)
print(r2.text)