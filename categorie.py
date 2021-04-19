#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv
import time

def livre(url, soup):
    # récupération des articles
    all_books = soup.find_all("article", class_ = "product_pod")

    for book in all_books:
        # url de chaque livre
        h3 = book.h3.find("a")["href"]
        #print(h3)
        # url absolue
        link = urljoin(urlpage, h3)
        #print(link)
        # Appel url du livre
        page = urllib.request.urlopen(link)
        # chargement html dans variable soup
        soup_book = BeautifulSoup(page, 'html.parser')
        # description du livre
        try:
            product_description = soup_book.find("div", class_= "sub-header", id="product_description").h2.find_next().text
        except AttributeError:
            product_description = None
        # titre
        title = book.h3.find("a")["title"]
        print(title)
        # image
        image_url = book.a.img["src"]
        image_url = urljoin(url, image_url)
        # print(image_url)
        # Récupération categorie
        ul = soup_book.find("ul", class_ = "breadcrumb")
        category = ul.find_all("a")[2].text     
        # Récupération autres informations
        table_data = soup_book.find("table", class_ = "table table-striped")
        td = table_data.findAll("td")
        #print(td)
        # écriture du livre 
        rows.append([link, td[0].text, title, td[2].text, td[3].text, td[5].text, product_description, category, td[6].text, image_url])
        # attente avant prochaine appel
        time.sleep(3)
             
def une_categorie(urlpage):
    # Appel url
    page = urllib.request.urlopen(urlpage)
    # chargement html dans variable soup
    soup = BeautifulSoup(page, 'html.parser')
    # chargement des livres
    livre(urlpage, soup)  
    # Recherche de la page suivante 

    if soup.find("li", class_ = "next"):
        time.sleep(3)
        li = soup.find("li", class_ = "next")
        url = urljoin("http://books.toscrape.com/catalogue/category/books/sequential-art_5/",li.find("a").get('href'))
        print(url)
        # Appel de la fonction si autre page
        une_categorie(url)
    
# création entête de colonnes
rows = []
rows.append(['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
             'price_excluding_tax', 'number_available','product_description', 'category', 'review_rating', 'image_url'])

# chargement url
urlpage =  'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html' 
une_categorie(urlpage)

# Lecture rows pour écriture
for i in rows:
    # creation csv
    with open('category_sequential-art.csv','w', newline='') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerows(rows)




    



