from db_utils import connect_to_db, categories_table_initilize, sites_table_initilize
from summerProjectPartOne import pharse_website


def main():
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
    con = connect_to_db(HOST, DATA_BASE, USER)
    cur = con.cursor()

    categories_table_initilize(cur, 'whiskey')
    sites_table_initilize(cur, 'דרך היין', 'https://www.wineroute.co.il',
                          'https://www.wineroute.co.il/cat/48/%d7%95%d7%95%d7%99%d7%a1%d7%a7%d7%99', 'whiskey')
    sites_table_initilize(cur, 'הטורקי', 'https://www.haturki.com',
                          'https://www.haturki.com/%D7%95%D7%99%D7%A1%D7%A7%D7%99/?page=1', 'whiskey')

    pharse_website(url_winery, tag_findall_winery, class_findall_winery, product_name_findall_winery,
                   price_num_findall_winery, cur)
    pharse_website(turky_url, tag_findall_turky, class_findall_turky, product_name_findall_turky,
                   price_num_findall_turky, cur)

    con.commit()
    con.close()


if __name__ == '__main__':
    main()