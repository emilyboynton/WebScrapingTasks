"""Find and print the name of the most recently added dataset on data.gov"""

from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://catalog.data.gov/dataset?q=&sort=metadata_created+desc&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C8.754794702435605%2C-59.0625%2C61.77312286453148")
bsObj = BeautifulSoup(html, "html.parser")

first_item = bsObj.find("li", {"class": "dataset-item"})
first_item = first_item.find("h3", {"class": "dataset-heading"})
first_item = first_item.find("a").get_text()

print first_item

