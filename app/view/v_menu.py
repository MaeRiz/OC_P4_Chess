

class View:

    def __init__(self):
        pass

    def main_menu(self):
        print('=================\n')
        print('-=[ MENU PRINCIPAL ]=-')
        print("\n\
1 ● Menu joueurs.\n\
2 ● Menu tournois.\n\
3 ● Quitter l'application.\n") 

    def players_menu(self):
        print('=================\n')
        print('-=[ MENU JOUEURS ]=-')
        print("\n\
1 ● Ajouter un joueur.\n\
2 ● Modifier un joueur.\n\
3 ● Liste des acteurs.\n\
4 ● Retour au menu principal.\n\
5 ● Quitter l'application.\n") 

    def tournaments_menu(self):
        print('=================\n')
        print('-=[ MENU TOURNOIS ]=-')
        print("\n\
1 ● Créer un tournois.\n\
2 ● Reprendre un tournois.\n\
3 ● Liste des tournois.\n\
4 ● Retour au menu principal.\n\
5 ● Quitter l'application.\n") 

    def current_tournament_menu(self):
        print('=================\n')
        print('-=[ TOURNOIS NOM_DU_TOURNOIS ]=-')
        print('EN COURS - 20-02-2021')
        print("\n\
1 ● Démarrer le tours n° 1\n\
2 ● Liste des joueurs.\n\
3 ● Liste des matchs.\n\
4 ● Liste des tours.\n\
5 ● Informations du tournois.\n\
6 ● Modifier les informations du tournois.\n\
7 ● Retour au menu tournois.\n\
8 ● Quitter l'application.\n") 

    def short(self, name):
        self.name = name
        if self.name == "err_choise":
            print("Ce choix est incorrect.")