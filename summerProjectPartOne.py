import gettext
import string
import requests
from bs4 import BeautifulSoup


#require to import BeautifulSoup and requests
def pharseWebsite(url,tag_findall,class_findall,pname_find,en_title_find,pricenum_find):
    if "/?page" in url:
        url = url.replace("=1", "={place:.2f}",1)
    else:
        url = url + "={place:.2f}"
    j = 0
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    productItem = soup.find_all(tag_findall, class_=class_findall)
    while (productItem != []): #go over all the pages on the website
        j = j + 1
        tempUrl = url.format(place=j)
        req = requests.get(tempUrl)
        soup = BeautifulSoup(req.content, "html.parser")
        productItem = soup.find_all('li', class_='CenterCataloge productItem') #put the information on all the products in an array
        i = 0
        for item in productItem: #print the name and price for each product
            pname = item.find(class_=pname_find).get_text()
            en_title = item.find(class_=en_title_find).get_text()
            priceNum = item.find(class_=pricenum_find).get_text()
            print(str(i) + " " + pname + "::" + en_title + ":::" + priceNum)
            i += 1

turkyUrl = "https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1"
tag_findall = 'li'
class_findall = 'CenterCataloge productItem'
pname_find = 'pname'
en_title_find = 'en_title'
pricenum_find = 'priceNum'
pharseWebsite(turkyUrl,tag_findall,class_findall,pname_find,en_title_find,pricenum_find)
