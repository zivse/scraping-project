import psycopg2
#connect to the db
con = psycopg2.connect(
    host = "localhost",
    database = "zivseker",
    user = "zivseker"
)

#cursor
cur = con.cursor()

scrapper = "scrapper.categories"
#excute
#cur.execute('INSERT INTO scrapper.categories (name) VALUES (%s)', ('ziv',))
cur.execute('INSERT INTO scrapper.categories (name) VALUES (%s)', ('maxim',))
#reset the serial id
#cur.execute('ALTER SEQUENCE scrapper.categories_id_seq RESTART WITH 1')
con.commit()
con.close()
