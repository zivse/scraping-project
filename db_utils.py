import psycopg2


def products_table_insert(cur, product_name, category_name):
    cur.execute("""INSERT INTO scrapper.products (category_id, name) SELECT id, %s FROM scrapper.categories
                WHERE categories.name = %s
                ON CONFLICT DO nothing""", (product_name, category_name))


def prices_table_insert(cur, price_num, data_page, product_name):
    cur.execute("""INSERT INTO scrapper.prices (product_id, site_id, price) SELECT products.id, sites.id, %s
                FROM scrapper.products  INNER JOIN scrapper.sites ON sites.data_page = %s WHERE products.name = %s
                """, (float(price_num), data_page, product_name))


def categories_table_initialize(cur, name):
    cur.execute('INSERT INTO scrapper.categories (name) VALUES (%s) ON CONFLICT DO nothing', (name,))


def sites_table_initialize(cur, name, base_url, data_page, category_name):
    cur.execute("""INSERT INTO scrapper.sites (category_id, name, base_url, data_page) 
    SELECT categories.id, %s, %s, %s
    FROM scrapper.categories WHERE categories.name = %s
    ON CONFLICT DO nothing
    """, (name, base_url, data_page, category_name))


def connect_to_db(host, database, user):
    con = psycopg2.connect(
        host=host,
        database=database,
        user=user
    )
    return con
