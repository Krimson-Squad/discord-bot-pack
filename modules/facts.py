import requests
import json
limit = 1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': '<api key>'})
if response.status_code == requests.codes.ok:
    fact = response.text
    data = json.loads(fact)
    # Access the first (and in this case, only) dictionary in the list
    msg = data[0]['fact']
else:
    print("Error:", response.status_code, response.text)
