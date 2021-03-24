#! /usr/bin/env python3
# coding: utf-8

from app.view import v_menu

class Controller:

    def input_result(self, menu_len):
        self.menu_len = menu_len
        
        self.menu_number = 0

        while self.menu_number < 1:
            v_menu.View().waiting_input()
            self.menu_number = int(input())

            if self.menu_number < 1:
                v_menu.View().error_choise()

            if self.menu_number > int(self.menu_len):
                v_menu.View().error_choise()
                self.menu_number = 0

        return self.menu_number
        

    def main(self):
        v_menu.View().main_menu()
        self.menu_number = Controller().input_result(4)
        

        if self.menu_number == 1:
            Controller().players_menu()

        if self.menu_number == 2:
            Controller().tournaments_menu()

        if self.menu_number == 3:
            Controller().rapports_menu()

        if self.menu_number == 4:
            pass
        


    def players_menu(self):
        v_menu.View().players_menu()
        self.menu_number = Controller().input_result(4)

    def tournaments_menu(self):
        v_menu.View().players_menu()
        self.menu_number = Controller().input_result(4)

    def rapports_menu(self):
        v_menu.View().rapports_menu()
        self.menu_number = Controller().input_result(9)
