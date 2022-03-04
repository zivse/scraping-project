import gettext
import string
import requests
from bs4 import BeautifulSoup
import psycopg2


#require to import BeautifulSoup and requests
def pharseWebsite(data_page,tag_findall,class_findall,pname_find,en_title_find,pricenum_find,cur):
    if "/?page" in data_page:
        url = data_page.replace("=1", "={place:.2f}",1)
    else:
        url = data_page + "={place:.2f}"
    j = 1
    tempUrl = url.format(place=j)
    req = requests.get(tempUrl)
    soup = BeautifulSoup(req.content, "html.parser")
    productItem = soup.find_all(tag_findall, class_findall)

    while (productItem != []): #go over all the pages on the website
        tempUrl = url.format(place=j)
        req = requests.get(tempUrl)
        soup = BeautifulSoup(req.content, "html.parser")
        productItem = soup.find_all(tag_findall, class_=class_findall) #put the information on all the products in an array

        for item in productItem: #print the name and price for each product
            pname = item.find(class_=pname_find).get_text()
            en_title = item.find(class_=en_title_find).get_text()
            priceNum = item.find(class_=pricenum_find).get_text().replace('₪', '')
            #insert to tables
            cur.execute("""INSERT INTO scrapper.products (category_id, name) SELECT id, %s FROM scrapper.categories
            WHERE categories.name = 'whiskey'
            ON CONFLICT DO nothing""", (pname,))

            cur.execute("""INSERT INTO scrapper.prices (product_id, site_id, price) SELECT products.id, sites.id, %s
            FROM scrapper.products  INNER JOIN scrapper.sites ON sites.data_page = %s WHERE products.name = %s
            """, (float(priceNum), data_page, pname))

        j += 1
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

#connect to the db
con = psycopg2.connect(
    host = "localhost",
    database = "zivseker",
    user = "zivseker"
)

#cursor
cur = con.cursor()

#excute
#first category of whiskey
cur.execute('INSERT INTO scrapper.categories (name) VALUES (%s) ON CONFLICT DO nothing', ('whiskey',))

#insert into sites

cur.execute("""INSERT INTO scrapper.sites (category_id, name, base_url, data_page) 
SELECT categories.id, %s, %s, %s
FROM scrapper.categories WHERE categories.name = 'whiskey'
ON CONFLICT DO nothing
""", ( 'דרך היין', 'https://www.wineroute.co.il','https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99'))

cur.execute("""INSERT INTO scrapper.sites (category_id, name, base_url, data_page) 
SELECT categories.id, %s, %s, %s
FROM scrapper.categories WHERE categories.name = 'whiskey'
ON CONFLICT DO nothing
""", ( 'הטורקי', 'https://www.haturki.com','https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1'))

pharseWebsite(url, tag_findall, class_findall, pname_find, en_title_find, pricenum_find, cur)

con.commit()
con.close()