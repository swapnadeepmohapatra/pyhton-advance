import bs4
import requests
import csv

res = requests.get(
    'https://www.youtube.com/watch?v=XQgXKtPSzUI')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup.get_text)
lst = (soup.select('.title'))
# print(lst)
for x in range(len(lst)):
    print(lst[x].getText())
