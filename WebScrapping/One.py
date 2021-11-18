import requests
from bs4 import BeautifulSoup

URL = "https://www.one.co.il/Soccer/League/1"

site_html = requests.get(URL).text

bs = BeautifulSoup(site_html,"html.parser")
teams = bs.find_all(class_="teamname")
place = bs.find_all(class_="place")

file = open("Groups.txt","w")
for placeteam in range(1, len(teams)): # 1,2,3,4,5....14
    file.write(f"{place[placeteam].text} {teams[placeteam].text}\n")
file.close()