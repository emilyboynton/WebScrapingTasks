"""Find and print the number of people visiting a U.S. government website right now"""

import json
import requests

jsonObj = requests.get("https://analytics.usa.gov/data/live/realtime.json")
print jsonObj.json()['data'][0]['active_visitors']