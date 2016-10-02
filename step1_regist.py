# Step 1: Registration

import requests

# Fill body of http request
body = {'token': '299d3c92524b9177499249cc21e6da28', 'github': 'https://github.com/gmgonzal/code2040'}

# POST request
response = requests.post("http://challenge.code2040.org/api/register", data=body)
