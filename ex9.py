"""Find and print the number of roll call votes that were rejected by a margin
of less than 5 votes, in the first session of the U.S. Senate in the 114th Congress"""
import requests
from urllib import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.htm")
bsObj = BeautifulSoup(html, "html.parser")

rows = bsObj.findAll("tr")

data = []
for r in rows:
	data.append(r.find("td"))
	tally = re.findall("([0-9]+-[0-9]+)", data)


