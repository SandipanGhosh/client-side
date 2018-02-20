# Submitting to a web form

import requests

url = 'http://httpbin.org/post'
data = {'fname': 'John', 'lname': 'Smith'}

r = requests.post(url, data=data)
print(r.content)