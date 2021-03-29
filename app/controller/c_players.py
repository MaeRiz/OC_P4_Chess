
from app.controller import c_menu
from app.model import m_players
from tinydb import TinyDB, Query

class playersControl:
    def __init__(self):
        pass

    def create_players(self):

        self.x_genre = 0
        self.rank = -1

        self.name = str(input('Prénom: '))
        while (len(self.name) == 0):
            self.name = str(input('Prénom: '))

        self.surname = str(input('Nom: '))
        while (len(self.surname) == 0):
            self.surname = str(input('Nom: '))

        self.birthday = input('Date de naissance (31/12/2000): ')
        while (len(self.birthday) == 0):
            self.birthday = input('Date de naissance (31/12/2000): ')

        while self.x_genre == 0:
            self.genre = input('M ou F: ')
            if self.genre == 'M':
                self.x_genre = 1
            if self.genre == 'F':
                self.x_genre = 1


        while self.rank < 0:
            try:
                self.rank = int(input('Classement: '))
                if self.rank < 0:
                    print('Veuillez choisir un nombre positif.')                
            except:
                print('Veuillez choisir un nombre.')


        print('\n')
        print("Prénom: " + self.name)
        print('Nom: ', self.surname)
        print("Anniversaire: " + self.birthday)
        print("Genre: " + self.genre)
        print("Rank: ", self.rank)
        print("\n\
1 ● Sauvegarder\n\
2 ● Annuler\n")

        self.menu_number = c_menu.Controller().input_result(2)

        if self.menu_number == 1:
            m_players.Players().create_players(self.name, self.surname, self.birthday, self.genre, self.rank )
            c_menu.Controller().players_menu()

        if self.menu_number == 2:
            c_menu.Controller().players_menu()


    def update_player(self):
        db = TinyDB('db_player.json')
        players_table = db.table('players')
        User = Query()

        self.search_player_name = input('Nom ou prénom: ')
        while (len(self.search_player_name) == 0):
            self.search_player_name = input('Nom ou prénom: ')

        self.search_player_birth = input('Date de naissance(31/12/2020): ')
        while (len(self.search_player_birth) == 0):
            self.search_player_birth = input('Date de naissance(31/12/2020): ')

        print(players_table.search((User.name == self.search_player_name) | (User.surname == self.search_player_name) & (User.birthday == self.search_player_birth)))
           
        self.update_player_rank = input('Nouveau classement ou CANCEL pour annuler: ')
        if self.update_player_rank == 'CANCEL':
            print('Action annuler')
        elif int(self.update_player_rank) > 0:
            print(players_table.search((User.name == self.search_player_name) | (User.surname == self.search_player_name) & (User.birthday == self.search_player_birth)))
        else:
            self.update_player_rank = ''
            
        while (len(self.update_player_rank) == 0):
            self.update_player_rank = input('Nouveau classement ou CANCEL pour annuler: ')
            if self.update_player_rank == 'CANCEL':
                print('Action annuler')
            elif int(self.update_player_rank) > 0:
                print(players_table.search((User.name == self.search_player_name) | (User.surname == self.search_player_name) & (User.birthday == self.search_player_birth)))
            else:
                self.update_player_rank = ''