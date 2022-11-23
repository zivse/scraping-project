psql postgres://zivseker@localhost:5432/zivseker - connection to postgres

- Create schema
    - CREATE SCHEMA scrapper;
- Create table categories
    - CREATE TABLE scrapper.categories( id INT PRIMARY KEY,  name TEXT UNIQUE);
- Create table sites
- CREATE TABLE scrapper.sites(                                                                                                                                                                      id SERIAL PRIMARY KEY,                                                                                                                                                                                      category_id INT,                                                                                                                                                                                            name TEXT,                                                                                                                                                                                                  base_url TEXT,                                                                                                                                                                                              data_page TEXT UNIQUE,                                                                                                                                                                                             time TIMESTAMPTZ default current_timestamp);

-Create table products:
- CREATE TABLE scrapper.products(                                                                                                                                                                  id SERIAL PRIMARY KEY,                                                                                                                                                                                      category_id INT,                                                                                                                                                                                            name TEXT UNIQUE,                                                                                                                                                                                                  time TIMESTAMPTZ default current_timestamp);
-Create table prices:
- CREATE TABLE scrapper.prices(
	id SERIAL PRIMARY KEY,
 	product_id INT,
 	site_id INT,
 	time TIMESTAMPTZ default current_timestamp,
	price FLOAT);

Backup db:
pg_dump -U zivseker -W -F t zivseker > /Users/zivseker/PycharmProjects/pythonProject1/backup_file.tar
