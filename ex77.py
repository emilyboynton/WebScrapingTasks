import requests
import json

data = requests.get("https://www.dallasopendata.com/resource/4gmt-jyx2.json").json()

date_key_str = "date"
date_val_str = "2014"

shoot_key_str = "suspect_deceased_injured_or_shoot_and_miss"
shoot_val_str = "Deceased"


results = [x for x in data if shoot_val_str in x[shoot_key_str] and date_val_str in x[date_key_str]]

print len(results)