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
    j = 1
    print(url)
    tempUrl = url.format(place=j)
    req = requests.get(tempUrl)
    soup = BeautifulSoup(req.content, "html.parser")
    productItem = soup.find_all(tag_findall, class_findall)
    print(productItem)
    while (productItem != []): #go over all the pages on the website
        tempUrl = url.format(place=j)
        req = requests.get(tempUrl)
        soup = BeautifulSoup(req.content, "html.parser")
        productItem = soup.find_all(tag_findall, class_=class_findall) #put the information on all the products in an array
        i = 0
        for item in productItem: #print the name and price for each product
            pname = item.find(class_=pname_find).get_text()
            en_title = item.find(class_=en_title_find).get_text()
            priceNum = item.find(class_=pricenum_find).get_text()
            print(str(i) + " " + pname + "::" + en_title + ":::" + priceNum)
            i += 1
            break
        j = j + 1
        break

#turkyUrl = "https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1"
#tag_findall = 'li'
#class_findall = 'CenterCataloge productItem'
#pname_find = 'pname'
#en_title_find = 'en_title'
#pricenum_find = 'priceNum'
url = 'https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99'
tag_findall= 'div'
class_findall= 'saleitem col-xs-6 col-sm-3'
pname_find= 'name'
en_title_find= None
pricenum_find = 'price'
pharseWebsite(url, tag_findall, class_findall, pname_find, en_title_find, pricenum_find)
