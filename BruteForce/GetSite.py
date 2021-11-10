import requests

URL = "https://flaskgetpost.shalomvanunu.repl.co/"

site_content  = requests.get(URL)
print(site_content.text)

