from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
import codecs
import csv

f=codecs.open("index.html", 'r')

#html = './html.html'
bs = BeautifulSoup(f.read(), 'html.parser')

# for sibiling in bs.find('select', {'class': 'fselect._all_species'}).optgroup.next_siblings:
#    print(sibiling)


total = []
for tag in bs.select('.fselect._all_species > optgroup > option'):
    print(tag.string, " : ",tag['value'].split('/')[1])
    name = tag.string
    data = tag['value'].split('/')[1]
    total.append([name, data])
#print(data)
print(len(total))
f = open("species.csv", "w")
writer =csv.writer(f)
for i in total: 
    writer.writerow(i)
f.close
