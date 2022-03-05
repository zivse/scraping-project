import requests
from bs4 import BeautifulSoup


# TODO: remove comments, you wont need them when you will move necessary code to functions
# TODO: at the end, create a main function that will run the project (use `__main__` which is standard way in python)
# TODO: function name should be with `_` instead of camelcase letters - !
from db_utils import products_table_initilize, prices_table_initilize


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
    product_item = soup.find_all(tag_findall, class_findall)
    while (product_item != []): #go over all the pages on the website
        tempUrl = url.format(place=page_num)
        req = requests.get(tempUrl)
        soup = BeautifulSoup(req.content, "html.parser")
        # put the information on all the products in an array
        product_item = soup.find_all(tag_findall, class_=class_findall)
        for item in product_item:
            product_name = item.find(class_=pname_find).get_text()
            # TODO: if there is no use for this like then remove it - !
            price_num = item.find(class_=pricenum_find).get_text().replace('₪', '')
            #insert to tables
            # TODO: create a function that inserts the product by its product_name and category name - !
            products_table_initilize(cur, product_name, 'whiskey')
            # TODO: create a function that insert the price by its price_num, data_page and product_name
            prices_table_initilize(cur, price_num, data_page, product_name)
            page_num += 1
        break



# TODO: create a function that connects to the db and returns the con - !
#     # TODO: create as constants


# TODO: create a function that initializes the categories table with the right values -!


# TODO: create a function that initializes the sites table with the right values - !


