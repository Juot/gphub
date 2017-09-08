from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re 
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bs0bj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    for link in bs0bj.findAll("a",href=re.compile("^(/|.*"+includerUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bs0bj,excludeUrl):
    externalLinks = []
    for link in bs0bj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs0bj = BeautifulSoup(html,"lxml")
    externalLinks = getExternalLinks(bs0bj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links ,looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bs0bj,domain)
        return getRandomExternalLink(internalLinks[random.randit(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is :"+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
