from app.controllers import c_tournaments
from app.controllers import c_input
from app.views import v_menu
from app.models import m_players
from tinydb import TinyDB, Query
import datetime


class Tournament:

    def __init__(self, id=None):
        self.name = ''
        self.place = ''
        self.start = ''
        self.end = ''
        self.rounds = ''
        self.round = ''
        self.rounds_nbr = ''
        self.timing = ''
        self.description = ''
        self.players = ''
        self.stat = ''
        self.id = id
        if id:
            self.set_data_from_db(id)
        else:
            self.set_data_from_input()

    def set_data_from_db(self, id):

        q = Query()
        data = TinyDB('app/data/db_tournaments.json').table(
            'tournaments').search(q.id == id)
        self.name = data[0]['name']
        self.place = data[0]['place']
        self.start = data[0]['start']
        self.end = data[0]['end']
        self.rounds_nbr = data[0]['rounds_nbr']
        self.timing = data[0]['timing']
        self.description = data[0]['description']
        self.players = data[0]['players']
        self.stat = data[0]['stat']
        self.rounds = data[0]['rounds']

    def set_data_from_input(self):

        call_inputs = c_tournaments.Tournaments().create_tournament()
        tournaments_table = TinyDB(
            'app/data/db_tournaments.json').table('tournaments')

        self.name = call_inputs[0]
        self.place = call_inputs[1]
        self.start = call_inputs[2]
        self.end = call_inputs[3]
        self.rounds_nbr = call_inputs[4]
        self.timing = call_inputs[5]
        self.description = call_inputs[6]
        self.players = call_inputs[7]
        self.stat = 1
        self.id = str(datetime.datetime.now())

        tournaments_table.insert({
            'name': self.name,
            'place': self.place,
            'start': self.start,
            'end': self.end,
            'rounds_nbr': self.rounds_nbr,
            'timing': self.timing,
            'description': self.description,
            'players': self.players,
            'stat': self.stat,
            'rounds': {},
            'id': self.id
        })

    def list_players(self, order):
        self.order = order
        list_players = []
        for i in range(len(self.players)):
            player = m_players.Player(self.players[i])
            p_data = ()
            p_data = (
                player.surname,
                player.name,
                player.genre,
                player.rank,
                player.get_score(self.id)
            )
            list_players.append(p_data)

        if self.order == 1:
            list_a = sorted(list_players, key=lambda colonnes: colonnes[0])
        elif self.order == 2:
            list_a = sorted(
                list_players, key=lambda colonnes: colonnes[3], reverse=True
            )
        elif self.order == 3:
            list_a = sorted(
                list_players, key=lambda colonnes: colonnes[4], reverse=True
            )
        for i in range(len(list_a)):
            v_menu.View().list_players_t(
                list_a[i][0], list_a[i][1], list_a[i][2],
                list_a[i][3], list_a[i][4]
            )

        input('\nEntrer pour revenir au menu précédent')

    def start_rounds(self):
        self.players_list = self.gen_match(self.stat)

        self.players_score = []
        self.round_start = datetime.datetime.now().strftime("%H:%M:%S")
        self.match = 1
        self.player_id = 0

        while self.match < 5:

            self.player1 = m_players.Player(self.players_list[self.player_id])
            self.player_id += 1
            self.player2 = m_players.Player(self.players_list[self.player_id])
            self.player_id += 1

            v_menu.View().current_round(
                self.stat, self.match, self.player1, self.player2
            )
            self.winner = c_input.Input().select_menu_number(3)

            if self.winner == 1:
                self.player1.update_score(self.id, 1)
                self.player1_score = 1
                self.player2_score = 0
            elif self.winner == 2:
                self.player2.update_score(self.id, 1)
                self.player1_score = 0
                self.player2_score = 1
            elif self.winner == 3:
                self.player1.update_score(self.id, 0.5)
                self.player2.update_score(self.id, 0.5)
                self.player1_score = 0.5
                self.player2_score = 0.5
            self.match += 1
            self.players_score.append([
                [self.player1.id, self.player1_score],
                [self.player2.id, self.player2_score]
            ])
        self.round_end = datetime.datetime.now().strftime("%H:%M:%S")

        self.rounds[self.stat] = {
            'time': [self.round_start, self.round_end],
            'matchs': self.players_score
        }
        self.stat += 1
        self.save()

    def gen_match(self, rounds):
        # Generate list players for first rounds
        if rounds == 1:
            list_players = []
            for i in range(len(self.players)):
                self.player = m_players.Player(self.players[i])
                p_data = ()
                p_data = (
                    self.player.id,
                    self.player.rank
                )
                list_players.append(p_data)

            list_a = sorted(
                list_players, key=lambda colonnes: colonnes[1], reverse=True
            )

            final_players_list = []
            for i in range(4):
                final_players_list.append(list_a[i][0])
                final_players_list.append(list_a[i+4][0])

            return (final_players_list)

        # Generate lists players for next rounds
        else:
            # Premier tri par ordre de score
            list_players = []
            for i in range(len(self.players)):
                self.player = m_players.Player(self.players[i])
                p_data = ()
                p_data = (
                    self.player.id,
                    self.player.get_score(self.id)
                )
                list_players.append(p_data)

            list_players_score = sorted(
                list_players, key=lambda colonnes: colonnes[1], reverse=True
            )

            # Tri par ordre de classement pour score égaux
            list_players_ranked = []
            while len(list_players_score) > 1:
                if list_players_score[0][1] == list_players_score[1][1]:
                    list_players_for_rank = []
                    while True:
                        try:
                            if (
                                list_players_score[0][1] ==
                                list_players_score[1][1]
                            ):
                                list_players_for_rank.append(
                                    list_players_score[0][0]
                                )
                                list_players_score.pop(0)
                            else:
                                list_players_for_rank.append(
                                    list_players_score[0][0]
                                )
                                list_players_score.pop(0)
                                break
                        except IndexError:
                            list_players_for_rank.append(
                                list_players_score[0][0]
                            )
                            list_players_score.pop(0)
                            break

                    temp_list_players = []
                    for i in range(len(list_players_for_rank)):
                        self.player = m_players.Player(
                            list_players_for_rank[i]
                        )
                        p_data = ()
                        p_data = (
                            self.player.id,
                            self.player.rank
                        )
                        temp_list_players.append(p_data)

                    temp_list_players_ranked = sorted(
                        temp_list_players, key=lambda colonnes: colonnes[1],
                        reverse=True
                    )
                    for i in range(len(temp_list_players_ranked)):
                        list_players_ranked.append(
                            temp_list_players_ranked[0][0]
                        )
                        temp_list_players_ranked.pop(0)
                else:
                    list_players_ranked.append(list_players_score[0][0])
                    list_players_score.pop(0)
            try:
                list_players_ranked.append(list_players_score[0][0])
                list_players_score.pop(0)
            except IndexError:
                pass

            # Vérification si les joueurs ont déjà jouer contre
            final_players_list = []
            while len(list_players_ranked) > 2:
                player1 = list_players_ranked[0]
                player2_id = 0
                for i in range(len(list_players_ranked)):
                    player2_id += 1
                    player2 = list_players_ranked[player2_id]
                    self.check = self.check_player_match(player1, player2)
                    if self.check is False:

                        final_players_list.append(
                            list_players_ranked[player2_id]
                        )
                        list_players_ranked.pop(player2_id)

                        final_players_list.append(list_players_ranked[0])
                        list_players_ranked.pop(0)
                        break

            final_players_list.append(list_players_ranked[0])
            list_players_ranked.pop(0)
            try:
                final_players_list.append(list_players_ranked[0])
                list_players_ranked.pop(0)
            except IndexError:
                pass

            return final_players_list

    def check_player_match(self, player1, player2):

        for i_rounds in range(len(self.rounds)):
            i_rounds_key = str(i_rounds + 1)
            for i_matchs in range(len(self.rounds[i_rounds_key]['matchs'])):
                matchs = self.rounds[i_rounds_key]['matchs'][i_matchs]
                for i_match in range(len(matchs)):
                    if player1 in matchs[i_match][0]:
                        if i_match == 0:
                            if player2 == matchs[1][0]:
                                return True

                        elif i_match == 1:
                            if player2 == matchs[0][0]:
                                return True

        return False

    def save(self):

        q = Query()
        t_tab = TinyDB('app/data/db_tournaments.json').table('tournaments')

        t_tab.update({"stat": self.stat}, q.id == self.id)
        t_tab.update({"rounds": self.rounds}, q.id == self.id)

    def list_rounds(self):
        if len(self.rounds) < self.stat:

            for i_rounds in range(len(self.rounds)):
                i_rounds_key = str(i_rounds + 1)
                v_menu.View().rounds_nbr(
                    i_rounds_key, self.rounds[i_rounds_key]['time'][0],
                    self.rounds[i_rounds_key]['time'][1]
                )
                for i_matchs in range(len(
                    self.rounds[i_rounds_key]['matchs']
                )):
                    player1 = m_players.Player(
                        self.rounds[i_rounds_key]['matchs'][i_matchs][0][0]
                    )
                    player2 = m_players.Player(
                        self.rounds[i_rounds_key]['matchs'][i_matchs][1][0]
                    )
                    v_menu.View().list_rounds(
                        i_matchs + 1, player1.name,
                        player1.surname, player2.name, player2.surname,
                        self.rounds[i_rounds_key]['matchs'][i_matchs][0][1],
                        self.rounds[i_rounds_key]['matchs'][i_matchs][1][1]
                    )
                input("\nEntrer pour afficher la suite")
