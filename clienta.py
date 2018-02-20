# Retrieving a web page

import requests

r = requests.get("http://www.python.org/")
print(r.content)