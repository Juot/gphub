from urllib.request import urlopen
from bs4 import BeautifulSoup

html  = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html,"lxml")
nameList = bs0bj.findAll({"h1","h2","h3","h4","h5","h6"})

for name in nameList:
    print(name)
    print(name.get_text())
