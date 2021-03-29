
from tinydb import TinyDB
import datetime


class Players:

    def __init__(self):
        pass

    def create_players(self, name, surname, birthday, genre, rank):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.genre = genre
        self.rank = rank
        self.date = str(datetime.datetime.now())

        db = TinyDB('db_player.json')
        players_table = db.table('players')

        players_table.insert({
            'name': self.name,
            'surname': self.surname,
            'birthday': self.birthday,
            'genre': self.genre,
            'rank': self.rank,
            'date': self.date
        })

        print('Le joueur ' + self.name + ' ' + self.surname + ' a était sauvegardé avec succès !')