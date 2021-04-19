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
        # url absolue
        link = urljoin(urlpage, h3)
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
        # Récupération categorie
        ul = soup_book.find("ul", class_ = "breadcrumb")
        category = ul.find_all("a")[2].text     
        # Récupération autres informations
        table_data = soup_book.find("table", class_ = "table table-striped")
        td = table_data.findAll("td")
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
        # mise en forme url
        pos = urlpage.rfind("/")
        url = urlpage[:pos+1] + li.find("a").get('href')
        # Appel de la fonction si autre page
        une_categorie(url)
    
# création entête de colonnes
rows = []
rows.append(['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
             'price_excluding_tax', 'number_available','product_description', 'category', 'review_rating', 'image_url'])


liste = ("travel","mistery","historical fiction","sequential art","Classics","philosophy","romance",
 "womens fiction","fiction","childrens","religion", "nonfiction", "Music", "default",
 "science fiction","sports and Games","add a comment","fantasy", "new adult", "young adult", 
 "science", "poetry","paranormal", "art", "psychology", "autobiography", "parenting", "adult fiction",
 "humor", "horror", "history", "food and drink", "christian fiction", "business", "biography",
 "thriller", "contemporary", "spirituality", "academic", "self help", "historical", "christian",
 "suspense", "short stories", "novels", "health", "politics", "cultural", "erotica", "crime")

print('Entrez une catégorie :')
categ = input()
categ = categ.lower()
if categ == " ":
    print("catégorie obligatoire")
elif categ not in liste:
    print("cette catégorie n'existe pas")
else:
    i = liste.index(categ)
    cat = categ.replace(" ","-")
    cat = cat + "_" + (str(i+2))

    # chargement url
    urlpage =  'http://books.toscrape.com/catalogue/category/books/{}/index.html'.format(cat) 
    une_categorie(urlpage)

    # Lecture rows pour écriture
    for i in rows:
    # creation csv
        nom_fichier = '{}.csv'.format(cat)
        with open(nom_fichier,'w', newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(rows)




    



