				# OPENCLASSROOMS_MARKET_ANALYSE

# Auteur
projet OPENCLASSROOMS : Utilisez les bases de Python pour l'analyse de marché
Auteur : Francis CAZERES

# ANALYSE DU MARCHÉ	

# PRÉ-REQUIS  
	Création environemment virtuel : env
	Pip install BEAUTIFULSOUP4
	Pip install REQUESTS
	
# STRUCTURE DU FICHIER EN SORTIE
    .universal_ product_code (upc)
    .title
    .price_including_tax
    .price_excluding_tax
    .number_available
    .product_description
    .category
    .review_rating
    .image_url

# INFORMATIONS GÉNÉRALES
Vous êtes analyste marketing chez Books Online, une importante librairie en ligne spécialisée dans les livres d'occasion. Dans le cadre de vos fonctions, vous essayez de suivre manuellement les prix des livres d'occasion sur les sites web de vos concurrents, mais cela représente trop de travail et vous n'arrivez pas à y faire face  : il y a trop de livres et trop de librairies en ligne  ! Vous et votre équipe avez décidé d'automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d'extraire les informations tarifaires d'autres librairies en ligne. 

# 1ÈRE PARTIE : EXTRACTION D'UN PRODUIT
Choisir n'importe quelle page Produit sur le site de Books to Scrape et écrire les données dans un fichier format csv.

# Produit choisi
its-only-the-himalayas

# Nom du programme	
P2_01_produit.py

# Fichier en sortie 	
extraction_produit.csv

# 2EME PARTIE : EXTRACTION D'UNE CATEGORIE
Choisir n'importe quelle catégorie sur le site de Books to Scrape, écrire un script Python qui consulte la page de la catégorie choisie, et extrait l'URL de la page Produit de chaque livre appartenant à cette catégorie. Extraire les données produit de tous les livres de la catégorie choisie, et écrire les données dans un seul fichier CSV.

# Catégorie choisie
Saisir une catégorie parmi les 50 catégories du site

# Nom du programme	
P2_02_categorie.py

# Fichier en sortie 	
nom de la catégorie.csv

# 3EME PARTIE : EXTRACTION DE TOUTES LES CATEGORIES
Ecrire un script qui consulte le site de Books to Scrape, qui extrait toutes les catégories de livres disponibles, puis extraire les informations produit de tous les livres appartenant à toutes les différentes catégories et écrire les données dans un fichier CSV distinct pour chaque catégorie de livres. 

Télécharger et enregistrer le fichier image de chaque page Produit.

# Nom du programme	
P2_03_toutes_categories.py

# Pré-requis
Création d'un répertoire pour le dépot de toutes les catégories en csv : categories_csv 
Création d'un répertoire pour le dépot de toutes les images du site : images

# Fichier en sortie 	
categories_csv/nom de la catégorie.csv

images/XXXX_nom du produit.jpg (XXXX = compteur nombre d'image) 



