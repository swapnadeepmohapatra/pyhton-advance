import bs4
import requests
import csv

res = requests.get(
    'https://www.flipkart.com/search?q=realme&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup = bs4.BeautifulSoup(res.text, 'lxml')

lst = (soup.select('._2cLu-l'))
lst2 = (soup.select('._1vC4OE'))
print(type(lst))
for x in lst:
    print(x.getText())
# for x in lst2:
    print(lst2[1 ].getText())

# with open('person.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvData)
# csvFile.close()
