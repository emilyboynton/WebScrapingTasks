"""Find and print the number of U.S. congressmembers who have Twitter accounts, 
according to Sunlight Foundation data """
import csv
from urllib import urlopen
import requests

url = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
file = urlopen(url)
reader = csv.DictReader(file)

total = 0

for row in reader:
	if (row['twitter_id'] != ""):
		total += 1

print total