
from app.view import v_menu
from app.controller import c_players


class Controller:

    def input_result(self, menu_len):
        self.menu_len = menu_len
        
        self.menu_number = 0

        while self.menu_number < 1:

            try:
                self.menu_number = int(input('Faire un choix : '))

                if self.menu_number < 1:
                    v_menu.View().short("err_choise")

                if self.menu_number > int(self.menu_len):
                    v_menu.View().short("err_choise")
                    self.menu_number = 0

            except:
                v_menu.View().short("err_choise")
                self.menu_number = 0

        return self.menu_number
        

    def main_menu(self):
        v_menu.View().main_menu()
        self.menu_number = Controller().input_result(3)

        if self.menu_number == 1:
            Controller().players_menu()

        if self.menu_number == 2:
            Controller().tournaments_menu()

        if self.menu_number == 3:
            pass


    def players_menu(self):
        v_menu.View().players_menu()
        self.menu_number = Controller().input_result(5)

        if self.menu_number == 1:
            c_players.playersControl().create_players()

        if self.menu_number == 2:
            c_players.playersControl().update_player()

        if self.menu_number == 3:
            pass                                                      #Afficher menu pour ordre alphabetique ou classement
            
        if self.menu_number == 4:
            Controller().main_menu()

        if self.menu_number == 5:
            pass

    def tournaments_menu(self):
        v_menu.View().tournaments_menu()
        self.menu_number = Controller().input_result(5)

        if self.menu_number == 1:   
            Controller().current_tournament_menu()                                      #Affichage d'exemple

        if self.menu_number == 2:
            Controller().current_tournament_menu()                                      #Affichage d'exemple

        if self.menu_number == 4:
            Controller().main_menu()

        if self.menu_number == 5:
            pass

    def current_tournament_menu(self):
        v_menu.View().current_tournament_menu()
        self.menu_number = Controller().input_result(8)

        if self.menu_number == 7:
            Controller().tournaments_menu()

        if self.menu_number == 8:
            pass
