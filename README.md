description:
------
collecting a data on alcohols from varied of websites. 
compare between the data from the different online shops recommend to the user where is the cheapest place to buy. 

project goal:
-----
- compare between alcohol drink from different online shops
- find the cheapest place to buy 

project structures:
---
- main:
   - connect to db
   - initialize tables in SQL
   - calling the scrape website function
  
- scrape_website:
    - find the relevant information from the website
    - using beautiful soup library to scrape the pages and find the relevant information

-db_utils:
  - create SQL tables
  - insert the information inside the tables