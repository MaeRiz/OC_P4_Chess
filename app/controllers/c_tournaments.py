from app.controllers import c_input
from app.views import v_menu
from app.models import m_tournaments
from app.controllers import c_menu
from app.controllers import c_players
from app.models import m_search
from app.models import m_players


class Tournaments:

    def create_tournament(self):

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

        # Add players with creation or search
        self.players = []
        while True:

            v_menu.View().short('add_players')
            self.number = c_input.Input().select_menu_number(2)

            # Search player and add in players list for tournament
            if self.number == 1:
                
                self.find_player = m_search.Search().player(c_input.Input().check_input('text', 'Nom ou Prénom: '))

                if self.find_player == 'None':
                    pass
                else:
                    self.players.append(self.find_player)
                    v_menu.View().short('player_added')

            # Create player & add in players list for tournament
            elif self.number == 2:
                self.player_created = m_players.Player()
                self.players.append(self.player_created.id)
                v_menu.View().short('player_added')


            if len(self.players) == 8:
                break


        return ([
            self.tournament_name, self.tournament_place,
            self.tournament_start, self.tournament_end,
            self.tournament_rounds, self.tournament_timing,
            self.tournament_description, self.players
        ])
