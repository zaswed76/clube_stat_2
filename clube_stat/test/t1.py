
import requests
from bs4 import BeautifulSoup

# need to capture a valid csrf token
# first visit the login page to generate one
s = requests.session()
response = s.get("http://adminold.itland.enes.tech/index.php/map")

# extract the token
# soup = BeautifulSoup(response.text)
# for n in soup('input'):
#     if n['name'] == '_csrf_token':
#         token = n['value']
#         break
# print(token)
# now post to that login page with some valid credentials and the token
# auth = {
#     'userName': 'batman'
#     , 'password': 'j0kersuck5'
#     , '_csrf_token': token
# }
# s.post('https://callmeduele.com/login', data=auth)
#
# # now we should be authenticated, try visiting a protected page
# response = s.get('https://callmeduele.com/cases')
# print(response.text)