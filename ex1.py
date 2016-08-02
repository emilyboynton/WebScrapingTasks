"""Find and print the number of datasets currently listed on data.gov"""

from urllib import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://catalog.data.gov/dataset")
bsObj = BeautifulSoup(html, "html.parser")

dataset = bsObj.find("div", {"class": "new-results"})

num = re.findall(r'[\d*,]+', dataset.get_text())
print num[0]
