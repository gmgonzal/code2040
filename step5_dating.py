# Step 5: The dating game

import requests
import json
import datetime
import dateutil.parser

token = '299d3c92524b9177499249cc21e6da28'

# Fill body of http request
body = {'token': token}

# POST request, get dictionary
api = 'http://challenge.code2040.org/api/dating'
response = requests.post(api, data=body)

# Parse JSON into a dictionary
parsed = json.loads(response.text)

# Use dateutil lib to parse the date 
date = dateutil.parser.parse(parsed['datestamp'])

# Use datetime to add the interval to the date
date = datetime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
new_date = date + datetime.timedelta(0, int(parsed['interval']))

# Format date
datestamp = new_date.isoformat()+'Z'

# POST datestamp
api_val = api+'/validate' 
body = {'token': token, 'datestamp': datestamp}
response = requests.post(api_val, data=body)

# Print response status
print response.text
