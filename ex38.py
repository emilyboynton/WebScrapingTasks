"""Find and print the domain of the most visited U.S. government website right now"""

import json
import requests

jsonObj = requests.get("https://analytics.usa.gov/data/live/top-pages-realtime.json")

print (jsonObj.json())['data'][0]['page']
