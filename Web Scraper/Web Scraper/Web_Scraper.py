import requests
from bs4 import BeautifulSoup

#Search espn for college basketball scores
webpage = "http://www.espn.com/mens-college-basketball/scoreboard/_/date/20181106"

r = requests.get(webpage)
c = r.content

soup = BeautifulSoup(c, "html.parser")
#print(soup)

away = soup.find_all("div", {"id": "events"})
print(away)
