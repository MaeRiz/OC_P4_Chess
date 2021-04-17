from app.controllers import c_input
from app.views import v_menu
from tinydb import Query, TinyDB

class Search:

    def player(self, name):
        """ Find player in DB, return player id or None """

        self.name = name
        q = Query()
        data = TinyDB('db_player.json').table('players')

        self.search_result = data.search(
                (q.name == self.name) | 
                (q.surname == self.name)
            )

        if len(self.search_result) == 0:
            print("Aucuns joueur n'a était trouver avec ce nom.")
            return 'None'

        elif len(self.search_result) == 1:
            print(self.search_result[0]['name'], self.search_result[0]['surname'], self.search_result[0]['birthday'], 'Classement actuel:', self.search_result[0]['rank'])
            return self.search_result[0]['id']

        elif len(self.search_result) >= 2:
            for i in range(len(self.search_result)):
                print(i+1 , '●' , self.search_result[i]['name'], self.search_result[i]['surname'], self.search_result[i]['birthday'], 'Classement actuel:', self.search_result[i]['rank'])

            self.player_number = c_input.Input().select_menu_number(
                len(self.search_result))

            return self.search_result[self.player_number-1]['id']

    def tournament(self, name):
        """ Find tournament in DB, return tournament id or None """
        self.name = name
        q = Query()
        data = TinyDB('db_tournaments.json').table('tournaments')

        self.search_result = data.search(
                (q.name == self.name) | 
                (q.place == self.name)
            )

        if len(self.search_result) == 0:
            print("Aucuns tounoi n'a était trouver avec ce nom.")
            return 'None'

        elif len(self.search_result) == 1:
            print(self.search_result[0]['name'], self.search_result[0]['place'], self.search_result[0]['start'])
            return self.search_result[0]['id']

        elif len(self.search_result) >= 2:
            for i in range(len(self.search_result)):
                print(i+1 , '●' , self.search_result[i]['name'], self.search_result[i]['place'], self.search_result[i]['start'])

            self.player_number = c_input.Input().select_menu_number(
                len(self.search_result))

            return self.search_result[self.player_number-1]['id']