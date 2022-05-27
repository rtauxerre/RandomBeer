#
# Projet tuteuré Random Beer
# IUT Auxerre - Département Réseaux et Télécommunications
# https://github.com/rtauxerre/RandomBeer
# Copyright (c) 2022 Michaël Roy
#

# Dépendance
import random

# Fonction permettant de lire le fichier de la liste des bières et la renvoyer
def GetBeerList() :
	# Lit le fichier de la liste des bières
	with open( 'Beer.txt' ) as beer_file :
		beer_list = beer_file.read().splitlines()
	# Renvoie la liste des bières
	return beer_list

# Fonction permettant de retourner une bière au hasard en fonction de la liste
def GetRandomBeer( beer_list ) :
	# Choisit une bière au hasard dans la liste et la renvoie
	return random.choice( beer_list )
