from app.views import v_menu
import datetime


class Input:

    # Check len of menu and return selected menu
    def select_menu_number(self, menu_len):
        self.menu_len = menu_len
        self.menu_number = 0
        while self.menu_number < 1:
            try:
                self.menu_number = int(input('Faire un choix : '))

                if self.menu_number < 1:
                    v_menu.View().short("err_choise")

                elif self.menu_number > int(self.menu_len):
                    v_menu.View().short("err_choise")
                    self.menu_number = 0

            except ValueError:
                v_menu.View().short("err_choise")
                self.menu_number = 0
        return self.menu_number

    # Check type input and return value
    def check_input(self, type, desc):

        self.type = type

        if self.type == 'text':
            self.input = str(input(desc)).upper()
            while (len(self.input) == 0):
                self.input = str(input(desc)).upper()
            return self.input

        elif self.type == 'genre':
            while True:
                self.input = input(desc).upper()
                if self.input == 'M' or self.input == 'F':
                    break
            return self.input

        elif self.type == 'number':
            self.input = -1
            while self.input < 0:
                try:
                    self.input = int(input(desc))
                    if self.input < 0:
                        v_menu.View().short("err_number")
                except ValueError:
                    v_menu.View().short("err_number")
            return self.input

        elif self.type == 'date':
            while True:
                try:
                    self.input = input(desc)
                    date = datetime.datetime.strptime(self.input, '%d/%m/%Y')
                    date = date.date()
                    break
                except ValueError:
                    v_menu.View().short("err_date")
            return self.input

    # Check rounds number, if empty set to 4, return value
    def rounds_tournament(self, desc):
        self.input = input(desc)
        while True:
            self.input = str(self.input)
            if (len(self.input) == 0):
                self.input = 4
                v_menu.View().short('default_rounds')
                break
            else:
                self.input = int(self.input)
                try:
                    if self.input <= 0:
                        v_menu.View().short("err_number")
                        self.input = int(input(desc))
                    else:
                        break
                except ValueError:
                    v_menu.View().short("err_number")
                    self.input = int(input(desc))

        return self.input
