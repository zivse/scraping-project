import gettext
import string
import requests
from bs4 import BeautifulSoup
import psycopg2

# TODO: remove comments, you wont need them when you will move necessary code to functions
# TODO: at the end, create a main function that will run the project (use `__main__` which is standard way in python)

# require to import BeautifulSoup and requests
# TODO: function name should be with `_` instead of camelcase letters - !
from db_utils import products_table_initilize, prices_table_initilize, connect_to_db, categories_table_initilize, \
    sites_table_initilize


def pharse_website(data_page, tag_findall, class_findall, pname_find, pricenum_find, cur):
    if "/?page" in data_page:
        url = data_page.replace("=1", "={place:.2f}",1)
    else:
        url = data_page + "={place:.2f}"
    # TODO: change the name of the parameter `page_num` to something more relevant, like page_num - !
    page_num = 1
    tempUrl = url.format(place=page_num)
    req = requests.get(tempUrl)
    soup = BeautifulSoup(req.content, "html.parser")
    productItem = soup.find_all(tag_findall, class_findall)

    while (productItem != []): #go over all the pages on the website
        tempUrl = url.format(place=page_num)
        req = requests.get(tempUrl)
        soup = BeautifulSoup(req.content, "html.parser")
        productItem = soup.find_all(tag_findall, class_=class_findall) #put the information on all the products in an array

        for item in productItem: #print the name and price for each product
            product_name = item.find(class_=pname_find).get_text()
            # TODO: if there is no use for this like then remove it - !
            price_num = item.find(class_=pricenum_find).get_text().replace('₪', '')
            #insert to tables
            # TODO: create a function that inserts the product by its product_name and category name - !
            products_table_initilize(cur, product_name, 'whiskey')
            # cur.execute("""INSERT INTO scrapper.products (category_id, name) SELECT id, %s FROM scrapper.categories
            # WHERE categories.name = %s
            # ON CONFLICT DO nothing""", (product_name, 'whiskey'))

            # TODO: create a function that insert the price by its price_num, data_page and product_name
            prices_table_initilize(cur, price_num, data_page, product_name)
            # cur.execute("""INSERT INTO scrapper.prices (product_id, site_id, price) SELECT products.id, sites.id, %s
            # FROM scrapper.products  INNER JOIN scrapper.sites ON sites.data_page = %s WHERE products.name = %s
            # """, (float(price_num), data_page, product_name))

        page_num += 1
        break

#turkyUrl = "https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1"
#tag_findall = 'li'
#class_findall = 'CenterCataloge productItem'
#pname_find = 'pname'
#en_title_find = 'en_title'
#pricenum_find = 'priceNum'
# TODO: change parameters to constants (for example, tag_findall should be TAG_FINDALL) - !
url = 'https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99'
TAG_FINDALL = 'div'
CLASS_FINDALL = 'saleitem col-xs-6 col-sm-3'
PRODUCT_NAME_FINDALL = 'name'
PRICE_NUM_FINDALL = 'price'

#connect to the db
# TODO: create a function that connects to the db and returns the con - !
HOST = "localhost"
DATA_BASE = "zivseker"
USER = "zivseker"
con = connect_to_db(HOST, DATA_BASE, USER)
# con = psycopg2.connect(
#     # TODO: create as constants
#     host="localhost",
#     database="zivseker",
#     user="zivseker"
# )

#cursor
cur = con.cursor()

# TODO: create a function that initializes the categories table with the right values -!
categories_table_initilize(cur, 'whiskey')
# cur.execute('INSERT INTO scrapper.categories (name) VALUES (%s) ON CONFLICT DO nothing', ('whiskey',))

#insert into sites

# TODO: create a function that initializes the sites table with the right values - !
sites_table_initilize(cur, 'דרך היין', 'https://www.wineroute.co.il', 'https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99', 'whiskey')
sites_table_initilize(cur, 'הטורקי', 'https://www.haturki.com', 'https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1', 'whiskey')
# cur.execute("""INSERT INTO scrapper.sites (category_id, name, base_url, data_page)
# SELECT categories.id, %s, %s, %s
# FROM scrapper.categories WHERE categories.name = %s
# ON CONFLICT DO nothing
# """, ( 'דרך היין', 'https://www.wineroute.co.il','https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99', 'whiskey'))

# cur.execute("""INSERT INTO scrapper.sites (category_id, name, base_url, data_page)
# SELECT categories.id, %s, %s, %s
# FROM scrapper.categories WHERE categories.name = %s
# ON CONFLICT DO nothing
# """, ( 'הטורקי', 'https://www.haturki.com','https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1','whiskey'))

pharse_website(url, TAG_FINDALL, CLASS_FINDALL, PRODUCT_NAME_FINDALL, PRICE_NUM_FINDALL, cur)

pharse_website(data_page=url, tag_findall=TAG_FINDALL)

con.commit()
con.close()

