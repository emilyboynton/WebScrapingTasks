""" The total number of inmates executed by Florida since 1976 """

from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.dc.state.fl.us/oth/deathrow/execlist.html")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.find("table", {"class" : "dcCSStableLight"})
rows = table.findAll("tr")

print table
print rows
results = 0

for row in rows:
	if row.find('th'):
		continue
	else:
		results += 1

print results