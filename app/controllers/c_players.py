from app.controllers import c_input

class playersControl:


    def create_players(self):
        """ Input for create player & return inputs """

        self.name = c_input.Input().check_input('text', 'Prénom: ')
        self.surname = c_input.Input().check_input('text', 'Nom: ')
        self.birthday = c_input.Input().check_input(
            'date', 'Date de naissance: ')
        self.genre = c_input.Input().check_input('genre', 'F ou M: ')
        self.rank = c_input.Input().check_input('number', 'Classement: ')
        return ([self.name, self.surname, self.birthday,
            self.genre, self.rank]
        )
        
