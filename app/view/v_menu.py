#! /usr/bin/env python3
# coding: utf-8


class View:

    def __init__(self):
        pass

    def main_menu(self):
        print("\n\
1 ● Menu joueurs.\n\
2 ● Menu tournois.\n\
3 ● Menu rapport.\n\
4 ● Quitter l'application.\n") 

    def players_menu(self):
        print("\n\
1 ● Ajouter un joueur.\n\
2 ● Modifier un joueur.\n\
3 ● Retour au menu principal.\n\
4 ● Quitter l'application.\n") 

    def tournaments_menu(self):
        print("\n\
1 ● Créer un tournois.\n\
2 ● Reprendre un tournois.\n\
3 ● Retour au menu principal.\n\
4 ● Quitter l'application.\n") 

    def rapports_menu(self):
        print("\n\
1 ● Liste de tous les acteurs (ordre alphabétique).\n\
2 ● Liste de tous les acteurs (ordre classement).\n\
3 ● Liste de tous les joueurs d'un tournoi (ordre alphabétique).\n\
4 ● Liste de tous les joueurs d'un tournoi (ordre classement).\n\
5 ● Liste de tous les tournois.\n\
6 ● Liste de tous les tours d'un tournoi.\n\
7 ● Liste de tous les matchs d'un tournoi.\n\
8 ● Retour au menu principal.\n\
9 ● Quitter l'application.\n") 

    def waiting_input(self):
        print("Choisir un menu :  ")

    def error_choise(self):
        print("Ce menu n'existe pas")