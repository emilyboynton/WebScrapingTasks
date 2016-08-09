"""Find and print the number of university-related datasets currently listed at data.gov"""

from urllib import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://catalog.data.gov/dataset?organization_type=University&sort=metadata_created+desc&q=")
bsObj = BeautifulSoup(html, "html.parser")

dataset = bsObj.find("div", {"class": "new-results"})

num = re.findall(r'[\d*,]+', dataset.get_text())
print num[0]
