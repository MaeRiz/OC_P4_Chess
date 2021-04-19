
from tinydb import TinyDB, Query
from app.controllers import c_input
from app.controllers import c_players
from app.views import v_menu
import datetime


class Player:


    def __init__(self, id=None):
       
        self.name = ''
        self.surname = ''
        self.birthday = ''
        self.genre = ''
        self.rank = ''
        self.scores = ''
        self.id = id

        if id:
           self.set_data_from_db(id)
        else:
            self.set_data_from_input()

    def set_data_from_db(self, id):

        q = Query()
        data = TinyDB('app/data/db_player.json').table('players').search(q.id == id)
        self.name = data[0]['name']
        self.surname = data[0]['surname']
        self.birthday = data[0]['birthday']
        self.genre = data[0]['genre']
        self.rank = data[0]['rank']
        self.scores = data[0]['scores']

    def set_data_from_input(self):
        """ Create player and insert in DB players """

        p_tab = TinyDB('app/data/db_player.json').table('players')
        call_input = c_players.playersControl().create_players()

        self.name = call_input[0]
        self.surname = call_input[1]
        self.birthday = call_input[2]
        self.genre = call_input[3]
        self.rank = call_input[4]
        self.id = str(datetime.datetime.now())

        p_tab.insert({
            'name': self.name,
            'surname': self.surname,
            'birthday': self.birthday,
            'genre': self.genre,
            'rank': self.rank,
            'scores': {},
            'id': self.id
        })
        v_menu.View().save_player(self.name, self.surname)
        return self.id


    def modify(self, new_rank):

        q = Query()
        p_tab = TinyDB('app/data/db_player.json').table('players')

        self.new_rank = new_rank
        p_tab.update({"rank": self.new_rank}, q.id == self.id)

        v_menu.View().modify_player(self.surname, self.name, self.birthday, self.new_rank)

    
    def update_score(self, id_tournament, score):

        q = Query()
        p_tab = TinyDB('app/data/db_player.json').table('players')

        if id_tournament in self.scores:
            self.scores[id_tournament] += score
            p_tab.update({"scores": self.scores}, q.id == self.id)
        else:
            self.scores[id_tournament] = score
            p_tab.update({"scores": self.scores}, q.id == self.id)


    def get_score(self, id_tournament):
        if id_tournament in self.scores:
            return self.scores[id_tournament]
        else:
            return 0