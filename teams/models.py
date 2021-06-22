from django.db import models
from nba_api.stats.static import teams

class Team:
    def all(self):
        return teams.get_teams()

    def find_team_by_full_name(self, name):
        return teams.find_teams_by_full_name(name)

    def find_teams_by_state(self, state):
        return teams.find_teams_by_state(state)
    
    def find_teams_by_city(self, city):
        return teams.find_teams_by_city(city)

    def find_team_by_nickname(self, nickname):
        return teams.find_teams_by_nickname(nickname)

    def find_teams_by_year_founded(self, year):
        return teams.find_teams_by_year_founded(year)

    def find_team_by_abbreviation(self, abbrev):
        return teams.find_team_by_abbreviation(abbrev)

    def find_team_name_by_id(self, team_id):
        return teams.find_team_name_by_id(team_id)
