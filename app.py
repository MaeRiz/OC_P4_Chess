from tinydb import TinyDB, Query, where


class Player:

    def __init__(self, name, surname, birthday, genre, rank):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank

        db = TinyDB('db.json')
        players_table = db.table('players')

        players_table.insert({
            'name': self.name,
            'surname': self.surname,
            'birthday': self.birthday,
            'genre': self.genre,
            'rank': self.rank
        })


player_test = Player("Maé", "Gonin", "13/01/2000", "Homme", 5)