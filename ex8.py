"""Find and print the number of times when a New York heart surgeon's rate of patient 
deaths for all cardiac surgical procedures was "significantly higher" 
than the statewide rate, according to New York state's analysis."""

from urllib import urlopen
import requests
import json

data = requests.get("https://health.data.ny.gov/resource/msvb-mnxf.json").json()
str_val = "Rate significantly higher than Statewide Rate"
results = [x for x in data if str_val in x['comparison_results']]

print len(results)