import requests
import re
from bs4 import BeautifulSoup

page = requests.get("https://www.google.dz/search?q=covid-19")
soup = BeautifulSoup(page.content)
links = soup.findAll("a")

for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print(re.split(":(?=http)",link["href"].replace("/url?q=","")))
