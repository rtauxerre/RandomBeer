#!/usr/bin/env python3

#
# Projet tuteuré Random Beer
# Interface client avec PyGame
# IUT Auxerre - Département Réseaux et Télécommunications
# https://github.com/rtauxerre/RandomBeer
# Copyright (c) 2022 Michaël Roy
#

# Dépendances externes
import pygame
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

# Définit la taille de l'écran
screen_size = ( 800, 480 )

# Initialise PyGame
pygame.init()

# Titre de l'application
pygame.display.set_caption( "Galopin Random Beer" )

# Configure la taille de l'écran
screen = pygame.display.set_mode( screen_size )

# Application en plein écran
#screen = pygame.display.set_mode( (0, 0), pygame.FULLSCREEN )

# Récupère la liste des bières
beer_list = GetBeerList()

# Choisit une bière au hasard
beer = GetRandomBeer( beer_list )

# Initialise la police de caractères
my_font = pygame.font.Font( pygame.font.get_default_font(), 36 )

# Initialise le texte à afficher
beer_text = my_font.render( beer, True, (0, 0, 0) )

# Boucle principale
while True :
	# Gestion des événements
	for event in pygame.event.get():
		# Touche Echappe appuyée
		if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ) :
			# Quitte le programme
			pygame.quit()
			exit()
		# Boutton de souris appuyé
		if event.type == pygame.MOUSEBUTTONDOWN :
			# Choisit une bière au hasard à nouveau
			beer = GetRandomBeer( beer_list )
			# Met à jour le texte à afficher
			beer_text = my_font.render( beer, True, (0, 0, 0) )
	# Fond d'écran
	screen.fill( (255,255,255) )
	# Affiche le nom de la bière
	screen.blit( beer_text, dest=(0,0) )
	# Met à jour l'écran
	pygame.display.flip()
