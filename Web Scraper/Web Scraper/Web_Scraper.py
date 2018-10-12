import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.century21.com/for-sale-homes/Portland-OR-179c")
c = r.content

soup = BeautifulSoup(c, "html.parser")
print(soup)
all = soup.find_all("div", {"class":"sr-card__price"})
print(all)
