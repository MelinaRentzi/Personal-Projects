#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') #Display text while downloading the Google page
res=requests.get('http://google.com/search?q=' + input())
res.raise_for_status()

#Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))