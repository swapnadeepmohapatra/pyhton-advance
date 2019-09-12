import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Jammu_and_Kashmir')
soup = bs4.BeautifulSoup(res.text, 'lxml')

print((soup.select('title')[0]))
print((soup.select('title')[0].getText()))
