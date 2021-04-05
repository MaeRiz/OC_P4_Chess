
from app.views import v_menu
from app.controllers import c_players
from app.controllers import c_input
from app.controllers import c_tournaments


class Controller:


    def main_menu(self):
        v_menu.View().main_menu()
        self.menu_number = c_input.Input().select_menu_number(3)

        if self.menu_number == 1:
            Controller().players_menu()

        elif self.menu_number == 2:
            Controller().tournaments_menu()

        elif self.menu_number == 3:
            pass


    def players_menu(self):
        v_menu.View().players_menu()
        self.menu_number = c_input.Input().select_menu_number(5)

        if self.menu_number == 1:
            c_players.playersControl().create_players()
            Controller().players_menu()

        elif self.menu_number == 2:
            self.find_player = c_players.playersControl().search_player()
            if self.find_player == 'None':
                Controller().players_menu()
            else:
                c_players.playersControl().update_player_rank(self.find_player)

        elif self.menu_number == 3:
            c_players.playersControl().list_players()
            
        elif self.menu_number == 4:
            Controller().main_menu()

        elif self.menu_number == 5:
            pass

    def tournaments_menu(self):
        v_menu.View().tournaments_menu()
        self.menu_number = c_input.Input().select_menu_number(5)

        if self.menu_number == 1:   
            c_tournaments.Tournaments().create_tournament()

        elif self.menu_number == 2:
            Controller().current_tournament_menu()                                      #Affichage d'exemple

        elif self.menu_number == 3:   
            c_tournaments.Tournaments().list_tournaments()

        elif self.menu_number == 4:
            Controller().main_menu()

        elif self.menu_number == 5:
            pass

    def current_tournament_menu(self):
        v_menu.View().current_tournament_menu()
        self.menu_number = c_input.Input().select_menu_number(8)

        if self.menu_number == 6:
            Controller().tournaments_menu()

        elif self.menu_number == 7:
            pass
