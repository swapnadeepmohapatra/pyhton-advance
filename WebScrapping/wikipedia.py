import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Jammu_and_Kashmir')
soup = bs4.BeautifulSoup(res.text, 'lxml')

# nothing for tags
# . for class
# # for ids

lst = (soup.select('.toctext'))

for x in lst:
    print(x.getText())
