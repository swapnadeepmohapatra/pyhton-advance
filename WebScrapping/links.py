import requests
import bs4

res = requests.get('https://www.learncodeonline.in')
# res = requests.get('https://en.wikipedia.org/wiki/Jammu_and_Kashmir')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(res.text)
for link in soup.find_all('a', href=True):
    if link['href'] == '#':
        pass
    # if link['href'].split()[0] == '#':
    #     pass
    print(link['href'])
