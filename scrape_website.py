import requests
from bs4 import BeautifulSoup
from db_utils import products_table_insert, prices_table_insert


def scrape_website(data_page, tag_findall, class_findall, pname_find, pricenum_find, cur):
    if "/?page" in data_page:
        url = data_page.replace("=1", "={place:.2f}",1)
    else:
        url = data_page + "={place:.2f}"
    page_num = 1
    temp_url = url.format(place=page_num)
    req = requests.get(temp_url)
    soup = BeautifulSoup(req.content, "html.parser")
    product_items = soup.find_all(tag_findall, class_findall)

    while product_items:
        temp_url = url.format(place=page_num)
        req = requests.get(temp_url)
        soup = BeautifulSoup(req.content, "html.parser")

        product_items = soup.find_all(tag_findall, class_=class_findall)
        for item in product_items:
            product_name = item.find(class_=pname_find).get_text()
            price_num = item.find(class_=pricenum_find).get_text().replace('₪', '')
            products_table_insert(cur, product_name, 'whiskey')
            prices_table_insert(cur, price_num, data_page, product_name)
            page_num += 1
        break
