from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bs0bj = BeautifulSoup(html.read(),'lxml')
print(bs0bj.title,bs0bj.h1,bs0bj.div,bs0bj.body)
