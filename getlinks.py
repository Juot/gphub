from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bs0bj = BeautifulSoup(html,"lxml")
    return bs0bj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    print(len(links),end = "  ")
    ran = random.randint(0,len(links)-1)
    print(ran)
    print(datetime.datetime.now())
    print("*********",random.randint(0,len(links)-1),"***********")
    newArticle = links[ran].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
