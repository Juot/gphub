from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getnamelist(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bs0bj = BeautifulSoup(html,"lxml")
        namelist = bs0bj.findall("span",{"class":"green"})
    except AttributeError as e:
        return  namelist
    return namelist

namelist = getnamelist("http://www.pythonscraping.com/pages/warandpeace.html")
if namelist is None:
    print("error")
else:
    for name in namelist:
        print(name.get_text())
