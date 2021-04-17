

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
2 ● Charger un tournois.\n\
3 ● Liste des tournois.\n\
4 ● Retour au menu principal.\n\
5 ● Quitter l'application.\n") 

    def current_tournament_menu(self, name, stat, start, end, rounds):
        print('\n')
        print('-=[', name, ']=-')
        print(start, '-', end)
        if stat > rounds:
            print('\nLe tournoi est terminé.')
        else:
            print("\n1 ● Démarrer le tours n°", stat,)
        print("\
2 ● Liste des joueurs.\n\
3 ● Liste des tours et matchs.\n\
4 ● Informations du tournois.\n\
5 ● Retour au menu tournois.\n\
6 ● Quitter l'application.\n")

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
            print('\n1 ● Rechercher un joueur \n2 ● Créer un joueur')
        elif self.name == 'tournament_created':
            print('\nTournoi créé avec succès !')
        elif self.name == 'player_added':
            print('\nJoueur ajouté.')

    def list_tournaments(
        self, name, place, start, end, rounds, timing, description
    ):
        print('\n', name, '-', place, '\n du', start, 'au',
            end, '\n Tours:', rounds, '\n', timing,
            '\n Description:\n', description
        )


    def current_round(self, round, match, player1, player2):
        print('\n \nTour', round, '- Match', match)
        print(player1.name, player1.surname, 'contre', player2.name, player2.surname)
        print('\nRésultats:')
        print('\n1 ●', player1.name, player1.surname, 'gagnant')
        print('2 ●', player2.name, player2.surname, 'gagnant')
        print('3 ● Match nul\n')


    def list_rounds(self, num_round, num_match, player1_name, player1_surname, player2_name, player2_surname, point1, point2):
        print('\nTour', num_round, '- Match', num_match)
        print(player1_name, player1_surname, point1)
        print(player2_name, player2_surname, point2)
