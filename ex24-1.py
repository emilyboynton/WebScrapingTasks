"""Find and print the percentage of NYPD stop-and-frisk reports
in which the suspect was white for the years 2003-2015"""
from __future__ import division
import requests
import re
import zipfile
import csv
from io import BytesIO

for year in range(2003, 2015):
	url = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/'+str(year)+'_sqf_csv.zip'
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
	print "Percent of white people stopped and frisked in the year "+str(year)+":"
	print white / total * 100