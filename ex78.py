""" Find and print the number of Cupertino, CA restaurants 
that have been shut down due to health violations in the last six months. """

from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://services.sccgov.org/facilityinspection/Closure/Index?sortField=sortbyEDate")
bsObj = BeautifulSoup(html, "html.parser")

table_body = bsObj.find("tbody")

rows = table_body.findAll("tr")
total_restaurants = 0

for row in rows:
	total_restaurants += 1

print total_restaurants