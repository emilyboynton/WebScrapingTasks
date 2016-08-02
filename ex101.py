"""Find and print the number of women currently serving in the U.S. Congress, 
according to Sunlight Foundation dataset"""
import csv
from urllib import urlopen
import requests

url = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
file = urlopen(url)
reader = csv.DictReader(file)

total = 0

for row in reader:
	if ((row['gender'] == "F") and (row['in_office'] == "1")):
		total += 1

print total