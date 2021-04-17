
from app.views import v_menu
from app.controllers import c_players
from app.controllers import c_input
from app.controllers import c_tournaments
from app.models import m_search
from app.models import m_players
from app.models import m_list
from app.models import m_tournaments


class Controller:


    def main_menu(self):
        v_menu.View().main_menu()
        self.menu_number = c_input.Input().select_menu_number(3)

        # Call player menu
        if self.menu_number == 1:
            Controller().players_menu()

        # Call tournaments menu
        elif self.menu_number == 2:
            Controller().tournaments_menu()

        # Close app
        elif self.menu_number == 3:
            pass


    def players_menu(self):
        v_menu.View().players_menu()
        self.menu_number = c_input.Input().select_menu_number(5)

        #  Call for create player
        if self.menu_number == 1:
            player = m_players.Player()
            Controller().players_menu()

        # Call search player and call modify player
        elif self.menu_number == 2:
            self.find_player = m_search.Search().player(
                c_input.Input().check_input('text', 'Nom ou Prénom: ')
            )
            if self.find_player == 'None':
                Controller().players_menu()
            else:
                player = m_players.Player(self.find_player)
                player.modify(c_input.Input().check_input(
                    'number', 'Nouveau classement: ')
                )
            Controller().players_menu()

        # Call list player
        elif self.menu_number == 3:
            v_menu.View().list_menu()
            m_list.List().players(c_input.Input().select_menu_number(2))
            Controller().players_menu()

        # Back to main menu
        elif self.menu_number == 4:
            Controller().main_menu()

        # Close app
        elif self.menu_number == 5:
            pass

    def tournaments_menu(self):
        v_menu.View().tournaments_menu()
        self.menu_number = c_input.Input().select_menu_number(5)

        # Call for create tounament
        if self.menu_number == 1:   
            m_tournaments.Tournament()
            Controller().tournaments_menu()

        # Search and load tounament
        elif self.menu_number == 2:
            self.find_tournament = m_search.Search().tournament(
                c_input.Input().check_input('text', 'Nom ou Lieu: ')
            )
            if self.find_tournament == 'None':
                Controller().tournaments_menu()
            else:
                Controller().current_tournament_menu(self.find_tournament)

        # Call list tounaments 
        elif self.menu_number == 3:   
            m_list.List().tournaments()
            Controller().tournaments_menu()

        # Back to main menu
        elif self.menu_number == 4:
            Controller().main_menu()

        # Close app
        elif self.menu_number == 5:
            pass

    def current_tournament_menu(self, id):
        self.tournament = m_tournaments.Tournament(id)

        self.show_menu = v_menu.View().current_tournament_menu(
            self.tournament.name, self.tournament.stat,
            self.tournament.start, self.tournament.end, self.tournament.rounds_nbr
        )
        self.menu_number = c_input.Input().select_menu_number(6)

        # Start round
        if self.menu_number == 1:
            if self.tournament.stat > self.tournament.rounds_nbr:
                print('Tournois fini')
            else:
                self.tournament.start_rounds()
                self.tournament.stat += 1
                self.current_tournament_menu(self.tournament.id)
                
        # List players
        elif self.menu_number == 2:
            v_menu.View().list_menu()
            self.tournament.list_players(c_input.Input().select_menu_number(2))
            Cself.current_tournament_menu(self.tournament.id)

        # List matchs et rounds
        elif self.menu_number == 3:
            self.tournament.list_rounds()
            self.current_tournament_menu(self.tournament.id)

        # Show tournament infos
        elif self.menu_number == 4:
            v_menu.View().list_tournaments(
                self.tournament.name, self.tournament.place,
                self.tournament.start, self.tournament.end,
                self.tournament.rounds_nbr, self.tournament.timing,
                self.tournament.description
            )
            input('Entrer pour revenir au menu précédent')
            Controller().current_tournament_menu(self.tournament.id)

        # Back to tournament menu
        elif self.menu_number == 5:
            Controller().tournaments_menu()

        # Close app
        elif self.menu_number == 6:
            pass
