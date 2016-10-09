# Step 2: Reverse a string

import requests

token = '299d3c92524b9177499249cc21e6da28'

# Fill body of http request
body = {'token': token}

# POST request, get string
api = 'http://challenge.code2040.org/api/reverse'
response = requests.post(api, data=body)

# Reverse string using extended slicing.
# Third argument added to slicing syntax allows for more modifications using 
# indexes. For negative values, the list is reversed.
# Source: https://docs.python.org/2.3/whatsnew/section-slices.html
reverse = response.text[::-1]

# POST reversed string
body = {'token': token, 'string': reverse}
api_val = api+'/validate'
response = requests.post(api_val, data=body)

# Print response status
print response.text
