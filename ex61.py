"""Find and print the number of miles traveled by the current U.S. Secretary of State"""
from urllib import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.state.gov/secretary/travel/index.htm")
bsObj = BeautifulSoup(html, "html.parser")

section = bsObj.find("div", {"class": "bottom"})
section_list = section.find("ul", {"class": "icon-list"})
mileage_item = section_list.find("li", {"id": "total-mileage"})
mileage_span = mileage_item.find("span")

mileage = re.findall(r'[\d*,]+', mileage_span.get_text())

print mileage[0]