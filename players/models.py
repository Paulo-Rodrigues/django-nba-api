from django.db import models
from nba_api.stats.static import players

class Player:
    def find_player_by_full_name(self, name):
        return players.find_players_by_full_name(name)

    def find_player_by_first_name(self, name):
        return players.find_players_by_first_name(name)

    def find_player_by_last_name(self,name):
        return players.find_players_by_last_name(name)

    def all(self):
        return players.get_players()

