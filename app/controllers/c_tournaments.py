from app.controllers import c_input
from app.views import v_menu
from app.models import m_tournaments
from app.controllers import c_menu
from app.controllers import c_players

from tinydb import TinyDB, Query

class Tournaments:

    def create_tournament(self):

        db = TinyDB('db_player.json')
        players_table = db.table('players')
        User = Query()

        self.tournament_name = c_input.Input().check_input('text', 'Nom du tournois: ')
        self.tournament_place = c_input.Input().check_input('text', 'Lieu du tournois: ')
        self.tournament_start = c_input.Input().check_input('date', 'Date de début: ')
        self.tournament_end = c_input.Input().check_input('date', 'Date de fin: ')
        self.tournament_rounds = c_input.Input().rounds_tournament('Nombre de tours (4 par défaut): ')

        v_menu.View().short('tournament_timing')
        self.menu_number = c_input.Input().select_menu_number(3)
        if self.menu_number == 1:
            self.tournament_timing = 'BULLET'
        elif self.menu_number == 2:
            self.tournament_timing = 'BLITZ'
        elif self.menu_number == 3:
            self.tournament_timing = 'COUP RAPIDE'
        
        self.tournament_description = c_input.Input().check_input('text', 'Description: ')

        self.count_players = 1
        self.players = {}
        while True:

            v_menu.View().short('add_players')
            self.number = c_input.Input().select_menu_number(3)

            if self.number == 1:
                self.find_player = c_players.playersControl().search_player()

                if self.find_player == 'None':
                    pass
                else:
                    self.player = players_table.search((User.date == self.find_player))

                    self.players[self.count_players] = list([self.player[0]['date'], self.player[0]['name'],
                    self.player[0]['surname'], self.player[0]['rank'], 0])

                    self.count_players = self.count_players + 1
                    v_menu.View().short('player_added')

            elif self.number == 2:
                self.player_created = c_players.playersControl().create_players()
                self.player = players_table.search((User.date == self.player_created))

                self.players[self.count_players] = list([self.player[0]['date'], self.player[0]['name'],
                self.player[0]['surname'], self.player[0]['rank'], 0])
                
                self.count_players = self.count_players + 1
                v_menu.View().short('player_added')

            elif self.number == 3:
                break

        self.tournament_id = m_tournaments.ModelTournaments().create_tournament(
            self.tournament_name, self.tournament_place,
            self.tournament_start, self.tournament_end,
            self.tournament_rounds, self.tournament_timing,
            self.tournament_description, self.players)

        #Tournaments().load_tournament(self.tournament_id)

    def load_tournament(self, id):
        pass



    def list_tournaments(self):

        db = TinyDB('db_tournaments.json')
        tournaments_table = db.table('tournaments')

        all_tournaments = tournaments_table.all()

        for i in range(len(all_tournaments)):
            v_menu.View().list_tournaments(all_tournaments[i]['name'],
            all_tournaments[i]['place'], all_tournaments[i]['start'],
            all_tournaments[i]['end'], all_tournaments[i]['rounds'],
            all_tournaments[i]['timing'], all_tournaments[i]['description'])

        input('\nEntrer pour revenir au menu précédent')
        c_menu.Controller().tournaments_menu()