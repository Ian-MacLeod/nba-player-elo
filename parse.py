import json
from itertools import groupby
from collections import defaultdict, Counter

from play import Play

def get_player_ids(play):
    for idx in [13, 20, 27]:
        if not play[idx] is None:
            yield play[idx]

def is_sub(play):
    play[2] == 8

with open('sample_data.txt', 'r') as file:
    data = file.read()

data = json.loads(data)
plays = data['resultSets'][0]['rowSet']

periods = groupby(plays, lambda x: x[4])

class PlayerList:
    def __init__(self):
        self.starters = defaultdict(set)
        self.non_starters = defaultdict(set)

    def update(self, play):
        if play.is_sub():
            player1, player2 = play.get_players()
            self.add_player(*player1)
            self.add_sub_player(*player2)
        else:
            for player in play.get_players():
                self.add_player(*player)

    def includes(self, player_id, team_id):
        return player_id in self.starters[team_id] or player_id in self.non_starters[team_id]

    def add_player(self, player_id, team_id):
        if not self.includes(player_id, team_id):
            self.starters[team_id].add(player_id)

    def add_sub_player(self, player_id, team_id):
        if not self.includes(player_id, team_id):
            self.non_starters[team_id].add(player_id)


class PossessionList:
    def __init__(self):
        self.score = [0, 0]
        self.checkpoint = [0, 0]
        self.possessions = []

    def new_lineups(self, home, away):
        self.home_control = None
        self.home = home
        self.away = away

    def offense(self):
        return self.home if self.home_control else self.away

    def defense(self):
        return self.away if self.home_control else self.away

    def switch_possession(self):
        self.home_control = not self.home_control

    def update(self, play):
        new_score = play.score()
        if self.home_control is None:
            self.home_control = play.home_control
        elif (not play.home_control is None) and play.home_control != self.home_control:
            if new_score:
                self.score = new_score
            assert(self.score[0] == self.checkpoint[0] or self.score[1] == self.checkpoint[1])
            self.possessions.append({
                "offense": self.offense(),
                "defense": self.defense(),
                "points": max(self.score[0] - self.checkpoint[0], self.score[1] - self.checkpoint[1])
            })
            self.checkpoint = self.score
        else:
            self.score = new_score


possessions = PossessionList()
for group in periods:
    period_plays = list(group[1])
    players = PlayerList()
    for play in period_plays:
        players.update(Play(play))
    # print(players.starters)
    # print(players.non_starters)

    possessions.new_lineups(list(players.starters[1610612759]), list(players.starters[1610612760]))
    # print(possessions.home)
    for play in period_plays:
        possessions.update(Play(play))

    print(Counter([p["points"] for p in possessions.possessions]))
