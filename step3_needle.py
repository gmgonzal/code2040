# Step 3: Needle in a haystack

import requests
import json

token = '299d3c92524b9177499249cc21e6da28'

# Fill body of http request
body = {'token': token}

# POST request, get dictionary
api = 'http://challenge.code2040.org/api/haystack'
response = requests.post(api, data=body)

# Parse JSON into a dictionary
# Use List index() method to locate "needle" in "haystack"
parsed = json.loads(response.text)
index = parsed['haystack'].index(parsed['needle'])

# POST reversed string
body = {'token': token, 'needle': index}
api_val = api+'/validate'
response = requests.post(api_val, data=body)

# Print response status
print response.text
