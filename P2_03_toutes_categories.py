#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv
import time
import os

def entete_csv(rows):
    # création entête de colonnes
    rows.append(['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax',
             'price_excluding_tax', 'number_available','product_description', 'category', 'review_rating', 'image_url'])

def ecriture_csv(cat, rows):
    global n
    # Lecture rows pour écriture
    for row in rows:
        # ecriture csv des livres
        filecsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "categories_csv", "{}.csv").format(cat)
        with open(filecsv,'w', newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(rows)
        
        # copie des images dans le repertoire
        if "http" in row[9]:
            # un des livres a un / dans le titre
            filename = "{}.jpg".format(row[2]).replace("/", " ")
            image_url = row[9]
            n = n + 1
            urllib.request.urlretrieve(image_url, "images/" + str(n) + "_" + filename)
    print(cat)
    
def livre(url, soup, rows): 
    # tous les livres de la balise article
    all_books = soup.find_all("article", class_ = "product_pod")
    # boucle sur tous les livres de la catégorie
    for book in all_books:
        # url de chaque livre
        h3 = book.h3.find("a")["href"]
        # url absolue
        link = urljoin(url, h3)
        # Appel url du livre
        page = urllib.request.urlopen(link)
        status = page.getcode()
        # Si erreur
        if status != 200:
            print("Erreur:", status, "page en erreur", url)
            return
        else:
            # chargement html dans variable soup
            soup_book = BeautifulSoup(page, 'html.parser')
            # description du livre
            try:
               product_description = soup_book.find("div", class_= "sub-header", id="product_description").h2.find_next().text
            except AttributeError:
               product_description = None
            # titre
            title = book.h3.find("a")["title"]
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
             
def une_categorie(url, categ, rows):
    # Appel url
    page = urllib.request.urlopen(url)
    status = page.getcode()
    # Si erreur
    if status != 200:
        print("Erreur:", status, "page en erreur", url)
        return
    else:
        # chargement html dans variable soup
        soup = BeautifulSoup(page, 'html.parser')
        # chargement des livres
        livre(url, soup, rows)
        # Recherche de la page suivante
        if soup.find("li", class_="next"):
            time.sleep(3)
            li = soup.find("li", class_="next")
            # mise en forme url
            pos = url.rfind("/")
            url = url[:pos+1] + li.find("a").get('href')
            # appel fonction si autre page
            une_categorie(url, categ, rows)

def toutes_categories(urlpage):
    # requete url
    page = urllib.request.urlopen(urlpage)
    status = page.getcode()
    # Si erreur
    if status != 200:
        print("Erreur:", status, "page en erreur", urlpage)
        return
    else:
        # chargement html dans variable soup
        soup = BeautifulSoup(page, 'html.parser')
        liste_categorie = soup.find("ul", class_ = "nav nav-list").find("ul").find_all("li")
    
        for categ in liste_categorie:
           url = urljoin(urlpage,categ.find("a").get('href'))
           cat = str(categ.text).strip()
           # entete csv
           rows = []
           entete_csv(rows)  
           # traitement d'une catégorie
           une_categorie(url, cat, rows)
           # ecriture csv
           ecriture_csv(cat, rows)  

# Debut du programme
n = 0 
urlpage = 'http://books.toscrape.com/index.html' 
toutes_categories(urlpage)






    



