description:
------
This project aims to find the cheapest alcoholic drink.
The way its done is by scraping a variety of different websites and saving their sold items in a DB.
Later, we query the relevant tables and get the results we are looking for,
like the cheapest item.

project goals:
-----
- compare between alcohol drinks from different online shops
- find the cheapest place

project structures:
---
- main:
   - connect to db
   - initialize tables in SQL
   - calling the scrape website function
  
- scrape_website:
    - find the relevant information from the website
    - using beautiful soup library to scrape the pages and find the relevant information

- db_utils:
  - create SQL tables
  - insert the information inside the tables