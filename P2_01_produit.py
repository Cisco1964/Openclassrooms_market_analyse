#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

# chargement url
urlpage =  'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html' 
print(urlpage)

# appel url
page = urllib.request.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Récupération du titre
title = soup.find("h1")
print(title.text)

# Récupération description du produit
product_description = soup.find("div", class_= "sub-header", id="product_description").h2.find_next()
print(product_description.text)

# Récupération autres informations
table_data = soup.find("table", class_ = "table table-striped")
td = table_data.findAll("td")
for m in td:
    print(m.text)

print(td)

# Récupération categorie
ul = soup.find("ul", class_ = "breadcrumb")
category= ul.find_all("a")[2].text
print(category)

# Récupération image_url
img = soup.find("div", class_ = "item active").img['src']
image = urljoin(urlpage, img)
print(urljoin(urlpage, img))

# creation entête de colonnes
rows = []
rows.append(['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
             'price_excluding_tax', 'number_available','product_description', 'category', 'review_rating', 'image_url'])

# écriture du produit
rows.append([urlpage, td[0].text, title.text, td[2].text, td[3].text, td[5].text, product_description.text, category, td[6].text, image])          

for i in rows:   
    ## creation csv
    with open('extraction_produit.csv','w', newline='') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerows(rows)
