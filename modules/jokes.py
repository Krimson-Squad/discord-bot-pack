import requests
import json
limit = 1
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': '<api key>'})
if response.status_code == requests.codes.ok:
    joke = response.text
    data = json.loads(joke)
    # Access the first (and in this case, only) dictionary in the list
    msg = data[0]['joke']
else:
    print("Error:", response.status_code, response.text)
