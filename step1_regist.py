# Step 1: Registration

import requests
import json

token = '299d3c92524b9177499249cc21e6da28'
github = 'https://github.com/gmgonzal/code2040'

# Fill body of http request
# HTTP enables communication between hosts and clients using a response and 
# request model.
# Source: https://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177
body = {'token': token, 'github': github}

# POST request
# The requests module simplifies the process of interacting with an API.
# Whereas other languages and python modules would require several lines of 
# code to post, this module only requires one. 
# Source: "Python Requests Essentials"
api = "http://challenge.code2040.org/api/register"
response = requests.post(api, data=body)

# Print response status
print response.text
