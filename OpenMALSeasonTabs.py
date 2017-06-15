"""
This script will parse the content of myanimelist.net's latest season and select x
links. Each link will then be opened in a seperate tab for viewing
"""

import requests, webbrowser,bs4, sys

#Get the number of tabs specified by user
try:
	no_of_tabs = int(sys.argv[1])
except ValueError:
	print("please enter a integer")
	sys.exit(1)


#Get the response from myanimelist.net
response = requests.get("https://myanimelist.net/anime/season")
response.raise_for_status()

#Parse the text and look for any <a> tags within the CSS class "title-text"
soup = bs4.BeautifulSoup(response.text, "html.parser")
results = soup.select(".title-text > a")

#Filter and select only the hyperlink
links_to_open = []
for r in results[:no_of_tabs]:
	links_to_open.append(r.get('href'))

#Open a tab for each link
for l in links_to_open:
	webbrowser.open(l)