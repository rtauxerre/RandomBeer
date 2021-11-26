#
# Projet tuteuré Random Beer
# IUT Auxerre - Département Réseaux et Télécommunications
# https://github.com/rtauxerre/RandomBeer
# Copyright (c) 2021 Michaël Roy
#

# Dépendance
import random

# Fonction permettant de lire le fichier de la liste des bières
# et d'en choisir une au hasard
def RandomBeer() :
	# Lit le fichier de la liste des bières
	with open( 'Beer.txt' ) as beer_file :
		beer_list = beer_file.read().splitlines()
	# Choisit une bière au hasard dans la liste et la renvoie
	return random.choice( beer_list )
