
import requests
from bs4 import BeautifulSoup

URL  ="https://corona.mako.co.il/"
#Step 1 Get HTML
html_site = requests.get(URL)
#print(type(html_site.text))
site_content = html_site.text #html_site.content

#Step2
site_soup = BeautifulSoup(site_content,"html.parser")
stat_toal_all = site_soup.find_all(class_="stat-total")
for item in stat_toal_all:
    print(item.text)

print(f"Number of sick {stat_toal_all[0].text}")




#print(site_content[site_content.find("539"):site_content.find("539")+3])

