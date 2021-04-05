

class View:

    def __init__(self):
        pass

    def main_menu(self):
        print('\n')
        print('-=[ MENU PRINCIPAL ]=-')
        print("\n\
1 ● Menu joueurs.\n\
2 ● Menu tournois.\n\
3 ● Quitter l'application.\n") 

    def players_menu(self):
        print('\n')
        print('-=[ MENU JOUEURS ]=-')
        print("\n\
1 ● Ajouter un joueur.\n\
2 ● Modifier un joueur.\n\
3 ● Liste des acteurs.\n\
4 ● Retour au menu principal.\n\
5 ● Quitter l'application.\n") 

    def tournaments_menu(self):
        print('\n')
        print('-=[ MENU TOURNOIS ]=-')
        print("\n\
1 ● Créer un tournois.\n\
2 ● Reprendre un tournois.\n\
3 ● Liste des tournois.\n\
4 ● Retour au menu principal.\n\
5 ● Quitter l'application.\n") 

    def current_tournament_menu(self):
        print('\n')
        print('-=[ TOURNOIS NOM_DU_TOURNOIS ]=-')
        print('EN COURS - 20-02-2021')
        print("\n\
1 ● Démarrer le tours n° 1\n\
2 ● Liste des joueurs.\n\
3 ● Liste des matchs.\n\
4 ● Liste des tours.\n\
5 ● Informations du tournois.\n\
6 ● Retour au menu tournois.\n\
7 ● Quitter l'application.\n")

    def list_menu(self):
        print("\n\
1 ● Liste par ordre alphabétique\n\
2 ● Liste par ordre de classement.\n")

    def short(self, name):
        self.name = name
        if self.name == "err_choise":
            print("Ce choix est incorrect.")
        elif self.name == 'err_number':
            print('Veuillez choisir un nombre positif.')
        elif self.name == 'err_date':
            print('Format demandé: JJ/MM/AAAA')
        elif self.name == 'default_rounds':
            print('4 (définis par défaut)')
        elif self.name == 'save_or_not':
            print("\n1 ● Sauvegarder \n2 ● Annuler\n")
        elif self.name == 'tournament_timing':
            print("\n1 ● Bullet \n2 ● Blitz \n3 ● Coup rapide\n")
        elif self.name == 'yes_or_cancel':
            print('1 ● Oui \n2 ● Annuler')
        elif self.name == 'add_players':
            print('\n1 ● Rechercher un joueur \n2 ● Créer un joueur \n3 ● Terminer\n')
        elif self.name == 'tournament_created':
            print('\nTournoi créé avec succès !')
        elif self.name == 'player_added':
            print('\nJoueur ajouté.')

    def list_tournaments(self, name, place, start, end, rounds, timing, description):
        print('\n', name, '-', place, '\n du', start, 'au', end,
        '\n Tours:', rounds, '\n', timing, '\n Description:\n', description)
