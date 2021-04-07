				# OPENCLASSROOMS_MARKET_ANALYSE

# Auteur
projet OPENCLASSROOMS : Utilisez les bases de Python pour l'analyse de marché
Francis CAZERES

# ANALYSE DU MARCHÉ

# INFORMATIONS GÉNÉRALES
Vous êtes analyste marketing chez Books Online, une importante librairie en ligne spécialisée dans les livres d'occasion. Dans le cadre de vos fonctions, vous essayez de suivre manuellement les prix des livres d'occasion sur les sites web de vos concurrents, mais cela représente trop de travail et vous n'arrivez pas à y faire face  : il y a trop de livres et trop de librairies en ligne  ! Vous et votre équipe avez décidé d'automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d'extraire les informations tarifaires d'autres librairies en ligne. 

Sam, votre responsable d'équipe, vous a chargé de développer une version bêta de ce système pour suivre les prix des livres chez Books to Scrape, un revendeur de livres en ligne. En pratique, dans cette version bêta, votre programme n'effectuera pas une véritable surveillance en temps réel des prix sur la durée. Il s'agira simplement d'une application exécutable à la demande visant à récupérer les prix au moment de son exécution.

# 1ÈRE PARTIE : EXTRACTION D'UN PRODUIT
J'espère que vous pourrez m'aider à créer un système de surveillance des prix. Pour élaborer une version bêta du système limitée à un seul revendeur, le mieux est probablement de suivre les étapes que j'ai définies ci-dessous.

Choisissez n'importe quelle page Produit sur le site de Books to Scrape. Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

    product_page_url
    universal_ product_code (upc)
    title
    price_including_tax
    price_excluding_tax
    number_available
    product_description
    category
    review_rating
    image_url

Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.

# PRÉ-REQUIS  
	Création environemment virtuel
	Pip install BEAUTIFULSOUP4
	Pip install REQUESTS

# LANCEMENT DU PROGRAMME	
recuperation_produit.py

# Fichier en sortie 	
extraction_produit.csv


