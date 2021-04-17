from tinydb import TinyDB
from app.views import v_menu

class List:

    def players(self, order):

        self.order = order
        p_tab = TinyDB('db_player.json').table('players')

        all_players = p_tab.all()
        list_players = []
        for i in range(len(all_players)):
            p_data = ()
            p_data = (all_players[i].get("surname"),
                        all_players[i].get('name'),
                        all_players[i].get('birthday'),
                        all_players[i].get('genre'),
                        all_players[i].get('rank'))
            list_players.append(p_data)

        if self.order == 1:
            list_a = sorted(list_players, key=lambda colonnes: colonnes[0])

        elif self.order == 2:
            list_a = sorted(list_players,
                key=lambda colonnes: colonnes[4], reverse=True)
                
        for i in range(len(list_a)):
            print(list_a[i])
        input('\nEntrer pour revenir au menu précédent')

    def tournaments(self):

        t_tab = TinyDB('db_tournaments.json').table('tournaments')
        all_tournaments = t_tab.all()

        for i in range(len(all_tournaments)):
            v_menu.View().list_tournaments(all_tournaments[i]['name'],
            all_tournaments[i]['place'], all_tournaments[i]['start'],
            all_tournaments[i]['end'], all_tournaments[i]['rounds'],
            all_tournaments[i]['timing'], all_tournaments[i]['description'])

        input('\nEntrer pour revenir au menu précédent')