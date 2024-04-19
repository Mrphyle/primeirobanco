import json
import requests
site = 'https://viasep.com.br/ws/15806080/json/'
result = requests.get(url=site)
print(result.text)