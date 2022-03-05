from db_utils import connect_to_db, categories_table_initialize, sites_table_initialize
from scrape_website import scrape_website

turky_url = "https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1"
tag_findall_turky = 'li'
class_findall_turky = 'CenterCataloge productItem'
product_name_findall_turky = 'pname'
price_num_findall_turky = 'priceNum'

url_winery = 'https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99'
tag_findall_winery = 'div'
class_findall_winery = 'saleitem col-xs-6 col-sm-3'
product_name_findall_winery = 'name'
price_num_findall_winery = 'price'

HOST = "localhost"
DATA_BASE = "zivseker"
USER = "zivseker"
categoty_name_whiskey = 'whiskey'


def main():
    con = connect_to_db(HOST, DATA_BASE, USER)
    cur = con.cursor()
    categories_table_initialize(cur, categoty_name_whiskey)
    sites_table_initialize(cur, 'דרך היין', 'https://www.wineroute.co.il', url_winery, categoty_name_whiskey)
    sites_table_initialize(cur, 'הטורקי', 'https://www.haturki.com', turky_url, categoty_name_whiskey)

    scrape_website(url_winery, tag_findall_winery, class_findall_winery, product_name_findall_winery,
                   price_num_findall_winery, cur)
    scrape_website(turky_url, tag_findall_turky, class_findall_turky, product_name_findall_turky,
                   price_num_findall_turky, cur)
    con.commit()
    con.close()


if __name__ == '__main__':
    main()
