import bs4 as bs
import urllib.request
import re

source = urllib.request.urlopen('https://www.gpw.pl/archiwum-notowan-full?type=10&instrument&date=05-10-2018').read()
soup = bs.BeautifulSoup(source, 'lxml')

table = soup.table
table_rows = soup.find_all(re.compile('tr'))

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
