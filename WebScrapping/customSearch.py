import requests
import sys
import webbrowser
import bs4

res = requests.get('https://google.com/search?q=' +
                   ''.join(sys.argv[1:]))
res.raise_for_status()
print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElem = soup.select('.r a')
links = min(5, len(linkElem))
print(linkElem)
for link in range(links):
    print(linkElem[link].get('href'))
    webbrowser.open('https://google.com'+linkElem[link].get('href'))
