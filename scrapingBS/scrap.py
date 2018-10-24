# <table class="table footable footable-loaded">

import urllib.request
from bs4 import BeautifulSoup

# https://pythonprogramming.net/parsememcparseface/
sauce = urllib.request.urlopen("https://www.gpw.pl/archiwum-notowan-full?type=10&instrument&date=05-10-2018&fbclid=IwAR3IqduBrwSnW6cAmmJnfgNTpPExFLuc27S3Vv8c5DbVM_SLKAv49I0zszI/").read()
soup = BeautifulSoup(sauce, 'lxml')

table = soup.find('table', {"class":"table footable footable-loaded"})

for tr in table.findAll('tr'):
    row = [i.text for i in tr.findAll('th')]

    print(row)
