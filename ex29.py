from urllib import urlopen
from bs4 import BeautifulSoup

url = "https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html"

html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.find("table", {"class":"os"})

rows = table.findAll("tr")

# rows[0] is header data

tds = rows[1].findAll("td")

print "next scheduled execution is on", tds[0].text


