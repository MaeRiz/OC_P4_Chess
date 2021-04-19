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
3 ● Liste des joueurs.\n\
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
1 ● Liste par ordre alphabétique.\n\
2 ● Liste par ordre de classement.\n")

    def list_menu_t(self):
        print("\n\
1 ● Liste par ordre alphabétique.\n\
2 ● Liste par ordre de classement.\n\
3 ● Liste par ordre de points.\n")

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
        print(
            '\n', name, '-', place, '\n du', start, 'au',
            end, '\n Tours:', rounds, '\n', timing,
            '\n Description:\n', description
        )

    def current_round(self, round, match, player1, player2):
        print('\n \nTour', round, '- Match', match)
        print(
            player1.name, player1.surname,
            'contre', player2.name, player2.surname
        )
        print('\nRésultats:')
        print('\n1 ●', player1.name, player1.surname, 'gagnant')
        print('2 ●', player2.name, player2.surname, 'gagnant')
        print('3 ● Match nul\n')

    def list_rounds(
        self, num_match, player1_name, player1_surname,
        player2_name, player2_surname, point1, point2
    ):
        print('\nMatch', num_match)
        print(player1_name, player1_surname, point1)
        print(player2_name, player2_surname, point2)

    def rounds_nbr(self, round_num, start, end):
        print('\nTour', round_num)
        print(start, '-', end)

    def list_players(self, surname, name, birth, genre, rank):
        print(
            surname, name, '- Date:', birth,
            '- Genre:', genre, '- Classement:', rank
        )

    def list_players_t(self, surname, name, genre, rank, score):
        print(
            surname, name, '- Genre:', genre,
            '- Classement:', rank, '- Points:', score
        )

    def search(self, type):
        if type == 'player_none':
            print("\nAucuns joueur n'a était trouver avec ce nom.")
        elif type == 'tournament_none':
            print("\nAucuns tounoi n'a était trouver avec ce nom.")

    def search_players(self, type, name, surname, birth, rank, num=None):
        if type == 'find_player':
            print(name, surname, birth, '- Classement actuel:', rank)
        elif type == 'find_players':
            print(
                num, '●', name, surname,
                birth, '- Classement actuel:', rank
            )

    def search_tournaments(self, type, name, place, start, num=None):
        if type == 'find_tournament':
            print(name, place, start)
        elif type == 'find_tournaments':
            print(num, '●', name, place, start)

    def modify_player(self, surname, name, birth, rank):
        print(
            '\nMise à joueur de:', surname, name,
            birth, '(Nouveau classement:', rank, ')'
        )

    def save_player(self, name, surname):
        print(
            '\nLe joueur', name,
            surname, 'a était sauvegardé avec succès !'
        )
