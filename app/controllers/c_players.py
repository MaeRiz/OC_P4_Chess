
from app.controllers import c_menu
from app.models import m_players
from app.controllers import c_input
from app.views import v_menu

from tinydb import TinyDB, Query

class playersControl:


    def create_players(self):
        self.name = c_input.Input().check_input('text', 'Prénom: ')
        self.surname = c_input.Input().check_input('text', 'Nom: ')
        self.birthday = c_input.Input().check_input(
            'date', 'Date de naissance: ')
        self.genre = c_input.Input().check_input('genre', 'F ou M: ')
        self.rank = c_input.Input().check_input('number', 'Classement: ')
        self.player_id = m_players.Players().create_players(self.name,
        self.surname, self.birthday, self.genre, self.rank)
        return self.player_id

    def search_player(self):
        db = TinyDB('db_player.json')
        players_table = db.table('players')
        User = Query()

        self.search_player_name = c_input.Input().check_input(
            'text', 'Nom ou Prénom: ')
        self.search_result = players_table.search(
            (User.name == self.search_player_name) | 
            (User.surname == self.search_player_name))

        if len(self.search_result) == 0:
            print("Aucuns joueur n'a était trouver avec ce nom.")
            return 'None'
        elif len(self.search_result) == 1:
            return self.search_result[0]['date']

        elif len(self.search_result) >= 2:
            for i in range(len(self.search_result)):
                print(i+1 , ' ● ' , self.search_result[i]['name'] , ' ' , self.search_result[i]['surname'] , ' ' , self.search_result[i]['birthday'])

            self.player_number = c_input.Input().select_menu_number(
                len(self.search_result))

            return self.search_result[self.player_number-1]['date']

    def update_player_rank(self, date):

        self.date = date

        db = TinyDB('db_player.json')
        players_table = db.table('players')
        User = Query()

        self.player = players_table.search((User.date == self.date))

        print('Changement de classement de:', self.player[0]['surname'], self.player[0]['name'], self.player[0]['birthday'], '(Classement actuel: ', self.player[0]['rank'], ')')

        self.new_rank = int(c_input.Input().check_input(
            'number', 'Nouveau classement: '))
        players_table.update({"rank": self.new_rank}, User.date == self.date)

        print('Mise à joueur de : ', self.player[0]['surname'], self.player[0]['name'], self.player[0]['birthday'], '(Nouveau classement: ', self.new_rank, ')')
        c_menu.Controller().players_menu()

    def list_players(self):
        v_menu.View().list_menu()
        self.menu_number = c_input.Input().select_menu_number(2)

        db = TinyDB('db_player.json')
        players_table = db.table('players')

        all_players = players_table.all()
        list_players = []
        for i in range(len(all_players)):
            p_data = ()
            p_data = (all_players[i].get("surname"),
                        all_players[i].get('name'),
                        all_players[i].get('birthday'),
                        all_players[i].get('genre'),
                        all_players[i].get('rank'))
            list_players.append(p_data)

        if self.menu_number == 1:
            list_a = sorted(list_players, key=lambda colonnes: colonnes[0])
            for i in range(len(list_a)):
                print(list_a[i])
            input('Entrer pour retourner au menu joueurs')
            c_menu.Controller().players_menu()

        elif self.menu_number == 2:
            list_a = sorted(list_players,
                key=lambda colonnes: colonnes[4], reverse=True)
            for i in range(len(list_a)):
                print(list_a[i])
            input('Entrer pour retourner au menu joueurs')
            c_menu.Controller().players_menu()
