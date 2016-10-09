# Step 4: Prefix

import requests
import json

token = '299d3c92524b9177499249cc21e6da28'

# Fill body of http request
body = {'token': token}

# POST request, get dictionary
api = 'http://challenge.code2040.org/api/prefix'
response = requests.post(api, data=body)

# Parse JSON into a dictionary
parsed = json.loads(response.text)

# Append entries to that do not start with the prefix to the array
array = []
for element in parsed['array']:
	if element.startswith(parsed['prefix']) == False: array.append(element)

# POST the array of entries that do not start with prefix
body = {'token': token, 'array[]': array}
api_val = api+'/validate'
response = requests.post(api_val, data=body)

# Print response status
print response.text
