"""Find and print the percentage of NYPD stop-and-frisk reports in which the suspect was white in 2014"""
from __future__ import division
import requests
import re
import zipfile
import csv
from io import BytesIO


url = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2014_sqf_csv.zip'
r = requests.get(url, stream=True)
z = zipfile.ZipFile(BytesIO(r.content))
fname = z.namelist()
f = z.extractall()

total = 0
white = 0

with open(fname[0]) as file:
    reader = csv.DictReader(file)
    for row in reader:
    	total += 1
    	if (row['race'] == 'W'):
        	white += 1

print white / total * 100